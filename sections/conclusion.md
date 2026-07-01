# AAAI 结论写作（Conclusion）

> Conclusion 是 reviewer 读的最后一节。目标是让 reviewer 带着清晰的印象关闭 PDF。

---

## 一、AAAI 特有约束

| 约束 | 说明 |
|------|------|
| **长度** | ≤ 0.5 页。Conclusion 不是第二篇 Intro——简洁收尾 |
| **位置** | 紧跟正文 / Appendix / Ethical Statement / Acknowledgments 之后，References 之前 |
| **字号** | 与正文相同（10pt），不能更小 |
| **无新信息** | Conclusion 不应引入正文中未讨论的新概念、新结果或新引用 |

---

## 二、三段式结构

### 段 1: Summary（2-3 句）

**重述核心贡献——但不复制 Abstract 和 Introduction。**

```
"We [做了什么] by [核心机制].
Our method achieves [最关键数字],
[与最强对手的对比]."
```

**关键**：这里用**不同的措辞**复述贡献，不是 copy-paste。Abstract 是预告，Introduction 是展开，Conclusion 是回望。

### 段 2: Limitations & Discussion（2-4 句）

**诚实面对局限性。** 这是 AAAI reviewer 越来越看重的一点。

可讨论：
- 方法在什么条件下可能不 work
- 数据/实验的范围限制（只在 X 类数据上验证了）
- 计算成本、部署挑战
- 理论假设与实际场景的 gap

> 📄 LLM2CLIP (AAAI 2026 Oral) 的局限性讨论写 "our adaptor currently only supports CLIP-ViT-L/14; extending to other vision encoders and VLM backbones requires architecture-specific tuning that we leave to future work"——具体到模型名称和扩展方向，reviewer 能明确判断局限性范围。
> 📄 CowClip (AAAI 2023) 对计算成本的局限性讨论同样具体："our method reduces training time from 12 hours to 10 minutes on 1 GPU for CTR prediction, but the batch size reduction strategy has only been validated on recommendation models with embedding layers; its effectiveness on dense transformer architectures remains unknown."

### 段 3: Future Work（1-2 句）

**具体而非泛泛。** 不说 "Future work could explore many directions"，而说：

- "Extending NAME to [specific new setting] would be a natural next step."
- "The [limitation] could be addressed by [specific approach] in future work."

---

## 三、避免的写法

| 病灶 | 问题 | 改法 |
|------|------|------|
| "In this paper, we proposed..."（逐条 recap） | 像在复制 contributions bullet | 用一段综述替代逐条 recap |
| 泛泛的 "Future work will explore many directions" | 无信息 | 具体的 1-2 个 future direction |
| 没有局限性讨论 | Reviewer 认为你没有 critical thinking | 至少 1-2 句具体局限性 |
| 营销口吻 "Our method is the first to..." | Red flag + Conclusion 不是卖广告的地方 | 客观陈述，去掉 superlative |
| 引入新图/新表 | Conclusion 不应有新信息 | 移到 Experiments |
| 太长（> 0.8 页） | 占用正文宝贵空间 | 压缩到 2-3 段 |
| "Code will be released" | 匿名投稿违规 + 无信息量 | 删掉 |

---

## 四、Before/After 改写（4 组）

### 组 1：逐条 Recap → 综述收束

| | |
|---|---|
| **Before** | "In this paper, we proposed FlowRefine, a flow-based refinement module. We also introduced a temporal consistency loss. We further designed a multi-scale fusion strategy. Experiments on Vimeo-90K, UCF101, and Middlebury show our method outperforms existing approaches." |
| **After** | "We presented FlowRefine, which unifies flow-based refinement, temporal consistency regularization, and multi-scale fusion into a single end-to-end video frame interpolation framework. Across three standard benchmarks spanning synthetic, real-world, and high-resolution scenarios, FlowRefine achieves consistent gains over prior work (2.1 dB on Vimeo-90K, 1.8 dB on UCF101)." |
| **改了什么** | 逐条 bullet 感 → 一句综述贡献 + 一句收束结果。三个模块用 "unifies" 串联，三个数据集用 "spanning" 归类，避免直接复制 Introduction 的贡献列表 |

### 组 2：泛泛 Future Work → 具体方向

| | |
|---|---|
| **Before** | "Future work could explore many interesting directions, including better architectures, more data, and different application domains." |
| **After** | "A natural next step is extending FlowRefine to the multi-frame setting (N > 2), where the temporal consistency loss could leverage longer-range motion patterns. On the data side, the current model is trained only on synthetic triplets; incorporating real-world video pairs with unknown intermediate frames via self-supervision could further close the domain gap." |
| **改了什么** | "many interesting directions" → 两个具体方向，每个都（1）说出具体做法（2）解释为什么值得做（3）与本文方法的当前限制关联 |

### 组 3：无局限性 → 诚实讨论

| | |
|---|---|
| **Before** | "Our method achieves state-of-the-art results across all benchmarks, demonstrating its effectiveness and generalizability." |
| **After** | "FlowRefine achieves strong results on standard benchmarks, though two limitations should be noted. First, all evaluated datasets consist of short video clips (< 10 seconds); performance on long-form video with scene changes remains untested. Second, the multi-scale fusion introduces ~15% parameter overhead compared to a single-scale baseline——a trade-off between accuracy and efficiency that future work could optimize." |
| **改了什么** | 只报喜 → 加两个具体局限性（场景限制 + 效率 trade-off），每个带量化细节 |

### 组 4：营销口吻 → 客观陈述

| | |
|---|---|
| **Before** | "Our novel FlowRefine framework is the first to successfully apply flow refinement to video frame interpolation, significantly advancing the state of the art." |
| **After** | "FlowRefine demonstrates that flow refinement——a technique previously limited to optical flow estimation——can be effectively adapted for video frame interpolation, providing a new perspective on motion representation in synthesis tasks." |
| **改了什么** | 删 "novel" / "first" / "significantly advancing SOTA"。改为主张一个可证伪的 insight（"flow refinement 可跨任务迁移"），语气从"宣告胜利"变为"分享发现" |

---

## 五、按论文类型的微调

| 类型 | 局限性讨论重点 | Future Work 重点 |
|------|--------------|-----------------|
| 理论/算法型 | 理论假设的限制、条件能否放宽 | Open problem / 放宽条件 |
| 模型/方法型 | 计算成本、未验证的数据类型 | 扩展到新 domain / 新 task |
| 基准/资源型 | 资源覆盖范围限制、标注偏见 | 社区如何使用、后续扩展 |
| 应用驱动型 | 真实部署中的 failure mode | 更大规模部署 / 长期效果 |

---

## 六、写完自查清单

- [ ] ≤ 0.5 页、2-3 段？
- [ ] 段 1 用不同于 Abstract/Intro 的措辞重述贡献？
- [ ] 段 2 有具体的局限性讨论（不是泛泛的）？
- [ ] 段 3 有具体的 future direction？
- [ ] 没有引入新图/新表/新引用？
- [ ] 没有 "novel"/"first"/"significant" 等营销词？
- [ ] 没有 "Code will be released"（匿名投稿）？
- [ ] Conclusion 能独立阅读——让只看过 abstract 和 conclusion 的人理解你做了什么？

---

> **句子级模板**（`modules/sentence-craft.md`）：Conclusion 的核心句子类型：
> - 贡献重述 → §2.5 模式 E（意义收束：These results [implication]...），注意措辞不同于 Abstract
> - 局限性讨论 → §2.8 局限性句（3 种模式：诚实局限性 / 限定条件 / 资源局限性）
> - 未来方向 → §2.7 过渡句 模式 D（Building on X, we next...）
> - 避免营销口吻 → §3 第 2 组（删 novel）、第 14 组（删 Interestingly）
> - 写完后过 → §六 Conclusion 句子自查（3 条）
