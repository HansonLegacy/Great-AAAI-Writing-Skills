# 架构设计

## 三层模块设计

```
┌─────────────────────────────────────┐
│            SKILL.md                  │
│      (编排层 — 零写作知识)            │
│      路由 / Phase 调度 / 类型注入      │
└──────────┬──────────┬───────────────┘
           │          │
    ┌──────▼───┐  ┌──▼──────────────┐
    │ sections/ │  │   paper-types/   │
    │ (纵向·按章)│  │   (类型区分层)    │
    │ 7 文件     │  │   4 文件          │
    └──────┬───┘  └──┬──────────────┘
           │          │
    ┌──────▼──────────▼──────────────┐
    │          modules/               │
    │    (横向·跨章节交叉)              │
    │    8 核心 + 6 review + 5        │
    │    review-simulator             │
    └────────────────────────────────┘
```

## 三层职责

| 层 | 目录 | 文件数 | 职责 |
|-----|------|--------|------|
| **编排层** | `SKILL.md` | 1 | 入口、Phase 调度、类型注入、上游 skill 集成 |
| **纵向层** | `sections/` | 7 | 按论文章节提供 Abstract/Intro/Method 等专属指导 |
| **横向层** | `modules/` | 8+6+5 | 跨章节的写作工艺（句子、图表、审稿、格式） |
| **类型层** | `paper-types/` | 4 | 4 种论文类型的关键差异注入 |

## 路由机制

每个模块文件末尾包含**双向交叉引用**，形成连接图：

```markdown
> **句子级模板**: `modules/sentence-craft.md` — Method 的核心句子类型：
>   - 模块动机句 → §2.4 模式 E
>   - 设计描述 → §2.4 模式 B, C
```

这使得 Claude Code 在加载当前模块时，可以自动发现并按需加载相关模块。

## 按需加载（Lazy Loading）

核心原则：**每次只加载当前 Phase/章节需要的子模块，不提前加载全部。**

- Phase 1：仅 `modules/paper-taxonomy.md`
- Phase 2：仅 `modules/outline-template.md`
- Phase 3：当前章节的 `sections/xxx.md` + `modules/sentence-craft.md`（按需）
- Phase 4：全篇一致性检查，需加载多个模块做交叉验证
- Phase 5：`modules/self-review.md`（轻量）或 `modules/review/`（深度）

## 上游 Skill 继承

```
aaai-writing（编排层）
  ├── research-paper-writing  → 通用写作方法论（reverse outlining / 三元组）
  │     https://github.com/Master-cai/Research-Paper-Writing-Skills (MIT)
  ├── paper-review + aaai-compliance-checker  → 审稿框架 + 格式合规
  │     https://github.com/FanBroWell/AI-paper-reviewer (MIT)
  └── aaai-paper              → 规范速查手册（独立使用）
```

**关键差异**：aaai-writing 不是简单拼接上游 skill，而是在上游方法论基础上叠加了：
- AAAI 2027 Author Kit 约束（7 页限制、禁用包/命令、natbib 等）
- 50 篇获奖论文的定量基准和实例
- 4 种论文类型的差异化策略

## 文件统计

| 目录 | 文件数 | 总行数 |
|------|--------|--------|
| `sections/` | 7 | ~985 |
| `modules/` (核心) | 8 | ~2,300 |
| `modules/review/` | 6 | ~1,020 |
| `modules/review-simulator/` | 5 | ~812 |
| `paper-types/` | 4 | ~317 |
| `paper-corpus/` | ~113 | (数据文件) |
| **合计** | **31 .md** | **~6,375** |
