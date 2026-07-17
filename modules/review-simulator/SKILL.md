---
name: aaai-review-simulator
description: AAAI 2027 诊断性审稿模拟器。以单个模拟 PC reviewer 视角审阅完整论文或部分材料，输出有证据的 Summary、Strengths、Weaknesses、Rebuttal priorities、0–6 Scientific Overall Score（可含一位小数）、独立的 0–5 Assessment Confidence，以及单独的格式/匿名/政策状态。用于“模拟 AAAI 审稿”“帮我审这篇 paper”“预估 reviewer 评价”“这篇能中 AAAI 吗”“生成 review report”或 rebuttal 预判；不得把结果表述为 AAAI 官方分制、录用概率或多审稿人共识。
---

# AAAI 诊断性审稿模拟器

输出一份可以追踪证据并复算数值的单 reviewer 情景评估。论文科学质量、当前评估信心和投稿合规状态必须分开。

## 工作流

```text
Preflight
  → 确定论文版本、类型、已提供材料、event policy 和 reviewer profile

Round 1: First Pass
  → 用 reviewer 自己的话复述问题、贡献、机制和主要证据
  → 记录初步倾向，但不打最终分

Round 2: Deep Read
  → 加载 criteria.md 和 scoring-rubric.md
  → 建立七维 Evidence Ledger
  → 每维使用状态 + 0–6 分（0.5 步进）+ 证据位置

Round 3: Cross-Cutting Check
  → Claim–Evidence、数字、符号、证明/协议一致性
  → 格式与匿名状态单独检查
  → scoring-calibration.md 只作非评分写作参照

Round 4: Deterministic Scoring
  → 用规则源和计算器聚合 Raw、coverage、gates、Final 和 label
  → 独立计算 0–5 Confidence
  → 按 review-template.md 输出
```

详细步骤见 `review-workflow.md`。

## 必须加载的资源

| 文件 | 用途 |
|---|---|
| `criteria.md` | 七个科学质量维度及四类论文的证据标准 |
| `scoring-rubric.md` | 0–6 量表、类型权重、coverage、门控、推荐映射和 0–5 Confidence |
| `review-workflow.md` | Preflight 与四轮审稿步骤 |
| `review-template.md` | 完整结构化输出 |
| `common-qa.md` | 问题和 rebuttal 预判素材；不得替代论文证据 |
| `scoring-calibration.md` | 获奖语料的非评分写作参照 |
| `../../rules/aaai-review-scoring.json` | 机器可读权重、区间和门控规则 |
| `../../scripts/aaai_review_score.py` | 确定性聚合计算器 |

## 核心评分协议

1. 先区分 `ASSESSED`、`MISSING_IN_PAPER`、`UNAVAILABLE_TO_REVIEWER` 和 `NOT_APPLICABLE`。
2. 未知信息不得填成 0 或默认平均分；0 必须有根本失败的直接证据。
3. 七维分数只使用 0.5 步进；Final 使用 decimal half-up 保留一位小数。
4. 每个分数必须指向章节、表格、图、证明、附录或明确的材料限制。
5. 同一弱点指定一个主扣分维度，避免重复处罚。
6. 科学门控必须显示 id、cap、reason、evidence/location 和 resolution condition。
7. 格式、匿名、伦理和 event policy 状态不自动进入 Scientific Overall。
8. Confidence 只由材料完整度、核验深度和显式 reviewer-profile 匹配度构成；不得随 Overall 高低变化。
9. 报告必须以固定 Score Footer 结束；Final Overall Score 和 Assessment Confidence 必须是全文最后两个非空行，其后不得追加解释、免责声明或其他内容。

## 计算

将 scorecard 写为 JSON，优先运行：

```bash
python scripts/aaai_review_score.py scorecard.json --format markdown
```

如果当前环境无法执行脚本，严格按 `scoring-rubric.md` 计算，并在输出中展开权重、Raw、coverage、active gates 和 Final，确保用户可以复算。

## 最小输出结构

```text
Review Scope
Paper Summary
Strengths
Weaknesses
Seven-Dimension Scorecard
Scientific Rating: Raw / Coverage / Gates / Final 0–6 / Recommendation
Assessment Confidence: components / 0–5 / limitations
Compliance / Policy Status
Ethical / Safety Concerns
Questions & Suggestions
Rebuttal Priorities
Summary for AC
Score Footer: mandatory final two non-empty lines
```

使用以下固定尾注格式，并保证数值与前文完全一致：

```text
Final Overall Score: <x.x / 6.0 — Recommendation | N/A — Insufficient information>
Assessment Confidence: <y / 5 — Confidence label>
```

始终声明：这是内部诊断性模拟，不是 AAAI 官方分制、录用概率或真实多审稿人共识。
免责声明应放在 Score Footer 之前；Footer 之后不得再输出任何内容。
