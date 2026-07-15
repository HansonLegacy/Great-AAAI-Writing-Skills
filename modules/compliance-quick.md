# AAAI 2027 格式合规速查

> 本页用于写作中和提交前的快速排查。它不替代完整审计，也不自行维护禁用包、禁用命令或事件页限的副本。机器可检查规则以 `rules/aaai27-format-rules.json` 为唯一清单，完整流程见 `modules/review/03-aaai-format-compliance.md`。

## 先确定检查上下文

在检查任何规则前，先记录以下信息；不能确定时不要猜测。

| 字段 | 可选值或内容 |
| --- | --- |
| `stage` | `anonymous` / `camera-ready` / `checklist` / `final-package` |
| `event_policy` | 当前会议与 track 对页数、参考文献页、Supplement、Checklist 提交方式的官方说明 |
| `artifacts` | 主 `.tex`、`.bib`、图文件、编译 PDF、`.log`、Checklist、最终 `.zip` 中实际提供的工件 |

Author Kit **没有通用“正文 7 页”规则**。页数、参考文献是否另计、Supplement 是否允许、Checklist 是内联还是单独提交，都必须来自当前 event policy。缺少该政策时，将相关项标为 `NEEDS_POLICY`。

## 阶段速查

| 阶段 | 必查重点 |
| --- | --- |
| `anonymous` | `\usepackage[submission]{aaai2027}`；作者与机构匿名；允许位于 abstract 与正文之间且不泄露身份的 `links`；清除识别性 PDF metadata；不得出现正式 camera-ready copyright notice |
| `camera-ready` | `\usepackage{aaai2027}`；最终作者与机构完整；保留样式自动生成的 copyright slug；不得使用 `\nocopyright` |
| `checklist` | 仅替换官方 Checklist 中的 `Type your response here`；是否 `\input` 到主文档或单独编译由 event policy 决定 |
| `final-package` | 仅用于 camera-ready 打包；核查单一主 `.tex`、独立 `.bib`、实际使用的图、所需 `.aux/.bbl`、命名和 ZIP 大小 |

不要把“无页脚”作为通用标准。正确要求是：无自定义页眉、页脚和页码，同时保留 `aaai2027.sty` 针对当前阶段自动生成的合法 slug。

## 三类易混工件

| 工件 | 位置与页限 | 是否总是允许 |
| --- | --- | --- |
| **Content Appendix** | 主内容之后、Ethical Statement / Acknowledgments / References 之前；属于主论文并计入 event page limit | 可选，但仍受主论文页限与格式约束 |
| **Supplementary Material / Technical Appendix** | 可在 References 之后或作为单独文件，具体方式由 event policy 决定 | 否；缺政策时为 `NEEDS_POLICY` |
| **Reproducibility Checklist** | 可在 `\end{document}` 前 `\input`，也可独立编译 | 提交方式由 event policy 决定；它既不是 Content Appendix，也不是 Supplement |

## 快速检查清单

### 1. Preamble 与阶段

- [ ] 使用 `\documentclass[letterpaper]{article}`。
- [ ] `anonymous` 使用 `[submission]`；`camera-ready` 不使用该选项。
- [ ] 保留 Author Kit 要求的 `url`、`graphicx`、`natbib`、`caption`、`\frenchspacing` 和 `/TemplateVersion (2027.1)` 设置；不得给 `natbib` 或 `caption` 加选项。
- [ ] 禁用包和禁用命令按 `rules/aaai27-format-rules.json` 检查，而不是只搜一小组示例名称。

### 2. 源文件与分页

- [ ] 主论文没有用 `\input` / `\include` 拆分正文。
- [ ] `.bib` 通过 `\bibliography{...}` 独立提供，**不得**用 `\input` 读入。
- [ ] `ReproducibilityChecklist.tex` 只有在 event policy 允许内联时才作为 `\input` 特例。
- [ ] `\setlength{\tabcolsep}{...}` 是表格列间距的明确例外；其他改页边距、字号、行距、浮动间距的命令按规则库处理。
- [ ] `camera-ready` 不使用 `\newpage`、`\clearpage` 或 `\pagebreak`；匿名评审稿若 event policy 要求参考文献另页，按政策判定，不能套用 camera-ready 结论。

### 3. 结构与匿名性

- [ ] Abstract 不含任何引用命令或参考文献。
- [ ] 安全 `links` 块位于 abstract 之后、正文之前；匿名稿中的 URL、仓库、项目名和数据地址均不泄露身份。
- [ ] 末尾结构为：正文 → Content Appendix（可选）→ Ethical Statement（可选、无编号）→ Acknowledgments（可选、无编号）→ References；之后只有 event policy 明确允许的 Supplement 或 Checklist。
- [ ] 章节编号可选；允许编号到 subsection，subsubsection 保持不编号。

### 4. 引用与参考文献

- [ ] 文内形式为 `(Author Year)`，作者与年份之间没有逗号。
- [ ] 两位作者使用 `and`；三位作者全部列出；四位及以上使用第一作者加 `et al.`。
- [ ] 不手写 `\bibliographystyle`；由 `aaai2027.sty` 选择 `aaai2027.bst`。
- [ ] 参考文献若缩小，只能缩到 `\small`（9pt），不得更小。

### 5. 图、表与 Caption

- [ ] 图文件仅为 `.jpg`、`.png` 或 `.pdf`；无 `.gif`、`.ps`、`.eps`。
- [ ] 只有位图检查有效分辨率，纳入文档时至少 300 dpi；矢量 PDF 不使用 DPI 判定。
- [ ] 图内标签和其他文字至少 9pt；字体已嵌入，无 Type 3 字体。
- [ ] 普通图注和表注位于图/表下方，使用 10pt roman；algorithm/listing 的 header caption 按 Author Kit 特例处理。
- [ ] `\caption{...}` 内不手写 `Figure N:` 或 `Table N:`，编号由 LaTeX 生成。
- [ ] 表格正文通常 10pt，必要时可为 9pt；不得用 `\resizebox` 缩放整张表。
- [ ] 颜色对比度大于 4.5:1，且内容在灰度与常见色觉差异下仍可辨。

### 6. PDF 与政策

- [ ] PDF 为 US Letter、版本不低于 1.5、无密码、无页码和自定义页眉页脚。
- [ ] 无内容侵入页边距或栏间距；同时检查 PDF 和 `.log` 中的 overfull box。
- [ ] 匿名稿 metadata 无作者、机构、本地路径或其他识别信息；通用的 `Creator: TeX` / `Producer: pdfTeX` 本身不等于泄露身份。
- [ ] 页数、Supplement 和 Checklist 的结论均能指向当前 event policy；否则标 `NEEDS_POLICY`。

## 状态含义

| 状态 | 含义 |
| --- | --- |
| `ERROR` | 已有证据证明违反适用于当前阶段的 Author Kit 硬规则 |
| `WARNING` | Author Kit 建议项、可读性风险或需要人工复核的问题 |
| `NEEDS_POLICY` | 结论取决于当前会议/track 政策，但政策未提供或不明确 |
| `NOT_CHECKED` | 缺少所需工件，或该项只能人工检查而尚未检查 |
| `PASS` | 对应规则已用所需工件实际验证通过 |

缺 PDF 时，PDF 字体、页面、metadata 等项目必须是 `NOT_CHECKED`；缺 event policy 时，页限和 Supplement/Checklist 项必须是 `NEEDS_POLICY`。只要仍有适用项处于 `ERROR`、`NEEDS_POLICY` 或 `NOT_CHECKED`，就不得给出全局 `PASS`。

## 运行自动检查

在仓库根目录先查看脚本的当前参数，再按实际阶段和工件运行：

```bash
python scripts/aaai27_check.py --help
python scripts/aaai27_check.py paper.tex \
  --stage anonymous --pdf paper.pdf --log paper.log \
  --technical-appendix unknown --checklist unknown
```

只有取得当前 event policy 后才传 `--page-limit N`，不要把经验页数写入命令。
检查 camera-ready 最终包时使用 manuscript mode `--stage camera-ready` 并增加 `--package final.zip`。
`checklist` 和 `final-package` 是本流程的工件阶段，不是脚本 `--stage` 的额外取值。

脚本输出中的规则 ID 对应 `rules/aaai27-format-rules.json`。自动结果只能覆盖可机器判断的部分；Title Case、匿名链接是否泄露身份、图内实际字号、灰度可读性和 event policy 仍需人工复核。

## 深度审查

- 完整 stage / artifact / event-policy 审计：`modules/review/03-aaai-format-compliance.md`
- 匿名性专项：`modules/review/04-aaai-double-blind.md`
- Caption 内容质量：`modules/caption-writing.md`
