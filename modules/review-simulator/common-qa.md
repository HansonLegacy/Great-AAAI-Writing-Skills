# Reviewer 常问问题库 & Rebuttal 预判

> 基于 AAAI 审稿经验 + 50 篇获奖论文的薄弱点分析。
> 审稿时预判 reviewer 最可能追问的问题，附带 rebuttal 策略建议。

---

## 一、关于贡献（Q1 — 最高频）

### Q1.1 "What exactly is the contribution beyond [closest prior work]?"

**为什么 reviewer 会问**：贡献不够突出，或与 prior work 的区分是 incremental 的。

**Rebuttal 策略**：
- 用 1-2 句明确陈述核心差异（不要用 "we are the first"，用 "Unlike X which does Y, we Z"）
- 如果之前没写清楚差异，在 rebuttal 中补充具体对比表

### Q1.2 "This seems like a straightforward combination of A and B. What is the technical insight?"

**为什么 reviewer 会问**：方法看起来像现成模块的拼接。

**Rebuttal 策略**：
- 具体解释为什么 A+B 的 naive 组合不 work（你有消融验证吗？）
- 突出你在组合中做的非平凡设计决策
- 如果有 Naive-A+B 的消融对比，在这里引用

### Q1.3 "The contribution density doesn't justify 7 pages."

**为什么 reviewer 会问**：正文有灌水段落，核心贡献只需 3-4 页就能说清。

**Rebuttal 策略**：
- 检查是否真有多余段落——如果有，在 final version 中压缩
- 强调贡献的多维度（如果确实有多个非平凡贡献）

---

## 二、关于实验（Q2 — 最高频）

### Q2.1 "Why wasn't baseline X included?"

**为什么 reviewer 会问**：X 是该领域最相关的工作，但实验中没有比较。

**Rebuttal 策略**：
- 如果确实遗漏：诚恳承认 + 补充实验（如果来得及）+ 在 final version 中加入
- 如果有意不比较：给出技术理由（"X solves a different problem setting where..."）
- 如果 X 是 concurrent work：说明并致歉

### Q2.2 "Are the improvements statistically significant?"

**为什么 reviewer 会问**：报告了 improvement 但没有 std/p-value。

**Rebuttal 策略**：
- 如果有 std：在 rebuttal 中补充统计检验结果
- 如果没跑多次：说明实验条件限制，承诺在 final version 中补充

### Q2.3 "Does the ablation cover every claimed contribution?"

**为什么 reviewer 会问**：消融不完整——声称了 3 个贡献但只做了 2 个消融。

**Rebuttal 策略**：
- 如果遗漏了消融：补充后报告
- 如果某贡献难以消融（如训练策略）：解释原因 + 提供替代的 evidence

### Q2.4 "Are the results reproducible?"

**为什么 reviewer 会问**：超参数不透明、没有代码、没有 seeds。

**Rebuttal 策略**：
- 提供完整的超参数表 + 随机种子设置
- 引用 AAAI 2027 Reproducibility Checklist
- 承诺开源代码（如果之前没承诺）

### Q2.5 "Why this specific choice of hyperparameters/datasets?"

**为什么 reviewer 会问**：选择理由不明确。

**Rebuttal 策略**：
- 超参数：说明搜索范围和选择方法（grid/random/Bayesian）
- 数据集：说明选择动机（"X is the standard benchmark, Y tests generalization"）

---

## 三、关于方法（Q3）

### Q3.1 "What is the motivation for this design choice?"

**为什么 reviewer 会问**：某模块的设计理由没有解释。

**Rebuttal 策略**：
- 补充 Motivation 段落
- 如果有对应的消融来验证该设计，指向消融

### Q3.2 "Why not use [obvious alternative] instead?"

**为什么 reviewer 会问**：reviewer 能想到一个明显的替代方案，但你没讨论。

**Rebuttal 策略**：
- 如果试过替代方案且不 work：在 rebuttal 中报告
- 如果没试过：解释为什么你的选择更适合 + 承诺在 final version 中讨论

### Q3.3 "The notation is inconsistent / confusing."

**为什么 reviewer 会问**：符号定义不清楚或前后冲突。

**Rebuttal 策略**：
- 提供修正后的符号定义表
- 承诺在 final version 中统一全文符号

---

## 四、关于适用范围

### Q4.1 "How well does this method generalize beyond the tested benchmarks?"

**为什么 reviewer 会问**：只在 1-2 个相似 benchmark 上测试了。

**Rebuttal 策略**：
- 如果测试了更多但没全放进正文：在 rebuttal 中报告
- 如果确实有限：诚实地将其列为 limitation，讨论为什么相信能泛化

### Q4.2 "What are the computational requirements for real-world deployment?"

**为什么 reviewer 会问**：没有报告 inference time/params。

**Rebuttal 策略**：
- 补充效率数据
- 如果确实很重：诚实讨论 + 作为 limitation

---

## 五、按论文类型的针对性问题

### 理论型常被问

| 问题 | Rebuttal 策略 |
|------|-------------|
| "Are all assumptions explicitly stated?" | 列出所有假设清单 |
| "Is the proof sketch in the main paper sufficient?" | 指向 Appendix 完整证明 |
| "What is the significance of this theoretical result in practice?" | 给出 1-2 个实际 implications |

### 模型方法型常被问

| 问题 | Rebuttal 策略 |
|------|-------------|
| "How sensitive is the method to hyperparameters?" | 补充 sensitivity analysis |
| "What happens in low-data / out-of-distribution settings?" | 补充或列为 limitation |
| "How does the training cost compare to baselines?" | 补充分钟数/GPU时数 |

### 基准资源型常被问

| 问题 | Rebuttal 策略 |
|------|-------------|
| "What is the inter-annotator agreement?" | 报告 Cohen's κ / Fleiss' κ |
| "How was data quality ensured?" | 描述质控流程 |
| "Why this dataset size / annotation granularity?" | 解释设计选择 |

### 应用驱动型常被问

| 问题 | Rebuttal 策略 |
|------|-------------|
| "How was the method validated with domain experts?" | 报告专家评估/案例分析 |
| "What are the ethical considerations for deploying this?" | 给出 ethical statement |
| "Does this work in the real deployment setting?" | 诚实讨论真实场景 limitations |

---

## 六、Rebuttal 写作快速指南

### 结构

```
Dear Reviewers,

Thank you for the thoughtful feedback.

[R1Q1 — Reviewer 1's main concern]
  → Our response: [1-2 句] + [具体行动：either 澄清 / 补充实验 / 承诺修改]

[R1Q2]
  → ...

[R2Q1]
  → ...

We believe these revisions address the key concerns raised.
Thank you again for your time and constructive feedback.
```

### 铁律

1. **每条 concern 都要回应**——跳过某条 = reviewer 认为你在逃避
2. **具体而非泛泛**——不写 "we will improve this"，写 "we will add X experiment / Y analysis / Z discussion"
3. **诚恳承认真正的弱点**——强行辩解不如诚实地列为 limitation
4. **不争论审稿人的 competence**——不用 "as you may not be aware..."
5. **承诺必须可兑现**——"we will add an experiment on dataset X" 必须是你能在 camera-ready 前完成的
