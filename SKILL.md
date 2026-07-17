---
name: aaai-writing
description: AAAI 2027 论文写作全流程编排。从大纲生成到逐节撰写到终稿打磨，针对不同论文类型（理论/模型方法/基准资源/应用驱动）提供特化指导。所有规则蒸馏自 2023-2026 AAAI 获奖论文，格式约束对齐 Author Kit 2027。当用户要写 AAAI 论文、准备 AAAI 投稿、问"AAAI 论文怎么写"时使用。
---

# AAAI 论文写作系统

> **核心设计**：一个父 Skill 管全局编排 + N 个子模块按需加载。你写到哪一节，就加载哪一节的专属 guidance。
> **所有规律**均标注来源：获奖论文实例（`📄`）或 Author Kit 规范（`📋`）。

## 触发场景

当用户提到以下任意关键词时，加载本 skill：
- "写 AAAI 论文" / "AAAI 写作" / "准备投 AAAI"
- "AAAI 投稿" / "AAAI 2027"
- "帮我写 paper"（上下文是 AAAI 会议时）
- "生成论文大纲" / "论文结构怎么组织"

## 工作流总览（5 阶段）

```
Phase 1: 定位     → 确定论文类型 + 核心贡献形态
Phase 2: 大纲     → 生成章节大纲 + 页数预算 + story arc 验证
Phase 3: 逐节撰写  → 按顺序路由到 sections/ 子 Skill（按需加载）
Phase 4: 整合打磨  → 全篇 flow / claim-evidence 映射 / 术语一致性
Phase 5: 合规+自审 → 格式合规 + AAAI 特化自审 + 双盲检查
```

---

## Phase 1: 定位（Understand）

### Step 1.1: 确定论文类型

加载 `modules/paper-taxonomy.md`，根据用户的研究内容判定论文类型。

| # | 类型 | 一句话定义 | 核心贡献形态 |
|---|------|-----------|-------------|
| 1 | **理论/算法型** | 定理、证明、复杂度分析、可判定性 | 新定理/新界/新算法 + 严格证明 |
| 2 | **模型/方法型** | 新架构、新训练方法、新框架（含 LLM/VLM/小模型/视觉等） | 新方法/新模块 + benchmark SOTA |
| 3 | **基准/资源型** | 新数据集、新 benchmark、系统性实证研究 | 新资源 + 全面 baseline 评估 + 洞见 |
| 4 | **应用驱动型** | AI 解决真实世界问题（社会影响/医疗/教育等） | 问题建模 + 领域验证 + 真实影响 |

判定完成后，**将类型编号（1-4）记为全局上下文**，后续所有子模块加载时自动注入对应类型的专属 guidance。

### Step 1.2: 明确核心贡献

让用户回答（或从讨论中提取）3 个问题：
1. **What's new?** 新任务 / 新方法 / 新理论 / 新基准 / 新应用？
2. **Why now?** 为什么之前没人做/做不好？技术瓶颈是什么？
3. **So what?** 做成了意味着什么？谁会关心？

---

## Phase 2: 大纲（Outline）

### Step 2.1: 生成大纲

加载 `modules/outline-template.md`，根据论文类型选择对应模板，生成包含以下元素的章节大纲：

- 各章节标题（对齐 AAAI 结构规范）
- 每节预计页数/栏数
- 每节核心信息点（3-5 bullet）
- Abstract 五功能句草稿

### Step 2.2: 验证大纲

大纲生成后，逐项验证：

- [ ] **页数预算**：先读取具体 event 的页限；Content Appendices 计入该页限，不从通用 Author Kit 推断固定页数
- [ ] **Story arc**：Abstract → Intro → Method → Experiments 逻辑链完整
- [ ] **贡献-证据映射**：每个核心贡献在 Experiments 中有对应验证
- [ ] **图表计划**：teaser、pipeline、main result table、ablation 各有位置
- [ ] **格式合规**：无禁用包/命令，章节顺序正确（详见 `modules/compliance-quick.md`）

---

## Phase 3: 逐节撰写（Write）

按 AAAI 论文的标准写作顺序推进。**每节只加载对应的子 Skill**，不提前加载后续章节。

### 写作顺序与子 Skill 映射

| 顺序 | 章节 | 加载文件 | 产出 |
|------|------|---------|------|
| 1 | **Title** | `sections/title.md` | 1-2 个候选标题 |
| 2 | **Abstract** | `sections/abstract.md` | 五步弧线摘要（150-200 词） |
| 3 | **Introduction** | `sections/introduction.md` | 5-7 段引言 + contributions 列表 |
| 4 | **Related Work** | `sections/related-work.md` | 组织策略 + 段落草稿 |
| 5 | **Method** | `sections/method.md` | 各模块三元组（设计/动机/优势） |
| 6 | **Experiments** | `sections/experiments.md` | 实验设计 + 表格模板 + 分析框架 |
| 7 | **Conclusion** | `sections/conclusion.md` | 总结 + 局限性 + 展望 |

### 撰写纪律

1. **每节写完后运行该节的自查清单**（每个 sections/ 文件末尾附带）
2. **句子级参考**：写作时加载 `modules/sentence-craft.md`——模板库 + Before/After 示例 + 节奏检查
3. **维护跨节一致性**：
   - Abstract 的每个功能句 → Intro 中对应段落
   - Intro 中 contributions bullet → Experiments 中对应结果
   - Method 中每个模块 → Experiments 中对应消融实验
4. **术语稳定**：方法名、组件名在首次定义后全文复用；缩写在 Abstract 和 Intro 各首次出现时均定义一次
5. **引用纪律**：Abstract 不含 `\cite`；Intro 引用尽早出现（段①/②即开始引用）

---

## Phase 4: 整合打磨（Polish）

所有章节写完后，进行全篇一致性打磨：

### 4.1 Reverse Outlining

对每节执行反向提纲：
1. 写出该节的核心论点
2. 提取每段的 topic sentence
3. 验证 topic sentence → 核心论点的支撑关系
4. 删掉或重写无法映射的段落

### 4.2 Claim-Evidence 映射

对 Abstract 和 Introduction 中的**每一个强 claim**，标注：
```
Claim: <具体断言>
Evidence: <实验章节/表号/图号>
Status: ✅ supported / ⚠️ needs evidence / ❌ contradicted
```
所有 ⚠️ 和 ❌ 项必须解决才能进入 Phase 5。

### 4.3 术语一致性扫描

- 方法名/组件名/缩写全文一致
- 数学符号无重载（同一符号不表示两个不同量）
- 所有缩写首次出现时已定义

### 4.4 图表最终检查

加载 `modules/figure-design.md`，检查：
- Teaser 图是否在第一页可见
- 位图分辨率 ≥ 300 dpi；矢量 PDF 不套用 DPI 阈值
- 图内文字在最终版面中 ≥ 9pt
- 表使用 booktabs 风格，数字对齐
- 图注/表注格式正确

---

## Phase 5: 合规+自审（Review & Comply）

### 5.1 格式合规

使用仓库内置的确定性检查器进行源文件预检；不要依赖未随本仓库安装的外部 skill：

```bash
python scripts/aaai27_check.py paper.tex --stage anonymous \
  --technical-appendix unknown --checklist unknown
```

检查前必须声明 `anonymous` 或 `camera-ready` 阶段，并尽可能提供具体 event 的页限、Technical Appendix 政策和 Checklist 提交方式。脚本未拿到 PDF、编译日志或最终打包文件时，会把相应维度标为 `NOT_CHECKED`，不能据此声称整篇完全合规。写作过程中可用 `modules/compliance-quick.md` 做快速自查。

深度格式审查用 `modules/review/03-aaai-format-compliance.md`（8 类别 × AAAI 2027 专项，替代 paper-review 的 IEEE 格式检查）。

### 5.2 AAAI 特化自审

**轻量自查** → 加载 `modules/self-review.md`（五维度框架）。

**深度审查** → 按需加载 `modules/review/` 下的 AAAI 特化 prompt：

| 文件 | 用途 | 使用时机 |
|------|------|---------|
| `review/00-aaai-master-workflow.md` | AAAI 10 维度完整审查（主入口） | 投稿前 1-2 周 |
| `review/01-aaai-section-review.md` | 章节级专项审查（5 模块） | 每节写完后 |
| `review/02-aaai-red-flags.md` | AAAI Reviewer 红旗速查（65 项） | 随时 Cmd+F |
| `review/03-aaai-format-compliance.md` | AAAI 格式合规专项扫描 | 投稿前格式终审 |
| `review/04-aaai-double-blind.md` | AAAI 双盲合规扫描 | 投稿前 24h |
| `review/05-aaai-reproducibility.md` | AAAI Reproducibility Checklist | 投稿前 |

### 5.3 提交前 10 项速查

```
□ frenchspacing 已开启
□ 无禁用包和命令
□ 图均为 jpg/png/pdf；位图 ≥ 300 dpi，图中文字 ≥ 9pt
□ 无 overfull boxes
□ 无页码
□ Abstract 无 \cite
□ 参考文献格式正确（aaai2027.bst）
□ 若具体 event 要求：可重复性清单已按 embedded/separate 政策填写
□ Camera-ready 打包时：单 .tex 文件及 ZIP 要求已按 event/Author Kit 核对
□ 匿名投稿：PDF metadata 已清除
```

---

## 论文类型 → 专属 Guidance 路由

当论文类型确定后，以下模块会自动注入类型专属内容：

| 类型 | paper-types/ | 关键差异 |
|------|-------------|---------|
| 理论/算法型 | `theory.md` | 定理环境、证明草图、叙事钩子开场 |
| 模型/方法型 | `model-method.md` | pipeline 图、贡献列表、SOTA 表 |
| 基准/资源型 | `benchmark-resource.md` | 数据统计、评估协议、baseline 全景 |
| 应用驱动型 | `application-driven.md` | 问题建模、领域指标、案例分析 |

---

## 子模块完整索引

### 横向交叉模块（`modules/`）

| 文件 | 用途 | 加载时机 |
|------|------|---------|
| `paper-taxonomy.md` | 4 类论文分类 + 贡献形态判定 | Phase 1 |
| `outline-template.md` | 大纲模板（按类型变体） | Phase 2 |
| `distilled-patterns.md` | 获奖论文蒸馏规律库（句法/段落/图表/记忆点的**统计数据**） | Phase 3-4（全局参考） |
| `sentence-craft.md` | 句子级写作工艺：句法模板库 + Before/After 改写 + 句子节奏（**怎么写好每句话**） | Phase 3-4（写作时逐句参考） |
| `figure-design.md` | AAAI 图表设计与获奖案例 | Phase 3（Method/Experiments 写作时） |
| `caption-writing.md` | AAAI 图注/表注写作规范：解剖结构 + 句法模板 + 病灶改写（图注与表注差异化） | Phase 3-4（图表定稿时） |
| `self-review.md` | AAAI 特化自审清单（轻量版） | Phase 5 快速自查 |
| `compliance-quick.md` | 分阶段格式速查 + 内置脚本用法 | Phase 3-5（随时） |

### AAAI 特化深度审查（`modules/review/`）

| 文件 | 用途 | 加载时机 |
|------|------|---------|
| `00-aaai-master-workflow.md` | AAAI 10 维度完整审查工作流（主入口） | 投稿前 1-2 周深度审稿 |
| `01-aaai-section-review.md` | 章节级专项审查（Abstract/Intro/Method/Experiments/Conclusion 5 模块） | 每节写完后 |
| `02-aaai-red-flags.md` | AAAI Reviewer 红旗速查表（65 项，含 19 项 AAAI 新增） | 随时 Cmd+F 自查 |
| `03-aaai-format-compliance.md` | AAAI 2027 格式合规专项扫描（8 类别，替代 IEEE 格式检查） | 投稿前格式终审 |
| `04-aaai-double-blind.md` | AAAI 2027 双盲合规扫描（含 submission 模式特有检查） | 投稿前 24h |
| `05-aaai-reproducibility.md` | AAAI 2027 可重复性清单审查 | 投稿前 |

### AAAI 审稿模拟器（`modules/review-simulator/`）

| 文件 | 用途 | 加载时机 |
|------|------|---------|
| `SKILL.md` | 诊断性审稿入口 + Preflight + 4 轮工作流 | 用户要求模拟审稿时 |
| `criteria.md` | 7 个科学质量维度及四类论文证据标准 | Round 2 |
| `scoring-rubric.md` | 0–6 Overall、类型权重、coverage、门控和独立 0–5 Confidence | Round 2-4 |
| `review-workflow.md` | 证据账本、交叉核验和确定性聚合步骤 | 全程 |
| `scoring-calibration.md` | 50 篇获奖论文的非评分写作参照；不得作为录取阈值 | Round 3 |
| `review-template.md` | 含七维 scorecard、数值分和不确定性的结构化模板 | Round 4 |
| `common-qa.md` | Reviewer 常问问题库 + Rebuttal 预判 | Round 4 |
| `rules/aaai-review-scoring.json` | 机器可读权重、区间和科学门控 | Round 4 |
| `scripts/aaai_review_score.py` | 确定性评分聚合器 | Round 4 |

> **调用时机**：仅当用户说"模拟审稿"、"审这篇 paper"、"预估 review 结果"、"这篇能中 AAAI 吗"时加载。
> **与 self-review 的区别**：self-review 是"我写完了，帮我找问题"（作者视角）；review-simulator 是"如果我是 AAAI PC member，我会怎么写审稿意见"（审稿人视角）。
> **评分边界**：0–6 是内部诊断分，0–5 是当前评估的 Confidence；二者相互独立，均不是 AAAI 官方量表或录用概率。
> **强制尾注**：每份模拟审稿必须以 `Final Overall Score` 和 `Assessment Confidence` 作为最后两个非空行结束。

### 章节子 Skill（`sections/`）

| 文件 | 用途 | 加载时机 |
|------|------|---------|
| `title.md` | 标题：Title Case + 命名规律 | Phase 3 第 1 步 |
| `abstract.md` | 摘要：五步弧线 + AAAI 约束 | Phase 3 第 2 步 |
| `introduction.md` | 引言：范式→骨架→撰写 | Phase 3 第 3 步 |
| `related-work.md` | 相关工作：组织策略 + 切割话术 | Phase 3 第 4 步 |
| `method.md` | 方法：模块三元组 + 按类型变体 | Phase 3 第 5 步 |
| `experiments.md` | 实验：设计 + 表格 + 分析框架 | Phase 3 第 6 步 |
| `conclusion.md` | 结论：总结 + 局限性 + 展望 | Phase 3 第 7 步 |

### 论文类型专属（`paper-types/`）

| 文件 | 适用类型 |
|------|---------|
| `theory.md` | 理论/算法型 |
| `model-method.md` | 模型/方法型 |
| `benchmark-resource.md` | 基准/资源型 |
| `application-driven.md` | 应用驱动型 |

---

## 与现有 Skill 的协同

```
本 skill（aaai-writing）是编排层，负责：
  ├── 全程编排：大纲 → 逐节 → 打磨 → 终审
  ├── AAAI 场景聚焦：不涉及 CVPR/NeurIPS/ICML 等其他会议
  ├── 论文类型特化：4 类 × 各章节 = 精准指导
  └── 获奖论文蒸馏：50 篇 AAAI 2023-2026 获奖论文的规律提取

具体写作执行时，会引用/继承：
  ├── research-paper-writing → 全局写作方法论（三元组、reverse outlining 等）
  │     https://github.com/Master-cai/Research-Paper-Writing-Skills
  ├── paper-review → modules/self-review.md 的上游参考
  │     https://github.com/FanBroWell/AI-paper-reviewer
  ├── scripts/aaai27_check.py → Phase 5 确定性源文件预检
  │     规则源：rules/aaai27-format-rules.json
  └── aaai-paper → 规范速查（保持不变，独立使用）
```

## 执行规则

1. **按需加载**：每次只加载当前 Phase/章节需要的子模块，不提前加载全部
2. **类型注入**：Phase 1 确定论文类型后，该类型作为全局上下文贯穿后续所有步骤
3. **来源标注**：每条写作建议标注 `📄`（获奖论文实例）或 `📋`（Author Kit 规范）
4. **先大纲后动笔**：不跳过 Phase 2 直接写正文
5. **每节自查**：写完一节立即自查，不要等全文写完再回头修
6. **Claim 有据**：Phase 4 claim-evidence 映射中任何 unsupported claim 必须削弱或删除
7. **用户主导**：写作方向和风格由用户决策；本 skill 提供结构化指导和规律参考，不替用户做学术判断
8. **规则分层**：Author Kit 的通用要求、具体 event 政策和经验性写作建议必须分开标注；缺少 event 政策时输出 `NEEDS_POLICY`，缺少检查工件时输出 `NOT_CHECKED`
