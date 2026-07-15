# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-07-15

### Added

- Machine-readable AAAI-27 rule registry with source locations, stages, severity, scope, exceptions, and event-policy requirements
- Bundled stage-aware `.tex` checker with explicit page-limit, technical-appendix, and reproducibility-checklist policies
- Regression tests for commented preambles, multi-package declarations, literal examples, appendix ordering, anonymous links, stage-specific page breaks, and missing artifacts

### Fixed

- Separated Content Appendices, Supplementary/Technical Appendices, and the Reproducibility Checklist into three independently governed artifacts
- Removed the unsupported universal seven-page rule; page limits and reference-page treatment now come from the target event
- Allowed identity-safe links in anonymous submissions while retaining human review for de-anonymization risk
- Replaced the inaccurate 14-item reproducibility summary with all 31 official questions, allowed answers, and gate conditions
- Corrected citations to `(Author Year)`, all three names for three authors, and `et al.` only for four or more authors
- Corrected figure text to at least 9pt, limited DPI checks to bitmaps, and removed duplicated `Figure N:` / `Table N:` prefixes from caption text
- Removed `.bib` as an `\input` exception and made checklist embedding conditional on event policy
- Made page-break, source-package, and camera-ready packaging checks stage-aware
- Replaced blanket “desk reject” claims and false global passes with `ERROR`, `WARNING`, `NEEDS_POLICY`, `NOT_CHECKED`, and scoped `PASS` results
- Removed the runtime dependency on an external, separately installed `aaai-compliance-checker` skill

### Changed

- Updated writing, review, double-blind, figure, outline, README, and example modules to use the same corrected Author Kit model

## [1.0.0] - 2026-07-01

### Added

- Initial open-source release
- 5-phase AAAI paper writing workflow
- 4 paper type specializations
- 34 sentence templates + 15 Before/After rewrite pairs
- 7 caption templates + 8 Before/After rewrite pairs
- AAAI reviewer simulator with scoring calibration
- AAAI 2027 format compliance checker (8 categories)
- 50-paper distilled patterns corpus (AAAI 2023-2026)
- CI: Markdown lint, link checker, stale issue management

[Unreleased]: https://github.com/HansonLegacy/Great-AAAI-Writing-Skills
