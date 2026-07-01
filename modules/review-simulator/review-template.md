# AAAI 审稿意见输出模板

> 对标 AAAI 审稿系统（CMT/OpenReview）的标准审稿格式。
> 所有 `[ ]` 为待填充项，审稿时逐项填写。

---

## 完整审稿输出模板

```
═══════════════════════════════════════════
AAAI 2027 Review Simulation
═══════════════════════════════════════════

## Paper Summary（~150 words）

[用 reviewer 自己的话复述论文核心贡献。
这有两个目的：
  a) 展示 reviewer 是否正确理解了论文
  b) 如果理解有偏差，作者可以在 rebuttal 中澄清

模板：
This paper addresses [problem/task] by proposing [method name],
a [one-clause characterization]. The key idea is [core insight].
The authors [what they did — e.g., "evaluate on X benchmarks and
show Y% improvement over Z"]. The main claimed contribution is
[specific contribution].
]

## Strengths

1. [具体优点 — 指到论文中的具体位置或具体内容]
   [例："The problem formulation in §2 is well-motivated and connects
    clearly to the real-world challenge of X."]

2. [具体优点]

3. [具体优点]
   [如适用：]

## Weaknesses

### 🔴 Critical（影响 accept/reject 决定）

**C1. [问题]**
  - 位置: [§X.Y / Table Z / Figure W]
  - 问题描述: [具体说明]
  - 影响: [这个弱点为什么可能导致拒稿]
  - 修复建议: [如果作者可以修复的话，具体怎么做]

**C2. ...**

### 🟠 Major（显著扣分）

**M1. [问题]**
  - 位置: [§X.Y]
  - 问题描述: [具体说明]
  - 建议: [具体改进方案]

**M2. ...**

### 🟡 Minor（可修复的细节）

| # | 位置 | 问题 | 建议 |
|---|------|------|------|
| 1 | §X.Y | ... | ... |
| 2 | ... | ... | ... |

## Questions & Suggestions

1. **Q1**: [具体问题 — reviewer 希望作者在 rebuttal 中回答的]
   [例："Why was baseline X not included in the comparison? X is the
    most related prior work and would strengthen the evaluation."]

2. **Q2**: ...

3. **S1**: [改进建议 — 不一定是 weakness，而是"如果加上会更好"]
   [例："An analysis of how the method performs with different random
    seeds would increase confidence in the results."]

## Overall Rating

[ ] Strong Accept (Top 5% — exceptional contribution, flawless execution)
[ ] Accept (Top 20% — solid contribution, minor issues only)
[ ] Weak Accept (Top 35% — good contribution, some concerns)
[ ] Borderline (could go either way)
[ ] Weak Reject (interesting but insufficient contribution/evidence)
[ ] Reject (fundamental issues with contribution or evidence)

## Confidence

[ ] High — I know this specific sub-area well and have reviewed extensively in it
[ ] Medium — I have general knowledge of this area
[ ] Low — This topic is somewhat outside my core expertise

## Ethical Concerns（如适用）

[检查以下内容，如有问题在此标注]
- 数据集是否涉及隐私/偏见/不适当使用？
- 方法是否有明显的 dual-use 风险？
- 实验是否涉及 human subjects（需 IRB）？

## Summary for AC（2-3 句）

[给 Area Chair 的精简总结，帮助 AC 在做 meta-review 时快速定位：
- 这篇论文的核心贡献是什么？
- 最关键的 Strengths 和 Weaknesses 各一条？
- 你的最终建议（accept/reject）和核心理由？
]

═══════════════════════════════════════════
```

---

## 输出风格规范

### 必须遵守

1. **建设性而非攻击性**：不用 "the authors failed to..."，用 "the paper would benefit from..."
2. **具体而不空洞**：每个评价指到论文中具体位置
3. **区分事实和判断**：不确定的地方标注 "it is unclear whether..."
4. **按 AAAI 标准评分**：不是 "写得好不好"，是 "这篇论文在 AAAI 的标准下能否被接受"

### 避免的措辞

| 避免 | 替代 |
|------|------|
| "The authors failed to..." | "The paper does not yet demonstrate..." |
| "This is wrong" | "This appears inconsistent with..." / "This claim is not supported by..." |
| "The method is simple" | "The technical contribution beyond [prior work] is not clearly articulated" |
| "This paper is not novel" | "The differentiation from [closest prior work] needs to be more explicit" |

### 关于评分

- **Strong Accept** 非常罕见——仅当贡献确实 exceptional 且执行无瑕疵
- **Accept** 是"我愿意在 AAAI 上看到这篇论文"——不是"这篇完美了"
- **Borderline** 是 AAAI 最常见的 borderline 地带——有好的部分但也有 concerns
- **Reject** 不等于"这篇论文不好"——可能适合其他会议
