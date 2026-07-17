# AAAI 模拟审稿工作流

> 目标是生成一份有证据、可复算、能明确表达不确定性的单 reviewer 情景评估，而不是预测真实录取结果。

## Preflight：确定审查边界

开始前记录：

```text
Paper type: theory / model_method / benchmark_resource / application_driven
Materials received: title / abstract / full paper / appendix / supplement / artifacts
Review stage: anonymous / camera-ready / unknown
Target event or track policy: known / unknown
Simulated reviewer profile: explicit / not provided
External verification performed: yes / no / partial
```

规则：

- 论文版本不明确时先说明正在评价哪个文件或文本；
- 用户只提供摘要或局部章节时，不假装已审完整论文；
- 混合型论文选择主类型，并用第二可能类型做权重敏感性分析；
- event policy 未知时标 `NEEDS_POLICY`，不自行补全页数或 supplement 规则；
- 未提供 reviewer profile 时，Confidence 的 `domain_match=0`。

## Round 1：First Pass

### 1.1 用 reviewer 自己的话复述

只读 Title、Abstract、Introduction 中的贡献陈述、核心图表和主要结果，写出：

```text
Problem:
Claimed contribution:
Core mechanism or insight:
Main supporting evidence:
Most important unresolved question:
```

如果无法准确复述，先标记理解障碍，不立即把它解释成技术错误。

### 1.2 建立初始假设

形成 `positive / mixed / negative / insufficient information` 的初步倾向，并记录最多三条依据。这个倾向不是最终评分，也不进入公式。

不要因以下表面模式自动加减分：

- 是否有方法缩写或 `NAME: Subtitle` 标题；
- 是否在第一页放 teaser；
- improvement 是否超过任意固定百分比；
- 是否使用固定数量的 baseline、引用或 contributions；
- 是否符合获奖论文语料的平均摘要长度。

## Round 2：Section-by-Section Deep Read

加载 `criteria.md` 和 `scoring-rubric.md`。逐节收集证据，并维护七维 Evidence Ledger。

### 2.1 Introduction 与 Related Work

检查：

- 问题的重要性、边界和目标受众是否清楚；
- 核心贡献能否与 closest prior work 形成具体差异；
- contribution、method 和 evidence 是否可互相追踪；
- 关键相关工作是否公平呈现；
- 当前是否实际完成了足够的文献核验。

主要映射到 Significance、Novelty、Clarity 和 Related Work。

### 2.2 Method / Theory / Resource Construction

根据论文类型检查：

- 理论型：假设、定理、证明链、边界情况和含义；
- 模型方法型：设计动机、算法定义、训练/推理逻辑和复杂度；
- 基准资源型：采集、标注、质控、泄漏防护和协议；
- 应用驱动型：问题建模、领域约束、安全边界和部署假设。

主要映射到 Novelty、Soundness 和 Reproducibility。

### 2.3 Evidence / Experiments / Analysis

为每个中心 claim 建立一条证据链：

```text
Claim → Evidence location → Evaluation appropriateness → Result → Remaining uncertainty
```

检查 baseline、公平性、消融、统计不确定性、证明支持、案例和外部有效性时，以论文实际 claim 和类型为准。不要把 p-value、SOTA、固定 baseline 数量或大规模实验当作所有论文的通用要求。

主要映射到 Soundness、Evidence 和 Reproducibility。

### 2.4 Conclusion、Limitations 与 Ethics

检查结论是否超出证据、局限是否具体、伦理与安全问题是否需要进一步审查。伦理问题单独输出；只有它实质影响科学有效性时，才在对应维度反映。

### 2.5 为每个维度赋状态和分数

使用：

```text
ASSESSED + 0–6 score
MISSING_IN_PAPER + 0–6 score
UNAVAILABLE_TO_REVIEWER + N/A
NOT_APPLICABLE + N/A
```

每个分数使用 0.5 步进，并附证据位置与主要 concern。0 分必须有直接的根本失败证据；未知不是 0。

## Round 3：Cross-Cutting Check

### 3.1 Claim–Evidence 与数字一致性

```text
| Claim | Abstract | Main text | Table/Figure/Proof | Consistent | Status |
|---|---|---|---|---|---|
```

区分：文字表述不清、数字冲突、评价协议不当和中心主张无支持。它们应落在不同的主扣分维度。

### 3.2 符号、定义和复核链

检查符号是否一致、关键定义是否完整、证明/算法/资源流程是否能被追踪，以及可重复性清单的适用项是否有正文依据。

### 3.3 合规与匿名性单独扫描

加载：

```text
review/02-aaai-red-flags.md
review/03-aaai-format-compliance.md
review/04-aaai-double-blind.md
scripts/aaai27_check.py（有源码时）
```

输出独立的 `Compliance / Policy Status`。格式、匿名和未知 event policy 不进入 Scientific Overall 公式，除非目标 event 的明确规则要求报告特定程序后果。

### 3.4 获奖论文语料只作非评分参照

加载 `scoring-calibration.md` 时，只把语料用于解释写作和呈现模式。不得据此设置录取阈值、percentile、默认 Borderline 或概率。

### 3.5 检查重复扣分

每个 weakness 指定：

```text
Primary dimension:
Secondary consequence, if any:
Why this is not double-counted:
```

同一缺陷在多个维度产生独立影响时才允许多维扣分。

## Round 4：确定性聚合与输出

### 4.1 计算 Overall Score

1. 确认论文类型与对应权重；
2. 计算 coverage；
3. 对已评分维度重归一化并得到 Raw Score；
4. 仅在有定位证据时声明科学门控；
5. 应用最低 gate cap；
6. decimal half-up 保留一位小数；
7. 映射 Recommendation 标签。

优先使用：

```bash
python scripts/aaai_review_score.py scorecard.json --format markdown
```

必须同时展示 Raw、Coverage、active gates、Final 和 label。若 coverage 不足，按 `scoring-rubric.md` 输出 provisional 结果或 `N/A`。

### 4.2 独立计算 Confidence

分别确定：

```text
material: 0–2
verification: 0–2
domain_match: 0–1
```

相加得到 0–5 的整数 Confidence，再应用材料上限。附 2–3 条依据或限制。不得使用 Overall 的高低、weakness 数量或推荐标签来计算 Confidence。

### 4.3 生成审稿意见

加载 `review-template.md`，输出：

- Paper Summary；
- Strengths；
- Weaknesses；
- 七维 Scorecard；
- Raw / gates / Final / Recommendation；
- Confidence 及依据；
- Compliance / Policy Status；
- Questions & Suggestions；
- Rebuttal priorities；
- Summary for AC；
- 强制 Score Footer。

加载 `common-qa.md` 只能帮助生成问题，不得用问题库替代论文证据。

### 4.4 最终一致性检查

- Final 是否可由 scorecard 复算；
- gate 是否有 reason、location 和 resolution condition；
- unknown 是否错误地记成 0 或默认分；
- Confidence 是否与 Overall 独立；
- 推荐标签是否与数值区间一致；
- 输出是否声明“诊断性模拟，不是 AAAI 官方分制或录用概率”；
- 最后两个非空行是否依次为 `Final Overall Score` 和 `Assessment Confidence`；
- Footer 数值是否与前文完全一致，且 Footer 后没有任何内容。
