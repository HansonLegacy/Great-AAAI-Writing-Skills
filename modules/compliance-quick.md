# AAAI 格式合规速查 10 项

> 写作过程中随时自查。提交前用 `aaai-compliance-checker` skill 做完整检查。

---

## 10 项速查（按 desk-reject 风险排序）

| # | 检查项 | ✅ 通过标准 | 🔴 不通过的后果 |
|---|--------|-----------|---------------|
| 1 | **禁用包** | 无 `geometry`, `titlesec`, `authblk`, `ulem`, `float`, `fullpage`, `CJK`, `hyperref`, `times`, `setspace`, `balance` | Desk reject |
| 2 | **禁用命令** | 无 `\newpage`, `\clearpage`, `\pagebreak`, `\vspace{-`, `\vskip{-`, `\tiny`, `\resizebox`, `\linespread`, `\baselinestretch` | Desk reject |
| 3 | **纸张** | US Letter (8.5 × 11 inch) | Desk reject |
| 4 | **Preamble** | 8 项必须行全部存在（`\documentclass[letterpaper]{article}`, `\usepackage[submission]{aaai2027}`, `\usepackage[hyphens]{url}`, `\usepackage{graphicx}`, `\urlstyle{rm}`, `\def\UrlFont{\rm}`, `\usepackage{natbib}`, `\usepackage{caption}`, `\frenchspacing`, `\pdfinfo{/TemplateVersion (2027.1)}`） | 格式退回 |
| 5 | **无页码** | PDF 无页眉/页脚/页码 | 格式退回 |
| 6 | **章节顺序** | Abstract → 正文 → [Appendix] → [Ethical Statement] → [Acknowledgments] → References | 格式退回 |
| 7 | **Abstract 无引用** | 无 `\cite` 在 abstract 环境内 | 格式退回 |
| 8 | **无 `\input` 拆分** | 单 `.tex` 文件（`.bib` 和 `ReproducibilityChecklist.tex` 除外） | 提交被拒 |
| 9 | **图格式** | 仅 `.jpg` / `.png` / `.pdf`（无 `.eps`, `.ps`, `.gif`） | 编译失败 |
| 10 | **PDF metadata**（匿名投稿） | 无作者名/机构/识别性信息 | 双盲违规 |

---

## 快速检查命令

### macOS / Linux (Bash)

```bash
# 检查禁用包
grep -nE '\\(usepackage|RequirePackage)' paper.tex | grep -iE '(geometry|titlesec|authblk|ulem|float|fullpage|CJK|hyperref|times|setspace|balance)'

# 检查禁用命令
grep -nE '\\(newpage|clearpage|pagebreak|tiny|resizebox|linespread|baselinestretch|vspace\{-' paper.tex

# 检查 abstract 中是否有引用
sed -n '/begin{abstract}/,/end{abstract}/p' paper.tex | grep '\\cite'

# 检查 \input 使用
grep -n '\\input{' paper.tex | grep -v '\.bib' | grep -v 'ReproducibilityChecklist'
```

### Windows (PowerShell)

```powershell
# 检查禁用包
Select-String -Pattern '(geometry|titlesec|authblk|ulem|float|fullpage|CJK|hyperref|times|setspace|balance)' paper.tex

# 检查禁用命令
Select-String -Pattern '(newpage|clearpage|pagebreak|tiny|resizebox|linespread|baselinestretch|vspace\{-)' paper.tex

# 检查 abstract 中是否有引用
$text = Get-Content paper.tex -Raw
if ($text -match '(?s)\\begin\{abstract\}(.*?)\\end\{abstract\}') {
    if ($matches[1] -match '\\cite') { Write-Host "WARNING: citation found in abstract" }
}

# 检查 \input 使用
Select-String -Pattern '\\input\{' paper.tex | Where-Object { $_.Line -notmatch '\.bib|ReproducibilityChecklist' }
```

---

## 完整检查

写作中做速查用本文件（10 项）即可。提交前用 Skill 工具调用 `aaai-compliance-checker` 做完整的 Step 1-Step 10 检查。

---

> **深度格式审查**：速查通过后，用以下模块做投稿前格式终审：
> - 8 类别 × AAAI 2027 专项格式扫描 → `modules/review/03-aaai-format-compliance.md`
> - AAAI 双盲合规专项 → `modules/review/04-aaai-double-blind.md`（含 submission 模式特有检查）
