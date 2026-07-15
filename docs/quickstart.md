# 快速上手

5 分钟开始使用 AAAI Writing Skill。

## 前提条件

- 已安装 [Claude Code](https://claude.ai/code)（v2.x+）
- 如需运行内置格式检查器：Python 3.9+
- 已安装上游 skill（可选但推荐）：
  - `research-paper-writing` ([GitHub](https://github.com/Master-cai/Research-Paper-Writing-Skills))
  - `paper-review` ([GitHub](https://github.com/FanBroWell/AI-paper-reviewer))

格式检查器已随本仓库提供，不需要另行安装 `aaai-compliance-checker`。

## 安装

### Claude Code

```bash
# Linux / macOS
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git ~/.claude/skills/Great-AAAI-Writing-Skills

# Windows (PowerShell)
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git $env:USERPROFILE\.claude\skills\Great-AAAI-Writing-Skills
```

### Codex CLI (OpenAI)

```bash
# Linux / macOS
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git ~/.codex/skills/Great-AAAI-Writing-Skills

# Windows (PowerShell)
git clone https://github.com/HansonLegacy/Great-AAAI-Writing-Skills.git $env:USERPROFILE\.codex\skills\Great-AAAI-Writing-Skills
```

> 💡 **Both Claude Code and Codex CLI use the same `SKILL.md` format** — no separate setup needed. Clone once to your preferred agent's skills directory.

### 验证安装

```bash
# Claude Code
claude code skills list | grep Great-AAAI-Writing-Skills

# Codex CLI
codex skills list | grep Great-AAAI-Writing-Skills
```

## 第一个用例

在 Claude Code 对话中输入：

> 我要写一篇 AAAI 2027 论文，研究方向是[你的领域]。帮我规划大纲。

AI 会：
1. **Phase 1**：判定你的论文类型（理论/模型方法/基准资源/应用驱动）
2. **Phase 2**：生成章节大纲 + 页数预算 + 图表计划
3. 然后你可以按章节逐节撰写

## 5 个阶段

```
Phase 1: 定位     → 确定论文类型 + 核心贡献形态
Phase 2: 大纲     → 生成章节大纲 + 页数预算 + story arc 验证
Phase 3: 逐节撰写  → 按顺序写 Title → Abstract → Intro → Related Work → Method → Experiments → Conclusion
Phase 4: 整合打磨  → 全篇 flow / claim-evidence 映射 / 术语一致性
Phase 5: 合规+自审 → 格式合规 + AAAI 特化自审 + 双盲检查
```

## 4 种论文类型

| 类型 | 一句话 | 你的研究方向举例 |
|------|--------|----------------|
| 理论/算法型 | 新定理、新算法、复杂度分析 | 优化理论、算法设计 |
| 模型/方法型 | 新架构、新训练方法 | 深度学习、LLM、CV、NLP |
| 基准/资源型 | 新数据集、新 benchmark | 数据标注、实证研究 |
| 应用驱动型 | AI 解决真实问题 | 医疗 AI、教育 AI、社会影响 |

## 常用指令

```bash
# 只看大纲模板
"加载 outline-template"

# 只看句子模板
"加载 sentence-craft，我要写 Method 的模块动机句"

# 审稿自审
"模拟 AAAI 审稿，帮我审查全文"

# 格式合规检查
"做一次 AAAI 格式合规扫描"
```

## 下一步

- [架构设计](architecture.md) — 理解三层模块设计和路由机制
- [工作流详解](workflow.md) — 5 阶段完整文档
- [常见问题](faq.md)
