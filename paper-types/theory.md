# 理论/算法型 — AAAI 写作专属指南

> 适用：论文核心贡献是定理、证明、界（bounds）、复杂度分析、可判定/不可判定结论。

---

## 一、核心叙事定位

**你不是在"提升 metric"，你是在回答一个问题。**

Reviewer 的期待：明确的问题陈述 → 严格的数学推导 → 确定的结论（decidable/undecidable/optimal/NP-hard/tight bound）。实验是锦上添花，不是核心。

---

## 二、各章节关键差异

### Title
- 常含关键词：`Optimal`, `Decidable`, `Tight Bound`, `Efficient`, `Complexity`
- 命名模式：「What question」型：`Eliminating Majority Illusion is Easy` vs 「Method: Answer」型：`Revelations: A Decidable Class of POMDPs`

### Abstract（详见 `sections/abstract.md` 类型 1 变体）
- 用 "问题→答案" 框架替代五步弧线
- ③ 处给核心结论（`We establish that...`），而非方法名
- ④ 处给证明策略直觉

### Introduction（详见 `sections/introduction.md` 类型 1 变体）
- **开篇二选一**：叙事钩子 vs 模型定义直入
- **核心问题视觉化**：缩进/斜体/粗体块
- Contributions bullet 谈结论性质（decidable/optimal/tight）

### Method
- 结构不是 "模块顺序" 而是 "Preliminaries → Main Results"
- 定理用 theorem 环境独立展示
- 证明草图给直觉，不在正文展开所有 technical lemma

### Experiments
- 实验预期最低——不强求大规模 benchmark
- Toy domain / 小型验证 / 概念验证即为合理
- 可以叫 "Case Study" 或 "Empirical Evaluation"

---

## 三、获奖论文参考

| 论文 | 核心贡献 | 推荐阅读：叙事策略 |
|------|---------|------------------|
| Revelations (2025) | POMDP 可判定类 | 模型定义直入 + 内联粗体路标 |
| Every-Bit-Helps (2025) | 最优 distortion | 叙事钩子（两个场景） + 缩进问题块 |
| Clustering w/ Outliers (2023) | 近似算法 + 理论保证 | 问题驱动 + 定理级贡献 |
| Computing Game Symmetries (2025) | 算法 + 理论性质 | 渐入式：场景→定义→结论 |
| Eliminating Majority Illusion (2025) | 计算复杂性结论 | 标题即结论 + 直观问题名 |

---

## 四、常见写作问题

| 问题 | 改法 |
|------|------|
| 开篇太抽象 | 叙事钩子或具体小例子落地 |
| 核心问题淹没在段落中 | 独立成块（缩进/斜体/粗体） |
| 定理陈述太长 | 把条件和结论分离；用 theorem 环境 |
| Contributions bullet 虚 | 每条给具体结论类型，不含糊 |
| 实验期待过高 | 理论论文不需要刷 SOTA——在 toy domain 验证就够了 |
| 引用不足 | 理论论文也需引用——Preliminaries 通常引 10-20 篇 |

---

> **句子级差异**（`modules/sentence-craft.md`）：理论型论文的句子层面特化：
> - 开场句 → §2.1 模式 A（定义型）或模式 C（任务-重要性），不走 "X has emerged as" 趋势型
> - 痛点句 → §2.2 模式 B（Despite+障碍）或模式 D（枚举 open questions）
> - 提案句 → §2.3 模式 C（In this work, we investigate/study...），动词选 `prove / establish / show` 而非 `propose`
> - 对比句 → §2.6 模式 C（收敛比较——"is optimal up to a constant factor"）
> - 结果句 → §2.5 模式 E（意义收束——"settles open questions"），注意关键词强度梯度表中 `proves/establishes` 仅理论型可用
> - 局限性 → §2.8 模式 B（限定条件——"Our analysis assumes X. Relaxing this is open."）
> - 量化基准 → `modules/distilled-patterns.md` §四（理论型 Abstract 均值 141 词，最短）
