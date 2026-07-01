# 基准/资源型 — AAAI 写作专属指南

> 适用：论文核心贡献是新数据集、新 benchmark、新评估协议、或大规模系统性实证研究。

---

## 一、核心叙事定位

**你给社区提供了一个前所未有的资源或视角。** 这个资源的长期价值（会被后续论文使用）才是核心贡献。

Reviewer 的期待：现有资源为什么不够 → 你如何构建新资源（采集+质量控制） → 这个资源揭示了什么洞见 → 对社区的长期价值。

---

## 二、各章节关键差异

### Title
- 常含关键词：`Dataset`, `Benchmark`, `Framework for...`, `Exploring...`
- 命名模式：`ResourceName: Type and Scale` 或 `Action on Domain Data`

### Abstract（详见 `sections/abstract.md` 类型 3 变体）
- ③ 处给资源构建（非方法贡献），④ 处给构建流程和评估协议
- ⑤ 处给关键发现/洞见 + 社区价值

### Introduction（详见 `sections/introduction.md` 类型 3 变体）
- 段② 是**资源痛点**（非方法痛点）——现有数据的盲区
- Contributions 中核心条目是新资源本身的命名 + 规模统计
- 需要论证"为什么这批论文的起点"而非"一篇论文的附属品"

### Method/Dataset
- 四个关键 subsection：Data Collection → Annotation Protocol → Statistics → Evaluation Protocol
- Inter-annotator agreement (Cohen's κ / Fleiss' κ) 是质量控制的关键证据
- 数据集统计图/表是本节的图表主角

### Experiments
- **baseline 全景覆盖**：覆盖不同方法论范式
- 关键输出不只是数字，还有**分析洞见**（为什么某些 baseline 在某种偏差下表现差）
- 与已有数据集的系统对比（如果没有直接可比数据集，做定性对比）

---

## 三、获奖论文参考

| 论文 | 年份 | 核心贡献 | 推荐阅读重点 |
|------|------|---------|------------|
| DivShift | 2025 | 7.5M 图像 + 5 类 distribution shift 分析框架 | 如何将偏差分类 + 反直觉洞见:"偏差的影响小于预期" |
| DISCount | 2024 | 大规模图像计数 + detector-based 采样框架 | 方法+资源双重贡献的叙事策略——两个贡献互相支撑 |
| SimFair | 2023 | Fairness-aware 多标签分类统一框架 + 基准 | 如何将 fairness 指标系统化为可复用的评估协议 |
| Fractured Glass | 2026 | 物理对抗样本基准：相机故障模拟 → 自动驾驶系统鲁棒性测试 | 真实世界系统性问题 → benchmark 设计的动机链 |
| Nowcasting Temporal Trends | 2024 | 间接调查数据的时间趋势推断方法 + 社交媒体案例 | 非传统数据源如何构建为可验证的科学资源 |
| PlantTraitNet | 2026 | 全球植物性状推断框架 + 不确定性感知 | 应用+基准双重类型融合——如何在一篇论文中同时服务 domain scientist 和 ML reviewer |

> **注**：PlantTraitNet 和 Generalizable Slum Detection（2026）是应用驱动型与基准/资源型的交叉——核心贡献同时包含领域应用和可复用资源。当你的论文有类似双重属性时，参考它们的叙事策略：Abstract 和 Introduction 以资源贡献为主线，Experiments 同时服务两个 audience。

---

## 四、常见写作问题

| 问题 | 改法 |
|------|------|
| 资源价值没说清楚 | 系统对比已有资源（表格！），明确你的资源填补了什么空白 |
| baseline 不够全 | 至少覆盖 5-10 个代表性方法、不同方法论范式 |
| 数据质量论证弱 | Inter-annotator agreement + 多轮质控流程描述 + 典型案例 |
| 只有统计没有洞见 | 解释 "why some baselines fail" 而不只是 "method A is best" |
| 规模被吹成核心贡献 | 规模本身不是贡献——通过规模揭示的新洞见才是 |

---

> **句子级差异**（`modules/sentence-craft.md`）：基准/资源型论文的句子层面特化：
> - 开场句 → §2.1 模式 E（资源痛点开场——"X have enabled progress. However, existing X remain limited..."）
> - 痛点句 → §2.2 模式 A（However+具体资源盲区），强调现有资源的**覆盖范围局限**
> - 提案句 → §2.3 模式 A（动词选 `introduce / curate / construct` 而非 `propose`——资源本身是核心贡献）
> - 方法描述 → §2.4 模式 A（组件枚举——"NAME consists of N samples across X categories..."）
> - 结果句 → §2.5 模式 B（观察+解读——"We find/observe that..."），强调**洞见**而非数字
> - 局限性 → §2.8 模式 C（资源局限性——"covers X but does not yet include Y"）
> - 量化基准 → `modules/distilled-patterns.md` §四（基准型 Abstract 均值 234 词，最长——含数据统计描述）
