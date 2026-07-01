# AAAI 图注/表注写作规范

> 图注（figure caption）和表注（table caption）是 reviewer 阅读路径上的关键节点——reviewer 通常先扫图/表再读正文。
> 一个自包含、信息丰富的 caption 可以让 reviewer 在 15 秒内理解你的贡献，而不需要回头翻正文。
> 本模块教**怎么写 `\caption{...}` 里的文字**，与 `figure-design.md`（教怎么设计图/表本身）和 `sentence-craft.md` §三 Group 13（教怎么在正文中引用图表）互补。

---

## 速查卡：5 个最高 ROI 的图注修改

| # | 病灶 | 问题 | 快速改法 |
|---|------|------|---------|
| 1 | `\caption{Overview of our method.}` | 标签式图注——零信息 | 写明方法名 + 几阶段 + 从左到右各模块功能 |
| 2 | `\caption{Experimental results.}` | 表注只说"实验结果"——不知比什么 | 写成：`[TASK] results on [DATASET]. We report [METRICS]. Best bold, second underlined.` |
| 3 | 表注无格式约定 | reviewer 不知道粗体/下划线含义 | 加一句 `Best results in \textbf{bold}, second-best \underline{underlined}.` |
| 4 | 图注无观察引导 | reviewer 看了图不知道关键发现在哪 | 加 `Note that [KEY_FINDING] (highlighted region).` |
| 5 | 图注用了正文才定义的缩写/术语 | reviewer 不读正文看不懂 | 在图注中简要定义首次出现的视觉元素 |

---

## 一、分清两个场景：Caption vs 正文引用

这是最常见的混淆来源——writing skill 的 `figure-design.md` 之前把两个场景的路由全指向了 `sentence-craft.md` Group 13，但 Group 13 只处理场景 B。

| | 场景 A：Caption 写法 | 场景 B：正文引用句写法 |
|---|---|---|
| **是什么** | `\caption{...}` 里的文字——Figure 1 / Table 1 下方的标题说明 | 正文段落里引用图/表的句子 |
| **例子** | `Figure 1: NAME's three-stage pipeline. The encoder (left)...` | "As shown in Figure 1, NAME outperforms baselines by 3-5%." |
| **谁读** | 先扫图/表的 reviewer（可能还没读正文） | 正在读正文的 reviewer |
| **自包含要求** | **必须**自包含——reviewer 可能不看正文只看图 | 不需要自包含——上下文由正文段落提供 |
| **指导文件** | **本文件** | `sentence-craft.md` §三 第 13 组 |

> 简单判断：`\caption{...}` 里的内容 → 本文件。正文中 `Figure X shows...` / `As shown in Table Y...` → `sentence-craft.md`。

---

## 二、核心原则

### 2.1 自包含原则（Self-Contained Caption）

**reviewer 不读正文，仅凭 caption + 图/表本身，就应该能大致理解图/表的内容和关键发现。**

这不是建议——AAAI reviewer 的典型阅读路径就是 Title → Abstract → Teaser Figure → Main Results Table，在读到正文之前已经形成了对论文质量的第一判断。

| **Before**（非自包含） | **After**（自包含） |
|---|---|
| `Figure 1: Overview of our proposed method.` | `Figure 1: NAME's three-stage pipeline. Stage 1 (left) extracts multi-scale features from input images. Stage 2 (center) fuses cross-modal representations via lightweight adaptors. Stage 3 (right) produces the final segmentation mask. Dashed arrows denote training-only data flow.` |
| `Table 1: Main results.` | `Table 1: Image classification accuracy (%) on ImageNet-1K and CIFAR-100. We report top-1 and top-5 accuracy. Best results in \textbf{bold}, second-best \underline{underlined}. NAME denotes our method.` |

### 2.2 第一句承重原则（First-Sentence Weight）

**Caption 的第一句承担 80% 的信息负载。** reviewer 可能只读第一句就扫图——如果第一句是 "Overview of our method"，reviewer 什么也没学到。

- **图注第一句**必须回答：这个图展示的**是什么**（方法名 + 图类型 + 各区域代表什么）
- **表注第一句**必须回答：这个表报告的**是什么任务、什么指标、在什么数据上**

```
图注第一句公式：[方法名]'s [N]-stage [图类型]. [组件A] (位置) [功能], [组件B] (位置) [功能], [组件C] (位置) [功能].
表注第一句公式：[任务名] results on [数据集]. We report [指标1] (↑/↓), [指标2] (↑/↓).
```

---

## 三、Caption 解剖学：一句一句写

### 3.1 图注（Figure Caption）三句式结构

| 句子 | 角色 | 必须？ | 内容 |
|------|------|--------|------|
| **S1** | Subject + viewer instruction | ✅ 必须 | 图展示什么；各区域（left/right/top/bottom/center）代表什么模块/阶段 |
| **S2** | Visual conventions | 🟡 建议 | 颜色含义、线型约定（实线=推理、虚线=训练）、箭头方向 |
| **S3** | Key takeaway / caveat | 🔵 可选 | 观察引导（"Note that..."）、关键发现、或注意事项（如 "X is only active during training"） |

**示例**（架构/Pipeline 图）：

```
Figure 1: NAME's three-stage pipeline for cross-modal alignment.
The encoder (left) extracts multi-scale visual features from input images.
The fusion module (center) aligns visual and textual representations via cross-attention.
The decoder (right) generates the final segmentation mask.
Solid arrows denote the inference path; dashed arrows denote training-only gradient flow.
Note that the auxiliary classifier (gray block, top-right) is only active during training.
```

### 3.2 表注（Table Caption）三句式结构

| 句子 | 角色 | 必须？ | 内容 |
|------|------|--------|------|
| **S1** | Task + metrics + scope | ✅ 必须 | 什么任务、什么数据集、报告什么指标、指标方向 |
| **S2** | Format conventions | ✅ 必须 | 粗体/下划线/箭头含义、方法名标注 |
| **S3** | Key observation | 🔵 可选 | 一行总结关键发现（不重复正文的详细分析） |

**示例**（主结果表）：

```
Table 1: Image classification accuracy (%) on ImageNet-1K, CIFAR-100, and CIFAR-10.
We report top-1 accuracy (↑) and top-5 accuracy (↑).
Best results in \textbf{bold}, second-best \underline{underlined}. NAME denotes our method.
NAME consistently outperforms all baselines across datasets, with the largest margin (3.7%) on ImageNet-1K.
```

### 3.3 图注 vs 表注：四维对比

| 维度 | 图注（Figure Caption） | 表注（Table Caption） |
|------|----------------------|---------------------|
| **核心任务** | 引导 reviewer **看图**——"左边是什么，右边是什么，颜色代表什么" | 告诉 reviewer **表里有什么**——"什么任务、什么指标、怎么读标注" |
| **空间/位置词** | 高频（`left`, `right`, `top`, `bottom`, `center`） | 几乎不用 |
| **格式约定** | 颜色、线型、箭头、框线 | 粗体/下划线/箭头方向/上标符号 |
| **典型长度** | 2-4 句，40-100 词 | 2-3 句，30-75 词 |

---

## 四、图注句法模板（Figure Caption Templates）

### 4.1 架构/Pipeline 图

**适用**：Method 段的 pipeline figure，展示模型的模块组成和数据流。

```
Figure [N]: [NAME]'s [N]-stage [ARCHITECTURE_TYPE].
[MODULE_A] ([position]) [VERB]s [INPUT] to produce [OUTPUT].
[MODULE_B] ([position]) [VERB]s [FUNCTION].
[MODULE_C] ([position]) generates [FINAL_OUTPUT].
[CONVENTIONS: colors, solid/dashed lines, arrows].
```

> **示例**：\
> `Figure 2: LLM2CLIP's two-stage fine-tuning framework. The LLM-to-CLIP embedding module (left) converts LLM representations into CLIP-compatible embeddings. The lightweight adaptor (center) couples the embeddings to the pretrained CLIP vision encoder via cross-attention. The adapted CLIP (right) produces the final cross-modal representation. Dashed blocks denote frozen parameters; solid blocks are trainable.`\
> *（结构参考 LLM2CLIP 2026 的 pipeline 描述）*

### 4.2 对比/结果图

**适用**：Experiments 段的结果可视化（准确率曲线、分布图、注意力热力图等）。

```
Figure [N]: [WHAT_IS_VISUALIZED] on [DATASET].
[METHOD] ([color/style]) shows [CHARACTERISTIC] compared to [BASELINE_1] ([color/style]) and [BASELINE_2] ([color/style]).
[KEY_OBSERVATION: Note that...].
```

> **示例**：\
> `Figure 3: t-SNE visualization of learned representations on CIFAR-100 test set. NAME (red) produces more compact and well-separated clusters compared to the strongest baseline EVA02 (blue) and the vanilla ViT (gray). Note that NAME's clusters exhibit clearer class boundaries (highlighted regions), consistent with the 3.7% top-1 gain in Table 1.`

### 4.3 概念/Teaser 图

**适用**：Introduction 的 teaser figure（Fig. 1），展示核心思想和问题-方案对比。

```
Figure [N]: [PROBLEM_SCENARIO] vs. [OUR_APPROACH].
Left: [WHAT_EXISTING_METHODS_DO], which leads to [FAILURE_MODE].
Right: [NAME] [KEY_MECHANISM] to achieve [DESIRED_OUTCOME].
[COLOR/STYLE CONVENTIONS].
```

> **示例**：\
> `Figure 1: Existing one-shot tuning methods vs. NAME (ours). Left: Standard fine-tuning updates all parameters, causing catastrophic forgetting of pretrained knowledge. Right: NAME freezes the backbone (gray) and inserts lightweight adaptors (orange) at each layer, preserving pretrained representations while learning task-specific mappings. Orange blocks denote trainable parameters; gray blocks are frozen.`\
> *（结构参考 MaskBooster 2025 / CowClip 2023 的 teaser 设计）*

---

## 五、表注句法模板（Table Caption Templates）

### 5.1 主结果表

**适用**：Experiments 段的主对比表（SOTA comparison）。

```
Table [N]: [TASK] results on [DATASET(S)].
We report [METRIC_1] (↑/↓) [, [METRIC_2] (↑/↓)].
Best results in \textbf{bold}, second-best \underline{underlined}.
[NAME] denotes our [method/model].
```

> **示例**：\
> `Table 1: Image classification accuracy (%) on ImageNet-1K validation set. We report top-1 accuracy (↑) and top-5 accuracy (↑). Best results in \textbf{bold}, second-best \underline{underlined}. NAME is our full model. † denotes methods using extra training data.`

### 5.2 消融表

**适用**：Method/Experiments 段的消融实验表。

```
Table [N]: Ablation study on [DATASET].
Each row removes one component from [FULL_MODEL_NAME] (Row 1).
We report [METRIC_1] [and METRIC_2]. Δ denotes the absolute degradation from the full model.
```

> **示例**：\
> `Table 3: Ablation study on CIFAR-100. Each row removes one component from NAME (Row 1). We report top-1 accuracy (%). Δ denotes the absolute degradation from the full model. Row 5 (w/o adaptor) incurs the largest drop (2.8%), confirming the adaptor as the most critical component.`

### 5.3 对比/分析表

**适用**：效率对比、超参数敏感性、不同配置下的性能分析。

```
Table [N]: [ANALYSIS_TYPE] of [NAME] under [CONDITIONS/VARIATIONS].
We report [METRICS] across [N] [configurations/datasets/settings].
[CONVENTIONS: what is being varied, what is fixed].
```

> **示例**：\
> `Table 4: Inference latency (ms) and GPU memory (GB) on a single V100. We compare NAME against three baselines at batch sizes {1, 4, 16}. Latency is averaged over 100 forward passes. NAME achieves the lowest latency at all batch sizes with ≤ 10% memory overhead.`

### 5.4 基准/资源表（数据集统计表）

**适用**：Benchmark/Resource 型论文的数据集统计表。

```
Table [N]: [DATASET_NAME] statistics compared to existing [RESOURCE_TYPE].
[NAME] contains [N] samples across [K] [categories/classes/tasks],
[X]× larger than [LARGEST_EXISTING] in terms of [DIMENSION].
[ADDITIONAL_DIMENSIONS].
```

> **示例**：\
> `Table 1: Statistics of PlantTraitNet-100K compared to existing plant trait datasets. PlantTraitNet-100K contains 103,247 images across 1,284 species, 4.2× larger than the largest existing dataset TRY in terms of image count, and uniquely provides citizen-science geolocation metadata for each sample.`\
> *（结构参考 PlantTraitNet 2026 的数据集描述）*

---

## 六、常见病灶 → 改写

### 第 1 组：标签式图注 → 描述式图注

| | 内容 |
|------|------|
| **病灶** | Caption 只说了图的名称，没说图的内容——reviewer 被迫读正文才能理解 |
| **Before** | `Figure 1: Overview of the proposed framework.` |
| **After** | `Figure 1: NAME's end-to-end framework for multi-modal fusion. The encoder (left) extracts modality-specific features. The gated fusion module (center) selectively combines features via learned gating weights. The task-specific heads (right) produce final predictions for classification and segmentation.` |
| **改了什么** | `Overview of the proposed framework` → 方法名 + 三阶段 + 各模块功能 + 各模块位置 |

### 第 2 组："Overview of our method" → 具体架构描述

| | 内容 |
|------|------|
| **病灶** | 图注用 "overview" 这个词——它是 AAAI caption 中最泛滥的无信息词 |
| **Before** | `Figure 2: Overview of our method. (a) Feature extraction. (b) Cross-modal fusion. (c) Prediction.` |
| **After** | `Figure 2: NAME's three-module architecture. (a) Feature extraction: a ViT-B/16 backbone produces patch-level visual tokens. (b) Cross-modal fusion: a 2-layer transformer aligns visual tokens with text embeddings via cross-attention. (c) Prediction: an MLP head maps fused tokens to class logits.` |
| **改了什么** | `Overview of our method` → 方法名 + 每个子图不仅说"是什么"还说"怎么做的" |

### 第 3 组："Experimental results" → 任务 + 指标 + 格式约定

| | 内容 |
|------|------|
| **病灶** | 表注只说数据集名，不说任务、指标、格式约定——reviewer 看不懂表里的数字 |
| **Before** | `Table 1: Experimental results on CIFAR-10 and CIFAR-100.` |
| **After** | `Table 1: Image classification accuracy (%) on CIFAR-10 and CIFAR-100. We report top-1 accuracy (↑). Best results in \textbf{bold}, second-best \underline{underlined}. NAME denotes our full model.` |
| **改了什么** | 加了任务类型（image classification）、指标名 + 方向（top-1 ↑）、粗体/下划线约定、方法标记 |

### 第 4 组：表注缺失格式约定

| | 内容 |
|------|------|
| **病灶** | 表里用了粗体和下划线标注最优/次优值，但 caption 里没解释——reviewer 得猜 |
| **Before** | `Table 2: Comparison with state-of-the-art methods on COCO object detection.` |
| **After** | `Table 2: Object detection results on COCO val2017. We report mAP (%), AP50 (%), and AP75 (%). Best results in \textbf{bold}, second-best \underline{underlined}. NAME is our method. † denotes methods using additional detection data.` |
| **改了什么** | 加了三个要素：①指标 + 方向、②粗体/下划线约定、③特殊符号定义（†） |

### 第 5 组：图注过于冗长 → 精炼关键信息

| | 内容 |
|------|------|
| **病灶** | 图注变成了 Method 段的复读机——5 句以上的 caption 吓跑 reviewer |
| **Before** | `Figure 1: Our proposed NAME framework consists of four main components. First, the input images are passed through a ResNet-50 backbone pretrained on ImageNet-21K to extract 2048-dimensional feature vectors. These features are then fed into a multi-head self-attention module with 8 heads and a hidden dimension of 512...`（继续 ~80 词） |
| **After** | `Figure 1: NAME framework. Input images → ResNet-50 backbone → multi-head self-attention (8 heads, d=512) → classification head. Dashed arrows denote training-only paths. See §3.1 for architectural details.` |
| **改了什么** | 删掉可以在 §3.1 读到的细节；保留核心数据流 + 视觉约定；用 `→` 压缩空间 |

### 第 6 组：图注缺失观察引导

| | 内容 |
|------|------|
| **病灶** | Caption 描述了图里有什么，但没告诉 reviewer **应该注意到什么** |
| **Before** | `Figure 4: Attention maps from the last layer of NAME on sample images from COCO. Warmer colors indicate higher attention weights.` |
| **After** | `Figure 4: Attention maps from the last layer of NAME on COCO samples. Warmer colors indicate higher attention weights. Note that NAME attends to the full object extent (highlighted by red bounding boxes) rather than discriminative parts only, consistent with its improved segmentation performance in Table 2.` |
| **改了什么** | 加了 `Note that...` 观察引导——告诉 reviewer 看什么、这个观察如何与定量结果一致 |

### 第 7 组：非自包含——依赖正文定义

| | 内容 |
|------|------|
| **病灶** | Caption 使用了只在正文中定义的术语/缩写——reviewer 扫图时看不懂 |
| **Before** | `Figure 3: The GAM module's internal structure. H_Q, H_K, H_V denote the projected representations.` |
| **After** | `Figure 3: Internal structure of the Gated Attention Module (GAM, the green block in Figure 2). Query (H_Q), key (H_K), and value (H_V) projections are computed from the input features before the gating mechanism selects informative attention heads.` |
| **改了什么** | ①展开了 GAM 全称 + 在图 2 中的位置；②解释了 H_Q/H_K/H_V 是什么（不只是命名） |

### 第 8 组：表注写成正文句 → 适合 standalone 阅读

| | 内容 |
|------|------|
| **病灶** | 表注写得像正文里的分析句——不独立、缺乏表格阅读所需的元信息 |
| **Before** | `Table 5: As can be seen from the table, our method consistently outperforms all baselines across the three evaluated benchmarks, with particularly large gains on the most challenging long-tailed split.` |
| **After** | `Table 5: Classification accuracy (%) on three long-tailed benchmarks: ImageNet-LT, iNaturalist 2018, and Places-LT. We report top-1 accuracy (↑). Best results in \textbf{bold}, second-best \underline{underlined}. NAME is our method. NAME achieves the largest gains on the most challenging setting (ImageNet-LT, 3.7% over the strongest baseline).` |
| **改了什么** | `As can be seen from the table` → 删；加了任务 + 数据集 + 指标 + 格式约定；末句给关键发现时才带具体数字 |

---

## 七、长度与信息密度

### 7.1 长度参考

| Caption 类型 | 推荐句数 | 推荐词数（英文） | 红线 |
|-------------|---------|---------------|------|
| Teaser 图注（Fig. 1） | 2-4 句 | 40-100 词 | < 25 词（不自包含）、> 120 词（吓跑 reviewer） |
| 架构/Pipeline 图注 | 2-4 句 | 40-90 词 | > 100 词（可能是 Method 段的重复） |
| 结果图注 | 1-3 句 | 30-70 词 | > 80 词（正文分析就够） |
| 主结果表注 | 2-3 句 | 30-60 词 | < 20 词（没写格式约定） |
| 消融表注 | 2-3 句 | 25-60 词 | < 20 词（没解释 Δ 列） |
| 基准/资源表注 | 2-4 句 | 35-80 词 | — |

### 7.2 Caption 该放什么、不该放什么

| ✅ 该放 | ❌ 不该放 |
|---------|----------|
| 图/表展示的**具体内容** | 完整的性能数字（那是正文的工作） |
| 各区域的**名称和功能** | 方法的 motivation（那是 Introduction 的工作） |
| 视觉/格式**约定**（颜色、线型、粗体规则） | Baseline 的详细介绍（那是 Related Work / Setup） |
| **观察引导**（一句话关键发现） | `\cite{}`——AAAI caption 中避免引用 |
| 正文未定义的**术语的简要解释** | 超参配置细节（那是 Implementation Details） |
| 图的**数据来源**（dataset name, split） | — |

---

## 八、写完自查清单

- [ ] 图注第一句说明了图展示的**具体内容**（不是 "Overview of..."）？
- [ ] 表注第一句包含了**任务 + 数据集 + 指标**？
- [ ] 表注说明了**格式约定**（粗体=最优、下划线=次优、↑/↓=指标方向）？
- [ ] **自包含测试**：reviewer 不读正文能否大致理解图/表的内容？
- [ ] 图注包含了必要的**空间/视觉信息**（left/right/center、颜色、线型）？
- [ ] 图注有**观察引导**——用 `Note that...` 告诉 reviewer 关键发现在哪里？
- [ ] 图注/表注避免了引用**只在正文中定义的缩写/术语**？
- [ ] 图注没有与 Method 段正文**逐句重复**？
- [ ] 表注中 `\textbf{bold}` 和 `\underline{underlined}` 的说明与表格实际标注一致？
- [ ] 图注/表注在图/表**下方**？10pt Roman？（AAAI 硬性规则——格式终审见 `review/03-aaai-format-compliance.md`）

---

## 九、模块关系与路由

| 你想知道 | 去哪个文件 |
|---------|-----------|
| 图的**视觉设计**（布局、颜色、分辨率、表格设计） | `modules/figure-design.md` |
| 图/表的**正文引用句**怎么写（"As shown in Figure 2..."） | `modules/sentence-craft.md` §三 第 13 组 |
| Experiments 部分的**段落结构和实验设计** | `sections/experiments.md` |
| Method 部分的**段落结构和模块描述** | `sections/method.md` |
| 你的论文属于什么类型、对图/表有什么预期 | `modules/paper-taxonomy.md` → `paper-types/` |
| 获奖论文的图/表使用统计（Figure 引用频率等） | `modules/distilled-patterns.md` |
| AAAI **格式硬性约束**（字号、位置、包限制） | `modules/review/03-aaai-format-compliance.md` |
| 图表自包含作为**审稿质量标准** | `modules/review-simulator/criteria.md` |
| **图注/表注的文字写法**（结构、模板、病灶改写） | **本文件** |
