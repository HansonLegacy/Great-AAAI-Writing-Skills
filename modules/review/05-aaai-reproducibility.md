# 05 · AAAI 2027 Reproducibility Checklist 审计

> **唯一规范来源**：AAAI-27 Author Kit 中的 `ReproducibilityChecklist.tex`（本补丁以工作区官方副本 `AuthorKit27/ReproducibilityChecklist.tex` 逐题核对）。若 AAAI 后续发布新版本，应重新机械比对，不能把本文件当成冻结的会议政策。
>
> 本模块只检查清单是否按官方要求填写、答案是否合法、条件分支是否一致，以及答案能否由论文或随附工件支持。它不计算“完成度”“覆盖率”或“合规分数”，也不把合法的 `no`、`partial` 自动视为必须修复的问题。

---

## 1. 先确认具体 event 的提交政策

AAAI 2027 Author Kit 提供了通用清单模板，但是否要求提交清单、以及如何提交，由具体 conference / track / event 的说明决定：

- **embedded**：按 event 要求，将 `ReproducibilityChecklist.tex` 用 `\input` 放在主文件的 `\end{document}` 之前；
- **separate**：将清单作为独立文档编译并单独提交；
- **not required**：event 明确不要求；
- **unknown**：尚未取得 event 说明。此时只能报告“政策待确认”，不能把清单缺失判为违规。

开始审计前记录：

```text
Event / track:
Policy source:
Checklist required: yes / no / unknown
Packaging: embedded / separate / unknown
```

若 event 要求 embedded，检查 `\input{ReproducibilityChecklist.tex}` 是否位于 `\end{document}` 前。若 event 要求 separate，则不要因为主论文没有该 `\input` 而报错。

---

## 2. 官方填写规则

1. 对每个**适用**问题，只替换紧随 `\question{...}{...}` 后的 `Type your response here`。
2. 不修改 `\question` 命令、问题文字、答案选项或清单中的其他行。
3. 答案必须是该问题括号中列出的一个值，大小写按模板写为 `yes`、`partial`、`no` 或 `NA`。
4. Q2.1、Q3.1、Q4.1 是 gate：只有回答 `yes` 时，其后对应分支的问题才适用。
5. gate 回答 `no` 时，不要强迫作者为不适用且没有 `NA` 选项的子问题伪造答案；审计报告应标记这些子问题为“由 gate 跳过”。
6. `no` 和 `partial` 是官方允许的披露答案，不等于格式错误。只有未填写、使用非法答案、违反 gate 逻辑，或答案与论文证据矛盾时才报告问题。

### 关于 data/code appendix 的术语边界

官方问题 Q3.3、Q4.3、Q4.4 分别使用 `data appendix`、`appendix`、`code appendix`。
这些是清单原文中的工件描述，**不能自动等同于**论文结构规则中的 `Content Appendices`，
也不能自动等同于 `Supplementary Material / Technical Appendices`。
其提交位置、是否作为主文一部分、是否单独上传，必须结合具体 event 政策判断。

“将在论文发表时公开”只回答未来公开问题 Q3.4 或 Q4.5，不能替代“当前已包含在 appendix/code appendix 中”的 Q3.3、Q4.3 或 Q4.4。

---

## 3. 官方 31 个问题的实际编号

下表按 `ReproducibilityChecklist.tex` 中 `\question` 的出现顺序编号。共 31 个问题：Q1.1–Q1.3、Q2.1–Q2.8、Q3.1–Q3.7、Q4.1–Q4.13。

### 3.1 General Paper Structure

| 编号 | 官方问题语义 | 允许答案 | 适用条件 |
| --- | --- | --- | --- |
| Q1.1 | 是否包含本文引入的 AI 方法的概念性纲要和/或伪代码描述 | `yes/partial/no/NA` | 始终检查 |
| Q1.2 | 是否清楚区分观点、假设和推测，与客观事实和结果 | `yes/no` | 始终检查 |
| Q1.3 | 是否为不熟悉该领域的读者提供明确标示的教学性参考资料，使其能获得复现论文所需的背景 | `yes/no` | 始终检查 |

### 3.2 Theoretical Contributions

| 编号 | 官方问题语义 | 允许答案 | 适用条件 |
| --- | --- | --- | --- |
| Q2.1 | 本文是否作出理论贡献 | `yes/no` | gate |
| Q2.2 | 是否清楚、正式地陈述所有假设与限制 | `yes/partial/no` | 仅当 Q2.1=`yes` |
| Q2.3 | 是否正式陈述所有新颖主张，例如写成定理 | `yes/partial/no` | 仅当 Q2.1=`yes` |
| Q2.4 | 是否包含所有新颖主张的证明 | `yes/partial/no` | 仅当 Q2.1=`yes` |
| Q2.5 | 是否为复杂和/或新颖结果给出证明草图或直觉说明 | `yes/partial/no` | 仅当 Q2.1=`yes` |
| Q2.6 | 是否适当引用所使用的理论工具 | `yes/partial/no` | 仅当 Q2.1=`yes` |
| Q2.7 | 是否通过实验证明所有理论主张成立 | `yes/partial/no/NA` | 仅当 Q2.1=`yes` |
| Q2.8 | 是否包含用于排除或证伪主张的全部实验代码 | `yes/no/NA` | 仅当 Q2.1=`yes` |

### 3.3 Dataset Usage

| 编号 | 官方问题语义 | 允许答案 | 适用条件 |
| --- | --- | --- | --- |
| Q3.1 | 本文是否依赖一个或多个数据集 | `yes/no` | gate |
| Q3.2 | 是否说明为何在所选数据集上开展实验 | `yes/partial/no/NA` | 仅当 Q3.1=`yes` |
| Q3.3 | 本文引入的所有新数据集是否已包含在 data appendix 中 | `yes/partial/no/NA` | 仅当 Q3.1=`yes` |
| Q3.4 | 本文引入的所有新数据集是否会在论文发表时公开，并采用允许免费研究使用的许可 | `yes/partial/no/NA` | 仅当 Q3.1=`yes` |
| Q3.5 | 从既有文献获得的所有数据集，包括作者自己先前发表工作中的数据集，是否附有适当引用 | `yes/no/NA` | 仅当 Q3.1=`yes` |
| Q3.6 | 从既有文献获得的所有数据集，包括作者自己先前发表工作中的数据集，是否公开可用 | `yes/partial/no/NA` | 仅当 Q3.1=`yes` |
| Q3.7 | 是否详细描述所有非公开数据集，并解释为何公开替代数据在科学上不能满足需要 | `yes/partial/no/NA` | 仅当 Q3.1=`yes` |

### 3.4 Computational Experiments

| 编号 | 官方问题语义 | 允许答案 | 适用条件 |
| --- | --- | --- | --- |
| Q4.1 | 本文是否包含计算实验 | `yes/no` | gate |
| Q4.2 | 是否报告论文开发期间每个超参数所尝试的取值数量和范围，以及选择最终参数设置的标准 | `yes/partial/no/NA` | 仅当 Q4.1=`yes` |
| Q4.3 | 数据预处理所需的任何代码是否已包含在 appendix 中 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.4 | 开展和分析实验所需的全部源代码是否已包含在 code appendix 中 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.5 | 开展和分析实验所需的全部源代码是否会在论文发表时公开，并采用允许免费研究使用的许可 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.6 | 实现新方法的全部源代码是否包含解释实现细节的注释，并引用论文中每个步骤的出处 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.7 | 若算法依赖随机性，是否充分描述设置随机种子的方法，使结果能够被复现 | `yes/partial/no/NA` | 仅当 Q4.1=`yes` |
| Q4.8 | 是否说明运行实验所用的计算基础设施，包括软硬件、GPU/CPU 型号、内存、操作系统，以及相关软件库和框架的名称与版本 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.9 | 是否正式描述所用评估指标，并解释选择这些指标的动机 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.10 | 是否说明计算每个已报告结果时使用的算法运行次数 | `yes/no` | 仅当 Q4.1=`yes` |
| Q4.11 | 实验分析是否超越平均值、中位数等单维度性能汇总，包含变异、置信度或其他分布信息 | `yes/no` | 仅当 Q4.1=`yes` |
| Q4.12 | 是否使用适当的统计检验，例如 Wilcoxon signed-rank，判断性能提升或下降的显著性 | `yes/partial/no` | 仅当 Q4.1=`yes` |
| Q4.13 | 是否列出论文实验中每个模型或算法使用的全部最终超参数 | `yes/partial/no/NA` | 仅当 Q4.1=`yes` |

---

## 4. 审计流程

### Step 1：政策与工件定位

1. 取得具体 event 的官方提交说明。
2. 记录清单是否要求，以及 packaging 是 embedded 还是 separate。
3. 找到实际提交版本的 `ReproducibilityChecklist.tex`；不要审计未提交的模板副本。
4. 若要核对答案与证据，读取论文正文以及实际随附的数据/代码工件说明。

### Step 2：逐问题解析

对每个适用问题记录：

```text
ID:
Allowed answers:
Recorded answer:
Applicable: yes / no（给出 gate 依据）
Evidence location: 论文节/页/表/附随工件，或 not found / unavailable
Consistency: consistent / contradicted / unverifiable
```

不得根据“通常做法”替作者补答案，也不得把计划中的实验、尚未上传的代码或未来公开承诺当作当前已存在的证据。

### Step 3：四类检查

1. **填写状态**
   - 适用问题仍为 `Type your response here`：报告未填写。
   - 被 gate 跳过的分支：记录为 skipped，不作为未填写错误。
2. **答案合法性**
   - 答案必须严格属于该问题的 allowed answers。
   - 例如 Q1.2 不允许 `partial` 或 `NA`；Q4.10 只允许 `yes/no`。
3. **条件分支一致性**
   - Q2.1=`yes` 时审计 Q2.2–Q2.8；Q2.1=`no` 时跳过该分支。
   - Q3.1=`yes` 时审计 Q3.2–Q3.7；Q3.1=`no` 时跳过该分支。
   - Q4.1=`yes` 时审计 Q4.2–Q4.13；Q4.1=`no` 时跳过该分支。
4. **论文证据一致性**
   - `yes` 但找不到支持材料：标记 `unverifiable`，请求作者提供位置；不要直接捏造为 `no`。
   - 答案与可见证据直接冲突：标记 `contradicted`，说明冲突位置。
   - `no` 或 `partial` 与证据一致：这是合法披露，不自动列为格式缺陷。

---

## 5. 输出格式

```markdown
# AAAI 2027 Reproducibility Checklist 审计报告

## A. Event 政策
- Event / track:
- Policy source:
- Checklist required: yes / no / unknown
- Packaging: embedded / separate / unknown
- Policy status: confirmed / unresolved

## B. 文件与包装
- Checklist file:
- Embedded input（仅在适用时）:
- Packaging finding:

## C. 填写与分支审计
| ID | Recorded answer | Allowed? | Applicable? | Gate basis | Finding |
| --- | --- | --- | --- | --- | --- |

## D. 证据一致性
| ID | Answer | Evidence location | Consistency | Note |
| --- | --- | --- | --- | --- |

## E. 需要作者处理的具体问题
### 未填写
- 仅列适用但仍为占位文本的问题。

### 非法答案
- 列出答案不属于 allowed answers 的问题。

### 分支矛盾
- 列出 gate 与子问题处理不一致之处。

### 证据矛盾或无法核验
- 区分 contradicted 与 unverifiable。

## F. 已确认无问题的项目
- 列出已检查且填写、答案、分支和证据均一致的项目。

## G. 未决信息
- 列出缺少的 event 政策、论文位置或工件，不给出推测性结论。
```

报告不得把答案汇总成比例或总分，不得与不存在的官方基准比较，也不得把合法的 `no` 当作优化目标或必修项。

---

## 6. 审计前所需输入

请提供：

1. 具体 event / track 的提交说明或其本地副本；
2. 实际提交版本的 `ReproducibilityChecklist.tex`；
3. 论文正文；
4. 若需核对 Q3.3、Q4.3、Q4.4 等问题，提供实际随附的数据/代码工件说明。

若缺少第 1 项，只能完成清单内容审计，不能判断清单缺失、内嵌或单独提交是否符合该 event 政策。
