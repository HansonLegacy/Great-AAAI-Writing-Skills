# AAAI 摘要写作（Abstract）

> 本文档是 AAAI 特化版——在通用摘要写作规律之上，叠加 AAAI 格式约束和论文类型微调。

---

## 〇、先读这个

通用摘要写作规律（Context → Gap → Solution → Method → Results 五步弧线、长度/缺陷挂后果/方法与痛点对应等七条硬规律、连接词工具箱）已内化到本文档中。

**本文档聚焦**：AAAI 特有约束 + 按 4 种论文类型的弧线微调 + 获奖论文摘要案例。

---

## 一、AAAI 特有约束

| 约束 | 说明 |
|------|------|
| **长度** | 140-180 词，单段。获奖论文均值 162 词，中位数 168 词。上限 220 词（📋 Author Kit 未硬限字数，但获奖论文极少超过 200 词） |
| **禁止 `\cite`** | 摘要内**绝对不能**出现 `\cite{...}`。点名数据集/对手方法名（如 "RefCOCO", "GLaMM", "EVA02"）允许 |
| **`\textbf` 可用** | 用于标方法名或最硬数字，但勿滥用——全篇摘要 1-2 处为宜 |
| **匿名投稿** | 不写 "code will be released" + 链接；不在摘要中暗示身份 |
| **单段** | AAAI 模板的 abstract 环境自动处理格式，不要手动分段（`\par` 或空行） |

---

## 二、按论文类型的五步弧线微调

### 类型 1: 理论/算法型

五步弧线变形为 **"问题→答案"** 框架：

| 步 | 标准版 | 理论型变体 | 示例句式 |
|----|--------|-----------|---------|
| ① Context | 领域+重要性 | **模型/场景定义**（1 句浓缩） | `Partially observable Markov decision processes (POMDPs) form a prominent model for sequential decision making under uncertainty.` |
| ② Gap | 现有方法缺陷 | **已知难度**（前人止步于何处） | `A long line of work has established that most formulations are undecidable.` |
| ③ Solution | we propose NAME | **核心结论**（我们回答了什么） | `In this work, we establish that ... is decidable / we prove a tight bound of ...` |
| ④ Method | 关键机制 | **证明策略概述**（给出直觉） | `Our proof proceeds by constructing a revelation mechanism that ...` |
| ⑤ Results | 硬数字+SOTA | **结论性质+意义** | `This result resolves an open question ... and enables exact algorithms for ...` |

> 📄 实例：Revelations (2025) 摘要——"POMDPs form a prominent model... A long line of work has established that most formulations are undecidable... In this work, we are interested in almost-sure strategies... We introduce a revelation mechanism which... The constructed belief levels can then be used to construct algorithms..."

### 类型 2: 模型/方法型

使用**标准五步弧线**，无特殊变形。这是 AAAI 最常见的情形。

### 类型 3: 基准/资源型

五步弧线的 ③④ 变形为 **"资源构建→揭示洞见"**：

| 步 | 标准版 | 基准型变体 | 示例句式 |
|----|--------|-----------|---------|
| ① Context | 领域+重要性 | 该领域现有数据/资源的概况 | `Large-scale, volunteer-collected datasets ... have enabled marked performance gains for fine-grained visual classification.` |
| ② Gap | 现有方法缺陷 | **现有资源的盲区/偏差**（资源痛点） | `However, such data are opportunistic and lack a structured sampling strategy, containing geographic, temporal, taxonomic biases whose impacts are unclear.` |
| ③ Solution | we propose NAME | **我们构建了什么资源** | `We introduce [DATASET NAME], a curated dataset of N images/samples across ...` |
| ④ "Method" | 关键机制 | **数据构建流程+评估协议** | `We partition data across five types of bias. We compare species recognition using diverse accuracy metrics.` |
| ⑤ Results | 硬数字+SOTA | **关键发现+资源价值** | `We observe that these biases confound model performance less than expected... Our framework enables future studies to...` |

> 📄 实例：DivShift (2025) 摘要——走完整 ①→②→③→④→⑤，但 ③ 是 "introduce DivShift-NAWC, a curated dataset"，④ 是 "partitioned across five types of expert-verified bias"，⑤ 是 "We observe that these biases confound model performance less than expected from the underlying label distribution."

### 类型 4: 应用驱动型

五步弧线的 ① 起手从**应用场景**而非任务定义出发，② 是该领域的 AI 化难点：

| 步 | 标准版 | 应用型变体 | 示例句式 |
|----|--------|-----------|---------|
| ① Context | 领域+重要性 | **应用场景+领域价值**（让外行也懂） | `Time-series and text data are prevalent in healthcare and frequently co-exist, yet they are typically modeled in isolation.` |
| ② Gap | 现有方法缺陷 | **该领域 AI 化的具体难点** | `Even studies that jointly model time-series and text do so by converting time-series to images or graphs. We hypothesize that explicitly modeling them jointly can improve tasks such as summarization.` |
| ③ Solution | we propose NAME | **我们的 AI 方案**（针对该领域） | `We introduce JoLT to jointly learn representations from pre-trained time-series and text models.` |
| ④ Method | 关键机制 | **核心设计+为什么适合该领域** | `JoLT utilizes a Querying Transformer to align the time-series and text representations.` |
| ⑤ Results | 硬数字+SOTA | **领域效果+实际意义** | `Our experiments on a large real-world electrocardiography dataset show that JoLT outperforms state-of-the-art image captioning approaches.` |

> 📄 实例：JoLT (2024) 摘要——① 从 healthcare 场景起手，② 点出 "modeled in isolation" 的 gap，③ "introduce JoLT"，④ "Q-Former to align"，⑤ "outperforms SOTA image captioning approaches"。

---

## 三、获奖摘要的高频套路（蒸馏）

基于 AAAI 2023-2026 获奖论文的摘要分析：

### 3.1 开头策略三选一

| 策略 | 适用类型 | 示例 |
|------|---------|------|
| **直接定义任务** | 模型/方法型 | `X has emerged as a mainstream approach for...` |
| **场景+痛点一句入** | 应用驱动型 | `While code LLMs have made remarkable progress, the generated code often exhibits poor runtime efficiency...` |
| **概念缩写+展开** | 理论型 | `POMDPs form a prominent model for... A long line of work has established that...` |

### 3.2 记忆点植入的 5 种方式

| 方式 | 效果 | 获奖实例 |
|------|------|---------|
| **惊人数字** | 最直接的记忆点 | `from 12 hours to 10 minutes on 1 GPU`（CowClip） |
| **一反直觉的发现** | 挑战预期 | `biases confound model performance less than expected`（DivShift） |
| **极简做法** | "一行代码"效应 | `compresses each feature into a single integer` |
| **破折号插入** | 强调意外性 | `—without large-scale retraining—` |
| **"第一个"话术** | 占位效应 | `the first framework that...`（仅当确为首次时用） |

### 3.3 结尾策略

不要以 "Code will be released" 结尾（空洞 + 匿名投稿违规）。用以下之一：

| 策略 | 示例 |
|------|------|
| 最强结果收尾 | `...outperforming GLaMM by up to 5.6% cIoU.` |
| 意义句收尾 | `These results demonstrate that X can serve as a practical path toward Y.` |
| 开放问题收尾（理论型） | `This opens the door to exact algorithms for a broad class of POMDPs.` |

---

## 四、写完自查清单

逐条过：

- [ ] 长度 150-200 词，单段？
- [ ] Abstract 内无 `\cite{...}`？
- [ ] 五步弧线完整（理论型用"问题→答案"变体）？
- [ ] 每个痛点带后果（`which <具体代价>`）？
- [ ] ③④ 的方法组件与 ② 的痛点可连线？
- [ ] 有记忆点钩子（数字/反直觉/极简/破折号插入）？
- [ ] 结尾不是 "code will be released"？
- [ ] Abstract 的关键信息与 Introduction 可逐句对应？
- [ ] 方法名在 ③ 引入一次，之后用缩写？
- [ ] 匿名投稿无身份暗示？

---

## 五、与 Introduction 的衔接

Abstract 定稿后，其五功能句将直接膨胀为 Introduction 各段（详见 `sections/introduction.md`）：

| Abstract 句 | Introduction 位置 |
|-------------|-------------------|
| ① Context | 段① 整段 |
| ② Gap | 段② 整段（常原句复用+加引用） |
| ③ Solution | 段④ 首句 |
| ④ Method 组件 | 段④ 主体 + contributions bullets |
| ⑤ Results | 段⑤ 末 + contributions 末条 |

**此对应关系是后续 Introduction 写作的核心约束。**

---

> **句子级模板**（`modules/sentence-craft.md`）：确定五步弧线后，按步索句：
> - ① Context → §2.1 开场句（5 种模式：定义型 / 趋势型 / 任务-重要性 / 让步型 / 资源痛点）
> - ② Gap → §2.2 痛点句（However+技术局限 / Despite+障碍 / 量化痛点）
> - ③ Solution → §2.3 "我们提出"句（4 种模式 + 动词选择指南）
> - ④ Method → §2.4 方法描述句（组件枚举 / By-gerund / Unlike 对比）
> - ⑤ Results → §2.5 结果报告句（数字+对比 / 观察+解读 / 意义收束）
> - 写完后过 → §六 Abstract 句子自查（5 条）
