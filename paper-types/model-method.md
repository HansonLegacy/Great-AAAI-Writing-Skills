# 模型/方法型 — AAAI 写作专属指南

> 适用：论文核心贡献是新架构、新训练方法、新框架设计。涵盖 LLM/基础模型、视觉/感知、小模型/高效型、多模态等子类。
> 这是 AAAI 最常见（>50%）的论文类型。

---

## 一、核心叙事定位

**你在修补一个明确的技术痛点，用你自己设计的方法。**

Reviewer 的期待：清晰的任务定义 → 现有方法的可量化盲区 → 你的方法设计（有技术理由支撑） → SOTA 实验 + 消融验证。

---

## 二、各章节关键差异

### Title
- 命名模式：`NAME: Descriptive Subtitle` ——占获奖论文标题的绝大多数
- 或 `Descriptive Action Phrase for Task`：`Unifying Random Dropping for Graph Neural Networks`
- 确保标题可被简记为 NAME（3-10 字符缩写）

### Abstract（详见 `sections/abstract.md` 类型 2）
- 标准五步弧线。这是所有类型中最标准的应用。
- 记忆点植入至关重要——惊人数字或极简做法

### Introduction（详见 `sections/introduction.md` 类型 2）
- 六段骨架完整执行。"三重一致"（痛点↔创新↔贡献）强制要求。
- 每个痛点量化。每个贡献可追溯。

### Method（详见 `sections/method.md` 类型 2）
- Module-by-module 结构，每个三元组（动机/设计/优势）。
- Pipeline 图是 Method 中最重要的图。

### Experiments（详见 `sections/experiments.md` 类型 2）
- 实验负担最重：多 benchmark SOTA + 消融 + 可视化。
- 每个 module 有对应消融行。

---

## 三、子类微调

| 子类 | 痛点重点 | 实验重点 | 获奖示例 |
|------|---------|---------|---------|
| **LLM/基础模型** | 幻觉/对齐/效率/训练成本 | 多 benchmark + 人工评估 + 效率 | LLM2CLIP, Alignment of LLMs |
| **视觉/感知** | 特征设计/泛化/domain gap | 多数据集 SOTA + 可视化 | MaskBooster, Fractured Glass |
| **小模型/高效型** | FLOPs/延迟/显存/训练时间 | 速度/显存 vs 精度 tradeoff 表 | CowClip, DropMessage |
| **多模态** | 模态对齐/融合策略/跨模态迁移 | 多模态 benchmark + 各模态消融 | ReconVLA, MindCross |
| **神经符号** | 神经与符号的桥接/一致性 | 推理质量 + 效率 + 可解释性 | Abductive Reflection |

---

## 四、获奖论文参考

| 论文 | 子类 | 推荐阅读重点 |
|------|------|------------|
| LLM2CLIP (2026) | LLM | LLM 如何增强视觉模型的叙事策略 |
| MaskBooster (2023) | 视觉 | 自训练教学框架的设计动机 |
| CowClip (2023) | 高效 | 标题即记忆点 + 极简效率突破 |
| Abductive Reflection (2025) | 神经符号 | 如何写问题驱动框架 |
| ReconVLA (2026) | 多模态+机器人 | VLA 框架的多模态融合策略 |

---

## 五、常见写作问题

| 问题 | 改法 |
|------|------|
| "加了几个 trick 凑出 SOTA" 的印象 | 每个模块写清楚三元组（动机+设计+优势），避免 trick 堆砌感 |
| 消融敷衍 | 每个 module → 一行消融；有交互效果则做组合消融 |
| 痛点太泛 | 每个痛点量化（>50% 参数 / 慢 3-13×） |
| 贡献列表流水账 | 每条 = 机制 + 收益 + 回指某痛点 |
| 实验只在一个 benchmark 上做 | 至少 2-3 个数据集（不同场景/规模） |
| LLM 论文中训练 cost 不透明 | 报告 GPU 型号 × 数量 × 训练时间 |

---

> **句子级差异**（`modules/sentence-craft.md`）：模型/方法型论文的句子层面特化：
> - 开场句 → §2.1 模式 A（定义型）或模式 B（趋势型——"X has emerged as"）
> - 痛点句 → §2.2 模式 A（However+技术局限）或模式 C（量化痛点——最有力道），优先用数字
> - 提案句 → §2.3 模式 A（We propose NAME, a...）或模式 B（To-X 过渡），动词选 `propose / introduce`
> - 方法描述 → §2.4 全部 5 种模式可用（组件枚举 / By-gerund / Mechanism→Purpose / Unlike 对比 / 观察驱动）
> - 结果句 → §2.5 模式 A（数字+对比——"achieves X, outperforming BASELINE by Y"），这是最标准的模型方法型结果句
> - 消融句 → §2.5 模式 C + §3 第 12 组 Before/After（贡献条目流水账→机制+收益）
> - 量化基准 → `modules/distilled-patterns.md` §四（模型方法型 Abstract 均值 165 词，23/50 篇为类型 2）
