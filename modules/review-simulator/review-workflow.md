# AAAI 审稿工作流（Round 1-4 详细步骤）

> 模拟 AAAI reviewer 的真实审稿过程。不是"逐段找 bug"，而是"先形成整体判断，再逐节验证，最后综合打分"。

---

## Round 1: First Pass（5 分钟模拟）

**目标**：形成初步的 Accept/Borderline/Reject 判断。大多数 AAAI reviewer 在 5 分钟内已经做出了初步决定。

### Step 1.1: 读 Title（5 秒）

```
[ ] 标题能否在 5 秒内告诉 reviewer 这篇论文在做什么？
[ ] 标题是否有可记忆的 NAME？
[ ] 标题是否包含"做了什么 + 效果"？（不仅"做了什么"）
```

### Step 1.2: 读 Abstract（30 秒）

```
[ ] 五步弧线是否完整？
[ ] 是否有具体数字（而非 "state-of-the-art" / "extensive experiments"）？
[ ] 是否有 \cite？（如果发现 = 直接扣分）
[ ] Abstract 读完后是否能一句话说清楚本文贡献？
[ ] 是否有记忆点？
```

**写下一句话总结**（reviewer 的心理笔记）：
> "This paper proposes [X] that [does Y], achieving [Z result]."

### Step 1.3: 扫 Teaser Figure + Contributions（1 分钟）

```
[ ] Teaser Figure 是否在第一页可见？
[ ] 看了 Teaser 后是否对方法有大致理解？
[ ] Contributions bullet 是否能一一对应到 Abstract 中的方法组件？
[ ] Contributions 末条是否有实验数字？
```

### Step 1.4: 扫 Main Results Table（30 秒）

```
[ ] 最优结果是否粗体标注？
[ ] 与次优结果的 margin 有多大？（<1% = 可能不 significant）
[ ] 是否有 std / p-value？
[ ] 是否在多个 benchmark 上评估？
[ ] Baseline 是否包含近年方法？（不是只有经典 baseline）
```

### Step 1.5: 形成初步判断

基于 Round 1，reviewer 心里已经有一个大致定位：

```
[ ] Likely Accept —— 贡献 clear，实验扎实，标题有记忆点
[ ] Could Go Either Way —— 有好的部分，但有明显的 question mark
[ ] Likely Reject —— 贡献不清晰，实验有 gap，或格式明显违规
```

---

## Round 2: Section-by-Section Deep Read（30 分钟模拟）

**加载 `criteria.md`**：按论文类型选择对应的评价权重。

### Step 2.1: Introduction（最重要的一节）

```
[ ] 段①-②：能否快速理解本文在解决什么问题？
[ ] 段②（痛点）：每个痛点是否带技术原因 + 具体代价？
[ ] 段④（方法）：是否显式 "we propose NAME" + teaser 图指针？
[ ] Contributions：每条是否 = 机制 + 收益？末条是否带数字？
[ ] 三重一致：痛点 ↔ 创新 ↔ contributions 数目与顺序是否对齐？
[ ] Abstract ↔ Intro 逐句是否能连线？
[ ] 引用：是否足够早出现（段①/②即有）？
[ ] 匿名投稿：自引是否匿名化？无机构暗示？

🚩 高危信号：
  - Introduction 读完后不知道贡献是什么
  - 痛点泛泛（"existing methods are limited" 没有具体技术原因）
  - 先讲朴素 baseline 再说自己改进（读着像打补丁）
  - 没有 contributions list
```

### Step 2.2: Related Work

```
[ ] 组织策略是否清晰（按技术线/任务/单段）？
[ ] 每组的最后一句是否收束到"我们与这组的区别"？
[ ] 是否遗漏了明显应该引的工作？
[ ] 对 prior work 的描述是否公平（不贬低）？
[ ] 自引比例是否合理（<30%）？
[ ] 页数是否 ≤ 1 页？

🚩 高危信号：
  - 明显遗漏了该 track 的重要工作
  - 引用堆砌（一段 5+ cite，没有区分度）
  - "None of them do what we do" 式 dismissive
```

### Step 2.3: Method

```
[ ] Overview 段是否包含 4 要素（setting + core idea + figure + roadmap）？
[ ] 每个 module 是否有 Motivation → Design → Forward Process → Advantage？
[ ] Pipeline 图是否清晰（数据流方向/张量形状/模块区分）？
[ ] 数学符号是否首次出现时定义？全文是否一致？
[ ] 每个 equation 是否有 "where..." 解释？
[ ] 每个 design choice 是否有理由？（对应 ablation）
[ ] 页数：Method 是否在 1.5-2.5 页内（7 页预算内）？

🚩 高危信号：
  - 模块没有 motivation——"we use X" 但不解释为什么
  - 符号前后不一致（同符号不同含义）
  - 公式没有解释（仅为装饰而堆公式）
```

### Step 2.4: Experiments

```
[ ] Setup 是否完整（datasets + baselines + metrics + implementation）？
[ ] 主表格式正确（booktabs / 数字对齐 / 最优粗体 / 无 \resizebox）？
[ ] 每个声称的 module 是否有对应消融行？
[ ] 每个结果段落 = setup + result + comparison + interpretation？
[ ] "significantly" 是否有 p-value？是否有 std？
[ ] Baseline 是否包含近年方法？是否公平比较？
[ ] 超参数信息是否完整（GPU/框架/lr/batch/seeds）？
[ ] 可视化是否灰度可读？分辨率 ≥ 300 dpi？

🚩 高危信号：
  - 没有消融实验
  - 数字跨表不一致
  - 只在一个 benchmark 上做实验
  - 没有 std
  - 用了 \resizebox
```

### Step 2.5: Conclusion

```
[ ] ≤ 0.5 页？2-3 段？
[ ] 用不同于 Abstract/Intro 的措辞重述贡献？
[ ] 有具体局限性（不是泛泛的 "more work is needed"）？
[ ] 有具体 future direction？
[ ] 不引入新信息（无新图/表/引用）？
[ ] 无营销口吻（"novel"/"first"/"redefine"）？

🚩 高危信号：
  - 没有局限性讨论
  - 复制 Abstract 内容
  - "Code will be released"（匿名投稿）
```

---

## Round 3: Cross-Cutting Check

### Step 3.1: 数字一致性矩阵

```
| 关键数字 | Abstract | Intro | Table X | Conclusion | 一致？ |
|----------|----------|-------|---------|------------|--------|
| 主结果 1 | ...      | ...   | ...     | ...        | ✅/❌    |
| 主结果 2 | ...      | ...   | ...     | ...        | ✅/❌    |
```

### Step 3.2: Claim-Evidence 追踪

```
Introduction 中的 claim 1 → Experiments 中的 [Table X, Row Y] → ✅/⚠️/❌
Introduction 中的 claim 2 → Experiments 中的 [Table X, Row Y] → ✅/⚠️/❌
```

### Step 3.3: 符号一致性

```
[ ] 同一符号全文是否同含义？
[ ] 所有符号是否首次出现时定义？
[ ] Ablation 表是否覆盖所有 Method 中的 module？
```

### Step 3.4: 格式合规扫描

```
[ ] 加载 review/02-aaai-red-flags.md → 扫描 65 项红旗
[ ] 加载 review/03-aaai-format-compliance.md → 8 类别格式检查
[ ] 特别关注：
    [ ] Abstract 无 \cite
    [ ] 无禁用包/命令
    [ ] US Letter 纸张
    [ ] 单 .tex 文件
    [ ] 正文 ≤ 7 页
    [ ] 无页码
```

### Step 3.5: 与获奖论文基准校准

```
加载 scoring-calibration.md：
[ ] Abstract 词数 vs 获奖论文基准（均值 160）
[ ] Title 模式 vs 获奖论文基准（58% NAME:Subtitle）
[ ] 记忆点存在性 vs 获奖论文基准（48% 有记忆点）
[ ] 按论文类型的贡献密度 vs 对应类型的获奖论文
```

---

## Round 4: 综合打分 + 输出

### Step 4.1: 汇总 Strengths 和 Weaknesses

从 Round 2 的各节标注中汇总，按严重度排序。

### Step 4.2: 给出 Overall Rating

根据 `scoring-calibration.md` 的评分边界，综合 Q1-Q7 的判断。

### Step 4.3: 生成审稿意见

```
加载 review-template.md → 按模板填充所有字段
加载 common-qa.md → 生成 Rebuttal 预判
```

### Step 4.4: 输出

按 `review-template.md` 的格式输出完整审稿意见。
