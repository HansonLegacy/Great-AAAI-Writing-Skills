# AAAI 论文类型分类与写作策略

> 基于 AAAI 2023-2026 获奖论文的分析，将 AAAI 论文归纳为 4 种类型。
> 每种类型在 **贡献形态、叙事主线、Intro 策略、Method 重点、实验预期** 上有显著差异。

---

## 四种论文类型总览

| | 理论/算法型 | 模型/方法型 | 基准/资源型 | 应用驱动型 |
|---|---|---|---|---|
| **核心贡献** | 新定理/新界/新算法 | 新架构/新训练方法/新框架 | 新数据集/新 benchmark/系统洞见 | AI × 真实问题的解决方案 |
| **叙事主线** | 抛问题→给答案（可判定？最优？） | 痛点→方法→SOTA | 现有资源不足→我们构建→揭示洞见 | 领域需求→AI 建模→真实验证 |
| **Method 主体** | 定义→引理→定理→证明草图 | 模块设计→前向流程→技术优势 | 数据采集→标注→质量控制→协议 | 问题建模→AI 方案适配→部署考量 |
| **实验角色** | 验证理论（实验为辅） | 支撑 claims（消融+SOTA） | 基准评估+baseline 全景 | 领域指标+案例分析 |
| **获奖实例** | Revelations, Every-Bit-Helps, Clustering w/ Outliers | LLM2CLIP, MaskBooster, ReconVLA, CowClip | DivShift, DISCount, SimFair | PlantTraitNet, JoLT, Slum Detection |

---

## 类型 1: 理论/算法型

### 识别特征

- 贡献是**定理、证明、界（bounds）、复杂度分析、可判定/不可判定结论**
- 实验不是主角（可能只有 toy example 或小规模验证）
- 论文标题常含 "Optimal", "Decidable", "Tight Bound", "Efficient", "Complexity" 等词

### 获奖论文映射

| 论文 | 年份 | 核心贡献形态 |
|------|------|-------------|
| Revelations: A Decidable Class of POMDPs | 2025 | 可判定性结论 + revelation mechanism |
| Every Bit Helps: Optimal Distortion with Few Queries | 2025 | 最优界的紧刻画 |
| Clustering What Matters: Optimal Approximation | 2023 | 近似算法 + 理论保证 |
| Computing Game Symmetries and Equilibria | 2025 | 算法 + 理论性质 |
| Eliminating Majority Illusion is Easy | 2025 | 计算复杂性结论 |
| Robust Average-Reward MDP | 2023 | MDP 鲁棒性理论 |
| Model Change for DL Concepts | 2026 | 逻辑理论 |
| Causal Structure Learning with Theoretical Score | 2026 | 理论得分分析 |

### 叙事主线

不跟 "metric 提升" 框架，走 **"回答一个核心问题"** 路线：

```
定义模型/场景
  → 已知的困难（先前工作止步于何处）
  → 抛出核心问题（常用缩进斜体视觉化：What is the complexity of ...?）
  → 我们的答案（定理/结论陈述）
  → 证明策略概述（给出直觉，非完整证明）
  → 贡献列表（谈结论性质：decidable/optimal/tight/exact）
```

### Intro 策略

- **开篇二选一**：
  - **叙事钩子**（Every-Bit-Helps 式）：用一个具体可视化场景起手（"Imagine you are tasked with..."），再抽象成概念
  - **模型定义直入**（Revelations 式）：定义模型 + 目标 + 已知困难 + 我们关注的范围
- **核心问题视觉化**：将核心问题用缩进/斜体/粗体单独拎出，让 reviewer 一眼看到"这篇论文在回答什么问题"
- **贡献 bullet**：每条给定理级结论与界，不写 "we propose a novel method"

### Method 结构模板

```
\section{Preliminaries}
  % 定义、记号、已知结果
\section{Main Results}
  % 定理 1: 陈述 + 证明草图 + 紧致性讨论
  % 定理 2: 陈述 + 证明草图 + 紧致性讨论
\section{Algorithm / Construction}（如适用）
\section{Experiments / Case Study}（如适用，通常是轻量验证）
```

### 实验预期

- AAAI 对纯理论论文的实验中立——不强求大规模实验
- 若有实验：通常为小规模验证（toy domain、合成数据）、展示理论预测的行为
- 实验节的标题常为 "Experiments" 或 "Case Study" 或 "Empirical Evaluation"（低调）

### 常见病灶

| 病灶 | 改法 |
|------|------|
| 开篇太抽象、不知所云 | 用叙事钩子或具体小例子落地 |
| 问题不突出 | 把核心问题做成缩进/粗体/斜体块，视觉上单独拎出 |
| 定理陈述淹没在文字中 | 用 `\begin{theorem}...\end{theorem}` 环境独立展示 |
| 贡献 bullet 写得太虚 | 每条给具体结论类型（"We establish that X is decidable"），不含糊 |

---

## 类型 2: 模型/方法型

### 识别特征

- 贡献是**新的神经网络架构、训练策略、表示学习方法、推理框架等**
- 有明确的 benchmark 评估和 SOTA 比较
- 占据 AAAI 接收论文的最大比例

### 子类（写作策略相同，细节微调）

| 子类 | 特征 | 获奖实例 |
|------|------|---------|
| LLM/基础模型 | 以大模型为核心研究对象 | LLM2CLIP, Alignment of LLMs, BindGPT |
| 视觉/感知 | CNN/Transformer/ViT 用于视觉任务 | MaskBooster, Two Heads Hand Pose, Fractured Glass |
| 小模型/高效型 | 聚焦效率、压缩、边缘部署 | CowClip, DropMessage, Cumulant Attention |
| 多模态/跨模态 | 多种数据模态的融合与对齐 | ReconVLA, MindCross, Caption Anything |
| 神经符号 | 神经+符号方法结合 | Abductive Reflection, Neurosymbolic RL |

### 叙事主线

标准 "痛点驱动" 框架（六段式结构）：

```
任务定义 + 应用场景
  → 现有方法 + 痛点（each with 技术原因 + 具体代价）
  → 我们的洞见/观察
  → 提出方法 NAME（+ teaser 图）
  → 方法步骤概述 + 与 concurrent work 切割
  → Contributions 列表
```

### Intro 策略

- 跟随六段式结构模板（段①-⑥ + contributions 列表）
- **三重一致**强制要求：痛点枚举 ↔ 创新枚举 ↔ contributions bullet，数目和顺序对齐
- **Abstract ↔ Intro 逐句可连线**（详见 `sections/introduction.md`）
- 每个痛点必须带 **技术原因** + **具体代价**（量化优先）

### Method 结构模板

```
\section{Method}
  \subsection{Overview}          % setting + 核心思想 + pipeline 图 + 各小节导读
  \subsection{Module 1}          % 动机 → 设计 → 前向流程 → 技术优势
  \subsection{Module 2}
  \subsection{Module 3}
  \subsection{Implementation Details}（或分散在各模块末尾）
```

### 实验预期

- **强预期**：多 benchmark SOTA 比较 + 消融实验 + 可视化分析
- 必须覆盖所有声称的贡献点（每个模块有对应消融）
- 需报告统计显著性（std/p-value）

---

## 类型 3: 基准/资源型

### 识别特征

- 贡献是**新数据集、新 benchmark、新评估协议、大规模系统性实证研究**
- 论文的核心价值在于"提供了社区前所未有的资源或洞见"
- 标题常含 "Dataset", "Benchmark", "Survey", "Analysis", "Exploring" 等词

### 获奖论文映射

| 论文 | 年份 | 核心贡献形态 |
|------|------|-------------|
| DivShift | 2025 | 大规模 biodiversity 分布偏移系统性研究 |
| DISCount | 2024 | 大规模图像集合的计数方法 + 采样框架 |
| SimFair | 2023 | Fairness-aware 多标签分类框架 |
| Arbitrariness and Social Prediction | 2024 | 公平分类中的方差混淆效应实证分析 |
| PlantTraitNet（兼具应用） | 2026 | 全球尺度植物性状推断框架 |
| Generalizable Slum Detection（兼具应用） | 2026 | 贫民窟检测 + 跨域泛化 |

### 叙事主线

强调"**为什么需要这个新资源/新视角**"：

```
为什么现有资源不够（规模/多样性/标注质量/视角盲区）
  → 我们构建/收集了什么（数据来源+规模+特点）
  → 如何保证质量（采集流程+标注协议+质量控制）
  → 这个资源揭示了什么（baseline 全景 + 关键洞见）
  → 对社区的长期价值
```

### Intro 策略

- **段②的痛点不是方法痛点，是资源痛点**：现有 benchmark 太小/太偏/没有覆盖 X 场景/标注不够细
- 贡献列表中的**核心条目是新资源本身**（命名 + 规模统计）
- 需要解释为什么这个资源是"一批论文的起点"而不只是"一篇论文的附属品"

### 实验结构模板

```
\section{The [NAME] Dataset/Benchmark}
  \subsection{Data Collection}      % 来源、规模、伦理
  \subsection{Annotation Protocol}  % 标注规范、质量控制、inter-annotator agreement
  \subsection{Dataset Statistics}   % 分布、统计图表
  \subsection{Evaluation Protocol}  % 评估指标、train/val/test 划分
\section{Experiments}
  \subsection{Baselines}            % 全面的 baseline 方法覆盖
  \subsection{Main Results}         % 全景对比表
  \subsection{Analysis}             % 关键发现与洞见
```

### 实验预期

- **必须全面**：覆盖足够多的 baseline（旧+新、弱+强）
- 数据统计是核心内容（图表比例可观）
- 需要让 reviewer 相信"这个资源将来会被使用"

### 常见病灶

| 病灶 | 改法 |
|------|------|
| 资源价值没说清 | 解释为什么现有资源不行，为什么你这个是"community service" |
| baseline 不够全 | 至少覆盖 5-10 个代表性方法 |
| 数据质量论证弱 | 必须有 inter-annotator agreement、质量控制流程描述 |
| 过度吹嘘规模 | 规模本身不是贡献——通过规模揭示的**新洞见**才是 |

---

## 类型 4: 应用驱动型

### 识别特征

- 核心贡献是用 AI **解决一个明确的实际问题**（医疗、教育、环保、农业、社会公平等）
- 方法不一定是全新的——方法的适配和部署可能比方法本身更关键
- 常出现于 AAAI 的 AI for Social Impact、IAAI 等 track
- 标题常含具体应用领域的术语

### 获奖论文映射

| 论文 | 年份 | 核心贡献形态 |
|------|------|-------------|
| JoLT: Language + Time-Series for Clinical | 2024 | 临床时间序列解读 |
| Nowcasting Temporal Trends Using Indirect Surveys | 2024 | 社会经济趋势预测 |
| Strategic Recommendation for Online Platforms | 2024 | 在线平台匹配 |
| Multi-Modal Hand-to-Mouth Gesture Recognition | 2025 | 自闭症行为分析 |
| Understanding Behavioral Patterns in Autistic Children | 2025 | 眼手协调多模态分析 |
| PlantTraitNet（兼具基准） | 2026 | 全球植物性状推断 |
| Generalizable Slum Detection（兼具基准） | 2026 | 卫星图像贫民窟检测 |
| Scaling Up Pareto Optimization in the Amazon | 2024 | 浮动太阳能-水电系统优化 |
| GxVAEs: Generate Hit Molecules from Gene Expression | 2024 | 药物发现 |

### 叙事主线

遵循 "应用场景先行" 逻辑——**先让 reviewer 理解为什么这个问题重要，再谈你的 AI 方案**：

```
领域背景：这是一个什么真实问题？为什么重要？（让非领域专家也能理解）
  → 这个问题的 AI 解决难点是什么（数据稀缺/标注贵/跨域泛化/部署约束...）
  → 我们的 AI 方案：如何针对该领域特点建模
  → 领域验证：在真实场景/真实数据上的效果
  → 对该领域的实际意义
```

### Intro 策略

- **段①从应用场景起手**而非从任务定义起手（与模型/方法型相反）
- 痛点带领域背景——不需 reviewer 是该领域专家也能理解
- 贡献列表中除了方法贡献，通常含"领域影响"类条目
- 如果同时有新方法贡献，可以"双线并行"：应用线 + 方法线

### Method 结构模板

```
\section{Problem Formulation}     % 将领域问题形式化为 AI 问题
\section{Method}
  \subsection{Overview}
  \subsection{Domain-Specific Module 1}  % 针对该领域特点的设计
  \subsection{Domain-Specific Module 2}
  \subsection{Integration & Deployment}（可选：部署/实际使用考量）
```

### 实验预期

- **领域指标优先**：除了标准 ML 指标，必须有该领域认可的评价方式
- **案例分析**很重要：show 几个具体的成功/失败案例
- **真实数据验证**被高度期待（不仅是公开 benchmark）
- 需要讨论局限性时的"诚实"——真实场景中的 failure mode

### 常见病灶

| 病灶 | 改法 |
|------|------|
| AI 方法和领域脱节 | 每个设计决策解释"为什么对这个领域必要" |
| 实验只用标准 benchmark | 补充真实场景数据/领域专用指标 |
| 领域贡献没说清 | 引言中让领域专家能点头，实验中有领域意义的讨论 |
| 方法太朴素但吹太大 | 应用驱动的论文审稿人更宽容方法的简洁性——但前提是应用贡献实在 |

---

## 类型快速判定流程

```
1. 论文的核心贡献是定理/证明/复杂度结论？
   → 是 → 类型 1: 理论/算法型
   → 否 → 2

2. 论文的核心贡献是一个新的数据集/benchmark/评估协议？
   → 是 → 类型 3: 基准/资源型
   → 否 → 3

3. 论文的核心动机是解决一个具体的实际领域问题（医疗/教育/环保...）？
   → 是 → 类型 4: 应用驱动型
   → 否 → 4

4. 其他情况（新的模型架构/训练方法/框架设计）→ 类型 2: 模型/方法型
```

## 跨类型论文的处理

有些论文跨两个类型（如 PlantTraitNet 既是新 benchmark 又是应用驱动）。处理原则：
- 按**主要贡献**归类，次要类型的 guidance 作为参考
- 或者让用户自行选择主要视角
- 写作时以主要类型的叙事主线为主，在相关章节融入次要类型的元素

---

> **类型判定后的下一步**：
> - 加载专属写作指南 → `paper-types/{theory,model-method,benchmark-resource,application-driven}.md`（类型级叙事策略 + 句子差异）
> - 生成章节大纲 → `modules/outline-template.md`（按类型的页数预算 + 大纲模板）
> - 逐节写作 → `sections/{title,abstract,introduction,...}.md`（段落骨架）
