---
name: aaai-review-simulator
description: AAAI 2027 审稿模拟器。以 AAAI PC member 视角对论文进行结构化审稿，输出完整审稿意见（Summary/Strengths/Weaknesses/Rating/Rebuttal预判）。基于 50 篇 AAAI 获奖论文数据校准评分。当用户要"模拟 AAAI 审稿"、"帮我审这篇 paper"、"预估 review 结果"、"这篇能中 AAAI 吗"时使用。
---

# AAAI 2027 审稿模拟器

> 核心理念：**在真实的 reviewer 看到你的论文之前，先让一个"模拟 reviewer"看一遍。**
>
> 这不是自查工具（自查用 `self-review.md`），而是**审稿人视角的完整模拟**——
> 输出一份 AAAI PC member 会写出的真实审稿意见。

## 触发场景

当用户提到以下关键词时加载本 skill：
- "模拟审稿" / "模拟 AAAI review" / "review this paper"
- "审稿人视角" / "如果我是 reviewer" / "reviewer 会怎么看"
- "帮我审这篇" / "这篇能中 AAAI 吗" / "预估 review 结果"
- "写一份 AAAI 审稿意见" / "生成 review report"
- "rebuttal 预判" / "审稿人可能会问什么"

## 与现有模块的明确分工

| 场景 | 用哪个 |
|------|--------|
| 我写完了，帮我找问题 | `modules/self-review.md`（轻量）或 `review/00-aaai-master-workflow.md`（深度） |
| 格式合规检查 | `review/03-aaai-format-compliance.md` + `scripts/aaai27_check.py` |
| 红旗扫描 | `review/02-aaai-red-flags.md` |
| **模拟一个 AAAI reviewer，输出完整审稿意见** | **本模块（review-simulator）** |

## 审稿工作流（4 轮）

```
Round 1: First Pass（5 分钟模拟）
  → 读 Title → Abstract → Teaser Fig → Contributions → Main Results Table
  → 形成初步判断：大概 Accept / Borderline / Reject？

Round 2: Section-by-Section Deep Read（30 分钟模拟）
  → Introduction → Related Work → Method → Experiments → Conclusion
  → 加载 criteria.md：按论文类型的差异化评价标准
  → 逐节标注 Strengths 和 Weaknesses

Round 3: Cross-Cutting Check
  → 数字跨表一致性
  → Claim-Evidence 映射
  → 符号全文一致
  → 格式合规（加载 review/02 + review/03）
  → 与 50 篇获奖论文基准校准（加载 scoring-calibration.md）

Round 4: 综合打分 + 输出
  → 加载 review-template.md 生成结构化审稿意见
  → 加载 common-qa.md 生成 Rebuttal 预判
```

## 子模块索引

| 文件 | 用途 | 加载时机 |
|------|------|---------|
| `criteria.md` | 7 个 AAAI reviewer 核心问题 + 按类型差异化权重 | Round 2 |
| `review-workflow.md` | Round 1-4 详细步骤 + 每步检查点 | 全程 |
| `scoring-calibration.md` | Accept/Reject 边界 + 50 篇获奖论文基准校准 | Round 3-4 |
| `review-template.md` | AAAI 结构化审稿输出模板 | Round 4 |
| `common-qa.md` | Reviewer 常问问题库 + Rebuttal 预判 | Round 4 |

## 执行协议

1. **先理解，再评价**：Round 1 先用 reviewer 自己的话复述论文贡献，确保正确理解
2. **评价有据**：每条 Weakness 指向论文中具体位置；每条 Strength 同样具体
3. **以 AAAI 标准评分**：不是"你写得好不好"，而是"这篇论文在 AAAI 的标准下能拿什么分数"
4. **区分事实与判断**：不确定的事情标注"需作者确认"
5. **建设性**：每条问题附带改进建议或可验证的具体方向
6. **按类型校准**：理论型不要求大规模实验；应用型不要求复杂的理论证明

## 输出结构

```
═══════════════════════════════════════════
AAAI 2027 Review Simulation
═══════════════════════════════════════════

Paper Summary（~150 words）

Strengths（3-5 条）

Weaknesses（按严重度排序）
  🔴 Critical
  🟠 Major
  🟡 Minor

Questions & Suggestions

Overall Rating
  [Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject]

Confidence
  [High / Medium / Low]

Rebuttal 预判（Reviewer 最可能追问的 3-5 个问题）

Summary for AC（2-3 句）
```
