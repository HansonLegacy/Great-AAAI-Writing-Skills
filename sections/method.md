# AAAI 方法写作（Method）

> **上游参考**：`research-paper-writing/references/method.md`（模块三元组、前向流程描述、Overview 模板）
> 本文档是 AAAI 特化版——按 4 种论文类型的 Method 结构分支 + 获奖论文实例。

---

## 〇、先读这个

`research-paper-writing/references/method.md` 中的**通用规律仍然适用**：
- 每个模块写清楚三元组：模块设计 / 模块动机 / 技术优势
- 先画 pipeline 图，再从图反推 subsection 结构
- 先写模块设计（骨架），再加动机和优势（血肉）
- Overview 段：setting + 核心贡献 + pipeline 图指针 + 各小节导读

**本文档新增**：按论文类型的 Method 结构差异 + AAAI 版式约束下的图表策略。

---

## 一、AAAI 版式约束下 Method 写作须知

| 约束 | 影响 |
|------|------|
| **7 页正文总限** | Method 通常占 1.5-2.5 页。需要在详细度和简洁性之间做取舍——算法伪代码比自然语言描述更省空间 |
| **算法与代码** | 推荐用 `algorithm` + `algorithmic` 包（`algorithm2e` 可能与 AAAI 样式冲突）。代码列表用 `newfloat` + `listings` |
| **双栏布局** | 大公式、宽表格需双栏（`\begin{figure*}` / `\begin{table*}`），但会打断阅读流——谨慎使用 |
| **数学公式字号** | 最小 6.5pt。不要降字号换密度——reviewer 看不清 |
| **图表放置** | 优先 `[t]`（页顶），次选 `[b]`（页底）。不得集中堆放于 Method 末尾 |

---

## 二、按论文类型的 Method 结构

### 类型 1: 理论/算法型

**Method = "Preliminaries + Main Results"**（无传统"方法"概念）。

```
\section{Preliminaries}           % 0.5-1 页
  % 模型定义、符号表、已知结论
  % 定义读者需要的基础概念

\section{Main Results}            % 1.5-2.5 页
  \subsection{[子结论1]}
    % 定理陈述（theorem 环境）
    % 证明草图（proof sketch）——给出直觉，不写完整证明
    % 紧致性讨论（tight? optimal? 条件能否放宽？）

  \subsection{[子结论2]}
    % 同上结构

\section{Algorithm / Construction} % 0.5-1 页（如适用）
  % 若从理论推出了算法，在此描述

\section{Experiments / Case Study} % 0.3-0.8 页
  % 轻量验证
```

**关键原则**：
- 定理陈述必须独立——reviewer 从 theorem 环境就能理解结论，不需读周围文字
- 证明草图的目标是"让 reviewer 相信证明是对的"，不是展开每一个 technical lemma
- 可在正文中 defer 部分证明到 Appendix（但核心定理的证明直觉必须在正文中）

> 📄 **Revelations (2025)** Method 结构：
> §2 Preliminaries (POMDP 定义、策略、目标)
> §3 Revelation Mechanism (定义 revelation、关键引理)
> §4 Belief Levels Construction (构造、主定理)
> §5 Implementation & Experiments (概念验证)

### 类型 2: 模型/方法型

**标准方法结构**——这是 AAAI 最常见的 Method 形态。

```
\section{Method}                         % 1.5-2.5 页
  \subsection{Overview}                  % ~0.2 页
    % Task setting（1-2 句回到问题定义）
    % Core idea（1-2 句核心思想）
    % Pipeline figure pointer（Fig. X）
    % Subsection roadmap（Section 3.1 covers..., 3.2 covers...）

  \subsection{[Module 1 Name]}           % ~0.4-0.7 页
    % Motivation: 为什么要这个模块（回指 Intro 中的痛点）
    % Module Design: 表示/网络结构/数据结构
    % Forward Process: input → step 1 → step 2 → output
    % Technical Advantage: 比起替代方案为什么更好

  \subsection{[Module 2 Name]}           % ~0.4-0.7 页
    % 同上三元组

  \subsection{[Module 3 Name]}           % ~0.4-0.7 页
    % 同上三元组

  \subsection{Implementation Details}    % ~0.2 页（或分散在各模块末尾）
    % 超参数、训练配置、优化器、学习率等
```

**关键原则**：
- 每个 subsection 独立可读——reviewer 读任何一个小节都能理解该模块
- 数学公式只在 serve 关键机制时使用——不要为了看起来"更数学"而堆公式
- Pipeline 图是 Method 中最重要的图——reviewer 常先看图再看文字

> 📄 **LLM2CLIP (2026)** Method 结构：
> §3.1 Preliminaries (CLIP background)
> §3.2 LLM2CLIP Framework (overview + architecture)
> §3.3 Caption Augmentation with LLM (LLM 生成 enhanced captions)
> §3.4 Fine-tuning with LLM Guidance (LLM 监督的微调策略)
> §3.5 Training and Implementation Details

### 类型 3: 基准/资源型

**Method = "数据构建 + 评估协议"。**

```
\section{The [NAME] Dataset/Benchmark}    % 1.5-2.5 页
  \subsection{Data Collection}
    % 数据来源（URLs / APIs / 合作机构 / 传感器类型）
    % 采集规模和时间范围
    % 伦理考量（IRB / 许可证 / 隐私）

  \subsection{Annotation Protocol}
    % 标注规范（annotation guideline）
    % 标注员资质和数量
    % Inter-annotator agreement（Cohen's κ / Fleiss' κ）
    % 质量控制流程（多轮审核 / 争议解决）

  \subsection{Dataset Statistics}
    % 样本数量、类别分布、数据划分
    % 与现有数据集的对比表

  \subsection{Evaluation Protocol}
    % 评估指标定义
    % Train / Val / Test 划分
    % 推荐的 baseline 方法列表
    % 公平比较的规则（如：所有方法用同样的数据增强？）

\section{Experiments}                     % 1-2 页
  % 全景 baseline 评估
  % 关键洞见分析
```

### 类型 4: 应用驱动型

**Method = "问题建模 + AI 方案适配"。**

```
\section{Problem Formulation}             % ~0.5 页
  % 将领域问题形式化为 AI 问题
  % 输入/输出/约束/目标函数

\section{Method}                          % 1.5-2 页
  \subsection{Overview}
  \subsection{[Domain-Specific Module 1]}
    % 为什么该领域需要这个模块（领域动机）
    % 模块设计 + 前向流程
  \subsection{[Domain-Specific Module 2]}
  \subsection{Integration & Deployment}（可选）
    % 实际部署的考量

\section{Experiments}                     % 1.5-2 页
  % 领域指标 + 标准 ML 指标
  % 真实场景数据
  % 案例分析
```

**关键原则（区别于类型 2）**：
- 每个设计决策解释"**为什么对这个领域必要**"——不只是"为什么比替代方案好"
- Problem Formulation 小节很重要——reviewer 可能不熟悉该领域
- 如果方法本身朴素，不必假装复杂——应用驱动的论文更看重实际效果和领域贡献

---

## 三、获奖 Method 的高频套路（蒸馏）

### 3.1 数学公式的使用法则

- **公式要有"使命"**：每个公式要么被引用解释（"Eq. X shows that..."），要么是算法的关键一步。不要为装饰而堆公式
- **关键公式给直觉**：先给直觉解释（"Intuitively, this means..."），再给公式；不要无过渡地抛公式
- **符号稳定**：全文用同一符号表示同一量。在某处首次定义后不再重新定义

### 3.2 Pipeline Figure 设计原则

- 数据流从左到右、从上到下
- 不同模块用不同颜色/框线区分
- 标出关键张量形状（`B×C×H×W`）
- Loss 函数位置清晰
- 训练/推理路径区隔（虚线 vs 实线）

### 3.3 模块动机的 4 种写法

| 写法 | 句式 | 适用场景 |
|------|------|---------|
| **问题驱动** | "A remaining challenge is... To address this, we design..." | 该模块对应 Intro 中某个显式痛点 |
| **观察驱动** | "We observe that... Considering this, we introduce..." | 该模块来自实验/经验中的发现 |
| **不足驱动** | "However, the above design alone cannot... because..." | 第二个模块承接第一个模块的不足 |
| **机会驱动** | "Benefiting from recent advances in..., we can..." | 该模块利用了某个新工具/新能力 |

---

## 四、写完自查清单

逐条过：

- [ ] Overview 段 ≥ 4 要素（setting + core idea + figure pointer + subsection roadmap）？
- [ ] 每个模块有明确的 Motivation → Design → Forward Process → Advantage？
- [ ] Pipeline 图清晰、颜色区分、关键张量形状标注？
- [ ] 数学公式每个都有"使命"——被文字引用解释？
- [ ] 符号全文稳定（无重载、无重复定义）？
- [ ] 图表放置 `[t]` / `[b]`，不在文末集中堆放？
- [ ] 页数预算：Method 节在 1.5-2.5 页内？
- [ ] 与 Intro 的 contributions 对应——每个 contribution 在 Method 中找到对应 subsection？

---

> **句子级模板**（`modules/sentence-craft.md`）：Method 的核心句子类型：
> - Overview 段 → §2.4 模式 A（组件枚举：NAME consists of (i)...(ii)...(iii)...）
> - 每个模块的动机句 → §2.4 模式 E（问题→观察→设计）或 §2.2（痛点句微缩版）
> - 每个模块的设计描述 → §2.4 模式 B（By+gerund）、模式 C（Mechanism→Purpose）
> - 与 prior work 切割 → §2.4 模式 D（Unlike X which Y, we Z）
> - 模块间过渡 → §2.7 过渡句 模式 C（However, Module A alone cannot...）
> - 公式写作 → §3 第 8 组 Before/After（公式无解读→加引导句+直觉解释）
> - 写完后过 → §六 Method 句子自查（3 条）
> - **Pipeline 图注写法** → `modules/caption-writing.md` §四 图注句法模板（架构图模板 + 自包含原则）
