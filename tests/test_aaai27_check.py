import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "aaai27_check.py"
RULES = ROOT / "rules" / "aaai27-format-rules.json"
SPEC = importlib.util.spec_from_file_location("aaai27_check", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
CHECKER = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = CHECKER
SPEC.loader.exec_module(CHECKER)


def manuscript(stage="anonymous", body_extra="", preamble_extra="", after_refs=""):
    style = (
        r"\usepackage[submission]{aaai2027}"
        if stage == "anonymous"
        else r"\usepackage{aaai2027}"
    )
    author = (
        "\\author{Anonymous Submission}\n\\affiliations{}"
        if stage == "anonymous"
        else "\\author{Alice Example}\n\\affiliations{Example University}"
    )
    return (
        "\\documentclass[letterpaper]{article}\n"
        + style
        + "\n"
        + "\\usepackage[hyphens]{url}\n"
        + "\\usepackage{graphicx}\n"
        + "\\urlstyle{rm}\n"
        + "\\def\\UrlFont{\\rm}\n"
        + "\\usepackage{natbib}\n"
        + "\\usepackage{caption}\n"
        + "\\frenchspacing\n"
        + "\\pdfinfo{/TemplateVersion (2027.1)}\n"
        + preamble_extra
        + "\n"
        + author
        + "\n\\begin{document}\n"
        + "\\maketitle\n"
        + "\\begin{abstract}\nClean abstract.\n\\end{abstract}\n"
        + body_extra
        + "\n\\section{Introduction}\nText.\n"
        + "\\bibliography{refs}\n"
        + after_refs
        + "\n\\end{document}\n"
    )


class AAAI27CheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def run_source(
        self,
        source,
        stage="anonymous",
        technical_appendix="forbidden",
        checklist="not-required",
        **artifacts,
    ):
        tex = self.directory / "paper.tex"
        tex.write_text(source, encoding="utf-8")
        return CHECKER.run_check(
            tex,
            stage=stage,
            rules_path=RULES,
            technical_appendix=technical_appendix,
            checklist=checklist,
            **artifacts,
        )

    @staticmethod
    def findings(report, rule_id, status=None):
        return [
            item
            for item in report["findings"]
            if item["rule_id"] == rule_id
            and (status is None or item["status"] == status)
        ]

    def test_commented_required_line_does_not_count(self):
        source = manuscript().replace("\\frenchspacing\n", "% \\frenchspacing\n")
        report = self.run_source(source)
        errors = self.findings(report, "preamble.required-lines", "ERROR")
        self.assertTrue(errors)
        self.assertIn("frenchspacing", errors[0]["message"])

    def test_geometry_in_multi_package_declaration_is_detected_case_insensitively(self):
        source = manuscript(preamble_extra="\\usepackage{booktabs,Geometry}")
        report = self.run_source(source)
        errors = self.findings(report, "package.forbidden", "ERROR")
        self.assertTrue(any("geometry" in item["message"] for item in errors))

    def test_requirepackage_multi_package_is_parsed(self):
        source = manuscript(preamble_extra="\\RequirePackage{booktabs,HYPERREF}")
        report = self.run_source(source)
        errors = self.findings(report, "package.forbidden", "ERROR")
        self.assertTrue(any("hyperref" in item["message"] for item in errors))

    def test_prose_clip_true_is_not_a_graphics_violation(self):
        prose = (
            "The forbidden example is "
            "\\textbackslash includegraphics*[clip=true, viewport 0 0 10 10]."
        )
        report = self.run_source(manuscript(body_extra=prose))
        self.assertFalse(
            self.findings(report, "command.graphics-cropping", "ERROR")
        )

    def test_real_includegraphics_crop_option_is_detected(self):
        report = self.run_source(
            manuscript(body_extra="\\includegraphics[width=2cm,trim=1 1 1 1]{x.pdf}")
        )
        self.assertTrue(
            self.findings(report, "command.graphics-cropping", "ERROR")
        )

    def test_comments_and_literal_code_are_masked(self):
        literal = (
            "% \\usepackage{geometry}\n"
            "\\begin{verbatim}\n\\usepackage{geometry}\n\\citep{x}\n\\end{verbatim}\n"
            "\\begin{lstlisting}\n\\RequirePackage{hyperref}\n\\end{lstlisting}\n"
            "\\begin{minted}{tex}\n\\usepackage{float}\n\\end{minted}\n"
            "\\verb|\\usepackage{geometry}|"
        )
        report = self.run_source(manuscript(body_extra=literal))
        self.assertFalse(self.findings(report, "package.forbidden", "ERROR"))

    def test_content_appendix_after_references_is_error(self):
        report = self.run_source(
            manuscript(after_refs="\\appendix\n\\section{Details}\n")
        )
        errors = self.findings(report, "structure.content-appendix", "ERROR")
        self.assertTrue(errors)

    def test_anonymous_safe_links_are_not_blanket_banned(self):
        links = (
            "\\begin{links}\n"
            "\\link{Code}{https://anonymous.example/code}\n"
            "\\end{links}\n"
        )
        report = self.run_source(manuscript(body_extra=links))
        self.assertFalse(self.findings(report, "structure.links", "ERROR"))
        self.assertFalse(self.findings(report, "structure.links", "WARNING"))
        unchecked = self.findings(report, "structure.links", "NOT_CHECKED")
        self.assertTrue(any("manual review" in item["message"] for item in unchecked))

    def test_page_break_is_warning_for_anonymous_and_error_for_camera_ready(self):
        anonymous = self.run_source(manuscript(body_extra="\\newpage"))
        self.assertTrue(
            self.findings(anonymous, "command.page-break.anonymous", "WARNING")
        )
        camera = self.run_source(
            manuscript(stage="camera-ready", body_extra="\\newpage"),
            stage="camera-ready",
        )
        self.assertTrue(
            self.findings(camera, "command.page-break.camera-ready", "ERROR")
        )

    def test_bib_input_is_never_an_input_exception(self):
        report = self.run_source(manuscript(body_extra="\\input{refs.bib}"))
        self.assertTrue(self.findings(report, "structure.bib-input", "ERROR"))

    def test_checklist_requires_exact_name_and_embedded_policy(self):
        exact = self.run_source(
            manuscript(after_refs="\\input{ReproducibilityChecklist.tex}"),
            checklist="embedded",
        )
        self.assertTrue(self.findings(exact, "structure.checklist", "PASS"))
        wrong = self.run_source(
            manuscript(after_refs="\\input{sub/ReproducibilityChecklist.tex}"),
            checklist="embedded",
        )
        self.assertTrue(self.findings(wrong, "structure.checklist", "ERROR"))

    def test_anonymous_source_split_needs_policy_not_camera_error(self):
        report = self.run_source(manuscript(body_extra="\\input{method.tex}"))
        self.assertTrue(
            self.findings(report, "structure.input.anonymous", "NEEDS_POLICY")
        )
        self.assertFalse(self.findings(report, "structure.single-source", "ERROR"))

    def test_missing_artifacts_force_not_checked_overall(self):
        report = self.run_source(manuscript(), page_limit=7)
        self.assertEqual(report["overall_status"], "NOT_CHECKED")
        self.assertTrue(self.findings(report, "artifact.pdf", "NOT_CHECKED"))
        self.assertTrue(self.findings(report, "artifact.log", "NOT_CHECKED"))
        self.assertTrue(
            self.findings(report, "artifact.package.anonymous", "NOT_CHECKED")
        )

    def test_anonymous_package_does_not_apply_camera_single_tex_rules(self):
        package = self.directory / "upload"
        package.mkdir()
        (package / "main.tex").write_text("", encoding="utf-8")
        (package / "section.tex").write_text("", encoding="utf-8")
        report = self.run_source(manuscript(), package=package)
        self.assertFalse(
            self.findings(report, "artifact.package.anonymous", "ERROR")
        )
        self.assertTrue(
            self.findings(report, "artifact.package.anonymous", "PASS")
        )

    def test_unknown_event_policies_are_explicit(self):
        report = self.run_source(
            manuscript(), technical_appendix="unknown", checklist="unknown"
        )
        self.assertTrue(
            self.findings(report, "structure.technical-appendix", "NEEDS_POLICY")
        )
        self.assertTrue(
            self.findings(report, "structure.checklist", "NEEDS_POLICY")
        )

    def test_author_count_rule_is_documentary_not_source_guessing(self):
        data = json.loads(RULES.read_text(encoding="utf-8"))
        rule = next(
            item for item in data["rules"] if item["id"] == "citation.author-count"
        )
        self.assertFalse(rule["automated"])
        self.assertIn("three authors", rule["rule"])
        self.assertIn("four or more", rule["rule"])

    def test_second_pdfinfo_block_is_rejected(self):
        source = manuscript(
            preamble_extra="\\pdfinfo{/Author (Leaked Author)}"
        )
        report = self.run_source(source)
        self.assertTrue(self.findings(report, "preamble.pdfinfo", "ERROR"))

    def test_extra_key_in_single_pdfinfo_block_is_rejected(self):
        source = manuscript().replace(
            "\\pdfinfo{/TemplateVersion (2027.1)}",
            "\\pdfinfo{/TemplateVersion (2027.1) /Author (Leaked Author)}",
        )
        report = self.run_source(source)
        self.assertTrue(self.findings(report, "preamble.pdfinfo", "ERROR"))

    def test_embedded_checklist_after_end_document_is_rejected(self):
        source = manuscript() + "\\input{ReproducibilityChecklist.tex}\n"
        report = self.run_source(source, checklist="embedded")
        errors = self.findings(report, "structure.checklist", "ERROR")
        self.assertTrue(any("before end{document}" in item["message"] for item in errors))

    def test_embedded_checklist_before_bibliography_is_rejected(self):
        source = manuscript(body_extra="\\input{ReproducibilityChecklist.tex}")
        report = self.run_source(source, checklist="embedded")
        errors = self.findings(report, "structure.checklist", "ERROR")
        self.assertTrue(any("after bibliography" in item["message"] for item in errors))

    def test_second_pdfinfo_in_document_body_is_rejected(self):
        source = manuscript(body_extra="\\pdfinfo{/Author (Leaked Author)}")
        report = self.run_source(source)
        self.assertTrue(self.findings(report, "preamble.pdfinfo", "ERROR"))

    def test_main_section_after_ethics_is_rejected(self):
        source = manuscript().replace(
            "\\bibliography{refs}",
            "\\section*{Ethical Statement}\nEthics.\n"
            "\\section{Late Main Result}\nLate.\n"
            "\\section*{Acknowledgments}\nThanks.\n"
            "\\bibliography{refs}",
        )
        report = self.run_source(source)
        errors = self.findings(report, "structure.order", "ERROR")
        self.assertTrue(any("terminal Ethics" in item["message"] for item in errors))

    def test_main_section_after_acknowledgments_is_rejected(self):
        source = manuscript().replace(
            "\\bibliography{refs}",
            "\\section*{Acknowledgments}\nThanks.\n"
            "\\section{Late Main Result}\nLate.\n"
            "\\bibliography{refs}",
        )
        report = self.run_source(source)
        self.assertTrue(self.findings(report, "structure.order", "ERROR"))

    def test_citation_author_count_is_emitted_as_not_checked(self):
        report = self.run_source(manuscript())
        unchecked = self.findings(report, "citation.author-count", "NOT_CHECKED")
        self.assertEqual(len(unchecked), 1)

    def test_supplied_pdf_retains_manual_not_checked_items(self):
        pdf = self.directory / "paper.pdf"
        pdf.write_bytes(
            b"%PDF-1.5\n1 0 obj << /Type /Page /MediaBox [0 0 612 792] >> endobj\n%%EOF"
        )
        report = self.run_source(manuscript(), pdf=pdf)
        self.assertTrue(self.findings(report, "artifact.pdf", "PASS"))
        unchecked = self.findings(report, "artifact.pdf", "NOT_CHECKED")
        self.assertTrue(any("Visible layout" in item["message"] for item in unchecked))

    def test_missing_page_limit_requires_policy(self):
        report = self.run_source(manuscript())
        self.assertTrue(self.findings(report, "page.limit", "NEEDS_POLICY"))
        self.assertEqual(report["overall_status"], "NEEDS_POLICY")


if __name__ == "__main__":
    unittest.main()
