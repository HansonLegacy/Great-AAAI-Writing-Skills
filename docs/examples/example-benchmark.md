# Example: Benchmark/Resource Paper — MedVQA-Bench

> 虚构案例，展示 AAAI Writing Skill 为基准/资源型论文的特化流程。
> 论文类型：**类型 3（基准/资源型）**

---

## 初始需求

```
User: 我们构建了一个医疗视觉问答（Medical VQA）的大规模基准数据集 MedVQA-Bench，
      包含 50,000 个经过专家标注的（医学图像, 问题, 答案）三元组，
      覆盖放射学、病理学、皮肤科 3 个子领域。
      
      我们发现现有的 VQA 模型在医疗领域表现很差（准确率只有 40-55%），
      而且不同模型在不同子领域上表现差异很大。
      
      我们在这个基准上评估了 12 个 SOTA VQA 模型，分析了它们的失败模式，
      给出了 5 个关键洞见。
```

---

## Phase 1: 定位

Claude 加载 `modules/paper-taxonomy.md`，判定为**类型 3（基准/资源型）**。

```
Claude: 你的核心贡献是数据集本身，还是数据+评估+洞见的组合？

User:   组合——数据集 + 12 模型全景评估 + 5 个失败模式洞见。
        单独的医疗 VQA 数据集已经有人做了，但规模小（~5K）、
        领域窄（仅放射学）、评估模型少（~3 个）。

Claude: 为什么现在需要这个基准？

User:   医疗 VQA 发展很快，但缺乏统一的评估标准。每个工作都在自己的数据集上报告，
        无法直接比较。我们需要一个像 ImageNet 之于图像分类那样的标准化基准。

Claude: 谁会关心这个基准？

User:   医疗 AI 研究者（用来评估新模型）、临床医生（了解 AI 在自己领域的能力边界）、
        VQA 方法研究者（医学图像对推理能力的要求和自然图像不同）。
```

**输出**：
- 论文类型：**3（基准/资源型）**
- 核心贡献：MedVQA-Bench = 50K 专家标注三元组 + 12 模型全景评估 + 5 洞见

---

## Phase 2: 大纲

基准型 Method = **数据构建 + 评估协议**。

```
Title (候选):
  MedVQA-Bench: A Large-Scale Multi-Domain Benchmark
  for Medical Visual Question Answering

章节大纲 (7 页预算):
  1. Introduction                 (~1.0 页)
  2. Related Work                 (~0.7 页)
  3. The MedVQA-Bench Dataset     (~2.0 页)
     3.1 Data Collection           — 来源（3 个医院 PACS 系统 + 3 个公开数据集）
     3.2 Annotation Protocol       — 标注规范 / 标注员资质 / 多轮审核
     3.3 Dataset Statistics        — 样本量 / 类别分布 / 与现有数据集对比表
     3.4 Evaluation Protocol       — 指标定义 / Train/Val/Test / Baselines 列表
  4. Experiments & Analysis        (~2.0 页)
     4.1 Baselines                 — 12 模型全景对比
     4.2 Cross-Domain Analysis     — 跨子领域泛化
     4.3 Failure Mode Analysis     — 5 个关键洞见
  5. Conclusion                    (~0.3 页)
  Ethical Statement                (~0.3 页) — 去标识化 / IRB / 数据使用协议

验证:
  - [x] 标注流程透明（inter-annotator agreement 必报）
  - [x] Baseline 覆盖 ≥ 5（实际 12 个）
  - [x] 数据统计表 + 对比表
```

---

## Phase 3: 逐节撰写（基准型关键差异点）

### Method = 数据构建 + 评估协议

这是基准型最长的章节（~2 页），重点在**构建流程的透明度**：

```latex
\section{The MedVQA-Bench Dataset}

\subsection{Data Collection}
% 数据来源：3 家医院 + 3 个公开数据集
% 纳入/排除标准
% 去标识化流程（HIPAA 合规）
% 采集时间范围：2023/01 – 2025/06

\subsection{Annotation Protocol}
% 标注规范：问题类型 = {presence, position, abnormality, comparison, diagnosis}
% 标注员资质：3 位放射科主治医师，5 年以上经验
% Inter-annotator agreement: Fleiss' κ = 0.82 (放射学) / 0.78 (病理) / 0.85 (皮肤科)
% 质量控制：两轮审核（标注员互审 → 资深医师仲裁）

\subsection{Dataset Statistics}
% 总样本 50,000 / 问题类型分布 / 答案类型分布 / 训练集 35K + 验证集 5K + 测试集 10K
% Table: 与现有医疗 VQA 数据集的全面对比

\subsection{Evaluation Protocol}
% 指标: Accuracy + BLEU + BERTScore (生成式) / Accuracy + F1 (选择式)
% 12 个 SOTA VQA baseline（含通用 VQA 模型 + 医疗专用模型）
% 公平比较规则：同数据划分 / 同预处理 / 官方代码优先
```

**自查清单重点**：
- [x] inter-annotator agreement 已报告
- [x] 数据集对比表齐全
- [x] 评估协议可复现

### Experiments（全景 baseline + 深度分析）

```latex
\section{Experiments and Analysis}

% 主结果表 (Table 2)
% ┌────────────────┬──────────┬──────────┬──────────┬──────────┐
% │ Model          │ Radiology│ Pathology│ Dermatol.│ Overall  │
% ├────────────────┼──────────┼──────────┼──────────┼──────────┤
% │ LLaVA-Med      │   52.3   │   48.7   │   55.1   │   52.0   │
% │ BiomedCLIP     │   49.8   │   45.2   │   51.3   │   48.8   │
% │ ...            │   ...    │   ...    │   ...    │   ...    │
% └────────────────┴──────────┴──────────┴──────────┴──────────┘

% 5 个关键洞见:
% 1. 所有模型的病理学表现最差——病理图像与自然图像的 domain gap 更大
% 2. 生成式模型在"诊断"类问题上严重幻觉（42% 错误率为捏造医学术语）
% 3. 医疗专用模型并不总是好于通用模型——LLaVA-1.5 在放射学上胜过 LLaVA-Med
% 4. 模型对"存在性问题"表现好（82%），但对"比较性问题"表现差（38%）
% 5. 领域预训练帮助很大的子领域差异——皮肤科受益最多（+9.2%），放射学受益最少（+2.1%）
```

---

## Phase 4: 整合打磨（基准型特有项）

| 检查项 | 结果 |
|--------|------|
| 标注员资质 + inter-annotator agreement 已报？ | ✅ |
| 数据集对比表（与现有数据集的维度对比）？ | ✅ |
| Baseline 公平性（同数据划分/同评估协议）？ | ✅ |
| 非只报有利结果——负面结果也报了（医疗专用模型不一定好于通用模型）？ | ✅ |
| 伦理声明（IRB / 去标识化 / 数据使用协议）？ | ✅ |
| 数据使用协议：Train 公开 / Test 通过 API 访问（防止测试集污染） | ⚠ 未提及 → 补充 |

---

## Phase 5: 合规+自审（基准型新增项）

- AAAI 格式合规：✅
- 伦理声明位置正确（References 前、Appendix 后）：✅
- 双盲合规：数据集标注员机构已匿名（"a tertiary hospital in [Region]"）

---

## 总结

基准/资源型论文的特有注意事项：
1. **构建流程透明度是第一要求**：数据来源、标注规范、质量控制缺一不可
2. **inter-annotator agreement 是硬指标**——AAAI reviewer 会专门找
3. **全景 baseline 而非挑选**：12 个模型、3 个子领域、含负面结果
4. **洞见 > 数字**：基准型的核心价值是"你从数据中发现了什么"，不只是"数据有多大"
5. **伦理声明不是可选的**：医疗数据必须报告 IRB 审批和去标识化流程
