# AAAI 句子级写作工艺

> **定位**：这是 `distilled-patterns.md`（统计数据）和 `sections/*.md`（段落骨架）之间的缺失层——教你**怎么写好每一句话**。
> 所有模板和示例均从 AAAI 2023-2026 获奖论文中提取。`📄` = 获奖论文实例。

---

## 速查卡：10 个最高 ROI 的句子级修改

写完全文后，Cmd+F 以下 10 个病灶词，逐一替换：

| # | 病灶 | 问题 | 快速改法 |
|---|------|------|---------|
| 1 | `novel` | 自评 novelty → reviewer 反感 | 删掉，描述具体差异 |
| 2 | `significantly`（无 p-value） | 统计学术语滥用 | `consistently outperforms` / `achieves +X% improvement` |
| 3 | `state-of-the-art`（未比最新 baseline） | 虚张声势 | 点名最强 baseline + 具体 margin |
| 4 | `better`（未说比谁好、好多少） | 空洞比较 | `outperforms [BASELINE] by [NUMBER] on [TASK]` |
| 5 | `is/are` 连续 3 句 | 弱动词堆积 | 至少 1 句换动作动词（`enables / captures / leverages`） |
| 6 | `This is because...` | 代词指代模糊 | 把 "This" 换成具体名词短语 |
| 7 | 句首连续 3 句用 `We` | 节奏单调 | 第 2 或第 3 句换 `Our method / Specifically / The key insight is` |
| 8 | `existing methods are limited` | 泛泛而谈，无技术原因 | 写清楚**什么方法**在**什么条件下**因为**什么技术原因**不行 |
| 9 | `Extensive experiments demonstrate` | filler 词 + 空洞 | 换成具体数字：`Experiments on X, Y, and Z show that...` |
| 10 | 句末弱词（`...is used.` / `...is shown.`） | 末尾重音浪费 | 把最强信息放在句末 |

---

## 一、核心原则

### 原则 1：具体压倒笼统

> **"The meaning of a sentence is the sum of its specific details, not its abstract claims."**

每当你写下一个抽象评价词（`limited`, `powerful`, `effective`, `challenging`），问自己：**具体怎么 limited？数字是多少？**

| 弱（笼统） | 强（具体） |
|-----------|-----------|
| Existing methods are limited in handling large-scale data. | While X achieves 82.3% on ImageNet-1K, its throughput drops to 12 img/s when batch size exceeds 256. |
| Our method achieves better performance. | NAME achieves 85.7% top-1 accuracy, outperforming the strongest baseline EVA02 by 2.4%. |
| Training is computationally expensive. | Training requires 8×V100 GPUs for 72 hours on the full dataset. |

> 📄 CowClip 用 `from 12 hours to 10 minutes on 1 GPU` 替代了 `our method is more efficient`——这是具体压倒笼统的教科书案例。

### 原则 2：旧信息 → 新信息（Given-New 原则）

> **每句的句首放读者已知的信息，句末放新信息。句末是读者注意力最集中的位置。**

```
❌ "A novel attention mechanism is proposed in this paper. The mechanism leverages cumulant expansion.
   Specifically, quadratic complexity is reduced to linear order by the low-order variant."

✅ "We propose a novel attention mechanism based on cumulant expansion.
   This mechanism reduces the quadratic complexity of standard attention to linear order,
   while preserving the nonlinearity that linear attention methods sacrifice."
```

检查方法：读每句的第一部分——如果读了前 5 个词不知道在说什么，说明旧信息没有承接上句。

### 原则 3：一句一义

> **每句只做一件事。如果你发现一句里有 "and" 连接了两个独立的观点，拆成两句。**

```
❌ "We propose DropMessage, which performs dropping operations directly on the propagated messages
   during the message-passing process, and importantly, we find that DropMessage provides
   a unified framework for most existing random dropping methods."

✅ "We propose DropMessage, which performs dropping operations directly on the propagated
   messages during the message-passing process. Importantly, we find that DropMessage provides
   a unifying framework for most existing random dropping methods,
   based on which we give a theoretical analysis of their effectiveness."
```
> 📄 来自 DropMessage (2023) ——作者自己就在第二个观点前断句了。

### 原则 4：动词驱动句子

> **弱动词（is/are/has/can be）不传递信息。用强动词替换弱动词，句子立即变紧凑。**

| 弱动词 | 强动词替代 |
|--------|-----------|
| X is a method for Y | X **enables** Y / X **addresses** Y |
| This is because of Z | This **arises from** Z / Z **drives** this effect |
| Our model has three components | Our model **integrates** three components |
| The results are shown in Table 1 | Table 1 **reports** the results |

```
❌ "The model has a Mixture of Experts architecture that is for capturing
   region-specific slum characteristics."

✅ "The model employs a Mixture of Experts architecture to capture
   region-specific slum characteristics while learning universal features
   through a shared backbone."
```
> 📄 改写自 GRAM slum detection (2026)

### 原则 5：末尾重音

> **英语句子的"重音位置"在末尾。把你想让 reviewer 记住的信息放在句末。**

```
❌ "Our method achieves 85.7% accuracy, which is a significant improvement."  ← 句末是弱词

✅ "Our method achieves 85.7% top-1 accuracy, surpassing the strongest baseline by 2.4%."
   ← 句末是 margin 数字

✅ "On the Criteo dataset, CowClip enlarges the batch size from 1K to 128K,
   reducing training time from 12 hours to 10 minutes on a single V100 GPU."
   ← 句末是记忆点数字
```
> 📄 第二个例子直接来自 CowClip (2023) 的 abstract。

---

## 二、句法模板库（按写作任务）

每个模板 = **模板句式** + **获奖实例** + **适用场景** + **类型微调**。

### 2.1 开场句（5 种模式）

#### 模式 A：定义型开场（最安全、最通用）

```
[SUBJECT] is/are a [adjective] [category] that [core function].
```

> 📄 "CLIP is a seminal multimodal model that maps images and text into a shared representation space." — LLM2CLIP (2026)
>
> 📄 "Partially observable Markov decision processes form a prominent model for sequential decision making under uncertainty." — Revelations (2025)

**适用**：模型/方法型、理论型。读者的基础概念需要先被建立。

**微调**：理论型可收窄关注点——`We consider POMDPs from a point of view common in planning...`

#### 模式 B：趋势型开场（领域已热）

```
[SUBJECT] has/have emerged as a [role] in [field], enabling [applications].
```

> 📄 "CLIP has emerged as one of the most influential cross-modal foundation models in recent years." — LLM2CLIP Intro
>
> 📄 "Large language models have become integral to everyday decision-making and assistance." — Global Human Opinion (2026)

**适用**：模型/方法型。你的研究踩在一个已经热起来的领域上——先承认这个事实，再指出缺口。

#### 模式 C：任务-重要性开场

```
[GERUND/TASK] is a fundamental/critical/central task in [FIELD], with applications in [X] and [Y].
```

> 📄 "A fundamental task in multi-agent systems is to assign agents to alternatives (e.g., resources or tasks)." — Every Bit Helps (2025)
>
> 📄 "Reconstructing video from brain signals is an important brain decoding task." — MindCross (2026)

**适用**：当你需要先明确任务定义时。应用驱动型可替换为领域场景描述。

#### 模式 D：让步型开场（一句话入痛点）

```
While [SUBJECT] has made [progress], [key limitation remains].
```

> 📄 "While much research has recently focused on physics-based adversarial samples, a critical overlooked category originates from physical failures of on-board camera components." — Fractured Glass (2026)
>
> 📄 "While code LLMs have made remarkable progress, the generated code often exhibits poor runtime efficiency." — (intro-writing skill 示例)

**适用**：你的贡献是对一个已知问题的突破性解决。让步型开场让 reviewer 一句话就知道你的定位。

**慎用**：如果 ① 或 ② 句就 turns negative，可能让 reviewer 觉得你太 aggressive。确保随后的 1-2 句是建设性的。

#### 模式 E：资源痛点开场（基准/资源型专属）

```
[RESOURCE TYPE], such as [EXAMPLE], have enabled [progress]. However, existing [resources] remain [limitation], because [technical reason].
```

> 📄 "Large-scale, volunteer-collected datasets of identified natural world imagery like iNaturalist have enabled marked performance gains for fine-grained visual classification. However, such data—sometimes referred to as citizen science data—are opportunistic and lack a structured sampling strategy." — DivShift (2025)
>
> 📄 "Global plant maps of plant traits... are essential for understanding ecosystem processes. However, existing trait maps remain limited by the high cost and sparse geographic coverage of field-based measurements." — PlantTraitNet (2026)

**适用**：基准/资源型论文的专属开场。段① 建立为什么这个资源重要，段② 立刻指出资源缺口。

---

### 2.2 痛点/空白句（4 种模式）

#### 模式 A：However + 技术局限（最常用）

```
However, [existing approaches] [specific limitation], which [consequence with quantifiable cost].
```

> 📄 "However, most existing HNNs primarily emphasize low-pass filtering while neglecting the role of high-frequency information." — High-Pass Matters (2026)
>
> 📄 "However, our empirical analysis reveals that current VLAs struggle to allocate visual attention to target regions. Instead, visual attention is always dispersed." — ReconVLA (2026)
>
> 📄 "However, the volume of these opportunistic volunteer records comes at a cost: as these observations become easier for the public to collect, sampling becomes unstructured, and injects a variety of biases into these data." — DivShift (2025)

**铁律**：`However` 之后必须跟**具体的技术原因**，不能跟笼统评价。

```
❌ "However, existing methods are limited."
✅ "However, existing methods rely on discretizing time—leading to poor performance on irregularly sampled data." (CADYT, 2026)
```

#### 模式 B：Despite + 优势 + 仍存在障碍

```
Despite [acknowledged progress/advantage], [key obstacle] remains unsolved.
```

> 📄 "Despite this promise, practical use is limited by optical aberrations, blur, and illumination sensitivity, which degrade both visual quality and machine perception." — Metalens Vision System (2026)
>
> 📄 "Despite these advancements, our understanding of the trade-offs between using two cardinal queries per agent and a logarithmic number of queries remains limited." — Every Bit Helps (2025)

**适用**：当你想先承认前人贡献（不树敌），再指出你的贡献空间时。

#### 模式 C：量化痛点（最有力道）

```
[Existing approach] causes [specific cost]: [NUMBER] [UNIT].
```

> 📄 "The softmax attention, the core component of the transformer, exhibits quadratic complexity in both time and memory as data scales up." — Cumulant Attention (2026)
>
> 📄 "CTR prediction model training on the Criteo dataset... takes 12 hours on a single V100 GPU." — CowClip (2023, 隐含痛点)
>
> 📄 "The computational cost of the softmax attention... exhibits quadratic complexity..." — Cumulant Attention (2026)

**适用**：当你有数字时，用数字做痛点句。这是最具说服力的痛点写法。

#### 模式 D：三重痛点枚举（Method 节最常用）

```
[Three/Two] key challenges arise when [doing X]:
(i) [CHALLENGE_1], (ii) [CHALLENGE_2], and (iii) [CHALLENGE_3].
```

> 📄 "two key challenges: 1. Feature separability 2. Training cost" — LLM2CLIP
>
> 📄 "three core challenges (i) subject variability, (ii) data scarcity for new subjects, and (iii) inadequate utilization of existing subjects' data" — MindCross (2026)

**铁律**：每个挑战在 Method 中有对应的解决方案，在 Experiments 中有对应的消融。

---

### 2.3 "我们提出"句（4 种模式）

#### 模式 A：We [verb] NAME, a [characterization] that [core function]

```
We [propose/introduce/present/develop] [NAME], a [one-clause characterization] that [what it does].
```

> 📄 "We propose DropMessage, which performs dropping operations directly on the propagated messages during the message-passing process." — DropMessage (2023)
>
> 📄 "We introduce CAT-V (Caption AnyThing in Video), a training-free framework for fine-grained object-centric video captioning." — CAT-V (2026)
>
> 📄 "We introduce PlantTraitNet, a multi-modal, multi-task uncertainty-aware deep learning framework that predicts four key plant traits from citizen science imagery." — PlantTraitNet (2026)

**动词选择指南**（基于获奖论文定量数据）：

| 动词 | 占比 | 适用场景 | 隐含语义 |
|------|------|---------|---------|
| `propose` | 26% | 新方法/新框架 | "这是我们的原创设计" |
| `introduce` | 22% | 新资源/新概念/新问题 | "这个以前不存在/没被这样用过" |
| `present` | 8% | 理论结果/系统/演示 | "我们展示一个已完成的结果" |
| `develop` | 6% | 算法/技术/工具 | "从头构建的实用工具" |
| `design` | 2% | 架构/系统 | "有意为之的设计决策" |

#### 模式 B：To [goal], we [verb] [NAME]

```
To [address/tackle/achieve] [specific goal], we [verb] [NAME], which [key mechanism].
```

> 📄 "To tackle this problem, we first theoretically show that different frequencies of ids make it challenging to scale hyperparameters... To stabilize the training process in a large batch size setting, we develop the adaptive Column-wise Clipping (CowClip)." — CowClip (2023)
>
> 📄 "To address this, we introduce a large-scale high-resolution dataset and propose GRAM (Generalized Region-Aware Mixture of Experts)." — Slum Detection (2026)

**适用**：当前面的痛点句已经明确说了要解决什么，To-X 模式提供自然的问题→方案过渡。

#### 模式 C：In this work, we [verb]...

```
In this work, we [verb] [NAME/approach] that [key contribution].
```

> 📄 "In this work, we introduce CAT-V (Caption AnyThing in Video), a training-free framework..." — CAT-V (2026)
>
> 📄 "In this work, we present a theoretical and practical investigation into this question." — High-Pass Matters (2026)
>
> 📄 "In this work, we are interested in almost-sure strategies..." — Revelations (2025)

**适用**：理论型论文（用 "investigate" / "study" / "are interested in" 替代 "propose"）。

#### 模式 D：We [verb] a novel approach that [key insight]

```
We [verb] a [adjective] approach that [captures/addresses/enables] [key capability], by [mechanism].
```

> 📄 "we propose a novel approach capable of performing causal discovery on dynamical systems in a continuous-time fashion, relaxing the regular sampling assumption." — CADYT (2026)
>
> 📄 "we propose a novel random dropping method called DropMessage, which performs dropping operations directly on the propagated messages." — DropMessage (2023)

**注意**：`novel` 在获奖论文中确实出现（如 DropMessage、CADYT），但只在**方法句本身**中使用且紧跟着具体的差异化描述。不要在 Abstract/Introduction 的其他位置单独用 `novel` 做评价。

---

### 2.4 方法描述句（5 种模式）

#### 模式 A：组件枚举

```
[NAME] combines/integrates/consists of (i) [COMPONENT_1], which [function]; (ii) [COMPONENT_2], which [function]; and (iii) [COMPONENT_3], which [function].
```

> 📄 "CAT-V combines (i) a SAMURAI-based Segmenter for precise object masks across frames, (ii) a TRACE-Uni Temporal Analyzer for event boundary detection and coarse event descriptions, and (iii) an InternVL-2.5 Captioner." — CAT-V (2026)
>
> 📄 "GxVAEs consists of two joint variational autoencoders (VAEs). The first VAE, ProfileVAE, extracts latent features from gene expression profiles. The extracted features serve as the conditions that guide the second VAE, called MolVAE, in generating hit-like molecules." — GxVAEs (2024)

**要点**：枚举完每个组件后，必须用至少 1 句说明它为什么是这个功能（动机），不只是它是什么。

#### 模式 B：By + gerund, we + verb

```
By [DOING_X], we [ACHIEVE_Y], enabling [CAPABILITY].
```

> 📄 "By aggregating individual trait predictions across space, we generate global maps of trait distributions." — PlantTraitNet (2026)
>
> 📄 "By integrating spatially-aware attention enhancement and reinforcement learning-based illumination control into a real-time system, our solution transforms degraded raw captures into high-fidelity images." — Metalens (2026)

#### 模式 C：Mechanism → Purpose

```
[COMPONENT] [VERB]s [INPUT] to [OUTPUT], thereby [BENEFIT].
```

> 📄 "Conditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image, which corresponds to the target manipulated objects." — ReconVLA (2026)
>
> 📄 "The LLM-enhanced CLIP delivers consistent improvements across a wide spectrum of downstream tasks, including linear-probe classification, zero-shot image–text retrieval, zero-shot/supervised image segmentation, and object detection." — LLM2CLIP (2026)

#### 模式 D：Unlike X, we Y

```
Unlike [EXISTING_APPROACH] which [LIMITATION], our [method] [KEY DIFFERENCE].
```

> 📄 "Unlike overly abstract vanilla captioning or overly terse dense captioning, CAT-V achieves object-level specificity with spatial accuracy and temporal coherence through modular prompting." — CAT-V (2026)
>
> 📄 "In contrast to existing state-of-the-art causal discovery methods that model the problem using Dynamic Bayesian networks, our formulation results in discrete-time Difference-based causal models, which allow milder assumptions for modeling the continuous nature of the underlying dynamics." — CADYT (2026)

#### 模式 E：问题 → 观察 → 设计

```
[PROBLEM]. We observe that [INSIGHT]. Considering this, we [DESIGN_DECISION].
```

> 📄 来自 `sections/method.md` 观察驱动模板

这种模式特别有力——它让 reviewer 看到你的设计决策不是任意的，而是由具体的观察洞察驱动的。

---

### 2.5 结果报告句（5 种模式）

#### 模式 A：数字 + 对比（最标准）

```
[NAME] achieves [NUMBER] on [TASK], outperforming [STRONGEST_BASELINE] by [MARGIN].
```

> 📄 (CowClip 精神) "...reduces training time from 12 hours to 10 minutes on a single V100 GPU."
>
> 📄 (LLM2CLIP 精神) "...achieves substantial performance gains over state-of-the-art CLIP variants such as EVA02 and DFN."

**铁律**：点名最强 baseline + 具体数字。不能说 `outperforms all baselines`。

#### 模式 B：观察 + 解读

```
We [find/observe] that [KEY_FINDING]. This [suggests/indicates/demonstrates] that [INTERPRETATION].
```

> 📄 "We observe that these biases confound model performance less than expected from the underlying label distribution shift, and that more data leads to better model performance but the magnitude of these improvements are bias-specific." — DivShift (2025)
>
> 📄 "We find that LLMs appropriately align or over-align with only a few countries while under-aligning with most countries." — Global Human Opinion (2026)

**关键词强度梯度**（从弱到强）：

| 强度 | 动词 | 需要的证据 |
|------|------|-----------|
| 弱 | `suggests` / `is consistent with` | 方向性一致 |
| 中 | `indicates` / `shows` | 明确的数字趋势 |
| 强 | `demonstrates` / `confirms` | 消融 + 统计检验 |
| 极强 | `proves` / `establishes` | 仅理论型可用；需定理级证据 |

#### 模式 C：消融报告

```
Removing [COMPONENT] degrades [METRIC] by [Δ], confirming its role in [FUNCTION].
```

> 📄 综合自 multi-paper ablation patterns

#### 模式 D：全景结果

```
[NAME] achieves consistent improvements across [RANGE]: [METRIC_1] (+X%), [METRIC_2] (+Y%), and [METRIC_3] (+Z%).
```

#### 模式 E：意义收束

```
These results [implication for the field], [specific direction/application].
```

> 📄 "These findings imply that while the structure within natural world images provides generalization improvements for biodiversity monitoring tasks, the biases present in volunteer-collected biodiversity data can also affect model performance; thus these models should be used with caution in downstream biodiversity monitoring tasks." — DivShift (2025)
>
> 📄 "Thus, our work settles open questions regarding the optimal distortion achievable with a fixed number of cardinal value queries in both settings." — Every Bit Helps (2025)

---

### 2.6 对比句（4 种模式）

#### 模式 A：直接比较

```
Compared to [BASELINE], our [NAME] achieves [NUMBER] (+Δ%), while requiring [LESS_RESOURCE].
```

#### 模式 B：Trade-off 句

```
While [BASELINE] prioritizes [STRENGTH_A], it sacrifices [WEAKNESS_B]. [NAME] balances both by [MECHANISM].
```

#### 模式 C：收敛比较（理论型）
```
Our result generalizes [PRIOR_WORK] by [EXTENSION], and is optimal up to a constant factor given [LOWER_BOUND].
```

> 📄 "We generalize their result by achieving O(n^{1/κ}) distortion with κ queries per agent for any constant κ, which is optimal up to a constant factor given a previous lower bound by Amanatidis et al. (2022)." — Every Bit Helps (2025)

#### 模式 D：切割但不树敌

```
[PRIOR_WORK] focuses on [SETTING_A], while we address [SETTING_B], where [KEY_DIFFERENCE].
```

> 📄 来自 `sections/related-work.md` 话术库

---

### 2.7 过渡句（4 种模式）

#### 模式 A：问题→方案（最关键的过渡）

```
[GAP_SUMMARY]. To address this [challenge/problem], we [VERB] [NAME].
```

#### 模式 B：方法→实验

```
We evaluate [NAME] on [TASK(S)] to answer [KEY_QUESTIONS].
```

#### 模式 C：模块→模块

```
However, [MODULE_A] alone cannot [FUNCTION], because [LIMITATION]. We therefore introduce [MODULE_B] to [PURPOSE].
```

#### 模式 D：段落→段落（段首衔接）

```
Building on [PREVIOUS_POINT], we next [NEXT_STEP].
```

```
While the above results focus on [SCOPE_A], we now examine [SCOPE_B].
```

---

### 2.8 局限性句（3 种模式）

#### 模式 A：诚实局限性

```
[NAME] has been tested only on [SCOPE]; its applicability to [BEYOND_SCOPE] remains to be explored.
```

> 📄 DivShift 和 PlantTraitNet 的局限性讨论风格：具体、坦诚、不泛泛。

#### 模式 B：限定条件

```
Our [result/analysis] assumes [CONDITION]. Relaxing this assumption is an open direction.
```

> 📄 理论型论文的经典局限性句式

#### 模式 C：资源局限性（基准/资源型专属）

```
The [DATASET] covers [SCOPE] but does not yet include [MISSING_DIMENSION], which limits [ANALYSIS_TYPE].
```

---

## 三、常见病灶 → 改写（15 组 Before/After）

### 第 1 组：笼统痛点

| | 内容 |
|------|------|
| **病灶** | 痛点只写抽象形容词，不写技术原因 |
| **Before** | "Existing methods are limited in handling complex scenes." |
| **After** | "Existing methods rely on global image features, which fail to distinguish fine-grained object boundaries in cluttered scenes with overlapping instances." |
| **改了什么** | `limited` → 具体技术原因（global features）+ 具体场景（cluttered scenes with overlapping instances） |

### 第 2 组：自评 novelty

| | 内容 |
|------|------|
| **病灶** | 自评 `novel` 但没有跟具体差异 |
| **Before** | "We propose a novel method for video understanding." |
| **After** | "We propose CAT-V, a training-free framework that unifies segmentation-based object tracking with temporally-aware captioning." |
| **改了什么** | `novel method` → 删 `novel`，用具体机制（segmentation + captioning unification）让 reviewer 自己判断 novelty |

### 第 3 组："better" 空洞比较

| | 内容 |
|------|------|
| **病灶** | `better` 没说比谁好、好多少 |
| **Before** | "Our method achieves better results than existing approaches." |
| **After** | "NAME achieves 85.7% top-1 accuracy on ImageNet-1K, outperforming the strongest baseline EVA02 by 2.4%." |
| **改了什么** | `better results` → 具体数字 + 最强 baseline + margin |

### 第 4 组：被动语态泛滥

| | 内容 |
|------|------|
| **病灶** | 连续被动语态让句子沉重 |
| **Before** | "The features are extracted by the encoder. Then they are passed to the decoder. The output is generated by the decoder." |
| **After** | "The encoder extracts features and passes them to the decoder, which generates the final output." |
| **改了什么** | 3 个被动动词 → 3 个主动动词；合并为一句（更紧凑） |

### 第 5 组："significant" 无统计

| | 内容 |
|------|------|
| **病灶** | `significant` 是统计术语，没 p-value 别用 |
| **Before** | "Our method significantly outperforms all baselines." |
| **After** | "Our method consistently outperforms all baselines across 5 benchmarks, with a mean improvement of 3.2% (p < 0.01)." |
| **改了什么** | `significantly` → `consistently`（没有 p-value 时的替代）+ 跨 benchmark 数字 |

### 第 6 组："There is/are" 弱开场

| | 内容 |
|------|------|
| **病灶** | `There is/are` 推迟了句子的真正主语 |
| **Before** | "There are many challenges in training large-batch CTR models." |
| **After** | "Training CTR models with large batches introduces three challenges: (i) embedding frequency skew, (ii) gradient variance amplification, and (iii) loss of rare feature information." |
| **改了什么** | `There are many challenges` → 具体动作主语（training）+ 三个具名挑战 |

### 第 7 组：代词模糊

| | 内容 |
|------|------|
| **病灶** | `This` 的指代不明确 |
| **Before** | "The attention map is dispersed across the image. This causes the model to miss the target object." |
| **After** | "The dispersed visual attention causes the model to miss the target object." |
| **改了什么** | 代词 `This` → 合并为一句，让原因直接做主语 |

### 第 8 组：公式无解读

| | 内容 |
|------|------|
| **病灶** | 公式堆在段落中间，没有前后文字解读 |
| **Before** | "The loss function is:
    $$L = L_{task} + \lambda L_{reg}$$
    where λ is a hyperparameter." |
| **After** | "We optimize a composite objective that balances task performance and regularization:
    $$L = L_{task} + \lambda L_{reg}$$
    Intuitively, L_task drives the model toward accurate predictions, while L_reg (weighted by λ = 0.1) prevents overfitting by penalizing large weight norms." |
| **改了什么** | 公式前加引导句（"We optimize..."），公式后加直觉解释（"Intuitively..."），λ 给具体值 |

### 第 9 组：句子过长（>35 词）

| | 内容 |
|------|------|
| **病灶** | 一个句子塞多个观点 |
| **Before** | "We introduce an efficient fine-tuning framework that integrates an LLM into a pretrained CLIP while incurring the same training cost as regular CLIP fine-tuning and our method first embedding-izes the LLM for the CLIP text encoder and couples it to the pretrained CLIP vision encoder via a lightweight adaptor trained on only a few million image-caption pairs." |
| **After** | "We introduce an efficient fine-tuning framework that integrates an LLM into a pretrained CLIP at the same training cost as regular CLIP fine-tuning. Our method first 'embedding-izes' the LLM for the CLIP text encoder, then couples it to the pretrained CLIP vision encoder via a lightweight adaptor. Critically, this adaptor is trained on only a few million image-caption pairs." |
| **改了什么** | 1 句 (56 词) → 3 句 (19+21+16 词)。每个观点独立成句。 |

> 📄 这个例子直接来自 LLM2CLIP (2026) 的原始 abstract，但原文就是一个长句。我们主动断开以示范节奏控制。

### 第 10 组：句末弱词

| | 内容 |
|------|------|
| **病灶** | 句末放弱信息——介词短语、空动词 |
| **Before** | "Our method achieves state-of-the-art performance on several benchmarks, as shown in Table 1." |
| **After** | "On five benchmarks spanning classification, retrieval, and segmentation, NAME surpasses the previous best method EVA02 by 2.4-5.6% (Table 1)." |
| **改了什么** | 句末 `as shown in Table 1` → 句末放 margin `2.4-5.6%` |

### 第 11 组："The proposed method" 自指

| | 内容 |
|------|------|
| **病灶** | Reviews 发现 `the proposed method` 让文字呆板 |
| **Before** | "The proposed method consists of three modules. The proposed method is trained end-to-end." |
| **After** | "NAME consists of three modules, trained end-to-end." |
| **改了什么** | `The proposed method` → 直接用方法名。合并重复主语的两句 |

### 第 12 组：贡献条目流水账

| | 内容 |
|------|------|
| **病灶** | 贡献 bullet 沦为 "we did X, we did Y, we did Z" |
| **Before** | "We propose a new attention mechanism. We conduct experiments on ImageNet. We achieve SOTA results." |
| **After** | "1. We propose Cumulant Attention, a statistically-motivated attention mechanism that reduces quadratic complexity to linear order while preserving softmax nonlinearity.
    2. On ImageNet-100 classification and UCF-101 video classification, Cumulant Attention matches softmax attention accuracy while reducing memory by 40%.
    3. We release code and pretrained models to facilitate further research on efficient attention." |
| **改了什么** | 每条 = 机制 + 收益 + 具体数字。第三条是社区贡献 |

### 第 13 组："As shown in Figure X" 空洞引用

| | 内容 |
|------|------|
| **病灶** | 图的引用没有解释从图里能看出什么 |
| **Before** | "As shown in Figure 2, our model has three modules." |
| **After** | "Figure 2 illustrates NAME's three-stage pipeline: the encoder extracts multi-scale features (left), the fusion module aligns cross-modal representations (center), and the decoder generates the final output (right)." |
| **改了什么** | `As shown in Figure 2` + 架构名 → 具体描述图的内容，让没看图的人也懂 |

> **注意**：本组处理的是**正文中引用图表的句子**（"As shown in Figure X, ..."）。图表本身的 `\caption{...}` 文字（即图注/表注的完整写法：解剖结构 + 句法模板 + 病灶改写），见 `modules/caption-writing.md`。

### 第 14 组："It is worth noting that" / "Interestingly"

| | 内容 |
|------|------|
| **病灶** | 主观评价词——让 reviewer 觉得你在替他们下判断 |
| **Before** | "Interestingly, biases confound model performance less than expected." |
| **After** | "Biases confound model performance less than expected from the underlying label distribution shift." |
| **改了什么** | 删掉 `Interestingly`——让事实自己说话。如果事实真的 interesting，reviewer 自己会注意到 |

> 📄 第二个句子来自 DivShift (2025)，他们直接写了观察，没有加 `Interestingly` 前缀。

### 第 15 组：非母语英语模式

| | 内容 |
|------|------|
| **病灶** | Chinglish 句式 |
| **Before** | "We make an analysis on the effect of batch size." |
| **After** | "We analyze how batch size affects training stability." |
| **改了什么** | `make an analysis on` → `analyze`。英语偏好动词而非名词化 |

更多非母语模式见 [第五节](#五非母语写作者的英语注意项)。

---

## 四、句子节奏与流畅度

### 4.1 首词变化

连续 3 句以同一词/短语开头 → 单调感立即产生。

```
❌ "We propose X. We evaluate X on Y. We find that X achieves Z."
✅ "We propose X. Evaluation on Y shows that X achieves Z. Specifically, X outperforms the strongest baseline by 2.4%."
```

**常用首词替换表**：

| 如果想以这个开头... | 换成... |
|-------------------|---------|
| We (第 2 次/第 3 次) | `Our method` / `Specifically` / `In particular` / `Experiments on X show` |
| The (连续) | `This` / `These` / `Such` / 直接主语 |
| However (连续) | `Yet` / `In contrast` / `On the other hand` / 省略转折词直接陈述差异 |

### 4.2 长短句交替

短句（8-15 词）有力——用于关键 claim。长句（20-30 词）适合解释——用于方法描述。交替使用。

```
长 (25) "We propose a novel sheaflet-based HNN framework that integrates cellular sheaf theory
      and framelet transforms to explicitly model both low- and high-frequency components on hypergraphs."
短 (10) "This design is guided by our theoretical findings."
短 (12) "Extensive experiments on multiple benchmarks validate its effectiveness."
```

### 4.3 代词回指距离

`This` / `These` / `It` 的回指应在同一句或紧邻上一句中解决。跨句回指 > 2 句 → 换具体名词。

### 4.4 平行结构

并列项保持相同的语法结构。

```
❌ "Our method improves accuracy, reduces latency, and the memory footprint is smaller."
      [verb+noun]    [verb+noun]      [noun+verb — 不平行!]

✅ "Our method improves accuracy, reduces latency, and shrinks memory footprint."
      [verb+noun]    [verb+noun]      [verb+noun]
```

---

## 五、非母语写作者的英语注意项

### 5.1 学术动词时态速查

| 内容 | 时态 | 示例 |
|------|------|------|
| 我们的方法是什么 | **现在时** | "NAME **consists** of three modules." |
| 我们的实验做了什么 | **过去时** | "We **evaluated** NAME on five benchmarks." |
| 实验结果是什么 | **现在时** | "Table 1 **reports** the main results." / "NAME **outperforms** baselines." |
| 前人的工作 | **现在完成时 / 过去时** | "Prior work **has focused** on..." / "X et al. (2023) **proposed**..." |
| Conclusion 中的展望 | **现在时 / 将来时** | "Extending NAME to video **remains** future work." |

### 5.2 5 个最高频 Chinglish 模式

| Chinglish | 问题 | 学术英语 |
|-----------|------|---------|
| `make a(n) [noun] on` | 动词名词化 | 直接用动词：`analyze`, `investigate`, `compare` |
| `[method] can [verb]` | 不必要的 can | `[method] [verb]s`（现在时第三人称） |
| `according to [our experiments]` | 中式 "根据" | `Our experiments show` / `As Table 1 reports` |
| `in the following` | 中文 "如下" | `below` / `in Section X` / 直接陈述不需要引导 |
| `plays an important role` | 万能填充词，无信息 | 说清楚**具体**是什么角色：`controls the trade-off between X and Y` |

### 5.3 冠词关键规则

| 场景 | 冠词 | 示例 |
|------|------|------|
| 首次引入方法名 | 不需要冠词 | `We propose DropMessage.` |
| 指代前述的特定东西 | `the` | `The mechanism reduces variance.` |
| 泛指一类东西 | 不需要 `the` | `Graph neural networks are powerful tools.` |
| 专有名词/方法名 | 不需要冠词 | `CLIP is a multimodal model.` |

---

## 六、分节句子级自查

### Abstract（5 条）
- [ ] 每句是否推进五步弧线的一步？（不要一句塞多步，不要跳步）
- [ ] 每个数字第一次出现即带单位（`85.7% top-1 accuracy`）？
- [ ] 方法名在第几句引入？（建议 ≤ 第 4 句）
- [ ] 有没有任何一句可以用更短的词说清？（删 `Extensive experiments demonstrate that` → 直接说结果）
- [ ] 最后一句末尾是否放了最强信息（而非 `code will be released`）？

### Introduction（5 条）
- [ ] 段① 第一句是否在 3 句内让 reviewer 知道本文做什么？
- [ ] 段② 每个痛点句是否有**技术原因 + 具体代价**？
- [ ] 段④ 的方法句是否点名方法名 + 核心机制（不只是 "we propose a method"）？
- [ ] Contributions 的每条是否 = 做了什么 + 带来了什么收益？
- [ ] 相邻段落之间的第一句和最后一句能否自然衔接？（检查每段的段首-段末）

### Method（3 条）
- [ ] 每个公式前面是否有 1 句引导（"We define..." / "The update rule is..."）？
- [ ] 每个公式后面是否有 1 句解读（"Intuitively, this means..." / "Equation X shows that..."）？
- [ ] 每个模块 subsection 的第一句是否说明了**为什么**需要该模块？

### Experiments（4 条）
- [ ] 每个结果句是否包含数字 + 比较对象 + 差距？
- [ ] `significant` / `significantly` 是否只在有 p-value 时才用？
- [ ] 表注是否自包含？（reviewer 不看正文也知表里有什么）→ 写法模板见 `modules/caption-writing.md`
- [ ] 消融句是否点名了移除的组件 + 观察到的退化 + 退化幅度？

### Conclusion（3 条）
- [ ] 段 1 的措辞与 Abstract 不同？（不是在 copy-paste）
- [ ] 局限性句是否有 1-2 个具体条件/场景限制？
- [ ] 没有引入新引用、新图、新数字？

---

## 七、与现有模块的关系

| 你想知道 | 去哪个文件 |
|---------|-----------|
| 50 篇获奖论文的**统计数据**（词数、频率分布） | `distilled-patterns.md` |
| 每节的**段落结构**（几段、每段做什么） | `sections/{title,abstract,introduction,...}.md` |
| 每句话**怎么写**（模板 + 例句 + 病灶改写） | **本文件** |
| 有哪些**红旗词**不能用 | `review/02-aaai-red-flags.md` |
| 章节整体的**大纲和页数** | `outline-template.md` |

> **使用方式**：写作时，先用 `outline-template.md` 定结构 → 用 `sections/*.md` 定段落骨架 → 用本文件的模板填句子 → 用 `review/02-aaai-red-flags.md` 和自查清单做最终扫描。
