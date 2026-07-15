# 5 阶段工作流详解

## 总览

```
Phase 1: 定位     → 确定论文类型 + 核心贡献形态
Phase 2: 大纲     → 生成章节大纲 + 页数预算 + story arc 验证
Phase 3: 逐节撰写  → 按顺序路由到 sections/ 子模块
Phase 4: 整合打磨  → 全篇 flow / claim-evidence 映射 / 术语一致性
Phase 5: 合规+自审 → 格式合规 + AAAI 特化自审 + 双盲检查
```

## Phase 1: 定位

**目标**：确定论文类型和核心贡献形态。

**输入**：用户的研究方向描述
**输出**：论文类型编号（1-4）+ 三个问题的答案

**步骤**：
1. 加载 `modules/paper-taxonomy.md`
2. 根据用户描述判定类型（理论/算法、模型/方法、基准/资源、应用驱动）
3. 引导用户回答三个问题：What's new? Why now? So what?

**验证点**：类型编号明确，三个问题有具体答案

## Phase 2: 大纲

**目标**：生成结构化大纲并验证完整性。

**输入**：论文类型 + 研究方向
**输出**：章节大纲 + 页数预算 + 图表计划

**步骤**：
1. 加载 `modules/outline-template.md`
2. 根据论文类型选择对应模板
3. 生成包含：章节标题、页数预算、核心信息点、Abstract 草稿
4. 验证：页数预算符合具体 event 政策、Content Appendices 已计入适用页限、story arc 完整、贡献-证据映射清晰

**验证点**：页数预算合理、所有章节有明确产出

## Phase 3: 逐节撰写

**目标**：按顺序完成 7 个章节的初稿。

**输入**：大纲 + 论文类型
**输出**：7 个章节的 LaTeX 初稿

**写作顺序**：
1. Title → 2. Abstract → 3. Introduction → 4. Related Work
→ 5. Method → 6. Experiments → 7. Conclusion

**每节纪律**：
- 只加载当前章节的 `sections/xxx.md`
- 写完立即过自查清单
- 疑难句子参考 `modules/sentence-craft.md`
- 维护跨节一致性（Abstract↔Intro, Intro↔Experiments, Method↔Ablation）

## Phase 4: 整合打磨

**目标**：全篇一致性检查。

**4 个步骤**：

### 4.1 Reverse Outlining
1. 写出每节核心论点
2. 提取每段 topic sentence
3. 验证支撑关系
4. 删除/重写无映射段落

### 4.2 Claim-Evidence 映射
对每个强 claim 标注：
- ✅ supported（有实验/表号/图号）
- ⚠️ needs evidence
- ❌ contradicted

### 4.3 术语一致性扫描
- 方法名/组件名/缩写全文一致
- 数学符号无重载
- 缩写首次出现已定义

### 4.4 图表最终检查
- Teaser 第一页可见
- 位图 ≥ 300 dpi；图中文字 ≥ 9pt
- 表用 booktabs

## Phase 5: 合规+自审

**目标**：投稿前最终防线。

**三种审查深度**：

| 深度 | 文件 | 时机 |
|------|------|------|
| 快速 | `compliance-quick.md` | 写作中随时 |
| 轻量 | `self-review.md` | Phase 5 初查 |
| 深度 | `modules/review/00-aaai-master-workflow.md` | 投稿前 1-2 周 |

**额外工具**：
- 审稿模拟器：`modules/review-simulator/SKILL.md`
- 格式自动化：运行 `python scripts/aaai27_check.py ...`；缺失工件保留 `NOT_CHECKED`
