# AAAI 获奖论文蒸馏规律库（V4 最终版）

> **来源**：AAAI 2023-2026 获奖论文 50 篇的系统性语料分析。
> 采用 column-aware 分栏提取 + wordninja 分词重建。50/50 abstract 成功提取，45/50 introduction 成功提取。
> **标注**：`[N=50]` = 基于全 50 篇统计；`[N=45]` = 基于 intro 成功提取的 45 篇统计。
> **数据文件**：`modules/paper-corpus/corpus_v4_corrected.json` + `summary_v4_final.json`

---

## 〇、核心统计数据速览

| 指标 | 数值 | 说明 |
|------|------|------|
| **论文类型分布** [N=50] | 理论 12 (24%) / 模型方法 23 (46%) / 基准 4 (8%) / 应用 11 (22%) | 手动矫正后 |
| Abstract 词数均值 | **160 词** [N=50] | 中位数 148 |
| Abstract 词数 IQR | **[133, 168]** [N=50] | P25=133, P75=168 |
| Abstract 词数分布 | <100: 3篇 / 100-150: **23篇** / 150-200: 17篇 / >200: 7篇 | 最佳区间 130-170 |
| 标题 "NAME: Subtitle" | **58%** [N=50] | 29/50 篇；Question 型 4% |
| "we" 出现次数 | **均值 2.4，众数 2**[N=50] | 16篇用2次, 13篇用1次, 11篇用3次 |
| "however" 使用率 | **34%** [N=50] | 17/50 篇 |
| "propose" / "introduce" | **26% / 22%** [N=50] | 13篇/11篇 |
| 记忆点（极简+破折号） | **30% / 18%** [N=50] | 15篇极简 / 9篇破折号 |

### 按论文类型的 Abstract 词数差异

| 类型 | 篇数 | Abstract 词数均值 | Abstract 词数中位数 |
|------|------|-----------------|-------------------|
| 理论/算法型 | 12 | **141** | 146 |
| 模型/方法型 | 23 | **165** | 150 |
| 基准/资源型 | 4 | **234** | 304 |
| 应用驱动型 | 11 | **145** | 138 |

> 📊 **结论**：基准/资源型论文 abstract 明显更长（含数据统计描述）。理论型和应用型较短。模型/方法型居中。

---

## 一、句法模式（Sentence-Level Patterns）[N=50]

### 1.1 开场第一句模式

由于双栏 PDF 文本交叠，50 篇中 39 篇开场模式未能自动检测。**成功检测的 11 篇**中：

| 模式 | 篇数 | 示例 |
|------|------|------|
| **Recent-trends** | 4 | `Large language models have emerged as one of the most influential...` |
| **Definitional-short** | 3 | `CLIP is a seminal multimodal model that maps images and text...` |
| **Definitional-long** | 2 | `Partially observable Markov decision processes form a prominent model...` |
| **Concessive** | 1 | `While many MARL methods..., they often...` |
| **In-this-paper** | 1 | `We propose CAT-V, a training-free framework...` |

### 1.2 引出方法的动词选择 [N=50]

| 动词 | 使用率 | 篇数 |
|------|--------|------|
| `we propose` | **26%** | 13 |
| `we introduce` | **22%** | 11 |
| `we present` | 8% | 4 |
| `we develop` | 6% | 3 |
| `we design` | 2% | 1 |
| `we devise` | 2% | 1 |
| **任何 we-verb** | **48%** | 24 |

> 📊 **结论**：约一半的获奖论文在 abstract 中使用 `we + verb` 引出方法。`propose` 和 `introduce` 是首选。

### 1.3 转折/连接词使用频率 [N=50]

| 连接词 | 使用率 | 篇数 |
|--------|--------|------|
| `however` | **34%** | 17 |
| `furthermore` | 12% | 6 |
| `yet` | 8% | 4 |
| `moreover` | 6% | 3 |
| `in contrast` | 4% | 2 |
| `to address this` | 4% | 2 |
| `despite` | 4% | 2 |
| `although` | 4% | 2 |
| `in particular` | 4% | 2 |
| `specifically` | 4% | 2 |

> 📊 **结论**：`however` 是唯一高频转折词。连接词总体使用克制。

### 1.4 "we" 的使用分布 [N=50]

| "we" 出现次数 | 篇数 | 占比 |
|-------------|------|------|
| **2 次** | 16 | 32% |
| **1 次** | 13 | 26% |
| **3 次** | 11 | 22% |
| 4 次 | 4 | 8% |
| 0 次 | 2 | 4% |
| ≥5 次 | 4 | 8% |

> 📊 **结论**：1-3 次 "we" 覆盖了 80% 的获奖论文。最典型的是 2 次——一次引入方法，一次报告结果。

---

## 二、记忆点植入策略 [N=50]

### 2.1 定量统计

| 记忆点类型 | 检测数 | 占比 | 代表论文 |
|-----------|--------|------|---------|
| **极简/低成本** | 15 | **30%** | CowClip: "on 1 GPU", "only a few million pairs" |
| **破折号强调** | 9 | **18%** | LLM2CLIP: "—without large-scale retraining—" |
| **惊人数字** | 未自动检测 | — | CowClip: "from 12 hours to 10 minutes" |

> 📊 **结论**：48% 的获奖论文至少使用了一种记忆点技术。极简/低成本是最常用的钩子。

### 2.2 破折号强调实例 [9/50]

- LLM2CLIP: `—without large-scale retraining—`
- Causal Structure Learning: `—leading to poor performance on irregularly sampled data—`
- Hand Gesture Recognition: `—either RGB or thermal—`
- PlantTraitNet: `—from citizen science to satellite imagery—`
- Reliable Conflictive Multi-view: `—even when views strongly disagree—`

### 2.3 极简/低成本实例 [15/50]

- CowClip: `on a single V100 GPU`, `from 1K to 128K batch size`
- LLM2CLIP: `only a few million image-caption pairs`, `same training cost`
- DropMessage: `without any additional parameters`
- Every Bit Helps: `with a few queries`

---

## 三、标题命名模式 [N=50]

| 模式 | 占比 | 篇数 |
|------|------|------|
| **NAME: Subtitle** | **58%** | 29 |
| Other / Mixed | 38% | 19 |
| Question-Based | 4% | 2 |

> 📊 **结论**：NAME:Subtitle 是 AAAI 获奖论文的绝对主流命名模式。

---

## 四、按论文类型的写作策略差异 [N=50]

### 4.1 理论型（12 篇）

| 特征 | 数据 |
|------|------|
| Abstract 词数均值 | **141**（最短） |
| 方法引出动词 | introduce: 2, propose: 2, present: 1（**低频**——理论论文不强调"方法"） |
| 记忆点 | 极简 3/12、破折号 3/12 |

**叙事特征**：定义模型 → 已知困难 → 核心问题 → 定理级答案。方法引出动词使用率低于平均值。

**代表作**：Revelations (POMDP 可判定性), Every-Bit-Helps (最优 distortion), Clustering with Outliers (近似算法)

### 4.2 模型/方法型（23 篇）

| 特征 | 数据 |
|------|------|
| Abstract 词数均值 | **165**（中位） |
| 方法引出动词 | propose: 8, introduce: 5, present: 2, develop: 2（**高频**） |
| 记忆点 | 极简 7/23、破折号 3/23 |

**叙事特征**：任务定义 → 痛点量化 → 方法提出 → SOTA 结果。这是 AAAI 的标准叙事模板。

**代表作**：LLM2CLIP, MaskBooster, CowClip, ReconVLA, DropMessage

### 4.3 基准/资源型（4 篇）

| 特征 | 数据 |
|------|------|
| Abstract 词数均值 | **234**（最长——含数据统计） |
| 方法引出动词 | introduce: 1（**低频**——资源本身是核心贡献） |
| 记忆点 | 极简 2/4、破折号 2/4 |

**叙事特征**：资源缺口 → 构建流程 → 数据统计 → 关键洞见。Abstract 显著更长。

**代表作**：DivShift (7.5M images), PlantTraitNet, Is My Prediction Arbitrary?

### 4.4 应用驱动型（11 篇）

| 特征 | 数据 |
|------|------|
| Abstract 词数均值 | **145**（次短） |
| 方法引出动词 | introduce: 3, propose: 3, present: 1, develop: 1 |
| 记忆点 | 极简 3/11、破折号 1/11 |

**叙事特征**：应用场景 → AI 化难点 → 问题建模 → 领域验证。Abstract 相对精简。

**代表作**：JoLT (临床), GxVAEs (药物发现), Slum Detection, BindGPT (分子设计)

---

## 五、段落组织与贡献列表 [N=45 intro]

### 5.1 贡献列表

- 引导句最常用：`To sum up, our contributions are as follows:` / `Our contributions are as follows:`
- 条数：3-4 条最常见
- 末条几乎总是实验结果

### 5.2 图/表引用模式

- Teaser Figure (Fig. 1) 在 Introduction 中被提及并展示核心思想
- 表格使用 booktabs 风格（三线表）、数字右对齐、最优值粗体

---

## 六、审稿心理与写作策略

### 6.1 Reviewer 阅读顺序

```
1. Title（5秒）→ 2. Abstract（30秒）→ 3. Teaser Fig + Contributions（1分钟）
→ 4. Main Results Table（30秒）→ 5. Introduction 段①-②
→ 6. Method Overview → 7. Ablation → 8. Conclusion
```

### 6.2 获奖论文的共性 [N=50]

1. **问题早暴露**：abstract 前 1/3 即明确本文解决的问题
2. **写作克制**："extensive experiments" 几乎不用，"state-of-the-art" 仅 13%
3. **主动第一人称**：abstract 中 "we" 出现 1-3 次（覆盖 80%）
4. **命名即记忆点**：58% NAME:Subtitle
5. **每篇一个记忆点**：48% 有极简或破折号强调
6. **理论论文不假装有实验**：理论型 abstract 最短，不强行刷 SOTA

---

## 七、定量证据索引

| 文件 | 内容 |
|------|------|
| `modules/paper-corpus/corpus_v4_corrected.json` | 50 篇完整数据（手动矫正类型标注） |
| `modules/paper-corpus/summary_v4_final.json` | 汇总统计 |
| `modules/paper-corpus/clean_v4/*.txt` (50 个) | 每篇清洗后的可读文本 |
| `AAAI great paper/extract_v4_final.py` | V4 提取脚本（column-aware + wordninja） |
| `AAAI great paper/analyze_patterns.py` | 语言学分析脚本 |

---

## 八、版本演进

| 版本 | Abstract 成功率 | 关键技术 | 主要局限性 |
|------|----------------|---------|-----------|
| V1 (PyPDF2) | 12/50 (24%) | `extract_text()` | 编码错误、GBK |
| V2 (pdfplumber raw) | 45/50 (90%) | `extract_text()` | 双栏交叠、词间空格丢失 |
| V3 (column-aware) | 42/50 (84%) | `extract_words()` + 分栏检测 | 空格丢失、abstract 截断 |
| **V4 (column + wordninja)** | **50/50 (100%)** | 分栏 + wordninja 分词 + 改进正则 | 少量专业术语拆分不准 |

**V4 最终方案**：pdfplumber 词级位置提取 → 分栏边界检测 → wordninja 智能分词 → 多模式正则 abstract/intro 检测 → 手动矫正论文类型标签。

---

> **如何使用这些数据**：本文档提供定量基准（*what*），以下模块提供操作指导（*how*）：
> - 将统计数据转化为可填空的句子模板 → `modules/sentence-craft.md`（句法模板库：开场/痛点/提案/方法/结果/对比/过渡/局限性，共 34 个模板）
> - 按论文类型的差异化写作策略 → `paper-types/{theory,model-method,benchmark-resource,application-driven}.md`
> - 数据来源与提取细节 → `modules/paper-corpus/`
