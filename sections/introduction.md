# AAAI 引言写作（Introduction）

> 本文档是 AAAI 特化版——在通用引言写作规律之上，叠加按论文类型的分支策略和获奖论文实例。

---

## 〇、先读这个

通用引言写作规律（方法类六段骨架：①任务+应用 → ②痛点 → ③铺垫 → ④提出方法 → ⑤对比+结果 → ⑥贡献列表；Abstract ↔ Intro 逐句对应；三重一致：痛点 ↔ 创新 ↔ contributions 数目与顺序对齐；贡献列表写法与连接词工具箱）已内化到本文档中。

**本文档聚焦**：按 4 种论文类型的 Intro 分支策略 + AAAI 特有约束 + 获奖论文 Intro 结构拆解。

---

## 一、AAAI 特有约束

| 约束 | 说明 |
|------|------|
| **引用** | Intro 可以含 `\cite`（与 Abstract 相反），且引用应尽早出现——段①/②即开始引用 |
| **长度** | 约 600-1000 词（5-7 段 + contributions），视觉上 1-1.5 栏。不得超过页数预算（正文共 7 页） |
| **Teaser 图** | `\includegraphics` 指向 teaser figure（`Fig. 1`）。图应在第一页可见——用 `[t]` 放置 |
| **`\textbf{}` 用法** | 用于标痛点名、方法名（2-4 词短名），方便 reviewer 快速扫描和引用 |
| **Contributions** | 标准结尾是 `\textbf{Our contributions are as follows:}` + itemize/enumerate 列表 |
| **匿名投稿** | Teaser 图中不含机构 logo/名称；自引匿名化；不用 "In our previous work..." |

---

## 二、按论文类型的 Intro 分支策略

### 类型 1: 理论/算法型

**不走 "metric 提升" 框架，走 "回答问题" 框架。**

#### 骨架（4-5 段 + contributions）

| 段 | 角色 | 内容 |
|----|------|------|
| ① 模型/场景 | 定义研究对象 + 为什么重要 | 1-2 句定义模型 + 目标 + 1 句应用/理论意义 |
| ② 已知难度 | 前人工作止步于何处 | 已有结论（undecidable / NP-hard / 界不够紧） + 留下什么 open question |
| ③ 核心问题 | **视觉化抛出**（缩进/斜体/粗体） | `This raises an important question: Is X decidable / What is the optimal bound for Y?` |
| ④ 我们的答案 | 定理级陈述 + 证明策略直觉 | `We answer this question in the affirmative. Specifically, we prove... The key insight is...` |
| ⑤ 贡献列表 | 3-4 bullet，每条给结论性质 | `We establish that X is decidable.` / `We provide a tight bound of O(n log n).` |

#### 开场二选一

**A. 叙事钩子（Every-Bit-Helps 式）**

```
"Imagine you are tasked with allocating office spaces in a medical building
to a group of doctors. Each doctor provides a ranked list..."
→ 把场景抽象成概念（distortion）
→ 接上已有界
→ 抛出核心问题
```

适用：贡献概念本身可用一个日常场景直觉化时。

**B. 模型定义直入（Revelations 式）**

```
"POMDPs form a prominent model for sequential decision making under
uncertainty. Our goal is to construct exact algorithms..."
→ 已知难度（undecidable）
→ 收窄关注点（almost-sure strategies）
→ 用内联粗体标记逻辑支点：**Our starting point is...**
  **The fundamental question we ask is whether...**
```

适用：领域专业性强，核心问题本身已是明确的技术问题。

#### 获奖实例拆解

> 📄 **Revelations (2025)** — Intro 结构：
> 段① POMDP 模型定义 + 目标（exact algorithms）
> 段② 已知：most formulations undecidable
> 段③ 收窄：almost-sure strategies + 抛出核心问题 **whether the problem is decidable**
> 段④ 引入 revelation mechanism + **this gives us the belief levels** + **this results in a decidable class**
> Contributions: 4 bullet 分别给 (1) revelation mechanism (2) decidable class (3) undecidable extension (4) 概念验证实现

### 类型 2: 模型/方法型

**使用完整的六段骨架。** 这是 AAAI 最常见的情形，不再重复骨架内容。

#### AAAI 模型/方法型特化要点

1. **痛点优先量化**：段② 的每个痛点尽量给数字——"> 50% 参数"、"慢 3-13×"、"显存 +40%"
2. **三重一致**严格执行：每个痛点用 `\textbf{}` 起短名，创新用同名回应
3. **与 concurrent work 切割**：段⑤ 点名最相关 concurrent work 并明确区分
4. **Contributions 末条上数字**：`Extensive experiments on X, Y, Z show that NAME achieves...`

#### LLM/大模型子类的特殊考量

- 段② 常涉及：LLM 幻觉/对齐/效率/训练成本
- 段③ 铺垫段（可选）常引入所用 LLM 的背景（如 "GRPO is a recent RL framework..."）
- 段⑤ 常与同名 concurrent work 对比（LLM 领域 concurrent work 多）
- 实验常涉及 GPU 时数——在 Intro 中提及效率时注意用词精确

#### 小模型/高效型子类的特殊考量

- 段② 的核心痛点是 **效率数字**——FLOPs / 延迟 / 显存 / 训练时间
- 段④ 的"记忆点"优先选"成本降低"
- 实验节的效率对比是核心——在 contributions 中预留效率条

### 类型 3: 基准/资源型

**骨架：段② 不是方法痛点，是资源痛点。**

| 段 | 角色 | 内容 |
|----|------|------|
| ① 该领域+现状 | 任务定义 + 领域应用 | 为什么这个领域需要数据/基准 |
| ② 资源痛点 | **现有资源的盲区** | 规模不够/多样性不够/视角缺失/标注不细 |
| ③ 我们构建的资源 | 命名 + 规模 + 特点 | `We introduce [NAME], a [size] [type] that...` |
| ④ 构建方法概述 | 数据来源+质量保证 | 采集+标注+协议+质量控制 |
| ⑤ 关键发现（可选） | 资源揭示了什么 | baseline 全景中的关键洞见 |
| ⑥ 贡献列表 | 3-4 bullet | (1) 资源 (2) 协议/方法 (3) 洞见 (4) 社区价值 |

#### 获奖实例拆解

> 📄 **DivShift (2025)** — Intro 结构：
> 段① 大规模众包数据 → 物种识别成功 → 但数据有偏见
> 段② 现有研究的盲区：偏见对细粒度识别的影响不清楚
> 段③ We introduce DivShift framework + DivShift-NAWC dataset（7.5M images, 5 bias types）
> 段④ 评估协议：species- and ecosystem-focused metrics
> 段⑤ 关键发现：biases confound model performance less than expected
> Contributions: (1) DivShift framework (2) NAWC dataset (3) comprehensive empirical study (4) recommendations

### 类型 4: 应用驱动型

**骨架：应用场景先行——先让 reviewer 理解"为什么这个问题重要"。**

| 段 | 角色 | 内容 |
|----|------|------|
| ① 领域场景 | **让外行理解的应用场景** | 这个真实问题是什么 + 规模/影响 |
| ② 领域 AI 化难点 | 为什么现有 AI 方案不够 | 数据稀缺/标注贵/部署约束/领域特殊性 |
| ③ 我们的 AI 方案 | 针对该领域的建模 | 问题形式化 + AI 方法适配 |
| ④ 方法核心设计 | 关键模块+为什么适合该领域 | 每个设计决策解释"为什么对这个领域必要" |
| ⑤ 贡献列表 | 3-4 bullet | (1) 问题建模 (2) 方法 (3) 领域影响 |

与模型/方法型的关键区别：**段① 从应用场景起手，不从任务定义起手。** 每个 AI 设计决策需解释其领域动机。

---

## 三、获奖 Intro 的高频套路（蒸馏）

### 3.1 痛点组织：二/三痛点枚举

几乎所有获奖论文在段② 用显式枚举：

> 📄 **LLM2CLIP**: "two key challenges: 1. Feature separability 2. Training cost"
> 📄 **MindCross**: 3 痛点与 3 创新一一对应
> 📄 **LENS (2026)**: "three core challenges (i)(ii)(iii)"
> 📄 **Code-Efficiency (2026)**: "three key insights (1)(2)(3)"

**规律**：给每个痛点起一个 `\textbf{短名}`（2-4 词），然后用 (i)(ii) 或 1. 2. 列出。短名在 contributions 中复用。

### 3.2 痛点的代价量化

| 论文 | 痛点 | 量化代价 |
|------|------|---------|
| Binary-Gaussian | high-dim category features | accounts for **over 50%** of parameter size |
| CowClip | CTR 模型训练慢 | **from 12 hours to 10 minutes**（反过来就是贡献） |
| Code-Efficiency | LLM 生成代码效率差 | **3 to 13 times slower** than efficient counterparts |

### 3.3 开场第一句的 5 种模式

| 模式 | 示例（采自语料） | 适用 |
|------|-----------------|------|
| X has emerged as... | "Large language models have emerged as one of the most influential..." | 模型/方法型（领域已热） |
| X is a long-standing goal... | "Reconstructing 3D scenes from images is a long-standing goal in..." | 经典任务 |
| X takes [input] and [output]... | "Visual segmentation takes an image and assigns a label to every pixel." | 需要先定义任务 |
| While X has made remarkable progress... | "While code LLMs have made remarkable progress, the generated code..." | 需要一句入痛点 |
| Imagine you are tasked with... | "Imagine you are tasked with allocating office spaces..." | 理论型叙事钩子 |

### 3.4 贡献列引导句

采自语料的常见引导句（任选其一）：
- `To sum up, our contributions are as follows:`
- `Our contributions are as follows:`
- `In summary, our main contributions are as follows:`
- `In conclusion, our contributions are as follows:`（稍弱，慎用）

---

## 四、写完自查清单

逐条过：

- [ ] 第一段是否在 3 句内让 reviewer 知道本文做什么？
- [ ] 每个痛点带**技术原因 + 具体代价**？
- [ ] 痛点 = 方法正面回应的那个？（段②→段④可连线）
- [ ] Abstract ↔ Intro **逐句可对应**？
- [ ] 痛点 ↔ 创新 ↔ contributions **数目与顺序一致**（三重一致）？
- [ ] Contributions 每条 = 机制 + 收益？（末条是否带数字/SOTA？）
- [ ] Teaser 图在段④ 被引用（`Fig. 1`）？
- [ ] 没有"先讲朴素 baseline 再说自己改进"的写法？
- [ ] 没有 "novel" / "significant" 等未证明的强词？
- [ ] 引用足够早（段①/② 即有 `\cite`）？
- [ ] 匿名投稿：无自引身份暗示？Teaser 图无机构 logo？

---

## 五、常见病灶 → 改法

| 病灶 | 改法 |
|------|------|
| 读着像"给朴素 baseline 打补丁" | 别先讲朴素解法再说改进；直接从任务难点引到你的洞见 |
| 第一段铺垫太久 | 段①末尾或段②开头就抛 challenge；LLM2CLIP/LENS 范式 |
| 痛点和方法对不上 | 用三重一致强制对齐；改段②收束的缺陷 |
| 贡献列表是流水账 | 每条 = 机制 + 收益 + 回指某痛点 |
| 理论论文开篇太抽象 | 换叙事钩子或模型定义+收窄关注点 |
| Introduction 和 Abstract 各说各话 | 做逐句连线自查 |
| Intro 里的实验 claim 在实验节找不到 | Claim-evidence 映射每个 claim |

---

> **句子级模板**（`modules/sentence-craft.md`）：按 Introduction 各段的任务选模板：
> - 段① 开场 → §2.1 开场句（5 种模式，按论文类型选择）
> - 段② 痛点 → §2.2 痛点句（优先用模式 C 量化痛点 或模式 D 三重枚举）
> - 段④ 方法 → §2.3 "我们提出"句（模式 B To-X 过渡最自然）
> - 段⑤ 对比 → §2.6 对比句（模式 D 切割不树敌）
> - 段间过渡 → §2.7 过渡句（模式 D 段首衔接）
> - Contributions → §3 第 12 组 Before/After（贡献条目流水账→机制+收益）
> - 写完后过 → §六 Intro 句子自查（5 条）
