# AAAI Reviewer 评价标准

> 基于 AAAI 2027 PC member 评审指南 + 50 篇获奖论文的逆向分析。
> 7 个核心问题，按 AAAI reviewer 的实际优先级排序。

---

## 一、AAAI Reviewer 的 7 个核心问题

### Q1: 贡献是否足够？（🔴 一票否决级）

**AAAI 的贡献门槛**：一篇 AAAI 论文需要有"一块硬东西"——一个新定理、一个新方法设计、一个新数据集、一个对真实问题的有效解决方案。

| 检查项 | 通过标准 |
|--------|---------|
| 核心贡献能否用一句话说清？ | "This paper proposes X that does Y, which matters because Z." |
| 贡献是否超越了 trivial combination？ | 不是"把 A 和 B 拼在一起"——有真正的设计 insight |
| 7 页正文中贡献密度是否足够？ | 正文每页都在推进核心贡献，没有灌水段落 |
| 与 closest prior work 的差异是否实质？ | Reviewer 能清楚说出"这篇论文的 X 与 [cite] 的 Y 有本质不同因为..." |

**This is the #1 AAAI rejection reason.**

### Q2: 实验是否可信？（🔴 一票否决级）

| 检查项 | 通过标准 |
|--------|---------|
| 消融覆盖所有声称的模块？ | 每个 module → 消融行 |
| 数字跨表一致？ | Abstract = Intro = Table = Conclusion |
| "significantly" 有 p-value？ | 有统计检验或至少 std |
| Baseline 公平？ | 同数据划分/同超参搜索预算/同评估协议 |
| Cherry-pick 嫌疑？ | 没有只报赢的 metric / 只报最优 seed |
| 可重复性 Checklist 完整？ | AAAI 2027 ReproducibilityChecklist.tex 已回答所有适用项 |

### Q3: 写作是否清晰？（🟠 高权重）

**AAAI 特别关注**：AAAI 审稿人池比 NeurIPS/ICML 更多样（有做理论的、应用的、系统的），你的论文需要让**非你子领域的审稿人也能看懂**。

| 检查项 | 通过标准 |
|--------|---------|
| 跨 track 可读性 | Abstract 和 Introduction 段①-② 让非子领域的人也能理解你在做什么 |
| 一段一义 | 每段 topic sentence 清晰 |
| 术语定义 | 新术语/缩写首次出现时定义 |
| 图表自包含 | 图注/表注让 reviewer 不读正文也能大致理解 |
| Abstract 标准 | 无 `\cite`、150-200 词、五步弧线完整 |

### Q4: 格式是否合规？（🔴 Desk Reject 防线）

| 检查项 | 通过标准 |
|--------|---------|
| 无禁用包（25 项） | geometry, titlesec, authblk, ulem, float, fullpage, CJK, hyperref... |
| 无禁用命令 | `\newpage`, `\clearpage`, `\vspace{-`, `\resizebox`, `\tiny`... |
| 单 .tex 文件 | 无 `\input` 拆分（.bib 除外） |
| US Letter 纸张 | `\documentclass[letterpaper]{article}` |
| 章节顺序正确 | Abstract → 正文 → [Appendix] → [Ethical] → [Ack] → References |
| 正文 ≤ 7 页 | References 额外 |
| 图仅 .jpg/.png/.pdf | 分辨率 ≥ 300 dpi |
| 匿名投稿合规 | `\author{Anonymous Submission}` + `\affiliations{}` + 无 links 块 |

### Q5: Related Work 是否完整公平？（🟠 高权重）

| 检查项 | 通过标准 |
|--------|---------|
| 覆盖了该子领域的关键工作？ | 没有明显遗漏 |
| 对 prior work 的描述公平？ | 不贬低（"X fails to..."），客观陈述差异 |
| 切割清晰但不树敌？ | "X focuses on Y, while we address Z" |
| 自引比例合理？ | 匿名投稿中自引已匿名化；自引不超过 30% |

### Q6: 方法是否有技术深度？（🟡 中权重）

| 论文类型 | 检查重点 |
|---------|---------|
| 理论型 | 证明是否严格？假设是否 explicit？定理陈述是否独立可读？ |
| 模型方法型 | 设计是否有 insight 而非简单组合？每个模块是否有 Motivation → Design → Advantage？ |
| 基准资源型 | 数据采集/标注/质量控制流程是否严密？inter-annotator agreement？ |
| 应用驱动型 | Problem Formulation 是否合理？AI 方案是否针对领域特点设计？ |

### Q7: 是否适合 AAAI？（🟡 中权重）

| 检查项 | 通过标准 |
|--------|---------|
| 受众广度 | AAAI 审稿人来自多个 track，论文是否能被足够宽的受众理解？ |
| 会议匹配度 | 这篇论文是否更适合投 NeurIPS（偏理论方法）/ CVPR（偏视觉）/ ACL（偏 NLP）？ |
| 页数适配 | 7 页限制下内容是否完整——还是明显缺了重要内容（limitations 等）？ |

---

## 二、按论文类型的差异化权重表

| Q# | 维度 | 理论型 | 模型方法型 | 基准资源型 | 应用驱动型 |
|----|------|--------|-----------|-----------|-----------|
| Q1 | 贡献清晰度 | 问题是否被回答了 | 痛点是否被解决了 | 资源是否填补了空白 | 问题是否被 AI 有效解决了 |
| Q2 | 实验要求 | 轻量验证即可 | **严格：SOTA+消融** | **严格：baseline 全景** | 领域指标+案例分析 |
| Q3 | 写作清晰度 | 理论直觉是否传达 | 设计理由是否清楚 | 构建流程是否透明 | 领域背景是否充分 |
| Q4 | 格式合规 | 同右 | 同右 | 同右 | 同右 |
| Q5 | Related Work | 是否覆盖理论线 | 是否覆盖方法线 | 是否覆盖已有资源 | 是否覆盖领域 AI 工作 |
| Q6 | 方法深度 | **严格：证明质量** | 设计 insight 质量 | 数据质量论证强度 | 问题建模合理性 |
| Q7 | AAAI 适合度 | 理论受众理解门槛 | 贡献量级是否够 AAAI | 社区长期价值 | 真实世界影响 |

---

## 三、与 paper-review 10 维度的映射

本文档重新整合了上游 paper-review 的 10 维度：

| 上游维度 | 映射到本框架 |
|---------|------------|
| [A] 逻辑 & 论证 | → Q1（贡献是否立得住）+ Q3（写作是否清晰） |
| [B] 实证严谨性 | → **Q2（独立为一级问题）** |
| [C] 写作质量 + [H] 语言纯净度 + [I] 结构 | → **Q3（合并）** |
| [D] 引用 & 归属 | → Q5 |
| [E] 数学符号 | → Q6（方法深度的一部分） |
| [F] 双盲匿名性 + [G] 格式 | → **Q4（合并为 Desk Reject 防线）** |
| [J] 红旗 | → 贯穿 Q1-Q7 所有维度 |

上游 10 维度 → 本框架 7 问题的**核心变化**：
- AAAI reviewer 优先问"**贡献够不够**"（Q1），而非先挑写作瑕疵（C/H/I）
- 格式和双盲**合并为一个 Desk Reject 防线**（Q4），不分散为两个维度
- 新增 **Q7（是否适合 AAAI）**——这是 AAAI 特有的考量

---

> **审稿中判定"图表不自包含"时**：修复方案见 `modules/caption-writing.md` —— 提供图注/表注的解剖结构、句法模板、8 组 Before/After 改写和自包含自查清单。
