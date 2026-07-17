#!/usr/bin/env python3
"""Deterministic AAAI review scoring. Python 3.9+, standard library only."""

from __future__ import annotations

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


DEFAULT_RULES = (
    Path(__file__).resolve().parents[1] / "rules" / "aaai-review-scoring.json"
)
ONE_DECIMAL = Decimal("0.1")
THREE_DECIMALS = Decimal("0.001")
FOUR_DECIMALS = Decimal("0.0001")


class ScoringInputError(ValueError):
    """Raised when a review-scoring input is incomplete or inconsistent."""


def _config_decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        raise ValueError("{} must be numeric".format(field))
    try:
        number = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError("{} must be numeric".format(field)) from error
    if not number.is_finite():
        raise ValueError("{} must be finite".format(field))
    return number


def _input_decimal(value: Any, field: str) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ScoringInputError("{} must be a JSON number".format(field))
    try:
        number = Decimal(str(value))
    except InvalidOperation as error:
        raise ScoringInputError("{} must be numeric".format(field)) from error
    if not number.is_finite():
        raise ScoringInputError("{} must be finite".format(field))
    return number


def _as_json_number(value: Optional[Decimal], quantum: Optional[Decimal] = None) -> Optional[float]:
    if value is None:
        return None
    if quantum is not None:
        value = value.quantize(quantum, rounding=ROUND_HALF_UP)
    return float(format(value, "f"))


def _require_object(value: Any, field: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise ScoringInputError("{} must be an object".format(field))
    return value


class RuleBook:
    """Validated scoring configuration loaded from the bundled JSON rule book."""

    def __init__(self, path: Path):
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("rule book root must be an object")
        self.schema_version = str(payload.get("schema_version", ""))

        scale = payload.get("scale")
        if not isinstance(scale, dict):
            raise ValueError("scale must be an object")
        self.minimum = _config_decimal(scale.get("minimum"), "scale.minimum")
        self.maximum = _config_decimal(scale.get("maximum"), "scale.maximum")
        self.step = _config_decimal(scale.get("step"), "scale.step")
        if self.minimum != Decimal("0") or self.maximum != Decimal("6"):
            raise ValueError("review scale must be 0 through 6")
        if self.step != Decimal("0.5"):
            raise ValueError("review score step must be 0.5")
        if scale.get("rounding") != "ROUND_HALF_UP":
            raise ValueError("rounding must be ROUND_HALF_UP")

        dimensions = payload.get("dimensions")
        if not isinstance(dimensions, list) or not dimensions:
            raise ValueError("dimensions must be a non-empty list")
        self.dimension_ids: List[str] = []
        self.dimension_labels: Dict[str, str] = {}
        for item in dimensions:
            if not isinstance(item, dict):
                raise ValueError("each dimension must be an object")
            dimension_id = item.get("id")
            label = item.get("label")
            if not isinstance(dimension_id, str) or not dimension_id:
                raise ValueError("dimension id must be non-empty")
            if dimension_id in self.dimension_labels:
                raise ValueError("duplicate dimension {}".format(dimension_id))
            if not isinstance(label, str) or not label:
                raise ValueError("dimension {} lacks a label".format(dimension_id))
            self.dimension_ids.append(dimension_id)
            self.dimension_labels[dimension_id] = label

        statuses = payload.get("dimension_statuses")
        if not isinstance(statuses, dict):
            raise ValueError("dimension_statuses must be an object")
        self.score_statuses = self._status_group(statuses, "score_bearing")
        self.unknown_statuses = self._status_group(statuses, "unknown")
        self.excluded_statuses = self._status_group(statuses, "excluded")
        all_statuses = self.score_statuses | self.unknown_statuses | self.excluded_statuses
        expected_statuses = {
            "assessed",
            "missing_in_paper",
            "unavailable_to_reviewer",
            "not_applicable",
        }
        if all_statuses != expected_statuses:
            raise ValueError("dimension statuses do not match the scoring protocol")
        if sum(
            len(group)
            for group in (
                self.score_statuses,
                self.unknown_statuses,
                self.excluded_statuses,
            )
        ) != len(all_statuses):
            raise ValueError("dimension status groups overlap")
        self.valid_statuses = all_statuses

        paper_types = payload.get("paper_types")
        if not isinstance(paper_types, dict) or not paper_types:
            raise ValueError("paper_types must be a non-empty object")
        self.paper_weights: Dict[str, Dict[str, Decimal]] = {}
        dimension_set = set(self.dimension_ids)
        for paper_type, item in paper_types.items():
            if not isinstance(paper_type, str) or not isinstance(item, dict):
                raise ValueError("invalid paper type entry")
            raw_weights = item.get("weights")
            if not isinstance(raw_weights, dict) or set(raw_weights) != dimension_set:
                raise ValueError("{} weights must cover every dimension".format(paper_type))
            weights = {
                dimension_id: _config_decimal(
                    raw_weights[dimension_id],
                    "paper_types.{}.weights.{}".format(paper_type, dimension_id),
                )
                for dimension_id in self.dimension_ids
            }
            if any(weight < 0 for weight in weights.values()):
                raise ValueError("{} contains a negative weight".format(paper_type))
            if sum(weights.values(), Decimal("0")) != Decimal("1"):
                raise ValueError("{} weights must sum to 1".format(paper_type))
            self.paper_weights[paper_type] = weights

        coverage = payload.get("coverage")
        if not isinstance(coverage, dict):
            raise ValueError("coverage must be an object")
        if coverage.get("method") != "weighted":
            raise ValueError("coverage method must be weighted")
        self.minimum_coverage = _config_decimal(
            coverage.get("minimum_for_score"), "coverage.minimum_for_score"
        )
        self.provisional_below = _config_decimal(
            coverage.get("provisional_below"), "coverage.provisional_below"
        )
        raw_required = coverage.get("required_dimensions")
        if not isinstance(raw_required, list) or not raw_required:
            raise ValueError("coverage.required_dimensions must be a non-empty list")
        if not all(item in dimension_set for item in raw_required):
            raise ValueError("coverage requires an unknown dimension")
        self.required_dimensions = tuple(raw_required)

        raw_gates = payload.get("gates")
        if not isinstance(raw_gates, dict):
            raise ValueError("gates must be an object")
        self.gates: Dict[str, Dict[str, Any]] = {}
        for gate_id, item in raw_gates.items():
            if not isinstance(gate_id, str) or not isinstance(item, dict):
                raise ValueError("invalid gate entry")
            label = item.get("label")
            if not isinstance(label, str) or not label:
                raise ValueError("gate {} lacks a label".format(gate_id))
            cap = _config_decimal(item.get("cap"), "gates.{}.cap".format(gate_id))
            if cap < self.minimum or cap > self.maximum:
                raise ValueError("gate {} cap is outside the score scale".format(gate_id))
            self.gates[gate_id] = {"label": label, "cap": cap}

        raw_bins = payload.get("rating_bins")
        if not isinstance(raw_bins, list) or not raw_bins:
            raise ValueError("rating_bins must be a non-empty list")
        self.rating_bins: List[Tuple[Decimal, int, str]] = []
        for item in raw_bins:
            if not isinstance(item, dict):
                raise ValueError("each rating bin must be an object")
            lower = _config_decimal(item.get("lower_bound"), "rating lower_bound")
            anchor = item.get("anchor")
            label = item.get("label")
            if type(anchor) is not int or not isinstance(label, str) or not label:
                raise ValueError("invalid rating bin")
            self.rating_bins.append((lower, anchor, label))
        self.rating_bins.sort(key=lambda item: item[0])

        confidence = payload.get("confidence")
        if not isinstance(confidence, dict):
            raise ValueError("confidence must be an object")
        components = confidence.get("components")
        if not isinstance(components, dict):
            raise ValueError("confidence.components must be an object")
        self.confidence_components: Dict[str, Tuple[int, int]] = {}
        for component in ("material", "verification", "domain_match"):
            limits = components.get(component)
            if not isinstance(limits, dict):
                raise ValueError("missing confidence component {}".format(component))
            minimum = limits.get("minimum")
            maximum = limits.get("maximum")
            if type(minimum) is not int or type(maximum) is not int or minimum > maximum:
                raise ValueError("invalid limits for confidence component {}".format(component))
            self.confidence_components[component] = (minimum, maximum)
        raw_caps = confidence.get("material_caps")
        raw_labels = confidence.get("labels")
        if not isinstance(raw_caps, dict) or not isinstance(raw_labels, dict):
            raise ValueError("confidence caps and labels must be objects")
        self.material_caps = {int(key): int(value) for key, value in raw_caps.items()}
        self.confidence_labels = {int(key): str(value) for key, value in raw_labels.items()}
        if set(self.confidence_labels) != set(range(6)):
            raise ValueError("confidence labels must cover 0 through 5")

    @staticmethod
    def _status_group(statuses: Mapping[str, Any], key: str) -> set:
        value = statuses.get(key)
        if not isinstance(value, list) or not value or not all(
            isinstance(item, str) and item for item in value
        ):
            raise ValueError("dimension_statuses.{} must be a string list".format(key))
        return set(value)

    def validate_score(self, value: Any, field: str) -> Decimal:
        score = _input_decimal(value, field)
        if score < self.minimum or score > self.maximum:
            raise ScoringInputError("{} must be between 0 and 6".format(field))
        units = (score - self.minimum) / self.step
        if units != units.to_integral_value():
            raise ScoringInputError("{} must use 0.5-point steps".format(field))
        return score

    def rating_for(self, score: Decimal) -> Dict[str, Any]:
        selected: Optional[Tuple[Decimal, int, str]] = None
        for rating_bin in self.rating_bins:
            if score >= rating_bin[0]:
                selected = rating_bin
            else:
                break
        if selected is None:
            raise ValueError("no rating bin covers score {}".format(score))
        return {"anchor": selected[1], "label": selected[2]}


def _normalise_evidence(value: Any, field: str) -> List[str]:
    if isinstance(value, str):
        evidence = [value.strip()] if value.strip() else []
    elif isinstance(value, list):
        evidence = []
        for index, item in enumerate(value):
            if not isinstance(item, str) or not item.strip():
                raise ScoringInputError(
                    "{}[{}] must be a non-empty string".format(field, index)
                )
            evidence.append(item.strip())
    else:
        raise ScoringInputError("{} must be a non-empty string or string list".format(field))
    if not evidence:
        raise ScoringInputError("{} must not be empty".format(field))
    return evidence


def _score_confidence(value: Any, rules: RuleBook) -> Dict[str, Any]:
    confidence = _require_object(value, "confidence")
    expected = set(rules.confidence_components)
    supplied = set(confidence)
    if supplied != expected:
        missing = sorted(expected - supplied)
        extra = sorted(supplied - expected)
        details = []
        if missing:
            details.append("missing {}".format(", ".join(missing)))
        if extra:
            details.append("unexpected {}".format(", ".join(extra)))
        raise ScoringInputError("confidence fields: {}".format("; ".join(details)))

    components: Dict[str, int] = {}
    for name, (minimum, maximum) in rules.confidence_components.items():
        component = confidence[name]
        if type(component) is not int:
            raise ScoringInputError("confidence.{} must be an integer".format(name))
        if component < minimum or component > maximum:
            raise ScoringInputError(
                "confidence.{} must be between {} and {}".format(
                    name, minimum, maximum
                )
            )
        components[name] = component

    raw_score = sum(components.values())
    material_cap = rules.material_caps.get(components["material"])
    score = min(raw_score, material_cap) if material_cap is not None else raw_score
    return {
        "components": components,
        "raw_score": raw_score,
        "material_cap": material_cap,
        "score": score,
        "label": rules.confidence_labels[score],
    }


def _parse_gates(value: Any, rules: RuleBook) -> Tuple[List[Dict[str, Any]], Optional[Decimal]]:
    if value is None:
        value = []
    if not isinstance(value, list):
        raise ScoringInputError("gates must be a list")
    parsed: List[Dict[str, Any]] = []
    seen = set()
    for index, item in enumerate(value):
        gate = _require_object(item, "gates[{}]".format(index))
        gate_id = gate.get("id")
        if not isinstance(gate_id, str) or gate_id not in rules.gates:
            raise ScoringInputError("gates[{}].id is not a recognised gate".format(index))
        if gate_id in seen:
            raise ScoringInputError("duplicate gate {}".format(gate_id))
        seen.add(gate_id)
        reason = gate.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ScoringInputError("gates[{}].reason must be non-empty".format(index))
        resolution_condition = gate.get("resolution_condition")
        if not isinstance(resolution_condition, str) or not resolution_condition.strip():
            raise ScoringInputError(
                "gates[{}].resolution_condition must be non-empty".format(index)
            )
        evidence = _normalise_evidence(
            gate.get("evidence"), "gates[{}].evidence".format(index)
        )
        definition = rules.gates[gate_id]
        parsed.append(
            {
                "id": gate_id,
                "label": definition["label"],
                "cap": _as_json_number(definition["cap"], ONE_DECIMAL),
                "reason": reason.strip(),
                "evidence": evidence,
                "resolution_condition": resolution_condition.strip(),
            }
        )
    cap = min(
        (rules.gates[item["id"]]["cap"] for item in parsed),
        default=None,
    )
    return parsed, cap


def score_review(
    payload: Any,
    *,
    rules_path: Path = DEFAULT_RULES,
) -> Dict[str, Any]:
    """Validate and score one structured review input."""
    review = _require_object(payload, "input")
    rules = RuleBook(Path(rules_path))

    paper_type = review.get("paper_type")
    if not isinstance(paper_type, str) or paper_type not in rules.paper_weights:
        raise ScoringInputError(
            "paper_type must be one of {}".format(
                ", ".join(sorted(rules.paper_weights))
            )
        )
    weights = rules.paper_weights[paper_type]

    raw_dimensions = _require_object(review.get("dimensions"), "dimensions")
    expected_dimensions = set(rules.dimension_ids)
    supplied_dimensions = set(raw_dimensions)
    if supplied_dimensions != expected_dimensions:
        missing = sorted(expected_dimensions - supplied_dimensions)
        extra = sorted(supplied_dimensions - expected_dimensions)
        details = []
        if missing:
            details.append("missing {}".format(", ".join(missing)))
        if extra:
            details.append("unexpected {}".format(", ".join(extra)))
        raise ScoringInputError("dimensions: {}".format("; ".join(details)))

    scores: Dict[str, Decimal] = {}
    statuses: Dict[str, str] = {}
    dimension_output: Dict[str, Dict[str, Any]] = {}
    for dimension_id in rules.dimension_ids:
        item = _require_object(
            raw_dimensions[dimension_id], "dimensions.{}".format(dimension_id)
        )
        status = item.get("status")
        if not isinstance(status, str) or status not in rules.valid_statuses:
            raise ScoringInputError(
                "dimensions.{}.status is invalid".format(dimension_id)
            )
        statuses[dimension_id] = status
        row: Dict[str, Any] = {
            "label": rules.dimension_labels[dimension_id],
            "status": status,
            "base_weight": _as_json_number(weights[dimension_id], FOUR_DECIMALS),
        }
        if status in rules.score_statuses:
            if "score" not in item:
                raise ScoringInputError(
                    "dimensions.{}.score is required for status {}".format(
                        dimension_id, status
                    )
                )
            score = rules.validate_score(
                item["score"], "dimensions.{}.score".format(dimension_id)
            )
            scores[dimension_id] = score
            row["score"] = _as_json_number(score, ONE_DECIMAL)
            row["evidence"] = _normalise_evidence(
                item.get("evidence"),
                "dimensions.{}.evidence".format(dimension_id),
            )
            concern = item.get("concern")
            if concern is not None:
                if not isinstance(concern, str) or not concern.strip():
                    raise ScoringInputError(
                        "dimensions.{}.concern must be a non-empty string".format(
                            dimension_id
                        )
                    )
                row["concern"] = concern.strip()
        elif "score" in item:
            raise ScoringInputError(
                "dimensions.{}.score must be omitted for status {}".format(
                    dimension_id, status
                )
            )
        else:
            reason = item.get("reason")
            if not isinstance(reason, str) or not reason.strip():
                raise ScoringInputError(
                    "dimensions.{}.reason must explain status {}".format(
                        dimension_id, status
                    )
                )
            row["reason"] = reason.strip()
        dimension_output[dimension_id] = row

    applicable_dimensions = [
        dimension_id
        for dimension_id in rules.dimension_ids
        if statuses[dimension_id] not in rules.excluded_statuses
    ]
    covered_dimensions = [
        dimension_id
        for dimension_id in applicable_dimensions
        if statuses[dimension_id] in rules.score_statuses
    ]
    unknown_dimensions = [
        dimension_id
        for dimension_id in applicable_dimensions
        if statuses[dimension_id] in rules.unknown_statuses
    ]
    applicable_count = len(applicable_dimensions)
    covered_count = len(covered_dimensions)
    dimension_coverage = (
        Decimal(covered_count) / Decimal(applicable_count)
        if applicable_count
        else Decimal("0")
    )

    assessed_weight = sum(
        (weights[dimension_id] for dimension_id in covered_dimensions),
        Decimal("0"),
    )
    applicable_weight = sum(
        (weights[dimension_id] for dimension_id in applicable_dimensions),
        Decimal("0"),
    )
    weighted_coverage = (
        assessed_weight / applicable_weight
        if applicable_weight
        else Decimal("0")
    )
    coverage = weighted_coverage

    weighted_known_sum = sum(
        (weights[dimension_id] * scores[dimension_id] for dimension_id in covered_dimensions),
        Decimal("0"),
    )
    known_score = (
        weighted_known_sum / assessed_weight if assessed_weight else None
    )
    if assessed_weight:
        for dimension_id in covered_dimensions:
            dimension_output[dimension_id]["effective_weight"] = _as_json_number(
                weights[dimension_id] / assessed_weight, FOUR_DECIMALS
            )

    plausible_low: Optional[Decimal]
    plausible_high: Optional[Decimal]
    if applicable_weight:
        plausible_low = weighted_known_sum / applicable_weight
        unknown_weight = sum(
            (weights[dimension_id] for dimension_id in unknown_dimensions),
            Decimal("0"),
        )
        plausible_high = (
            weighted_known_sum + unknown_weight * rules.maximum
        ) / applicable_weight
    else:
        plausible_low = None
        plausible_high = None

    parsed_gates, gate_cap = _parse_gates(review.get("gates", []), rules)

    def apply_cap(value: Optional[Decimal]) -> Optional[Decimal]:
        if value is None or gate_cap is None:
            return value
        return min(value, gate_cap)

    known_after_gate = apply_cap(known_score)
    plausible_low_after_gate = apply_cap(plausible_low)
    plausible_high_after_gate = apply_cap(plausible_high)

    score_reasons: List[str] = []
    if coverage < rules.minimum_coverage:
        score_reasons.append(
            "coverage is below {:.0f}%".format(float(rules.minimum_coverage * 100))
        )
    unassessed_required = [
        dimension_id
        for dimension_id in rules.required_dimensions
        if statuses[dimension_id] not in rules.score_statuses
    ]
    if unassessed_required:
        score_reasons.append(
            "required dimensions are unassessed: {}".format(
                ", ".join(unassessed_required)
            )
        )

    if score_reasons:
        score_status = "N/A"
    elif coverage < rules.provisional_below:
        score_status = "provisional"
    else:
        score_status = "normal"

    rounded_known = (
        known_score.quantize(ONE_DECIMAL, rounding=ROUND_HALF_UP)
        if known_score is not None
        else None
    )
    rounded_after_gate = (
        known_after_gate.quantize(ONE_DECIMAL, rounding=ROUND_HALF_UP)
        if known_after_gate is not None
        else None
    )
    if score_status == "N/A" or rounded_after_gate is None:
        final_score = None
        rating = None
    else:
        final_score = rounded_after_gate
        rating = rules.rating_for(final_score)

    confidence = _score_confidence(review.get("confidence"), rules)
    if confidence["score"] == 0:
        score_reasons.append("assessment confidence is 0")
        score_status = "N/A"
        final_score = None
        rating = None

    return {
        "schema_version": rules.schema_version,
        "paper_type": paper_type,
        "dimensions": dimension_output,
        "coverage": {
            "assessed": covered_count,
            "applicable": applicable_count,
            "excluded_not_applicable": len(rules.dimension_ids) - applicable_count,
            "ratio": _as_json_number(coverage, THREE_DECIMALS),
            "dimension_ratio": _as_json_number(dimension_coverage, THREE_DECIMALS),
            "weighted_ratio": _as_json_number(weighted_coverage, THREE_DECIMALS),
        },
        "gates": {
            "applied": parsed_gates,
            "active_cap": _as_json_number(gate_cap, ONE_DECIMAL),
        },
        "overall": {
            "status": score_status,
            "score": _as_json_number(final_score, ONE_DECIMAL),
            "rating": rating,
            "known_score_before_gate": _as_json_number(rounded_known, ONE_DECIMAL),
            "known_score_after_gate": _as_json_number(rounded_after_gate, ONE_DECIMAL),
            "plausible_range": {
                "minimum": _as_json_number(plausible_low_after_gate, ONE_DECIMAL),
                "maximum": _as_json_number(plausible_high_after_gate, ONE_DECIMAL),
            },
            "reasons": score_reasons,
        },
        "confidence": confidence,
    }


def format_markdown(report: Mapping[str, Any]) -> str:
    """Render a compact, audit-friendly Markdown score report."""
    overall = report["overall"]
    coverage = report["coverage"]
    confidence = report["confidence"]
    score = overall["score"]
    if score is None:
        overall_text = "N/A"
    else:
        overall_text = "{:.1f}/6 — {}".format(score, overall["rating"]["label"])
    plausible = overall["plausible_range"]
    if plausible["minimum"] is None:
        plausible_text = "N/A"
    else:
        plausible_text = "{:.1f}–{:.1f}".format(
            plausible["minimum"], plausible["maximum"]
        )

    lines = [
        "# AAAI Review Score",
        "",
        "- Paper type: `{}`".format(report["paper_type"]),
        "- Score status: **{}**".format(overall["status"]),
        "- Overall: **{}**".format(overall_text),
        "- Coverage: {}/{} dimensions; {:.1f}% weighted".format(
            coverage["assessed"], coverage["applicable"], coverage["weighted_ratio"] * 100
        ),
        "- Plausible range: {}".format(plausible_text),
        "- Confidence: **{}/5 — {}**".format(
            confidence["score"], confidence["label"]
        ),
        "",
        "## Dimension scores",
        "",
        "| Dimension | Status | Score | Base weight | Effective weight | Evidence / reason |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in report["dimensions"].values():
        dimension_score = (
            "{:.1f}".format(item["score"]) if "score" in item else "—"
        )
        effective_weight = (
            "{:.1%}".format(item["effective_weight"])
            if "effective_weight" in item
            else "—"
        )
        lines.append(
            "| {} | `{}` | {} | {:.1%} | {} | {} |".format(
                item["label"],
                item["status"],
                dimension_score,
                item["base_weight"],
                effective_weight,
                "; ".join(item.get("evidence", []))
                or item.get("reason", "—"),
            )
        )

    lines.extend(["", "## Gates", ""])
    applied = report["gates"]["applied"]
    if not applied:
        lines.append("No score gate applied.")
    else:
        for gate in applied:
            lines.append(
                "- **{}** (cap {:.1f}): {} Evidence: {} Resolution: {}".format(
                    gate["id"],
                    gate["cap"],
                    gate["reason"],
                    "; ".join(gate["evidence"]),
                    gate["resolution_condition"],
                )
            )

    lines.extend(
        [
            "",
            "## Confidence components",
            "",
            "- Material: {}/2".format(confidence["components"]["material"]),
            "- Verification: {}/2".format(
                confidence["components"]["verification"]
            ),
            "- Domain match: {}/1".format(
                confidence["components"]["domain_match"]
            ),
        ]
    )
    if overall["reasons"]:
        lines.extend(["", "## Why the overall score is unavailable", ""])
        lines.extend("- " + reason for reason in overall["reasons"])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Score a structured AAAI review (Python 3.9+, standard library only)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Input JSON shape:
  {
    "paper_type": "model_method",
    "dimensions": {
      "significance": {
        "status": "assessed", "score": 4.0,
        "evidence": ["Section 1"], "concern": "Optional note"
      },
      ... all seven dimensions ...
    },
    "gates": [{
      "id": "UNSUPPORTED_CENTRAL_CLAIM",
      "reason": "Why the gate applies",
      "evidence": ["Section 4"],
      "resolution_condition": "Evidence needed to remove the gate"
    }],
    "confidence": {"material": 2, "verification": 1, "domain_match": 0}
  }

Use reason instead of score/evidence for unavailable_to_reviewer or not_applicable.
""",
    )
    parser.add_argument("input", type=Path, help="structured review JSON")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        report = score_review(payload, rules_path=args.rules)
    except (OSError, json.JSONDecodeError, ScoringInputError, ValueError) as error:
        print("aaai_review_score: {}".format(error), file=sys.stderr)
        return 1
    if args.format == "markdown":
        print(format_markdown(report))
    else:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
