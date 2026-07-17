import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "aaai_review_score.py"
RULES = ROOT / "rules" / "aaai-review-scoring.json"
SPEC = importlib.util.spec_from_file_location("aaai_review_score", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
SCORER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = SCORER
SPEC.loader.exec_module(SCORER)


DIMENSIONS = (
    "significance",
    "novelty",
    "soundness",
    "evidence",
    "clarity",
    "related_work",
    "reproducibility",
)


def review_input(paper_type="theory", score=4.0):
    return {
        "paper_type": paper_type,
        "dimensions": {
            dimension: {
                "status": "assessed",
                "score": score,
                "evidence": ["Synthetic test evidence"],
            }
            for dimension in DIMENSIONS
        },
        "gates": [],
        "confidence": {
            "material": 2,
            "verification": 2,
            "domain_match": 1,
        },
    }


def set_available(payload, count):
    for index, dimension in enumerate(DIMENSIONS):
        if index < count:
            payload["dimensions"][dimension] = {
                "status": "assessed",
                "score": 4.0,
                "evidence": ["Synthetic test evidence"],
            }
        else:
            payload["dimensions"][dimension] = {
                "status": "unavailable_to_reviewer",
                "reason": "Synthetic material is unavailable",
            }


class AAAIReviewScoreTests(unittest.TestCase):
    def score(self, payload):
        return SCORER.score_review(payload, rules_path=RULES)

    def assert_input_error(self, payload):
        with self.assertRaises(SCORER.ScoringInputError):
            self.score(payload)

    def test_all_four_weight_profiles_match_the_protocol(self):
        raw = json.loads(RULES.read_text(encoding="utf-8"))
        expected = {
            "theory": [0.15, 0.20, 0.30, 0.10, 0.10, 0.08, 0.07],
            "model_method": [0.15, 0.20, 0.20, 0.25, 0.08, 0.07, 0.05],
            "benchmark_resource": [0.20, 0.12, 0.15, 0.25, 0.08, 0.08, 0.12],
            "application_driven": [0.20, 0.15, 0.20, 0.20, 0.10, 0.07, 0.08],
        }
        for paper_type, expected_weights in expected.items():
            actual = raw["paper_types"][paper_type]["weights"]
            actual_weights = [actual[dimension] for dimension in DIMENSIONS]
            self.assertEqual(actual_weights, expected_weights)
            self.assertEqual(
                sum(Decimal(str(value)) for value in actual_weights), Decimal("1.00")
            )

    def test_type_specific_weighted_score(self):
        payload = review_input("benchmark_resource")
        for index, dimension in enumerate(DIMENSIONS):
            payload["dimensions"][dimension]["score"] = float(index)
        report = self.score(payload)
        self.assertEqual(report["overall"]["score"], 2.6)
        self.assertEqual(report["overall"]["rating"]["label"], "Borderline")

    def test_final_score_uses_decimal_half_up(self):
        payload = review_input("theory", 2.0)
        payload["dimensions"]["significance"]["score"] = 3.0
        payload["dimensions"]["novelty"]["score"] = 2.5
        report = self.score(payload)
        self.assertEqual(report["overall"]["known_score_before_gate"], 2.3)
        self.assertEqual(report["overall"]["score"], 2.3)

    def test_half_point_rating_boundaries(self):
        cases = (
            (0.0, 0, "Strong Reject"),
            (0.5, 1, "Reject"),
            (1.5, 2, "Weak Reject"),
            (2.5, 3, "Borderline"),
            (3.5, 4, "Weak Accept"),
            (4.5, 5, "Accept"),
            (5.5, 6, "Strong Accept"),
            (6.0, 6, "Strong Accept"),
        )
        for score, anchor, label in cases:
            with self.subTest(score=score):
                report = self.score(review_input(score=score))
                self.assertEqual(report["overall"]["rating"]["anchor"], anchor)
                self.assertEqual(report["overall"]["rating"]["label"], label)

    def test_score_bearing_statuses_require_scores(self):
        for status in ("assessed", "missing_in_paper"):
            payload = review_input()
            payload["dimensions"]["evidence"] = {"status": status}
            self.assert_input_error(payload)

        payload = review_input()
        payload["dimensions"]["evidence"] = {
            "status": "missing_in_paper",
            "score": 1.5,
            "evidence": ["Section 4 omits the required evaluation"],
        }
        report = self.score(payload)
        self.assertEqual(report["coverage"]["assessed"], 7)
        self.assertEqual(report["dimensions"]["evidence"]["score"], 1.5)

    def test_unknown_and_not_applicable_statuses_forbid_scores(self):
        for status in ("unavailable_to_reviewer", "not_applicable"):
            payload = review_input()
            payload["dimensions"]["reproducibility"] = {
                "status": status,
                "score": 0.0,
            }
            self.assert_input_error(payload)

    def test_dimension_scores_must_be_numeric_half_steps_in_range(self):
        for invalid in (4.25, -0.5, 6.5, "4.5", True):
            with self.subTest(invalid=invalid):
                payload = review_input()
                payload["dimensions"]["clarity"]["score"] = invalid
                self.assert_input_error(payload)

    def test_coverage_below_sixty_percent_makes_overall_unavailable(self):
        payload = review_input("model_method")
        set_available(payload, 3)
        report = self.score(payload)
        self.assertEqual(report["coverage"]["ratio"], 0.55)
        self.assertEqual(report["overall"]["status"], "N/A")
        self.assertIsNone(report["overall"]["score"])

    def test_sixty_to_seventy_nine_percent_is_provisional(self):
        payload = review_input()
        set_available(payload, 4)
        report = self.score(payload)
        self.assertEqual(report["coverage"]["ratio"], 0.75)
        self.assertEqual(report["overall"]["status"], "provisional")
        self.assertEqual(report["overall"]["score"], 4.0)

    def test_eighty_percent_or_more_is_normal(self):
        payload = review_input()
        set_available(payload, 6)
        report = self.score(payload)
        self.assertEqual(report["coverage"]["ratio"], 0.93)
        self.assertEqual(report["overall"]["status"], "normal")

    def test_not_applicable_is_excluded_from_coverage_denominator(self):
        payload = review_input()
        set_available(payload, 4)
        payload["dimensions"]["reproducibility"] = {
            "status": "not_applicable",
            "reason": "Synthetic theory example does not use this item",
        }
        report = self.score(payload)
        self.assertEqual(report["coverage"]["assessed"], 4)
        self.assertEqual(report["coverage"]["applicable"], 6)
        self.assertEqual(report["coverage"]["ratio"], 0.806)
        self.assertEqual(report["overall"]["status"], "normal")

    def test_core_dimension_must_be_assessed_even_with_high_coverage(self):
        payload = review_input()
        payload["dimensions"]["significance"] = {
            "status": "unavailable_to_reviewer",
            "reason": "Introduction was not supplied",
        }
        report = self.score(payload)
        self.assertEqual(report["coverage"]["ratio"], 0.85)
        self.assertEqual(report["overall"]["status"], "N/A")
        self.assertTrue(
            any("significance" in reason for reason in report["overall"]["reasons"])
        )

    def test_known_weights_are_renormalised_and_unknowns_get_a_range(self):
        payload = review_input("theory", 4.0)
        payload["dimensions"]["reproducibility"] = {
            "status": "unavailable_to_reviewer",
            "reason": "Appendix was not supplied",
        }
        report = self.score(payload)
        self.assertEqual(report["overall"]["score"], 4.0)
        self.assertEqual(
            report["overall"]["plausible_range"],
            {"minimum": 3.7, "maximum": 4.1},
        )
        effective_sum = sum(
            item.get("effective_weight", 0.0)
            for item in report["dimensions"].values()
        )
        self.assertAlmostEqual(effective_sum, 1.0, places=3)

    def test_multiple_gates_apply_the_lowest_cap(self):
        payload = review_input(score=6.0)
        payload["gates"] = [
            {
                "id": "UNSUPPORTED_CENTRAL_CLAIM",
                "reason": "The primary theorem is asserted without a proof.",
                "evidence": ["Section 3, Theorem 1"],
                "resolution_condition": "Provide a complete proof of Theorem 1.",
            },
            {
                "id": "FATAL_VALIDITY",
                "reason": "The evaluation leaks test labels into training.",
                "evidence": "Algorithm 1 and Table 2",
                "resolution_condition": "Re-run evaluation without test-label leakage.",
            },
        ]
        report = self.score(payload)
        self.assertEqual(report["gates"]["active_cap"], 1.0)
        self.assertEqual(report["overall"]["known_score_before_gate"], 6.0)
        self.assertEqual(report["overall"]["score"], 1.0)
        self.assertEqual(report["overall"]["rating"]["label"], "Reject")
        self.assertEqual(
            report["overall"]["plausible_range"],
            {"minimum": 1.0, "maximum": 1.0},
        )

    def test_each_gate_has_the_required_cap(self):
        expected = {
            "FATAL_VALIDITY": 1.0,
            "UNSUPPORTED_CENTRAL_CLAIM": 2.0,
            "CORE_NOVELTY_UNESTABLISHED": 2.5,
            "DECISIVE_EVIDENCE_MISSING": 2.5,
        }
        for gate_id, cap in expected.items():
            with self.subTest(gate_id=gate_id):
                payload = review_input(score=6.0)
                payload["gates"] = [
                    {
                        "id": gate_id,
                        "reason": "Concrete blocking defect.",
                        "evidence": "Section 4",
                        "resolution_condition": "Add decisive evidence in Section 4.",
                    }
                ]
                report = self.score(payload)
                self.assertEqual(report["overall"]["score"], cap)

    def test_gate_requires_reason_evidence_and_resolution(self):
        for gate in (
            {
                "id": "FATAL_VALIDITY",
                "evidence": "Table 1",
                "resolution_condition": "Fix the protocol",
            },
            {
                "id": "FATAL_VALIDITY",
                "reason": "Broken protocol",
                "resolution_condition": "Fix the protocol",
            },
            {
                "id": "FATAL_VALIDITY",
                "reason": "Broken protocol",
                "evidence": [],
                "resolution_condition": "Fix the protocol",
            },
            {
                "id": "FATAL_VALIDITY",
                "reason": "Broken protocol",
                "evidence": "Table 1",
            },
            {
                "id": "NOT_A_GATE",
                "reason": "x",
                "evidence": "y",
                "resolution_condition": "z",
            },
        ):
            with self.subTest(gate=gate):
                payload = review_input()
                payload["gates"] = [gate]
                self.assert_input_error(payload)

    def test_confidence_is_independent_and_material_caps_apply(self):
        high_payload = review_input(score=4.0)
        high = self.score(high_payload)

        low_payload = review_input(score=4.0)
        low_payload["confidence"] = {
            "material": 0,
            "verification": 2,
            "domain_match": 1,
        }
        low = self.score(low_payload)
        self.assertEqual(high["overall"], low["overall"])
        self.assertEqual(high["confidence"]["score"], 5)
        self.assertEqual(high["confidence"]["label"], "Very High")
        self.assertEqual(low["confidence"]["raw_score"], 3)
        self.assertEqual(low["confidence"]["score"], 1)
        self.assertEqual(low["confidence"]["label"], "Very Low")

        capped_payload = review_input()
        capped_payload["confidence"] = {
            "material": 1,
            "verification": 2,
            "domain_match": 1,
        }
        capped = self.score(capped_payload)
        self.assertEqual(capped["confidence"]["raw_score"], 4)
        self.assertEqual(capped["confidence"]["score"], 3)

    def test_zero_confidence_makes_overall_unavailable(self):
        payload = review_input(score=5.0)
        payload["confidence"] = {
            "material": 0,
            "verification": 0,
            "domain_match": 0,
        }
        report = self.score(payload)
        self.assertEqual(report["confidence"]["score"], 0)
        self.assertEqual(report["overall"]["status"], "N/A")
        self.assertIsNone(report["overall"]["score"])

    def test_confidence_components_are_strict_integers_in_range(self):
        cases = (
            {"material": 2.0, "verification": 2, "domain_match": 1},
            {"material": 3, "verification": 2, "domain_match": 1},
            {"material": 2, "verification": -1, "domain_match": 1},
            {"material": 2, "verification": 2, "domain_match": 2},
            {"material": 2, "verification": 2},
        )
        for confidence in cases:
            with self.subTest(confidence=confidence):
                payload = review_input()
                payload["confidence"] = confidence
                self.assert_input_error(payload)

    def test_input_requires_exact_dimensions_and_known_paper_type(self):
        payload = review_input()
        del payload["dimensions"]["clarity"]
        self.assert_input_error(payload)

        payload = review_input()
        payload["dimensions"]["other"] = {
            "status": "assessed",
            "score": 4.0,
            "evidence": ["Synthetic test evidence"],
        }
        self.assert_input_error(payload)

        payload = review_input("unknown_type")
        self.assert_input_error(payload)

    def test_cli_supports_json_and_markdown(self):
        with tempfile.TemporaryDirectory() as temporary:
            input_path = Path(temporary) / "review.json"
            input_path.write_text(json.dumps(review_input()), encoding="utf-8")
            json_run = subprocess.run(
                [sys.executable, str(SCRIPT), str(input_path), "--format", "json"],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            )
            self.assertEqual(json_run.returncode, 0, json_run.stderr)
            self.assertEqual(json.loads(json_run.stdout)["overall"]["score"], 4.0)

            markdown_run = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPT),
                    str(input_path),
                    "--format",
                    "markdown",
                ],
                check=False,
                capture_output=True,
                text=True,
                encoding="utf-8",
                env={**os.environ, "PYTHONIOENCODING": "utf-8"},
            )
            self.assertEqual(markdown_run.returncode, 0, markdown_run.stderr)
            self.assertIn("# AAAI Review Score", markdown_run.stdout)
            self.assertIn("4.0/6", markdown_run.stdout)
            self.assertIn("5/5", markdown_run.stdout)


if __name__ == "__main__":
    unittest.main()
