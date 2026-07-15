# 02 · AAAI 2027 Reviewer 红旗速查表

> **上游参考**：`paper-review/prompts/14_reviewer_red_flags.md`
> 本文档在原 46 项红旗基础上，新增 AAAI 2027 特有红旗（格式违规类 + AAAI reviewer 敏感词）。

---

## 🔴 Critical 级红旗（AAAI 特化版 = 通用 10 条 + AAAI 新增 8 条）

### 通用 Critical（上游保留）

**1. `we are the first to ...`**
→ reviewer 第一反应是 Google 找反例。修复：`We recast ... as ...` / `To our knowledge, no prior work has systematically investigated ...`

**2. `Obviously / Clearly / Easy to see / It is trivial that`**
→ 如果真 obvious 就不需要说；不 obvious 就是 lazy。修复：删掉，直接陈述事实。

**3. `Significantly outperforms` 但无 p-value**
→ `significant` 是统计术语。修复：有 std → `outperforms by X% (p < 0.05)`；没 std → `consistently outperforms`

**4. `State-of-the-art` 没比 latest baselines**
→ 比的是 2 年前的 SOTA？修复：列出 baseline 时间，包含近 6 个月工作。

**5. `Novel` 自评**
→ `novel` 是 reviewer 评价你，不是你自评。修复：删 `novel`，描述具体差异。

**6. `mathematical theory` / `redefine the field`**
→ 言过其实。修复：`framework` / `formulation` / `methodology`

**7. `world's largest by volume` / `world-class`**
→ marketing puffery。修复：删整个从句，数字说话。

**8. `we sincerely hope to inspire enthusiasm`**
→ 励志演讲 tone，不是学术 tone。修复：`We hope these findings motivate further investigation of ...`

**9. 自引用第一人称 `our previous work`（双盲）**
→ 直接破匿名。修复：`Prior work [X] showed ...`

**10. `Our model achieves the best performance`（无数字）**
→ "the best" 是 claim 必须有数字证据。修复：`achieves XX (+Y% over the strongest baseline)`

### AAAI 新增 Critical（格式违规类）

**A1. Abstract 中有 `\cite{...}`**
→ 🔴 **AAAI 硬性规则违反 = 格式退回**。修复：改为点名数据集/方法名（如 "RefCOCO", "GLaMM"），不加 `\cite{}`

**A2. 使用任何禁用包**
→ 🔴 **ERROR**。以 `rules/aaai27-format-rules.json` 为唯一列表；从 preamble 中移除并使用 AAAI 模板自带样式。不要把所有格式错误统一描述成 desk reject

**A3. 使用禁用命令**
→ 🔴 **ERROR 或阶段相关**。负间距、整表缩放、字号/版芯修改按规则表处理；`\newpage` / `\clearpage` / `\pagebreak` 在 camera-ready 为硬错误，anonymous 阶段还需核对具体 event。表可用 `\setlength{\tabcolsep}` 合理调列间距

**A4. 非 US Letter 纸张**
→ 🔴 **ERROR**。检查：`\documentclass[letterpaper]{article}`

**A5. 超过具体 event 的主文页限**
→ 🔴 **ERROR**。Author Kit 不给通用 “7 页”；Content Appendices 计入 event-specific 页限。未提供页限时标 `NEEDS_POLICY`

**A6. 图表格式违规**
→ 🔴 `.eps` / `.ps` / `.gif`、LaTeX 内裁剪、`minipage` 组合图、实时 `pgfplots` 和整表 `\resizebox` 均按规则处理；位图需 ≥ 300 dpi，图中文字需 ≥ 9pt

**A7. `\input` 拆分子文件**
→ 🔴 Camera-ready 包要求单 `.tex` 文件。`.bib` 必须通过 `\bibliography{...}` 引用，并不是 `\input` 例外；只有 event 要求 embedded checklist 时才允许精确的 `\input{ReproducibilityChecklist.tex}`

**A8. 出现页码**
→ 🔴 AAAI 禁止页码。检查：无 `\pagestyle`、PDF 无页眉页脚

---

## 🟠 Major 级红旗（AAAI 新增 5 条 + 通用 10 条）

### AAAI 新增 Major

**B1. 标题未用 Chicago Title Case**
→ 🟠 用 https://titlecaseconverter.com/ 验证（选 Chicago + Show explanations）

**B2. `frenchspacing` 未开启**
→ 🟠 Preamble 缺少 `\frenchspacing`

**B3. Abstract > 220 词 或 < 120 词**
→ 🟠 超出推荐范围（150-200 词）

**B4. 表注在图上方**
→ 🟠 AAAI 规则：图注/表注必须在图/表**下方**

**B5. 浮动体集中堆放在文末**
→ 🟠 浮动体优先 `[t]` / `[b]`，分布在各页

### 通用 Major（上游保留）

11-20 项与上游 `paper-review/prompts/14_reviewer_red_flags.md` 🟠 Major 部分一致：`no matter how complex`、`It is widely known` 无 cite、`Extensive experiments demonstrate`、`simple yet effective`、`intuitive / natural choice`、`as we will see in §X` 滥用、`Empirical / Theoretical results show` 模糊、`with little to no overhead`、`the proposed method` 自指、`superior performance` / `remarkable improvement`

---

## 🟡 Minor 红旗

21-30 项与上游 Minor 部分一致：`In this paper, we ...` 开头、`It is worth noting that`、`In other words` / `That is to say`、过度 `furthermore / moreover / additionally`、`outperforms baselines on most metrics`、`For each / For all` 无证据、`As shown in Figure X` 空 ref、`Notably / Interestingly / Surprisingly` 情绪词、em-dash 不一致、`the model` 指代不清

---

## 🛡️ AAAI 2027 双盲专属红旗

### 通用双盲（上游保留）
D1-D6: Personal GitHub / Acknowledgments 段 / PDF Author 字段 / LaTeX 注释 / Figure metadata / 引用集中在某 PI 的 lab

### AAAI 2027 新增双盲

**D7. 未使用 `\usepackage[submission]{aaai2027}`**
→ 🔴 必须用 submission 模式。`\usepackage{aaai2027}` 是 camera-ready 模式

**D8. `\author{}` 不是 `Anonymous Submission`**
→ 🔴 匿名投稿必须 `\author{Anonymous Submission}`，`\affiliations{}` 空

**D9. `links` 块含识别性 URL**
→ 🔴 Personal GitHub、实验室主页、机构仓库或可反查作者的重定向会破坏匿名；身份安全的匿名 code/data 链接可以保留

**D10. 写了 "Code will be released" 或代码链接**
→ 仅在链接或措辞泄露身份时为 🔴；未来发布声明本身不等于泄密，也不等于 Checklist 所说“代码已包含”

**D11. 致谢段未 placeholder 或未省略**
→ 🟠 匿名投稿不应有 `\section*{Acknowledgments}`（或内容留空占位）

**D12. Teaser 图中含机构 logo/名称/识别性信息**
→ 🟠

---

## 🌍 文化 / 语言红旗（中文母语者常踩）

L1-L10 项与上游完全一致（保留全部 10 条）：`Despite the fact that`、`the both`、`more better`、`In the meanwhile`、中文标点残留、双语并置、`we propose to xxx the yyy`、过度 `the`、漏 `the`、时态混乱

---

## 📊 红旗完整分布

```
🔴 Critical (18):  ←── 通用 10 + AAAI 新增 8
🟠 Major (15):     ←── 通用 10 + AAAI 新增 5
🟡 Minor (10):     ←── 通用（不变）
🛡️ 双盲 (12):      ←── 通用 6 + AAAI 新增 6
🌍 语言 (10):      ←── 通用（不变）
                 ━━━━
                 65 项红旗（原 46 + AAAI 新增 19）
```

---

## 💡 AAAI 投稿前 24h 必检

```
☐ 1. Abstract 内所有 citation command（含 starred 变体、`\nocite`）均为 0
☐ 2. `python scripts/aaai27_check.py ...` 的禁包/命令检查无 ERROR（不要用会扫描注释和示例文本的裸 grep 代替）
☐ 3. 断页命令已按 anonymous/camera-ready 阶段和 event 政策判断
☐ 4. 已提供并满足具体 event 页限；Content Appendices 已计入
☐ 5. PDF 无页码
☐ 6. 图均 .jpg/.png/.pdf — 无 .eps/.ps/.gif
☐ 7. frenchspacing 已开启
☐ 8. 标题 Chicago Title Case
☐ 9. \author{Anonymous Submission}, \affiliations{}
☐ 10. PDF metadata 无作者、机构等身份信息（通用 Creator/Producer 不误报）
```
