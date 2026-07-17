<div align="center">
  <img src="assets/header-banner.png" width="100%" alt="Great AAAI Writing Skills — AI-powered structured writing system for AAAI 2027" />
</div>

<div align="center">

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?color=blue)](LICENSE)
[![Version: 1.0.2](https://img.shields.io/badge/version-1.0.2-2ea44f.svg)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-6C3C99?color=6C3C99)](https://claude.ai/code)
[![Codex CLI](https://img.shields.io/badge/Codex-CLI-000000?color=000000)](https://github.com/openai/codex)
[![AAAI 2027](https://img.shields.io/badge/AAAI-2027-1a5276?color=1a5276)](https://aaai.org/conference/aaai/aaai-27/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?color=brightgreen)](CONTRIBUTING.md)

[中文](README.md) · **English**

</div>

---

## What Is This?

**Great AAAI Writing Skills** is a Claude Code / Codex CLI skill purpose-built for AAAI 2027 paper writing.

- 📄 **50 AAAI award-winning papers distilled** — writing patterns from AAAI 2023–2026 Oral, Distinguished, and Best Paper winners systematically extracted into reusable templates, sentence patterns, and strategies
- 📋 **Layered 2027 format checks** — separates Author Kit rules, event-specific policy, and human-only checks;
  source-verifiable rules are automated, while missing PDF/log/package artifacts are reported as `NOT_CHECKED`
- 🧠 **Not a one-click generator** — it won't write your paper for you, but it gives you evidence-backed, sentence-level, actionable guidance at every stage

Describe your research. The skill handles orchestration, templates, self-checks, and review simulation.

---

## 🚀 Quick Start

```bash
# Claude Code
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git ~/.claude/skills/aaai-writing

# Codex CLI (OpenAI)
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git ~/.codex/skills/aaai-writing

# Windows
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git %USERPROFILE%\.claude\skills\aaai-writing
```

> 💡 Works with **Claude Code** and **Codex CLI** — same `SKILL.md` format. The skill auto-activates when you mention writing an AAAI paper.

> ⚡ **Prerequisite**: [Claude Code](https://claude.ai/code) or [Codex CLI](https://github.com/openai/codex) installed.

---

## 📖 What You Can Do

### 📝 Get Per-Section Draft Feedback

> *"I have a draft of my Method section. Help me improve it."*
> *"My Introduction doesn't flow well. What should I fix?"*

Drop in a draft of any section. The skill loads the corresponding module (`sections/method.md`, `sections/introduction.md`, etc.) and gives you **line-by-line suggestions** based on patterns distilled from 50 award-winning AAAI papers — not generic writing tips.

| Section | What It Checks |
|---------|---------------|
| Title | Is it searchable? Does it encode the paper type? Does it include a memorable 3–10 character abbreviation? |
| Abstract | Does it follow the 5-step arc? Is it 140–180 words? Are there forbidden `\cite` commands? |
| Introduction | Does it follow the 6-paragraph skeleton? Are pain points quantified? Do contributions align 1:1 with innovations? |
| Method | Is there a clear overview figure? Are design choices motivated? Is the notation consistent? |
| Experiments | Does each claim have a matching experiment? Are ablations complete? Are baselines comprehensive? |
| Related Work | Is it thematic (not author-list)? Does it end with a clear gap statement? |
| Conclusion | Is it ≤ 0.5 pages? Does it include honest limitations? Is the future work specific? |

### 🔍 Run an AI-Powered Peer Review

> *"Review my full paper as if you were an AAAI PC member."*

The built-in **review simulator** produces an evidence-backed **0–6 Scientific Overall Score** across seven dimensions:
significance, novelty, soundness, evidence, clarity, related work, and reproducibility. It also reports an independent **0–5 Assessment Confidence**.
Paper-type weights, missing-information handling, scientific gates, and recommendation bands are reproducible; format and anonymity statuses remain separate.
This is a diagnostic simulation, not an official AAAI scale or acceptance probability.
Every report ends with a fixed two-line footer containing the Final Overall Score and Assessment Confidence.

You also get access to **65+ red-flag trigger words** (with regex-ready patterns) that reviewers commonly flag: `"novel"`, `"first to"`, `"significantly outperforms"`, `"extensive experiments demonstrate"`, and more. Run a quick grep before submitting.

### 📋 Check Your .tex for Format Violations

> *"Is my paper.tex compliant with the AAAI 2027 Author Kit?"*

The built-in checker uses explicit `anonymous` / `camera-ready` profiles to inspect forbidden packages and commands,
active preamble declarations, abstract citations, section order, `\input` use, and the boundaries among content appendices,
technical appendices, and the reproducibility checklist. Page limits and supplementary-material policy come from the target event;
identity-safe anonymous `links` are not blanket-rejected.

```bash
python scripts/aaai27_check.py paper.tex --stage anonymous \
  --technical-appendix unknown --checklist unknown
```

Works on **macOS, Linux, and Windows**. Source checks do not replace PDF or final-package inspection; unavailable artifacts remain `NOT_CHECKED`.

### ✍️ Polish Your Sentences

> *"My abstract feels wordy. Can you tighten it?"*
> *"The reviewer said my contribution claims sound inflated."*

Use **34 fill-in-the-blank sentence templates** and **15 Before/After rewrite pairs**, organized by section and function:

- Opening hooks → 5 patterns
- Pain point sentences → 3 patterns
- Contribution statements → 4 patterns
- Result reporting → 3 patterns
- Limitation statements → 3 patterns
- Transition sentences → 4 patterns

Each template shows what to fill in, what to avoid, and which paper type it fits best.

### 📐 Write Better Captions

> *"Does this caption follow AAAI conventions? Is it self-contained?"*

**7 caption templates** and **8 Before/After rewrite groups**. Figure captions (pipeline, comparison, teaser) and table captions (main results, ablation, analysis, resource) are treated separately. Core principle: a reviewer should understand your figure **without reading the body text**.

### 🏷️ Get Paper-Type-Specific Strategy

> *"I'm writing a benchmark paper. How should I structure my Introduction differently?"*

The skill identifies your paper as one of **4 types** and injects type-specific guidance throughout:

| Type | Example Papers (AAAI Award-Winning) | Special Handling |
|------|-------------------------------------|-----------------|
| **Theory / Algorithm** | Revelations (2025), Every-Bit-Helps (2025) | Proof sketch structure, Preliminaries + Main Results instead of Method |
| **Model / Method** | LLM2CLIP (2026), CowClip (2023) | Module-by-module description, SOTA tables, full ablation |
| **Benchmark / Resource** | DivShift (2025), DISCount (2024) | Data collection + inter-annotator agreement + baseline diversity |
| **Application-Driven** | PlantTraitNet (2026), Slum Detection (2026) | Domain problem → AI solution, real-world deployment, ethical statement |

---

## ⚡ The Workflow

| # | Phase | What Happens | Output |
|---|-------|-------------|--------|
| 1 | 🧭 **Position** | Identify paper type + core contribution | Type (1–4) + 3 answers |
| 2 | 🗺️ **Outline** | Section plan + page budget + figure plan | Structured outline |
| 3 | ✍️ **Write** | 7 sections in order (lazy-loaded guidance) | LaTeX first draft |
| 4 | ✨ **Polish** | Reverse outlining + claim-evidence mapping + term scan | Coherent manuscript |
| 5 | 🔍 **Review** | Format compliance + double-blind + reproducibility | Submission-ready PDF |

Each phase loads only the modules it needs — zero context bloat.

---

## 🏗️ How It's Organized

```
Great-AAAI-Writing-Skills/
│
├── SKILL.md                  Orchestration layer — 5-phase dispatcher
│
├── sections/                 Per-chapter writing guidance
│   ├── title.md              ├── abstract.md         ├── introduction.md
│   ├── related-work.md       ├── method.md           ├── experiments.md
│   └── conclusion.md
│
├── modules/                  Cross-cutting craft modules
│   ├── sentence-craft.md     34 sentence templates + Before/After rewrites
│   ├── caption-writing.md    7 caption templates + diagnostics
│   ├── figure-design.md      Visual design and layout rules
│   ├── self-review.md        Lightweight self-audit framework
│   ├── distilled-patterns.md Quantitative benchmarks from 50 papers
│   ├── paper-taxonomy.md     4-type classification + strategy
│   ├── outline-template.md   Page budget + section plan
│   ├── compliance-quick.md   Stage-aware format quick check
│   ├── review/               6-module deep review (AAAI 2027-specific)
│   ├── review-simulator/     PC-member view: scoring + Q&A + rebuttal
│   └── paper-corpus/         50 award-winning paper abstracts + analysis
│
├── rules/                    AAAI-27 format + reviewer-scoring rules
├── scripts/                  Format checker + deterministic review scorer
├── tests/                    Format and scoring regression tests
│
└── paper-types/              Type-specific injection layer
    ├── theory.md             ├── model-method.md
    ├── benchmark-resource.md └── application-driven.md
```

The architecture is **3-layer lazy-loading**: the orchestrator (`SKILL.md`) dispatches to the right module at the right time. You never load all files — only the 2–3 relevant to your current phase and paper type.

📖 [Full architecture docs →](docs/architecture.md)

---

## 📚 Documentation

| Document | |
|----------|--|
| [Quick Start](docs/quickstart.md) | Get writing in 5 minutes |
| [Architecture](docs/architecture.md) | Module design + routing |
| [Workflow Details](docs/workflow.md) | 5 phases with inputs, outputs, and checkpoints |
| [Paper Types](docs/paper-types.md) | 4 types explained with a decision tree |
| [Examples](docs/examples/) | 3 complete walkthroughs (model / theory / benchmark) |
| [FAQ](docs/faq.md) | Language, copyright, other conferences, etc. |

---

## 🔗 Acknowledgments

This skill builds upon excellent open-source work:

| Upstream Project | Author | License | How We Use It |
|-----------------|--------|---------|---------------|
| [Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) | [@Master-cai](https://github.com/Master-cai) | MIT | Core writing methodology — AAAI-adapted and extended with 50-paper corpus |
| [AI-paper-reviewer](https://github.com/FanBroWell/AI-paper-reviewer) | [@FanBroWell](https://github.com/FanBroWell) | MIT | Review framework, compliance checks, red-flag lexicon — rewritten for AAAI 2027 |

> **Note**: Research-Paper-Writing-Skills adapts Prof. Peng Sida's [open notes](https://github.com/pengsida/learning_research). We thank both the original author and the curator.

---

## 🤝 Contributing

We welcome additions — especially from researchers who have been through the AAAI review process.

- 🐛 **Found a broken rule?** [Open a bug report](.github/ISSUE_TEMPLATE/bug_report.md)
- 💡 **Noticed a missing pattern?** [Propose it](.github/ISSUE_TEMPLATE/feature_request.md)
- 📄 **Studied a great AAAI paper?** [Share the instance](.github/ISSUE_TEMPLATE/paper_type_request.md)

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## ⭐ Show Your Support

If this skill helped you write a better AAAI paper, **please star this repo** — it helps other researchers find it.

---

## 📝 License

MIT © 2026 HansonLegacy

---

## ⚠️ Disclaimer

**Not affiliated with AAAI.** This tool provides writing guidance based on publicly available Author Kit specifications and published papers. Acceptance depends on the AAAI review process — we help with writing quality, not contribution quality.

* * *

<div align="center">
  <sub>Built for the AI research community</sub>
</div>
