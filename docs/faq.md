# 常见问题

## 这和直接问 ChatGPT/Claude 有什么区别？

ChatGPT/Claude 是通用对话工具，你需要自己设计 prompt、自己管理上下文。

AAAI Writing Skill 提供了：
- **结构化的 5 阶段工作流**：不会漏步骤
- **AAAI 专有约束**：7 页限制、禁用包、natbib 格式——通用 AI 不知道这些
- **获奖论文规律**：50 篇 AAAI 获奖论文的定量基准（Abstract 160 词均值等）
- **按需加载**：只加载当前需要的模块，不会上下文爆炸

## 能写中文论文吗？

本 skill 关注的是**英文 AAAI 论文**的写作。中文论文的规范完全不同（结构、引用格式、写作习惯）。

如果你要写中文论文，本 skill 不适合——我们可能以后会做中文会议版本，但目前没有计划。

## 能用于其他会议吗（CVPR / NeurIPS / ICML）？

**不推荐。** 本 skill 的每个模块都做了 AAAI 特化：
- 格式约束是 AAAI Author Kit 2027
- 评审标准是 AAAI 审稿指南
- 获奖论文实例是 AAAI 的

如果你要写其他会议的论文，建议直接使用上游 skill：
- `research-paper-writing` — 通用写作方法论 ([GitHub](https://github.com/Master-cai/Research-Paper-Writing-Skills))
- `paper-review` — 通用审稿框架 ([GitHub](https://github.com/FanBroWell/AI-paper-reviewer))
- 然后自己叠加对应会议的 Author Kit 约束

我们以后可能会做 CVPR / NeurIPS 版本，但目前只覆盖 AAAI。

## 需要付费吗？

不需要。MIT 开源，完全免费。

## 语料库的版权问题

`modules/paper-corpus/` 包含 AAAI 获奖论文的**短摘要和片段**，用于学术写作分析。

这些属于**合理使用**范畴：
- 仅有短文摘，非全文
- 目的为学术写作研究和教育
- 不会替代原论文

如果你对某个摘录有版权顾虑，请开 Issue，我们会立即移除。

## 这个 skill 会让我一定能中 AAAI 吗？

**不会。** 本 skill 提供的是写作指导和格式约束，让你的论文在写作层面达到 AAAI 标准。但论文是否被接受取决于：
- 研究贡献的实质质量
- 实验的可信度
- 审稿人的判断

写作是必要条件，不是充分条件。但一篇写作差的论文即使贡献好也可能被拒。

## 如何贡献？

详见 [CONTRIBUTING.md](../CONTRIBUTING.md)。主要方式：
- 报告 bug（写作规律错误、引用断裂）
- 提议新模板（句法模板、审稿红旗）
- 贡献论文实例（AAAI 获奖论文的写作特征）

## 上游 Skill 没有安装怎么办？

上游 skill 是**可选依赖**。没有安装的话：
- `aaai-writing` 仍可独立运行
- 大部分模块已内置了 AAAI 特化版本，不需要上游
- 上游 skill 可从其 GitHub 仓库获取：[Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills)、[AI-paper-reviewer](https://github.com/FanBroWell/AI-paper-reviewer)

建议安装以获得最佳体验，但不是必须。

## 支持 Windows 吗？

Claude Code 支持 Windows，本 skill（纯文本 prompt 文件）也完全跨平台。

部分格式检查脚本最初是 Unix shell 语法（`grep`/`sed`），我们正在添加 PowerShell 等价命令。欢迎贡献 Windows 版本的检查脚本。
