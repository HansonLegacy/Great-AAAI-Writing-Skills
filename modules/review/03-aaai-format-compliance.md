# 03 · AAAI 2027 格式合规专项审查

> 本模块用于 source、PDF、Checklist 和 camera-ready 最终包的深度审查。所有机器规则及规则 ID 统一来自 `rules/aaai27-format-rules.json`；不要在本文件另建一份容易失同步的黑名单。

## 审查原则

1. **先定阶段，再套规则**：`anonymous`、`camera-ready`、`checklist`、`final-package` 不能混检。
2. **先收工件，再判通过**：缺 PDF、日志、图文件、Checklist 或 ZIP 时，对应项为 `NOT_CHECKED`，不能推断为通过。
3. **事件政策优先显式化**：Author Kit 不提供通用 7 页上限。页数、参考文献是否另计、Supplement 和 Checklist 提交方式必须来自当前会议与 track 的官方 event policy。
4. **区分硬规则与建议**：不要把可读性建议写成 desk-reject 结论，也不要给 Author Kit 未定义的违规臆测固定后果。
5. **保留样式行为**：不得修改 `aaai2027.sty` 或 `aaai2027.bst`；无自定义页眉页脚不等于删除样式自动生成的合法 slug。

## 状态模型

每条结果只能使用以下状态：

| 状态 | 使用条件 |
| --- | --- |
| `ERROR` | 有文件、行号或 PDF 证据证明违反当前阶段适用的硬规则 |
| `WARNING` | 建议项未满足、存在可读性风险，或自动检查需要人工确认 |
| `NEEDS_POLICY` | 规则取决于 event policy，但该政策缺失、过期或不明确 |
| `NOT_CHECKED` | 缺少所需工件，或尚未完成必要的人工/视觉检查 |
| `PASS` | 已取得所需工件并对该规则实际验证通过 |

全局状态不得掩盖未知项：只要存在适用的 `ERROR`、`NEEDS_POLICY` 或 `NOT_CHECKED`，报告就不能是全局 `PASS`。

## 第一步：建立审查上下文

审查开始时先输出以下清单：

```text
stage: anonymous | camera-ready | checklist | final-package
event / track: <名称>
event_policy_source: <官方页面、文件或“未提供”>
main_tex: <路径或缺失>
bib: <路径列表或缺失>
figures: <路径列表或缺失>
pdf: <路径或缺失>
log: <路径或缺失>
checklist: <路径或缺失>
package_zip: <路径或缺失>
```

### 阶段矩阵

| 检查点 | `anonymous` | `camera-ready` | `checklist` | `final-package` |
| --- | --- | --- | --- | --- |
| `aaai2027` 选项 | 必须 `[submission]` | 不得有 `submission` | standalone 时按官方 Checklist 模板 | 主文稿必须是 camera-ready |
| 作者信息 | `Anonymous Submission`，机构空 | 最终作者与机构完整 | 不单独判断 | 与 camera-ready PDF/source 一致 |
| `links` | 允许，但必须身份安全 | 允许 | 不适用 | 检查目标文件与主文一致 |
| 首页 slug | 保留样式生成的匿名审稿声明；无正式版权声明 | 保留样式生成的正式 copyright slug | 按官方模板 | 不得在打包时移除 |
| PDF metadata | 清除识别性信息 | 按最终出版要求 | 按提交方式 | source 与 PDF 一致 |
| 打包规则 | 不套用 camera-ready 打包清单 | 仅在进入最终打包时检查 | 由 event policy 决定单独或内联 | 全部适用 |

### 必须取得的 event policy

至少记录以下项目及官方来源：

- 主文页数上限与参考文献页规则；
- Content Appendix 是否影响页限（Author Kit 的默认结论是计入主论文页限）；
- 是否允许 Supplementary Material / Technical Appendix，以及内联、refs 后或单独提交的方式；
- Reproducibility Checklist 是否要求提交，以及内联还是单独提交；
- event-specific 的文件大小、命名、日期或 submission-site 要求。

任何一项没有政策证据时，返回 `NEEDS_POLICY`，不得使用“通常 7 页”等经验数字填空。

## 第二步：运行规则检查器

在仓库根目录使用仓库脚本，不再给出容易漏项的 `grep` / `Select-String` 黑名单：

```bash
python scripts/aaai27_check.py --help
python scripts/aaai27_check.py paper.tex \
  --stage anonymous --pdf paper.pdf --log paper.log \
  --technical-appendix unknown --checklist unknown
python scripts/aaai27_check.py final.tex \
  --stage camera-ready --pdf final.pdf --log final.log \
  --package final.zip --technical-appendix unknown --checklist unknown
```

脚本的 `--stage` 表示主文稿模式，因此只取 `anonymous` 或 `camera-ready`；本流程中的 `checklist` 与 `final-package` 通过相应政策参数和工件参数进入检查。
只有官方 event policy 已给出数值时才传 `--page-limit N`。`--technical-appendix` 与 `--checklist` 也必须反映已知政策；未知时显式传 `unknown`，不得猜测。
脚本输出的 `rule_id` 必须能在 `rules/aaai27-format-rules.json` 中找到；报告中保留该 ID、命中位置和证据。自动检查之后继续完成人工与视觉审查。

## 第三步：逐类人工复核

### A. Preamble 与阶段模式

匿名主稿应保留：

```latex
\documentclass[letterpaper]{article}
\usepackage[submission]{aaai2027}
\usepackage[hyphens]{url}
\usepackage{graphicx}
\urlstyle{rm}
\def\UrlFont{\rm}
\usepackage{natbib}
\usepackage{caption}
\frenchspacing
\pdfinfo{
/TemplateVersion (2027.1)
}
```

Camera-ready 仅将 `\usepackage[submission]{aaai2027}` 改为 `\usepackage{aaai2027}`。不得给 `natbib` 或 `caption` 加选项，也不得自行加载 `times`、`helvet`、`courier` 等与样式冲突的字体包。

禁用包、禁用命令及例外以 `rules/aaai27-format-rules.json` 为准。人工复核尤其注意：

- 直接或间接改变 margin、column、font、font size、line spacing、float spacing、caption spacing、heading spacing 或引用样式的宏；
- `\setlength{\tabcolsep}{...}` 是压缩表格列间距的明确例外，不代表其他 `\setlength` 合法；
- 不得用 `\resizebox` 或同类命令缩放整张表；
- 不得用负 `\vspace` / `\vskip` 挤压 caption、figure、table、section、subsection、subsubsection 或 references 周边空间；
- `\newpage`、`\clearpage`、`\pagebreak` 对 final camera-ready 是错误；匿名稿若 event policy 明确要求 review references 另页，则按政策判断，否则不要把 camera-ready 规则机械外推。

### B. 主源文件与三类附属工件

主论文的正文与自定义宏应在单一主 `.tex` 中，不用 `\input` / `\include` 拆分章节。

- `.bib` 必须作为独立文件通过 `\bibliography{...}` 使用，**不是** `\input` 例外；`\input{references.bib}` 为错误。
- `ReproducibilityChecklist.tex` 只有在 event policy 要求或允许内联时才是受控的 `\input` 例外。
- 官方 Checklist 本身含为其排版所需的命令；不要把扫描主稿的通用黑名单递归套到未经修改的官方模板部分。

三类工件必须分别判定：

| 工件 | 正确位置 | 页限 / 提交政策 |
| --- | --- | --- |
| Content Appendix | 主内容之后，Ethical Statement、Acknowledgments、References 之前 | 属于主论文并计入 event page limit |
| Supplementary Material / Technical Appendix | References 之后或单独文件 | 仅在 event policy 允许时合法；否则 `NEEDS_POLICY` 或 `ERROR` |
| Reproducibility Checklist | `\end{document}` 前内联，或独立编译 | 方式完全由 event policy 决定；不得当作前两类工件 |

主论文顺序应为：Abstract → 可选安全 `links` → 主内容 → 可选 Content Appendix → 可选未编号 Ethical Statement → 可选未编号 Acknowledgments → References。References 之后只能出现政策允许的 Supplement 或 Checklist，不得残留普通浮动体。

章节编号可选。若编号，可编号到 section 或 subsection；subsubsection 应保持不编号。不要把“subsubsection 存在”误报为错误。

### C. 标题、作者、Abstract、Links 与匿名性

- 标题使用 Chicago Title Case，不手动覆盖模板字号与布局。
- 匿名稿使用 submission 模式、匿名作者和空机构；camera-ready 使用最终作者信息。
- Abstract 使用 `abstract` 环境，不额外缩进，不得含任何引用命令或参考文献；不要只检查字面量 `\cite`。
- `links` 环境位于 abstract 之后、正文之前。匿名稿允许安全链接，但个人仓库、实验室/项目名、私有域名、带用户名的 URL 或可反推出身份的数据说明是 `ERROR`。
- “Code will be released upon publication” 这类无识别信息的陈述本身不是双盲违规。
- 不添加自定义页眉、页脚或页码；保留 `aaai2027.sty` 按阶段生成的合法 slug。

### D. 引用与参考文献

- 文内作者—年份形式为 `(Author Year)`，作者与年份之间没有逗号。
- 两位作者全部列出并用 `and`；三位作者全部列出；四位及以上使用第一作者加 `et al.`。
- 同一作者同一年使用小写字母区分，例如 `(Li 2027a)`。
- 不手写 `\bibliographystyle`；`aaai2027.sty` 自动选择 `aaai2027.bst`。
- References 位于主论文末尾相应位置，内容完整准确；如需缩小，只能将 references 降到 `\small`（9pt），不得更小。
- 禁止 `hyperref`、`navigator` 及产生嵌入链接或书签的等价方案；`links` 环境显示 URL 不等于允许 PDF 嵌入 hyperlink。

### E. 图、表、Algorithm 与 Caption

#### 图

- 文件只能是 `.jpg`、`.png` 或 `.pdf`；不得使用 `.gif`、`.ps`、`.eps`。
- 裁剪与缩放在 LaTeX 外完成，不使用 `clip`、`trim`、`viewport` 或 bounding-box 技巧。
- 不用 `minipage` 组合多图，不在 source 中加载 `pgfplots`；需要时在外部导出 PDF。
- 位图纳入文档时至少 300 dpi；矢量 PDF 不作 DPI 判定，而检查字体嵌入、Type 3 字体、线宽和实际可读性。
- 图内标签及其他文字至少 9pt；字体全部嵌入，线条不得细于 0.5pt。
- 图应靠近首次讨论、不得侵入 margin 或 gutter；结合 PDF 视觉检查和 `.log` 的 overfull box 判断。

#### 表

- 表格正文通常为 10pt，必要时可以为 9pt，不得更小。
- 不用 `\resizebox` 或其他整体缩放命令控制表格大小；可缩短表头、减少小数位、调整允许的 `\tabcolsep`、跨双栏或拆表。
- `booktabs` 是推荐项，不是缺失即违规的硬规则。

#### Caption

- 普通 figure caption 和 table caption 位于图/表下方，使用 10pt roman，不整体加粗或斜体。
- Algorithm 与 listing 是特例：caption 位于 header、左对齐并置于横线之间。
- 在 `\caption{...}` 内只写 caption 文本，**不要手写** `Figure N:` 或 `Table N:`；编号和前缀由 LaTeX 自动生成。
- Caption 是否自包含、句数和信息密度属于写作质量，不应冒充 Author Kit 格式错误。

#### 颜色

- 论文不能依赖颜色传递信息，图在灰度和常见色觉差异下仍须可辨。
- 颜色对比度必须大于 4.5:1；正文与表格采用保守策略，不用颜色装饰整句、标题或段落。

### F. PDF 视觉与技术检查

只有取得编译 PDF 后才能检查并判 `PASS`：

- US Letter、双栏、PDF 版本不低于 1.5；
- 无密码保护、嵌入链接或书签；
- 所有字体已嵌入且无 Type 3，包括图中的字体；
- 无页码和自定义页眉页脚，同时保留当前阶段的样式 slug；
- 无内容侵入页边距或栏间距，无不可接受的 overfull box；
- 匿名稿无作者、机构、用户名、本地路径或其他识别性 metadata。通用的 `Creator: TeX` 或 `Producer: pdfTeX` 本身不构成身份泄露；
- source 与 PDF 内容一致。

若只有 `.tex` 而没有 PDF，上述各项全部标 `NOT_CHECKED`，不得写“PDF 合规”。

### G. Reproducibility Checklist

Checklist 审查独立于论文格式审查：

- 使用 Author Kit 原始 `ReproducibilityChecklist.tex`；
- 只替换 `Type your response here`，不改 `\question`、选项或其他模板行；
- 每题使用该题列出的 `yes` / `partial` / `no` / `NA` 选项；
- 是否要求提交以及内联/单独方式以 event policy 为准；
- 不把 Checklist 统计成“通过率”，也不把诚实的 `no` 自动升级为格式 `ERROR`。

未提供 Checklist 时：若 policy 要求提交则为 `NOT_CHECKED`；若是否要求未知则为 `NEEDS_POLICY`；只有 policy 明确不要求时才可标不适用。

### H. Final Package（仅 camera-ready）

本节只在 `stage=final-package` 且主文稿为 camera-ready 时运行：

- 合规 PDF；
- 单一主 `.tex`，包含正文、自定义宏和 bibliography 命令；
- 独立 `.bib` 文件；不得通过 `\input` 引入 `.bib`；
- 仅包含实际使用的图；
- 出版方需要的 `.aux`、`.bbl` 等生成文件；
- 不包含未使用图、说明模板、评审材料、额外正文源文件或无关构建产物；
- ZIP 不超过 Author Kit 的 10 MB 上限；
- camera-ready 主源文件按第一作者姓命名，除非 event policy 另有说明。

不要对 `anonymous` 或单纯的 `camera-ready` 文稿审查提前套用最终 ZIP 清单；未提供 ZIP 时，final-package 项为 `NOT_CHECKED`。

## 第四步：输出审查报告

```markdown
# AAAI 2027 格式合规报告

## 审查上下文
- Stage:
- Event / track:
- Event policy source:
- 已提供工件:
- 缺失工件:

## 状态总览
| 状态 | 数量 |
| --- | ---: |
| ERROR | 0 |
| WARNING | 0 |
| NEEDS_POLICY | 0 |
| NOT_CHECKED | 0 |
| PASS | 0 |

## Findings
| Rule ID | 状态 | Stage | Artifact | 位置/证据 | 问题 | 修复或下一步 |
| --- | --- | --- | --- | --- | --- | --- |

## Event-policy 待确认项
- [政策问题] — [为什么影响结论] — [所需官方来源]

## 未检查项
- [规则/工件] — [缺少什么]

## 已验证通过项
- [Rule ID] [验证证据]

## 结论
- 仅当所有适用硬规则均实际验证、且没有 ERROR / NEEDS_POLICY / NOT_CHECKED 时写 `PASS`。
- 否则准确报告当前状态，不使用“Desk Reject”作为 Author Kit 未定义的自动后果。
```

每个 finding 必须保留 `rules/aaai27-format-rules.json` 中的 Rule ID。无法机器验证的视觉判断也要写明工件和证据，不得虚构行号、PDF 属性或 event policy。

## 与其他模块的边界

- 写作中的快速自查：`modules/compliance-quick.md`
- 双盲内容泄露专项：`modules/review/04-aaai-double-blind.md`
- Reproducibility 回答内容审查：`modules/review/05-aaai-reproducibility.md`
- Caption 的内容质量与写法：`modules/caption-writing.md`

本模块只判断 Author Kit 格式、阶段、工件和外部政策是否合规；teaser 是否在第一页、caption 应写几句、是否必须使用 `booktabs` 等写作偏好只能作为 `WARNING` 或转交相应写作模块。
