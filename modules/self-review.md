# AAAI 特化自审清单

> **上游参考**：`paper-review` skill（10 维度框架、4 级 flag 体系）
> 本文档是 AAAI 特化自审的**快速入口**——做轻量自查用。
> **深度审查**请用 `modules/review/` 下的 AAAI 特化 prompt：
> - `00-aaai-master-workflow.md` — AAAI 完整审查工作流（10 维度 AAAI 化）
> - `01-aaai-section-review.md` — 章节级专项审查（Abstract/Intro/Method/Experiments/Conclusion）
> - `02-aaai-red-flags.md` — AAAI Reviewer 红旗速查表（65 项，含 19 项 AAAI 新增）
> - `03-aaai-format-compliance.md` — AAAI 2027 格式合规专项扫描（8 类别，替代 IEEE 格式检查）
> - `04-aaai-double-blind.md` — AAAI 2027 双盲合规扫描（含 submission 模式特有检查）
> - `05-aaai-reproducibility.md` — AAAI 2027 可重复性清单审查

---

## 〇、审查工作流

```
Step 1: 先运行 aaai-compliance-checker（格式硬伤先排除）
Step 2: 轻量自查 → 用本文档五维度框架快速过一遍
Step 3: 深度审查 → 用 modules/review/00-aaai-master-workflow.md 逐段详细审
Step 4: 专项检查 → 按需加载 review/01-05 对应 prompt
Step 5: 生成自审报告（🔴/🟠/🟡/🟢 四级）
```

---

## 一、AAAI 自审五维度

### [A] 贡献清晰度（AAAI 最高频拒稿原因）

| 检查项 | 通过标准 |
|--------|---------|
| 论文在解决什么问题？ | 任何一篇 AAAI 论文在 Introduction 段①-② 应该清晰回答 |
| 贡献是什么？（1 句话） | 不读完整 Intro 也能说出 "this paper proposes X that does Y" |
| 贡献和已有工作有本质区别？ | 不是 "加了 attention / 换了 backbone / 调了 loss" |
| Novelty illusion？ | 没有用抽象术语包装朴素做法 |
| Contributions bullet 可追溯？ | 每条 → Method subsection → Experiments table |

### [B] 逻辑与实证（Claim-Evidence 对齐）

| 检查项 | 通过标准 |
|--------|---------|
| Abstract 和 Intro 中的每个强 claim 有实验支撑？ | Claim-Evidence 映射全部 ✅ |
| 因果声称恰当？ | "X improves Y" 有消融支撑；"X causes Y" 需要更强证据 |
| 数字跨表一致？ | 同一数字在 Abstract / Intro / Experiments 中一致 |
| 消融覆盖所有声称模块？ | 每个 module → 对应消融行 |
| 有 std / p-value？ | 至少报告方差；要 claim "显著优于" 必须有统计检验 |
| Baseline 公平？ | 所有 baseline 用相同数据预处理/评估协议 |

### [C] 写作与技术质量

| 检查项 | 通过标准 |
|--------|---------|
| 一段一义？ | 每段 topic sentence 清晰 |
| 指代无歧义？ | "this" / "it" 的指代明确 |
| 时态一致？ | 自己的方法用现在时，别人的方法用过去时/现在完成时 |
| 术语稳定？ | 方法名/组件名/缩写全文一致 |
| 公式有使命？ | 每个公式在正文中被引用和解释 |
| Abstract 无 `\cite`？ | ✅ |

### [D] 格式合规（Desk Reject 防线）

详见 `aaai-compliance-checker`，此处仅列最高频的 5 个 format-killer：

| # | 检查项 | 风险 |
|---|--------|------|
| 1 | 无禁用包（geometry, titlesec, authblk...） | 🔴 Desk reject |
| 2 | 无禁用命令（\newpage, \clearpage, \vspace{-...}） | 🔴 Desk reject |
| 3 | 纸张为 US Letter | 🔴 Desk reject |
| 4 | frenchspacing 已开启 | 🟠 格式退回 |
| 5 | 无页码 | 🟠 格式退回 |

### [E] 双盲与伦理（匿名投稿）

| 检查项 | 通过标准 |
|--------|---------|
| PDF metadata 无作者信息？ | 已清理 |
| 无 "In our previous work..."？ | 自引匿名化 |
| 无 links 块包含识别性链接？ | 匿名投稿不允许 links 块 |
| Teaser 图无机构 logo/名称？ | ✅ |
| Acknowledgments 留空或占位？ | 匿名投稿不写致谢 |
| Ethical Statement 已填写（如适用）？ | ✅ |

---

## 二、全局一致性扫描

### 2.1 跨章节可追溯链

```
Abstract ① Context         → Introduction 段①
Abstract ② Gap             → Introduction 段②
Abstract ③ Solution        → Introduction 段④ 首句
Abstract ④ Method 组件     → Introduction contributions + Method subsections
Abstract ⑤ Results         → Introduction 段⑤ + Experiments 主表

Introduction contributions → Method 的 subsections（是否能一一映射？）
Method 的每个 module       → Experiments 的消融表（是否有消融行？）
Introduction 的每个 claim  → Experiments 的表/行/图（是否有证据？）
```

### 2.2 术语一致性

- [ ] 方法名：全文统一（同一种拼写、同一种大小写）
- [ ] 数学符号：全程一个符号一种含义，无重载
- [ ] 缩写：Abstract 和 Introduction 各首次出现时均定义一次

### 2.3 数字一致性

- [ ] Abstract 里的数字 = Introduction 里的数字 = Experiments 里的数字
- [ ] 图/表中的数字与正文引用一致
- [ ] 消融表中 Full model 的数字 = 主表中 NAME 的数字

---

## 三、红旗词扫描

以下词汇在 AAAI 投稿中会被 reviewer 特别关注——每出现一次就要确保有充分证据：

| 红旗词 | Reviewer 反应 | 需要什么证据 |
|--------|-------------|------------|
| `novel` | "是吗？让我看看..." | 充分的相关工作对比 + 明确的新机制 |
| `significant` / `significantly` | "统计显著？" | p-value / 统计检验 |
| `state-of-the-art` / `SOTA` | "在所有 benchmark 上？" | 多数据集 SOTA 表 + 与最强 baseline 的 margin |
| `first` | "真的是第一个？" | 非常确信没有遗漏相关工作 |
| `robust` | "对什么鲁棒？" | 明确说明鲁棒的对象和验证方式 |
| `simple` / `efficient` | "量化一下？" | 复杂度分析 / 速度/显存数字 |
| `better` | "比谁好？好多少？" | 指名 baseline + 具体数字 |

---

## 四、自审报告模板

```
=== AAAI Self-Review Report ===

🔴 CRITICAL (投稿阻断级):
  - [列在此处]

🟠 MAJOR (强烈建议修):
  - [列在此处]

🟡 MINOR (尽量修):
  - [列在此处]

🟢 PASS:
  - [列出所有通过检查的大项]

=== Claim-Evidence Summary ===
Total claims: N
✅ Supported: N
⚠️ Needs evidence: N
❌ Contradicted: N

=== Format Compliance ===
aaai-compliance-checker output: [PASS / FAIL with N issues]

=== Overall Readiness ===
[Ready to submit / Ready after fixing MAJOR items / Needs significant revision]
```

---

> **自查后的下一步**：
> - 发现句子级写作问题 → `modules/sentence-craft.md`（句法模板 + Before/After 改写 + 节奏检查）
> - 需要更深度审查 → `modules/review/00-aaai-master-workflow.md`（AAAI 10 维度完整审查）
> - 想模拟审稿人视角 → `modules/review-simulator/SKILL.md`（完整 Review 意见 + Rebuttal 预判）
