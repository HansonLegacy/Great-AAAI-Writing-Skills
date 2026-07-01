# AAAI 标题写作（Title）

> 标题是第一印象。Reviewer 花在标题上的时间 ≈ 5 秒——这 5 秒决定是否继续读 abstract。

---

## 一、AAAI 格式约束

| 约束 | 说明 |
|------|------|
| **大小写** | Title Case（Chicago Manual of Style 规则）。用 [titlecaseconverter.com](https://titlecaseconverter.com/)（选 Chicago + Show explanations）验证 |
| **字体** | 16pt 粗体，24pt 行距（模板自动设置——不要手动干预 `\textbf`, `\Large` 等） |
| **居中** | 模板自动居中 |
| **长度** | 通常 8-16 词。过长会被 reviewer 认为不够聚焦 |

---

## 二、获奖论文标题命名模式

基于 50 篇 AAAI 获奖论文的标题分析，归纳出 4 种命名模式：

### 模式 1: `NAME: Descriptive Subtitle`（最主流，~50%）

```
LLM2CLIP: Powerful Language Model Unlocks Richer Cross-Modality Representation
CowClip: Reducing CTR Prediction Model Training Time from 12 Hours to 10 Minutes on 1 GPU
DropMessage: Unifying Random Dropping for Graph Neural Networks
DivShift: Exploring Domain-Specific Distribution Shifts in Large-Scale, Volunteer-Collected Biodiversity Datasets
```

**模式**：`[记忆点名称]: [一句话描述做了什么 + 效果]`

### 模式 2: `Gerund Phrase for Task`（~25%）

```
Unifying Random Dropping for Graph Neural Networks
Exploring Tuning Characteristics of Ventral Stream's Neurons for Few-Shot Image Classification
Computing Game Symmetries and Equilibria That Respect Them
```

**模式**：`[动名词短语 doing X] for [任务/领域]`

### 模式 3: `Statement of Finding`（~15%，理论型常见）

```
Eliminating Majority Illusion is Easy
Two Heads Are Better than One: Image-Point Cloud Network for Depth-Based 3D Hand Pose Estimation
Every Bit Helps: Achieving the Optimal Distortion with a Few Queries
```

**模式**：`[核心发现陈述]` 或 `[发现]: [解释]`

### 模式 4: `Question-Based`（~5%，较少见）

虽在获奖论文中少见，但在 AAAI 中偶有出现：
`Is My Prediction Arbitrary? The Confounding Effects of Variance in Fair Classification Benchmarks`

---

## 三、标题设计原则

### 3.1 好标题的特征

1. **包含可被记忆的 NAME**（3-10 字符缩写）。NAME 会成为 reviewer 讨论你论文时的 token
2. **包含 "做了什么 + 效果"**。仅 "做了什么" 不够——加上效果让 reviewer 一眼看到 value
3. **可搜索**——含领域关键词。方便后人在 Google Scholar 中找到你
4. **不多词**。删掉 "A Study of..." "Towards..." "On the..." 等 filler

### 3.2 命名 NAME 的原则

- 3-10 字符：`LLM2CLIP` (8), `CowClip` (7), `JoLT` (4), `DropMessage` (11)
- 可读：能被口头讨论
- 不与已有知名方法同名
- 最好暗示核心机制/来源：`CowClip`（Cow + Clip gradient）, `LLM2CLIP`（LLM → CLIP）

### 3.3 避免的写法

| 病灶 | 问题 | 改法 |
|------|------|------|
| "A Novel Approach for..." | "Novel" 是 red flag 词 + filler | 删掉，直接说做了什么 |
| "Towards..." / "On the..." | 太虚、不承诺 | 删掉前缀 |
| 标题吹太大 | 审稿人看实验匹配不上 | 标题范围 ≈ 实际贡献范围 |
| NAME 太泛 | "DeepModel" / "NeuralNet" 不可用 | 取有区分度的名字 |
| 副标题和主标题不对齐 | 主标题说 A，副标题说 B | 确保主副标题一致 |

---

## 四、按论文类型的标题微调

| 类型 | 推荐模式 | 关键词 |
|------|---------|--------|
| 理论/算法型 | 模式 3（发现陈述）或 模式 1+结论 | Optimal, Decidable, Tight, Complexity, Easy |
| 模型/方法型 | 模式 1（NAME: descriptive） | 方法名 + 任务/效果 |
| 基准/资源型 | 模式 1 或 2 | Dataset, Benchmark, Framework, Exploring |
| 应用驱动型 | 模式 1 或 2（含领域术语） | 领域术语 + AI 方法 |

---

## 五、写完自查清单

- [ ] Title Case 符合 Chicago Manual of Style？
- [ ] 长度 8-16 词？
- [ ] 包含可记忆的 NAME？
- [ ] 包含 "做了什么 + 效果"？
- [ ] 无 "Novel" "Towards" "A Study of" 等 filler？
- [ ] 标题范围 ≈ 实际贡献范围（不吹太大）？
- [ ] 在 Google Scholar 上可搜索（含领域关键词）？

---

> **句子级模板**（`modules/sentence-craft.md`）：标题确定后，用以下模板撰写 Abstract 第一句（开场）和全文的记忆点句：
> - 记忆点句 → §2.5 模式 A（数字+对比，如 `reduces training time from 12 hours to 10 minutes on 1 GPU`）
> - 破折号强调 → §速查卡（48% 获奖论文使用的记忆点技术）
