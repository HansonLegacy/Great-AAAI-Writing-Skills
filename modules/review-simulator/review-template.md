# AAAI 模拟审稿输出模板

> 非官方诊断模板。所有数值必须能从 `scoring-rubric.md` 和 scorecard 复算；所有判断必须指向当前论文材料。

## 完整输出

```text
═══════════════════════════════════════════
AAAI Review Simulation
═══════════════════════════════════════════

Diagnostic simulation only — not an official AAAI score,
acceptance probability, or multi-reviewer consensus.

## Review Scope

Paper type: [theory / model_method / benchmark_resource / application_driven]
Materials reviewed: [full paper / abstract / appendix / supplement / artifacts]
Unavailable materials: [... / none]
Simulated reviewer profile: [... / not provided]
External verification: [performed / partial / not performed]

## Paper Summary

[用 reviewer 自己的话复述问题、核心贡献、方法和主要证据。
不得复制摘要，也不得加入论文没有声称的贡献。]

## Strengths

1. [具体优点]
   - Evidence: [§X.Y / Table Z / Figure W / Appendix]
   - Why it matters: [...]

2. [...]

## Weaknesses

### Critical

**C1. [问题]**
- Primary dimension: [dimension id]
- Location / evidence: [...]
- Why it affects the decision: [...]
- Resolution condition: [什么证据或修改可以解决]
- Gate, if any: [gate id / none]

### Major

**M1. [问题]**
- Primary dimension: [...]
- Location / evidence: [...]
- Impact: [...]
- Suggested action: [...]

### Minor

| # | Primary dimension | Location | Issue | Suggestion |
|---|---|---|---|---|
| 1 | ... | ... | ... | ... |

## Seven-Dimension Scorecard

| Dimension | Status | Weight | Score (0–6) | Evidence / Location | Main Concern |
|---|---|---:|---:|---|---|
| Significance | [...] | [...] | [...] | [...] | [...] |
| Novelty | [...] | [...] | [...] | [...] | [...] |
| Soundness | [...] | [...] | [...] | [...] | [...] |
| Evidence | [...] | [...] | [...] | [...] | [...] |
| Clarity | [...] | [...] | [...] | [...] | [...] |
| Related Work | [...] | [...] | [...] | [...] | [...] |
| Reproducibility | [...] | [...] | [...] | [...] | [...] |

Status 只能为 ASSESSED / MISSING_IN_PAPER /
UNAVAILABLE_TO_REVIEWER / NOT_APPLICABLE。

## Scientific Rating

Raw weighted score: [x.xxx / 6.0]
Coverage: [xx% — COMPLETE / PROVISIONAL / INSUFFICIENT]
Plausible range: [x.x–x.x / 6.0, when needed]

Active scientific gates:
- [gate id — cap — reason — evidence/location — resolution condition]
- [none]

Final Overall Score: [x.x / 6.0 or N/A]
Recommendation: [Strong Reject / Reject / Weak Reject / Borderline /
                 Weak Accept / Accept / Strong Accept / Insufficient information]

Score rationale: [2–4 句，解释决定性维度和门控；不写录用概率。]

## Assessment Confidence

Material completeness: [0–2] — [reason]
Verification depth: [0–2] — [reason]
Reviewer-profile domain match: [0–1] — [reason]

Confidence: [0–5] — [No confidence / Very Low / Low / Medium / High / Very High]
Confidence limitations:
- [...]
- [...]

## Compliance / Policy Status

Format: [ERROR / WARNING / NOT_CHECKED / scoped PASS]
Anonymity: [ERROR / WARNING / NOT_CHECKED / scoped PASS]
Event-specific policy: [known result / NEEDS_POLICY]
Notes: [...]

These statuses are separate from the Scientific Overall Score.

## Ethical / Safety Concerns

[None identified within reviewed materials / concern + evidence + needed review]

## Questions & Suggestions

1. [最可能改变评分的具体问题]
2. [...]
3. [非决定性的改进建议]

## Rebuttal Priorities

| Priority | Concern | Can rebuttal address it? | Required evidence |
|---|---|---|---|
| 1 | ... | fully / partially / unlikely | ... |

## Summary for AC

[2–4 句：核心贡献、决定性优点、决定性问题、Final Score、Confidence，
并说明 provisional / missing information / active gate（若有）。]

═══════════════════════════════════════════

Final Overall Score: [x.x / 6.0 — Recommendation | N/A — Insufficient information]
Assessment Confidence: [y / 5 — Confidence label]
```

## 输出约束

1. 每个维度分必须有论文位置或明确的材料限制。
2. `0` 只表示有证据的根本失败；未知使用 `N/A`。
3. 同一问题只在一个主维度扣分，除非能解释独立的次级影响。
4. gate 必须显式列出；不得静默压分。
5. Final 保留一位小数；维度分使用 0.5 步进。
6. Confidence 使用 0–5 整数，并与论文质量严格独立。
7. 不使用 “Top 5%”“真实录取阈值”或录用概率措辞。
8. 建设性描述问题，例如使用 “The paper does not yet establish...” 而不是攻击作者。
9. 上述 Score Footer 必须是报告最后两个非空行，且必须与 Scientific Rating 和 Assessment Confidence 小节中的值完全一致。
10. Score Footer 之后不得放免责声明、总结、分隔线或任何其他内容；免责声明必须提前出现。
