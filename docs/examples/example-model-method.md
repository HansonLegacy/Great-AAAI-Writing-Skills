# Example: Model/Method Paper — FlowRefine

> 虚构案例，展示 AAAI Writing Skill 的完整 5 阶段使用流程。
> 论文类型：**类型 2（模型/方法型）**

---

## 初始需求

```
User: 我要写一篇 AAAI 2027 论文。研究方向是视频插帧（Video Frame Interpolation），
      我做了一个基于光流引导+特征细化的新方法 FlowRefine，
      在 Vimeo-90K 和 UCF101 上都超过了 SOTA。
```

---

## Phase 1: 定位

Claude 加载 `modules/paper-taxonomy.md`，判定为**类型 2（模型/方法型）**。

三个问题引导：

```
Claude: 你的核心贡献是什么？用一句话说。

User:   我们提出了 FlowRefine——一个光流引导的特征细化网络，
        它先用轻量光流估计器预测粗运动，再通过可变形卷积在特征空间细化，
        解决了插帧中遮挡和大运动两个核心难点。

Claude: 为什么之前的方法没解决这个问题？

User:   之前的方法要么纯依赖光流（但光流对遮挡不准），
        要么用 kernel-based 方法（但核大小限制了运动范围）。
        我们结合了二者的优势。

Claude: 做成了意味着什么？

User:   视频插帧在慢动作生成、视频压缩、VR/AR 中有广泛应用。
        更好的插帧 → 更流畅的用户体验。
```

**输出**：
- 论文类型：**2（模型/方法型）**
- 核心贡献：FlowRefine = 轻量光流估计 + 可变形特征细化
- 痛点：光流法 occlusion 不准 + kernel 法运动范围受限

---

## Phase 2: 大纲

Claude 加载 `modules/outline-template.md`（类型 2 模板），生成：

```
Title (候选):
  FlowRefine: Optical Flow Guided Feature Refinement for Video Frame Interpolation

Abstract (五步弧线草稿):
  ① Context: Video frame interpolation is fundamental for...
  ② Gap: However, existing methods struggle with occlusions and large motions...
  ③ Solution: We propose FlowRefine, which combines...
  ④ Method: FlowRefine first estimates coarse motion via a lightweight optical flow
     estimator, then refines features through deformable convolutions...
  ⑤ Results: On Vimeo-90K, FlowRefine achieves PSNR 36.2 dB, outperforming...

章节大纲（示例假设具体 event 给出 7 页主文预算；请按目标 event 调整）:
  1. Introduction          (~1.0 页) — 痛点 + contributions
  2. Related Work          (~0.7 页) — 光流法 / kernel 法 / 混合法
  3. Method                (~2.0 页) — Overview + Flow Estimator + Feature Refiner + Loss
  4. Experiments           (~2.0 页) — SOTA 对比 + 消融 + 效率
  5. Conclusion            (~0.3 页)
  References               (是否计入由具体 event 决定)

图表计划:
  Fig. 1: Teaser — FlowRefine 在一帧遮挡场景的对比
  Fig. 2: Pipeline — 整体架构图
  Table 1: SOTA comparison on Vimeo-90K and UCF101
  Table 2: Ablation study
```

大纲验证：
- [x] 页数 6.0/7 页
- [x] Story arc: 痛点 → 方法 → 验证
- [x] 每个 module 有对应消融行

---

## Phase 3: 逐节撰写

### Step 1: Title → `sections/title.md`

```
FlowRefine: Optical Flow Guided Feature Refinement
for Video Frame Interpolation
```

### Step 2: Abstract → `sections/abstract.md`

```
Video frame interpolation synthesizes intermediate frames between
consecutive video frames, with applications in slow-motion generation
and video compression. However, existing flow-based methods degrade
sharply under occlusion, while kernel-based approaches are limited by
their fixed receptive field when handling large motions. We propose
FlowRefine, a two-stage framework that first estimates coarse optical
flow to capture large displacements and then applies deformable
convolutions in feature space to refine the warped features around
occlusion boundaries. This design combines the large-motion handling of
flow-based methods with the occlusion robustness of feature-space
refinement. On Vimeo-90K, FlowRefine achieves a PSNR of 36.2 dB,
outperforming the strongest baseline by 0.8 dB, with 30% fewer
parameters. On UCF101, FlowRefine sets a new state-of-the-art of 35.1 dB.
Extensive ablation studies confirm that both the flow guidance and the
deformable refinement are essential to the performance gains.
(160 words)
```

自查清单通过 ✓（无 `\cite`、150-200 词、五步弧线完整、含具体数字）

### Step 3-7: 依次撰写 Introduction / Related Work / Method / Experiments / Conclusion

每节写完后即时过自查清单。

---

## Phase 4: 整合打磨

### Reverse Outlining

```
§1 Introduction:
  ¶1: VFI 应用 + 挑战（✓ 支撑核心论点）
  ¶2: 现有方法痛点（光流遮挡 + kernel 运动范围）（✓）
  ¶3: FlowRefine 解决方案（✓）
  ¶4: Contributions（✓ 3 条，末条带数字）

§3 Method:
  ¶1: Overview（✓ 4 要素齐全）
  ¶2: Flow Estimator（✓ Motivation→Design→Advantage）
  ¶3: Feature Refiner（✓ Motivation→Design→Advantage）
  ¶4: Training Loss（⚠ 缺少 Advantage——为什么这个 loss 组合？）
  ¶5: Implementation（✓）

→ 行动项：§3.4 补充 loss 组合的设计理由
```

### Claim-Evidence 映射

```
Claim: "FlowRefine outperforms the strongest baseline by 0.8 dB"
Evidence: Table 1, Row "FlowRefine (Ours)" vs Row "AMT"
Status: ✅ supported

Claim: "30% fewer parameters than the strongest baseline"
Evidence: Table 1, Params column
Status: ✅ supported

Claim: "both flow guidance and deformable refinement are essential"
Evidence: Table 2, Rows "w/o optical flow" and "w/o deformable refinement"
Status: ✅ supported
```

---

## Phase 5: 合规+自审

- 格式合规扫描（8 类别）：🟢 PASS
- AAAI 双盲检查：🟢 PASS
- 可重复性清单：🟢 已填写
- 红旗词扫描：发现 1 处 "novel" → 改为 "new"

**提交前 10 项速查**：全部 ✅

---

## 总结

通过 5 阶段工作流，FlowRefine 从研究方向描述变成了一篇格式合规、逻辑完整的 AAAI 论文草稿。关键收益：

1. **Phase 2 页数预算**避免了 Method 写太长导致 Experiments 被压缩
2. **Phase 4 claim-evidence 映射**发现了 Loss 段缺少设计理由
3. **Phase 5 红旗词扫描**抓到了 "novel" 措辞
