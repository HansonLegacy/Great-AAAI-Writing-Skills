# AAAI 2023-2026 Best Paper Corpus

## Overview

This directory contains the 50-paper corpus used to distill writing patterns for the AAAI Writing Skill. All papers are AAAI award-winning papers (oral, distinguished paper, best paper finalists) from 2023 to 2026.

## Structure

```
paper-corpus/
├── README.md                  # This file
├── corpus_summary.json        # Structured metadata for all 50 papers
├── corpus_summary_v2.json     # Extended metadata (v2)
├── analysis_report.txt        # Quantitative analysis of writing patterns
├── YYYY_NN_Title.txt          # Raw extracted text (50 files)
└── clean_abstracts/           # Cleaned abstract-only extracts
    └── YYYY_NN_Title.txt
```

## File Naming Convention

```
YYYY_NN_Short_Title.txt
```

- `YYYY` — Publication year (2023-2026)
- `NN` — Sequential number (01-50)
- `Short Title` — Paper title (underscore_separated)

## Usage

These files are **reference data**, not loaded by Claude Code at runtime. They were used offline to:
1. Extract statistical norms (word counts, structure frequencies)
2. Build sentence templates from recurring patterns
3. Provide non-scoring writing and presentation references for the reviewer simulator; the positive-only corpus is not used to infer acceptance thresholds
4. Identify AAAI-specific writing conventions

## Copyright Note

These extracts contain short excerpts from published AAAI papers for the purpose of academic writing analysis. Full papers are available in the AAAI Digital Library.

**If you are a copyright holder and have concerns about any excerpt**, please open a GitHub Issue and we will remove it promptly.

## Contributing New Papers

To add a new paper to the corpus:
1. Ensure the paper is an AAAI award-winning paper (oral, distinguished paper, or best paper)
2. Extract the paper text following the existing format
3. Add metadata to `corpus_summary.json`
4. Submit a PR with the `corpus` label
