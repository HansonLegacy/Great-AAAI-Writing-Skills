# AAAI 实验写作（Experiments）

> 本文档覆盖 AAAI 论文实验部分的设计、表格规范、消融策略和分析框架。
> 按论文类型有显著差异——类型 1（理论型）的实验预期最轻，类型 2（模型/方法型）的实验负担最重。

---

## 〇、AAAI 实验的核心要求

| 要求 | 来源 |
|------|------|
| 可复现性 | AAAI 2027 Reproducibility Checklist（必须填写） |
| 统计显著性 | 期望报告 std/p-value（至少报告方差） |
| 公平比较 | 所有 baseline 用相同数据增强/预训练/评估协议 |
| 消融实验 | 每个声称的贡献点对应消融实验 |
| 超参数透明 | 搜索范围 + 选择依据 + 最终值 |

---

## 一、AAAI 实验写作结构模板

```
\section{Experiments}                          % 2-3 页

  \subsection{Experimental Setup}              % ~0.6 页
    % Datasets（任务、规模、划分、引用）
    % Baselines（为什么选这些、简要描述每个 baseline）
    % Metrics（定义 + 为什么选这些指标）
    % Implementation Details（框架、GPU、optimizer、lr、batch size、epochs、seeds）

  \subsection{Main Results}                    % ~1 页
    % 主表（SOTA 对比）
    % 每个结果段落 = What was done + What was observed + Why this matters

  \subsection{Ablation Study}                  % ~0.6 页
    % 每个声称的组件有对应消融行
    % 从完整的 NAME → 逐个移除组件的退化

  \subsection{Analysis / Discussion}           % ~0.4 页
    % 可视化、case study、超参数敏感性、局限性
```

---

## 二、按论文类型的实验差异

### 类型 1: 理论/算法型

**实验预期最低。** AAAI 不强求理论论文做大规模实验。

最少配置：
- **Toy domain 验证**：在合成数据上展示理论预测的行为
- **小型 benchmark**：1-2 个经典 benchmark 的概念验证
- 实验节标题常用 "Experiments"、"Case Study"、"Empirical Evaluation"（低调）

> 📄 **Revelations (2025)**：§5 Implementation & Experiments——单页概念验证，展示 revelation mechanism 可行。

### 类型 2: 模型/方法型

**实验预期最高。** 这是 AAAI 最常见的实验模式。

必须包含：
- **多数据集/benchmark SOTA 表**（3-5 个数据集常见）
- **消融实验**：每个 module → 一行消融结果
- **与多个 baseline 对比**（≥ 5 个，包含经典和最新）
- **定性结果/可视化**（至少 1 组）

> 📄 **LLM2CLIP (2026)**：多 benchmark 表、消融表、attention map 可视化。
> 📄 **CowClip (2023)**：核心表就是训练时间 vs 精度，简洁有力。

### 类型 3: 基准/资源型

实验的核心是 **baseline 全景覆盖**：
- **代表性 baseline**：覆盖不同方法论范式（CNN/Transformer/GNN 等）
- **数据统计**：多张数据分布图/表（论文核心内容）
- **洞察分析**：不只报数字，要分析 "why some baselines fail"
- 与已有 benchmark 对比（如果适用）

### 类型 4: 应用驱动型

实验的核心是 **真实场景验证**：
- **领域指标** + 标准 ML 指标
- **真实数据**（不仅是公开 benchmark）
- **案例分析**：挑选 3-5 个具体案例展示成功和失败模式
- **与领域专家的判断对比**（如适用）

---

## 三、表格规范（AAAI 版式约束）

### 3.1 基础要求

| 要求 | 说明 |
|------|------|
| **字号** | 10pt 正常；9pt 必要时（不得更小） |
| **包** | 推荐 `booktabs`（`\toprule`, `\midrule`, `\bottomrule`） |
| **禁用** | `\resizebox`（绝对禁止）；字号 `\tiny`（禁止） |
| **跨栏** | 单栏放不下→跨双栏（`table*`）；仍放不下→拆两表 |
| **`\setlength{\tabcolsep}`** | 允许（唯一允许的 `\setlength` 例外） |

### 3.2 SOTA 对比表模板

```latex
\begin{table}[t]
\centering
\caption{Main results on [TASK]. Best results in \textbf{bold}, second best \underline{underlined}.}
\label{tab:main}
\small  % 仅在必要时
\setlength{\tabcolsep}{4pt}  % 压缩列间距
\begin{tabular}{lcccccc}
\toprule
\multirow{2}{*}{Method} & \multicolumn{3}{c}{Dataset A} & \multicolumn{3}{c}{Dataset B} \\
                         & Metric1 & Metric2 & Metric3 & Metric1 & Metric2 & Metric3 \\
\midrule
Baseline 1 & 82.3 & 75.1 & 90.2 & 80.1 & 73.5 & 88.9 \\
Baseline 2 & 83.1 & 76.0 & 91.0 & 81.2 & 74.1 & 89.5 \\
... \\
\textbf{NAME (Ours)} & \textbf{85.7} & \textbf{78.4} & \textbf{93.1} & \textbf{83.6} & \textbf{76.8} & \textbf{91.4} \\
\bottomrule
\end{tabular}
\end{table}
```

### 3.3 消融表模板

```latex
\begin{table}[t]
\centering
\caption{Ablation study on [dataset]. Each row removes one component from the full NAME model.}
\label{tab:ablation}
\begin{tabular}{lcccc}
\toprule
Configuration & Metric1 & Metric2 & Metric3 & Δ from full \\
\midrule
Full NAME     & 85.7 & 78.4 & 93.1 & -- \\
- Module A    & 83.2 & 75.1 & 90.8 & -2.5 / -3.3 / -2.3 \\
- Module B    & 84.1 & 76.9 & 91.5 & -1.6 / -1.5 / -1.6 \\
- Module C    & 84.9 & 77.2 & 92.0 & -0.8 / -1.2 / -1.1 \\
\bottomrule
\end{tabular}
\end{table}
```

**消融表设计原则**：
- 从完整模型开始，逐行移除组件——每行退化即该组件的贡献
- 加一列 **Δ from full**（或 Δ%）让 reviewer 一目了然
- 如果模块之间有交互，加多组件同时移除的行

### 3.4 常见表格错误

| 错误 | 为什么不对 | 正确做法 |
|------|-----------|---------|
| `\resizebox{\linewidth}{!}{...}` | 导致字体不可控，且被 AAAI 禁止 | 调 `\tabcolsep` + 用缩写表头 + 拆表 |
| 表注在表上方 | AAAI 规则：表注必须在表**下方** | `\caption{}` 默认位置即可 |
| 数字不右对齐 | reviewer 无法快速比较 | 用 `l` 列放文字、`c`/`r` 列放数字 |
| 无粗体/下划线区分 | reviewer 找不到最好结果 | `\textbf{85.7}` + `\underline{84.1}` |

---

## 四、实验分析写作规范

### 4.1 每个结果段落的四要素

```
1. Setup：什么 setting（数据集/task/协议）下做这个实验
2. Result：观察到的数字/现象
3. Comparison：与谁比、差多少
4. Interpretation：为什么是这个结果（不猜测）
```

**示例**（改写自获奖论文风格）：
> "Table 1 reports the main results on ImageNet-1K. NAME achieves 85.7% top-1 accuracy, outperforming the strongest baseline Baseline-X by 1.8%. We attribute this gain to Module A, which explicitly models long-range dependencies that Baseline-X handles only implicitly."

### 4.2 避免的写法

| 病灶 | 改法 |
|------|------|
| "As shown in Table 1..." 没有解读 | 补上为什么是这个数字 + 与谁比差多少 |
| "Our method achieves SOTA performance." | 具体数字 + 点名最强对手 + 差多少 |
| "This demonstrates the effectiveness of our approach." | 说清楚**什么组件带来了什么效果** |
| 只报最好结果、不说方差 | 补 `± std` 或多次运行的统计 |

### 4.3 可视化规范

- 图注在图**下方**，10pt Roman
- 图片格式 `.jpg` / `.png` / `.pdf` 三选一
- 位图分辨率 ≥ 300 dpi；矢量 PDF 不套用 DPI 阈值
- 图内文字在最终版面中 ≥ 9pt
- 颜色可读性：灰度打印也必须可读
- 每张图在正文中被引用和讨论（不只 "see Fig. X"）

---

## 五、超参数与可复现性

### 5.1 必须报告的信息

```
[ ] GPU/硬件型号、显存大小
[ ] 框架和版本（PyTorch X.Y, CUDA X.Y）
[ ] Optimizer（Adam/AdamW/SGD...）、学习率、weight decay
[ ] Batch size、训练 epochs/iterations
[ ] 随机种子（所有实验用同样的 seeds）
[ ] 数据预处理细节（resize、normalization、augmentation）
[ ] 每个 baseline 的超参数——是复现还是用原作者发布的结果
```

### 5.2 对 Reproducibility Checklist 的对齐

若具体 event 要求提交 `ReproducibilityChecklist.tex`，实验节应为所有适用问题提供可定位的论文证据：
- [ ] 超参数搜索范围有文档
- [ ] 计算资源用量有报告（GPU 型号、数量、训练时间）
- [ ] 评估指标有精确定义
- [ ] 统计显著性测试有执行（至少方差）

---

## 六、写完自查清单

- [ ] Setup subsection 包含 datasets + baselines + metrics + implementation details？
- [ ] 主表格式正确（booktabs / 数字对齐 / 最优粗体 / 表注在下方）？
- [ ] 无 `\resizebox`、无 `\tiny`？
- [ ] 每个结果段落 = setup + result + comparison + interpretation？
- [ ] 消融实验覆盖所有声称的模块？
- [ ] 可视化位图 ≥ 300 dpi、图中文字 ≥ 9pt、灰度可读？
- [ ] 超参数信息完整（GPU/框架/optimizer/lr/batch/epochs/seeds）？
- [ ] 所有实验 claim 可追溯到对应表和行号？
- [ ] 与 Intro 中 claims 对照——每个实验 claim 都能在 Intro 中找到对应承诺？

---

> **句子级模板**（`modules/sentence-craft.md`）：Experiments 的核心句子类型：
> - 主表结果句 → §2.5 模式 A（数字+对比：NAME achieves X, outperforming BASELINE by Y）
> - 消融报告句 → §2.5 模式 C（Removing COMPONENT degrades METRIC by Δ）
> - 跨 benchmark 总结 → §2.5 模式 D（全景结果：consistent improvements across RANGE）
> - 发现与解读 → §2.5 模式 B（We find/observe that...） + 关键词强度梯度表（suggests→indicates→demonstrates→proves）
> - 与 baseline 对比 → §2.6 对比句 模式 A（直接比较）、模式 B（Trade-off）
> - 避免空洞 → §3 第 3 组（better→具体数字）、第 5 组（significant→consistently）
> - 写完后过 → §六 Experiments 句子自查（4 条）
> - **表注/图注的文字写法** → `modules/caption-writing.md`（结构、模板、病灶改写、自包含原则）
