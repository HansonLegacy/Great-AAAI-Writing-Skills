#!/usr/bin/env python3
"""Executable AAAI-27 checker. Python 3.9+, standard library only."""

from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


STATUSES = ("ERROR", "WARNING", "NEEDS_POLICY", "NOT_CHECKED", "PASS")
PRIORITY = ("ERROR", "NEEDS_POLICY", "NOT_CHECKED", "WARNING", "PASS")
DEFAULT_RULES = Path(__file__).resolve().parents[1] / "rules" / "aaai27-format-rules.json"


@dataclass(frozen=True)
class Finding:
    status: str
    rule_id: str
    message: str
    line: Optional[int] = None


class RuleBook:
    REQUIRED = {"id", "stage", "level", "scope", "source", "rule"}

    def __init__(self, path: Path):
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.python_requires = payload.get("python_requires")
        self.rules: Dict[str, Dict[str, Any]] = {}
        for rule in payload.get("rules", []):
            missing = self.REQUIRED.difference(rule)
            if missing:
                raise ValueError("{} missing {}".format(rule.get("id"), sorted(missing)))
            if "exception" not in rule and "event_policy" not in rule:
                raise ValueError("{} lacks exception/event_policy".format(rule["id"]))
            if rule["level"] not in STATUSES:
                raise ValueError("{} has invalid level".format(rule["id"]))
            if rule["id"] in self.rules:
                raise ValueError("duplicate rule {}".format(rule["id"]))
            self.rules[rule["id"]] = rule

    def get(self, rule_id: str) -> Dict[str, Any]:
        return self.rules[rule_id]


def _blank(chars: List[str], start: int, end: int) -> None:
    for index in range(start, min(end, len(chars))):
        if chars[index] not in "\r\n":
            chars[index] = " "


def _escaped(text: str, index: int) -> bool:
    count = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        count += 1
        index -= 1
    return bool(count % 2)


def mask_latex(text: str) -> str:
    """Mask comments, inline verb, and literal environments without moving lines."""
    chars = list(text)
    index = 0
    while index < len(text):
        if text.startswith("\\verb", index):
            tail = index + 5
            if tail < len(text) and text[tail].isalpha():
                index += 1
                continue
            if tail < len(text) and text[tail] == "*":
                tail += 1
            if tail < len(text) and not text[tail].isspace():
                delimiter = text[tail]
                close = text.find(delimiter, tail + 1)
                newline = text.find("\n", tail + 1)
                if close >= 0 and (newline < 0 or close < newline):
                    _blank(chars, index, close + 1)
                    index = close + 1
                    continue
        if text[index] == "%" and not _escaped(text, index):
            newline = text.find("\n", index)
            end = len(text) if newline < 0 else newline
            _blank(chars, index, end)
            index = end
            continue
        index += 1

    base = "".join(chars)
    begin_re = re.compile(
        r"\\begin\s*\{\s*(verbatim\*?|lstlisting|minted)\s*\}", re.I
    )
    cursor = 0
    while True:
        begin = begin_re.search(base, cursor)
        if not begin:
            break
        env = begin.group(1)
        end_re = re.compile(r"\\end\s*\{\s*" + re.escape(env) + r"\s*\}", re.I)
        end = end_re.search(base, begin.end())
        finish = len(base) if end is None else end.end()
        _blank(chars, begin.start(), finish)
        cursor = finish
    return "".join(chars)


def line_no(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


@dataclass(frozen=True)
class PackageUse:
    command: str
    package: str
    options: Tuple[str, ...]
    line: int


def parse_packages(preamble: str) -> List[PackageUse]:
    pattern = re.compile(
        r"\\(?P<cmd>usepackage|RequirePackage)\s*"
        r"(?:\[(?P<opts>[^\]]*)\])?\s*\{(?P<pkgs>[^{}]*)\}", re.I
    )
    result: List[PackageUse] = []
    for match in pattern.finditer(preamble):
        options = tuple(
            part.strip().lower()
            for part in (match.group("opts") or "").split(",")
            if part.strip()
        )
        for package in match.group("pkgs").split(","):
            package = package.strip().lower()
            if package:
                result.append(
                    PackageUse(match.group("cmd"), package, options, line_no(preamble, match.start()))
                )
    return result


class Checker:
    def __init__(
        self,
        tex: Path,
        stage: str,
        rules: RuleBook,
        pdf: Optional[Path],
        log: Optional[Path],
        package: Optional[Path],
        page_limit: Optional[int],
        technical_appendix: str,
        checklist: str,
    ):
        self.tex = tex
        self.stage = stage
        self.rules = rules
        self.pdf = pdf
        self.log = log
        self.package = package
        self.page_limit = page_limit
        self.technical_appendix = technical_appendix
        self.checklist = checklist
        self.raw = tex.read_text(encoding="utf-8", errors="replace")
        self.masked = mask_latex(self.raw)
        self.findings: List[Finding] = []
        document = re.search(r"\\begin\s*\{\s*document\s*\}", self.masked)
        self.document = document
        self.preamble = self.masked[: document.start()] if document else self.masked
        self.body = self.masked[document.end() :] if document else ""
        self.body_offset = document.end() if document else len(self.masked)
        self.pdf_pages: Optional[int] = None

    def emit(
        self,
        rule_id: str,
        message: str,
        status: Optional[str] = None,
        position: Optional[int] = None,
        line: Optional[int] = None,
    ) -> None:
        rule = self.rules.get(rule_id)
        if self.stage not in rule["stage"]:
            return
        status = status or rule["level"]
        if line is None and position is not None:
            line = line_no(self.masked, position)
        self.findings.append(Finding(status, rule_id, message, line))

    def run(self) -> Dict[str, Any]:
        self.check_preamble()
        self.check_commands()
        self.check_structure()
        self.check_artifacts()
        self.check_page_limit()
        statuses = {item.status for item in self.findings}
        overall = next((status for status in PRIORITY if status in statuses), "PASS")
        serialized = []
        for item in sorted(
            self.findings,
            key=lambda value: (PRIORITY.index(value.status), value.line or 0, value.rule_id),
        ):
            data = asdict(item)
            rule = self.rules.get(item.rule_id)
            data["scope"] = rule["scope"]
            data["source"] = rule["source"]
            serialized.append(data)
        return {
            "checker": "aaai27_check",
            "python_requires": self.rules.python_requires,
            "stage": self.stage,
            "tex": str(self.tex),
            "overall_status": overall,
            "findings": serialized,
        }

    def check_preamble(self) -> None:
        if not self.document:
            self.emit("structure.maketitle-abstract", "Missing active begin{document}.", line=1)

        classes = list(
            re.finditer(r"\\documentclass\s*(?:\[([^\]]*)\])?\s*\{([^{}]+)\}", self.preamble, re.I)
        )
        if len(classes) != 1:
            self.emit("preamble.documentclass", "Expected one active documentclass.", line=1)
        else:
            options = [part.strip().lower() for part in (classes[0].group(1) or "").split(",") if part.strip()]
            if classes[0].group(2).strip().lower() != "article" or options != ["letterpaper"]:
                self.emit("preamble.documentclass", "Use exactly documentclass[letterpaper]{article}.", position=classes[0].start())
            else:
                self.emit("preamble.documentclass", "Document class is correct.", "PASS")

        packages = parse_packages(self.preamble)
        style = [item for item in packages if item.package == "aaai2027"]
        if len(style) != 1:
            self.emit("preamble.aaai-style", "Expected one active aaai2027 declaration.", line=1)
        else:
            options = set(style[0].options)
            valid = options == {"submission"} if self.stage == "anonymous" else options.issubset({"ccby"}) and "submission" not in options
            if not valid or options.intersection({"draft", "preprint"}):
                self.emit("preamble.aaai-style", "aaai2027 options do not match stage {}.".format(self.stage), line=style[0].line)
            elif options == {"ccby"}:
                self.emit("preamble.aaai-style", "ccby requires explicit AAAI authorization.", "WARNING", line=style[0].line)
            else:
                self.emit("preamble.aaai-style", "aaai2027 mode matches stage.", "PASS")

        required = self.rules.get("preamble.required-lines")
        missing = [
            item["name"] for item in required["requirements"]
            if not re.search(item["pattern"], self.preamble, re.S)
        ]
        if missing:
            self.emit("preamble.required-lines", "Missing active preamble item(s): {}.".format(", ".join(missing)), line=1)
        else:
            self.emit("preamble.required-lines", "Required preamble commands are active.", "PASS")
        for package in packages:
            if package.package in {"natbib", "caption"} and package.options:
                self.emit("preamble.required-lines", "{} must have no options.".format(package.package), line=package.line)

        pdfinfo = self.rules.get("preamble.pdfinfo")
        pdfinfo_blocks = list(
            re.finditer(r"\\pdfinfo\s*\{[^{}]*\}", self.masked, re.S)
        )
        if (
            len(pdfinfo_blocks) == 1
            and re.fullmatch(
                pdfinfo["pattern"], pdfinfo_blocks[0].group(0), re.S
            )
            and (
                self.document is None
                or pdfinfo_blocks[0].end() <= self.document.start()
            )
        ):
            self.emit("preamble.pdfinfo", "pdfinfo block is exact.", "PASS")
        else:
            self.emit(
                "preamble.pdfinfo",
                "Require exactly one pdfinfo block containing only /TemplateVersion (2027.1).",
                line=1,
            )

        forbidden = set(self.rules.get("package.forbidden")["packages"])
        hits = [item for item in packages if item.package in forbidden]
        for hit in hits:
            self.emit("package.forbidden", "Forbidden package {} via {}.".format(hit.package, hit.command), line=hit.line)
        if not hits:
            self.emit("package.forbidden", "No forbidden package declaration found.", "PASS")

        if self.stage == "anonymous":
            rule = self.rules.get("stage.anonymous-author")
            good = re.search(rule["author_pattern"], self.preamble, re.S) and re.search(rule["affiliations_pattern"], self.preamble, re.S)
            if good:
                self.emit("stage.anonymous-author", "Anonymous author block is correct.", "PASS")
            else:
                self.emit("stage.anonymous-author", "Require Anonymous Submission and empty affiliations.", line=1)
        else:
            anonymous = re.search(self.rules.get("stage.camera-author")["anonymous_pattern"], self.preamble, re.S)
            author = re.search(r"\\author\s*\{(.*?)\}", self.preamble, re.S)
            affiliations = re.search(r"\\affiliations\s*\{(.*?)\}", self.preamble, re.S)
            if anonymous or not author or not author.group(1).strip() or not affiliations or not affiliations.group(1).strip():
                self.emit("stage.camera-author", "Camera-ready author/affiliations are missing or anonymous.", line=1)
            else:
                self.emit("stage.camera-author", "Camera-ready author blocks are non-empty.", "PASS")

    def check_commands(self) -> None:
        rule = self.rules.get("command.forbidden")
        hits = 0
        for command in rule["commands"]:
            for match in re.finditer(r"\\" + re.escape(command) + r"\b", self.masked):
                hits += 1
                self.emit("command.forbidden", "Forbidden command \\{}.".format(command), position=match.start())
        for command in rule["layout_assignments"]:
            pattern = r"\\" + re.escape(command) + r"\b\s*(?:=|[-+]?(?:\d+(?:\.\d*)?|\.\d+))"
            for match in re.finditer(pattern, self.masked):
                hits += 1
                self.emit("command.forbidden", "Forbidden assignment to \\{}.".format(command), position=match.start())
        if not hits:
            self.emit("command.forbidden", "No forbidden command invocation found.", "PASS")

        allowed = set(self.rules.get("command.setlength")["allowed_targets"])
        bad_lengths = 0
        for match in re.finditer(r"\\setlength\s*\{\s*\\([A-Za-z@]+)\s*\}\s*\{", self.masked):
            if match.group(1).lower() not in allowed:
                bad_lengths += 1
                self.emit("command.setlength", "Disallowed setlength target \\{}.".format(match.group(1)), position=match.start())
        if not bad_lengths:
            self.emit("command.setlength", "No disallowed setlength target found.", "PASS")

        forbidden_options = set(self.rules.get("command.graphics-cropping")["forbidden_options"])
        crop_hits = 0
        pattern = re.compile(r"\\includegraphics\*?\s*(?:\[([^\]]*)\])?\s*\{", re.S)
        for match in pattern.finditer(self.masked):
            options = {
                part.split("=", 1)[0].strip().lower()
                for part in (match.group(1) or "").split(",") if part.strip()
            }
            bad = sorted(options.intersection(forbidden_options))
            if bad:
                crop_hits += 1
                self.emit("command.graphics-cropping", "Forbidden includegraphics option(s): {}.".format(", ".join(bad)), position=match.start())
        if not crop_hits:
            self.emit("command.graphics-cropping", "No in-LaTeX crop options found.", "PASS")

        page_rule = "command.page-break.anonymous" if self.stage == "anonymous" else "command.page-break.camera-ready"
        page_hits = 0
        for command in self.rules.get(page_rule)["commands"]:
            for match in re.finditer(r"\\" + command + r"\b", self.body):
                page_hits += 1
                status = "WARNING" if self.stage == "anonymous" else "ERROR"
                self.emit(page_rule, "\\{} requires {} handling.".format(command, self.stage), status, position=self.body_offset + match.start())
        if not page_hits:
            self.emit(page_rule, "No manual page break found.", "PASS")

    def check_structure(self) -> None:
        end_document = re.search(r"\\end\s*\{\s*document\s*\}", self.masked)
        if not end_document:
            self.emit("structure.maketitle-abstract", "Missing active end{document}.", line=self.raw.count("\n") + 1)

        begins = list(re.finditer(r"\\begin\s*\{\s*abstract\s*\}", self.masked))
        ends = list(re.finditer(r"\\end\s*\{\s*abstract\s*\}", self.masked))
        maketitles = list(re.finditer(r"\\maketitle\b", self.masked))
        abstract_end: Optional[int] = None
        if len(begins) != 1 or len(ends) != 1 or ends[0].start() <= begins[0].end():
            self.emit("structure.maketitle-abstract", "Expected one complete abstract.", line=1)
        else:
            abstract_end = ends[0].end()
            if len(maketitles) != 1 or maketitles[0].start() > begins[0].start():
                self.emit("structure.maketitle-abstract", "maketitle must precede abstract.", position=begins[0].start())
            else:
                self.emit("structure.maketitle-abstract", "maketitle/abstract order is valid.", "PASS")
            text = self.masked[begins[0].end() : ends[0].start()]
            cite_re = re.compile(self.rules.get("abstract.no-citations")["citation_pattern"])
            citations = list(cite_re.finditer(text))
            for citation in citations:
                self.emit("abstract.no-citations", "Citation {} in abstract.".format(citation.group(0)), position=begins[0].end() + citation.start())
            if not citations:
                self.emit("abstract.no-citations", "No citation command in abstract.", "PASS")

        section_re = re.compile(r"\\section(?P<star>\*)?\s*\{(?P<title>[^{}]*)\}")
        sections = list(section_re.finditer(self.masked))
        first_section = sections[0].start() if sections else None
        link_begins = list(re.finditer(r"\\begin\s*\{\s*links\s*\}", self.masked))
        link_ends = list(re.finditer(r"\\end\s*\{\s*links\s*\}", self.masked))
        link_ok = len(link_begins) == len(link_ends) and len(link_begins) <= 1
        if link_ok and link_begins:
            link_ok = abstract_end is not None and link_begins[0].start() >= abstract_end and link_ends[0].start() > link_begins[0].end() and (first_section is None or link_ends[0].end() <= first_section)
        if not link_ok:
            self.emit("structure.links", "links must be complete and between abstract and main body.", line=1)
        elif link_begins and self.stage == "anonymous":
            self.emit(
                "structure.links",
                "Anonymous links position is valid, but URL identity safety requires manual review.",
                "NOT_CHECKED",
            )
        else:
            self.emit("structure.links", "Optional links placement is valid.", "PASS")

        bibliographies = list(re.finditer(r"\\bibliography\s*\{([^{}]+)\}", self.masked))
        bib_pos = bibliographies[0].start() if bibliographies else None
        if len(bibliographies) != 1:
            self.emit("bibliography.style", "Expected exactly one bibliography command.", line=1)
        manual = list(re.finditer(r"\\bibliographystyle\s*\{", self.masked))
        for match in manual:
            self.emit("bibliography.style", "Manual bibliographystyle is forbidden.", position=match.start())
        if len(bibliographies) == 1 and not manual:
            self.emit("bibliography.style", "Bibliography invocation is valid.", "PASS")

        appendices = list(re.finditer(r"\\appendix\b", self.masked))
        bad_appendices = [match for match in appendices if bib_pos is not None and match.start() > bib_pos]
        for match in bad_appendices:
            self.emit("structure.content-appendix", "Content appendix appears after References.", position=match.start())
        if not bad_appendices:
            self.emit("structure.content-appendix", "Content appendices precede References.", "PASS")

        order_rule = self.rules.get("structure.order")
        supplement_titles = {title.casefold() for title in order_rule["supplement_titles"]}
        supplements = []
        ethics = []
        acknowledgments = []
        order_errors = 0
        ordinary_sections = []
        for section in sections:
            title = section.group("title").strip()
            folded = title.casefold()
            if folded in supplement_titles:
                supplements.append(section)
            elif bib_pos is not None and section.start() > bib_pos:
                order_errors += 1
                self.emit("structure.order", "Non-supplement section after References: {}.".format(title), position=section.start())
            if folded not in supplement_titles and folded not in {
                order_rule["ethical_title"].casefold(),
                order_rule["acknowledgments_title"].casefold(),
            }:
                ordinary_sections.append(section)
            if folded == order_rule["ethical_title"].casefold():
                ethics.append(section)
                if not section.group("star"):
                    order_errors += 1
                    self.emit("structure.order", "Ethical Statement must use section*.", position=section.start())
            if folded == order_rule["acknowledgments_title"].casefold():
                acknowledgments.append(section)
                if not section.group("star"):
                    order_errors += 1
                    self.emit("structure.order", "Acknowledgments must use section*.", position=section.start())
        if ethics and acknowledgments and ethics[0].start() > acknowledgments[0].start():
            order_errors += 1
            self.emit("structure.order", "Ethical Statement must precede Acknowledgments.", position=ethics[0].start())
        if any(bib_pos is not None and item.start() > bib_pos for item in ethics + acknowledgments):
            order_errors += 1
            self.emit("structure.order", "Ethics/Acknowledgments must precede References.", line=1)
        terminal_sections = ethics + acknowledgments
        if terminal_sections:
            terminal_start = min(item.start() for item in terminal_sections)
            for section in ordinary_sections:
                if section.start() > terminal_start and (
                    bib_pos is None or section.start() < bib_pos
                ):
                    order_errors += 1
                    self.emit(
                        "structure.order",
                        "Main/content section appears after the terminal Ethics/Acknowledgments sequence: {}.".format(
                            section.group("title").strip()
                        ),
                        position=section.start(),
                    )
        if not order_errors:
            self.emit("structure.order", "Detected section order is valid.", "PASS")

        self.check_inputs(bib_pos)
        self.check_technical(supplements, bib_pos)
        self.emit(
            "citation.author-count",
            "Rendered citation punctuation and the three-author/four-author threshold require PDF/manual verification.",
            "NOT_CHECKED",
        )

    def check_inputs(self, bib_pos: Optional[int]) -> None:
        pattern = re.compile(r"\\(?P<cmd>input|include)\s*\{(?P<arg>[^{}]+)\}")
        checklist_file = self.rules.get("structure.single-source")["checklist_filename"]
        checklist_inputs = []
        misplaced_checklist_inputs = []
        other_inputs = []
        end_document = re.search(r"\\end\s*\{\s*document\s*\}", self.masked)
        for match in pattern.finditer(self.masked):
            command = match.group("cmd")
            argument = match.group("arg").strip()
            if argument.lower().endswith(".bib"):
                self.emit("structure.bib-input", "Do not {} .bib; use bibliography.".format(command), position=match.start())
            elif command == "input" and argument == checklist_file:
                if (
                    bib_pos is not None
                    and match.start() > bib_pos
                    and end_document is not None
                    and match.start() < end_document.start()
                ):
                    checklist_inputs.append(match)
                else:
                    misplaced_checklist_inputs.append(match)
            else:
                other_inputs.append(match)
        if self.stage == "camera-ready":
            for match in other_inputs:
                self.emit("structure.single-source", "Camera-ready source split: {}.".format(match.group(0)), position=match.start())
            if not other_inputs:
                self.emit("structure.single-source", "No camera-ready source split found.", "PASS")
        else:
            for match in other_inputs:
                self.emit("structure.input.anonymous", "Anonymous source split needs event policy: {}.".format(match.group(0)), "NEEDS_POLICY", position=match.start())
            if not other_inputs:
                self.emit("structure.input.anonymous", "No anonymous source split found.", "PASS")

        if self.checklist == "unknown":
            self.emit("structure.checklist", "Checklist delivery policy is unknown.", "NEEDS_POLICY")
        elif self.checklist == "embedded":
            for match in misplaced_checklist_inputs:
                self.emit(
                    "structure.checklist",
                    "Embedded checklist input must occur after bibliography and before end{document}.",
                    "ERROR",
                    position=match.start(),
                )
            if len(checklist_inputs) != 1:
                self.emit("structure.checklist", "Embedded policy requires exact input{ReproducibilityChecklist.tex}.", "ERROR", line=1)
            else:
                self.emit("structure.checklist", "Exact embedded checklist input found.", "PASS")
        elif checklist_inputs or misplaced_checklist_inputs:
            for match in checklist_inputs + misplaced_checklist_inputs:
                self.emit("structure.checklist", "Checklist must not be embedded under {} policy.".format(self.checklist), "ERROR", position=match.start())
        else:
            self.emit("structure.checklist", "Checklist embedding matches policy.", "PASS")

    def check_technical(self, supplements: Sequence[re.Match[str]], bib_pos: Optional[int]) -> None:
        policy = self.technical_appendix
        if policy == "unknown":
            self.emit("structure.technical-appendix", "Technical appendix policy is unknown.", "NEEDS_POLICY")
        elif policy in {"separate", "forbidden"} and supplements:
            for section in supplements:
                self.emit("structure.technical-appendix", "Inline {} conflicts with {} policy.".format(section.group("title"), policy), "ERROR", position=section.start())
        elif policy == "inline":
            misplaced = [section for section in supplements if bib_pos is None or section.start() < bib_pos]
            for section in misplaced:
                self.emit("structure.technical-appendix", "Inline technical appendix must follow References.", "ERROR", position=section.start())
            if not misplaced:
                self.emit("structure.technical-appendix", "Inline technical appendix placement matches policy.", "PASS")
        else:
            self.emit("structure.technical-appendix", "No inline technical appendix conflicts with policy.", "PASS")

    def check_artifacts(self) -> None:
        self.check_pdf()
        self.check_log()
        self.check_package()

    def check_pdf(self) -> None:
        if self.pdf is None:
            self.emit("artifact.pdf", "No PDF supplied.", "NOT_CHECKED")
            return
        if not self.pdf.is_file():
            self.emit("artifact.pdf", "PDF path is not a file.", "ERROR")
            return
        data = self.pdf.read_bytes()
        errors = []
        header = re.match(br"%PDF-(\d+)\.(\d+)", data[:16])
        if not header:
            errors.append("invalid PDF header")
        elif (int(header.group(1)), int(header.group(2))) < (1, 5):
            errors.append("PDF version below 1.5")
        if b"/Encrypt" in data:
            errors.append("encrypted PDF")
        if re.search(br"/Subtype\s*/Type3\b", data):
            errors.append("Type 3 font")
        self.pdf_pages = len(re.findall(br"/Type\s*/Page\b", data)) or None
        for error in errors:
            self.emit("artifact.pdf", error + ".", "ERROR")
        if not errors:
            self.emit("artifact.pdf", "Basic PDF header/encryption/Type3 checks passed.", "PASS")
            self.emit(
                "artifact.pdf",
                "Visible layout, complete font embedding, headers/footers/page numbers, links/bookmarks, and figure quality require external or manual inspection.",
                "NOT_CHECKED",
            )

    def check_log(self) -> None:
        if self.log is None:
            self.emit("artifact.log", "No LaTeX log supplied.", "NOT_CHECKED")
            return
        if not self.log.is_file():
            self.emit("artifact.log", "Log path is not a file.", "ERROR")
            return
        text = self.log.read_text(encoding="utf-8", errors="replace")
        match = re.search(r"Overfull \\[hv]box|^! (?:LaTeX|Package|pdfTeX) Error", text, re.I | re.M)
        if match:
            self.emit("artifact.log", "Build error or overfull box found.", "ERROR", line=line_no(text, match.start()))
        else:
            self.emit("artifact.log", "No explicit error/overfull box found.", "PASS")

    def check_package(self) -> None:
        rule_id = "artifact.package.anonymous" if self.stage == "anonymous" else "artifact.package"
        if self.package is None:
            self.emit(rule_id, "No submission package supplied.", "NOT_CHECKED")
            return
        if not self.package.exists():
            self.emit(rule_id, "Package path does not exist.", "ERROR")
            return
        try:
            if self.package.is_dir():
                files = [item for item in self.package.rglob("*") if item.is_file()]
                names = [item.relative_to(self.package).as_posix() for item in files]
                size = sum(item.stat().st_size for item in files)
            elif zipfile.is_zipfile(self.package):
                with zipfile.ZipFile(self.package) as archive:
                    names = [item.filename for item in archive.infolist() if not item.is_dir()]
                size = self.package.stat().st_size
            else:
                raise ValueError("package is not a directory or zip")
        except (OSError, ValueError, zipfile.BadZipFile) as error:
            self.emit(rule_id, str(error) + ".", "ERROR")
            return
        if self.stage == "anonymous":
            self.emit(rule_id, "Anonymous package is readable; naming/content remain event-specific.", "PASS")
            return
        errors = []
        main_tex = [name for name in names if name.lower().endswith(".tex") and Path(name).name != "ReproducibilityChecklist.tex"]
        if len(main_tex) != 1:
            errors.append("camera-ready package needs one main tex")
        for suffix in (".bib", ".pdf", ".bbl", ".aux"):
            if not any(name.lower().endswith(suffix) for name in names):
                errors.append("missing {}".format(suffix))
        if size > 10 * 1024 * 1024:
            errors.append("archive exceeds 10 MB")
        for error in errors:
            self.emit(rule_id, error + ".", "ERROR")
        if not errors:
            self.emit(rule_id, "Basic camera-ready package checks passed.", "PASS")

    def check_page_limit(self) -> None:
        if self.page_limit is None:
            self.emit(
                "page.limit",
                "No event page limit supplied; resolve the conference-specific page policy.",
                "NEEDS_POLICY",
            )
            return
        if self.page_limit <= 0:
            self.emit("page.limit", "page-limit must be positive.", "ERROR")
        elif self.pdf_pages is None:
            self.emit("page.limit", "PDF page count unavailable.", "NOT_CHECKED")
        elif self.pdf_pages <= self.page_limit:
            self.emit("page.limit", "Total PDF pages do not exceed supplied limit.", "PASS")
        else:
            self.emit("page.limit", "Total pages exceed limit; manually separate references from main text.", "NOT_CHECKED")


def run_check(
    tex: Path,
    *,
    stage: str,
    rules_path: Path = DEFAULT_RULES,
    pdf: Optional[Path] = None,
    log: Optional[Path] = None,
    package: Optional[Path] = None,
    page_limit: Optional[int] = None,
    technical_appendix: str = "unknown",
    checklist: str = "unknown",
) -> Dict[str, Any]:
    return Checker(
        tex, stage, RuleBook(rules_path), pdf, log, package,
        page_limit, technical_appendix, checklist,
    ).run()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AAAI-27 checker (Python 3.9+, standard library only)")
    parser.add_argument("tex", type=Path)
    parser.add_argument("--stage", required=True, choices=("anonymous", "camera-ready"))
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--package", type=Path)
    parser.add_argument("--page-limit", type=int)
    parser.add_argument("--technical-appendix", choices=("unknown", "inline", "separate", "forbidden"), default="unknown")
    parser.add_argument("--checklist", choices=("unknown", "embedded", "separate", "not-required"), default="unknown")
    parser.add_argument("--rules", type=Path, default=DEFAULT_RULES)
    parser.add_argument("--json", action="store_true")
    return parser


def format_text(report: Dict[str, Any]) -> str:
    lines = ["AAAI-27 format check", "Stage: " + report["stage"], "Overall: " + report["overall_status"], ""]
    for item in report["findings"]:
        location = " line {}".format(item["line"]) if item["line"] else ""
        lines.append("[{}] {}{}: {}".format(item["status"], item["rule_id"], location, item["message"]))
        lines.append("  Source: {}:{}".format(item["source"]["file"], item["source"]["lines"]))
    return "\n".join(lines)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if not args.tex.is_file():
        print("tex file not found: {}".format(args.tex), file=sys.stderr)
        return 1
    try:
        report = run_check(
            args.tex, stage=args.stage, rules_path=args.rules, pdf=args.pdf,
            log=args.log, package=args.package, page_limit=args.page_limit,
            technical_appendix=args.technical_appendix, checklist=args.checklist,
        )
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print("aaai27_check: {}".format(error), file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else format_text(report))
    if report["overall_status"] == "ERROR":
        return 1
    if report["overall_status"] in {"NEEDS_POLICY", "NOT_CHECKED"}:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
