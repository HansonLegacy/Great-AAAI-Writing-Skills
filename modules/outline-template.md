# AAAI 论文大纲模板

> 按论文类型提供可填空的章节大纲。使用方式：确定论文类型 → 套用对应模板 → 填入具体内容 → 验证页数预算。

---

## 一、通用页数预算（7 页正文）

| 章节 | 推荐页数 | 说明 |
|------|---------|------|
| Introduction | 1.0-1.5 页 | 含 teaser figure |
| Related Work | 0.5-1.0 页 | 紧凑为佳，不要喧宾夺主 |
| Method | 1.5-2.5 页 | 论文核心，按类型差异大 |
| Experiments | 2.0-3.0 页 | 主体内容；模型/方法型取上限 |
| Conclusion | 0.2-0.4 页 | 简洁收尾 |
| References | 0.5-1.0 页 | 额外不计入 7 页限制 |
| **合计正文** | **≤ 7.0 页** | |

---

## 二、类型 1: 理论/算法型大纲

```
\section{Introduction}                          [1.0-1.5 页]
  % ① 模型定义 + 目标
  % ② 已知困难 + 前人止步之处
  % ③ Core question（视觉化抛出）
  % ④ Our answer（定理级陈述 + 直觉）
  % ⑤ Contributions (3-4 bullet)

\section{Preliminaries}                         [0.5-1.0 页]
  % 模型形式化定义
  % 符号表
  % 已知结果引用

\section{Main Results}                          [2.0-3.0 页]
  \subsection{[Theorem/Result 1 Name]}
    % Theorem statement
    % Proof sketch
    % Tightness discussion
  \subsection{[Theorem/Result 2 Name]}
    % 同上

\section{[Algorithm / Construction]}（如适用）  [0.5-1.0 页]

\section{Experiments / Case Study}              [0.5-1.0 页]
  % Setup
  % Toy domain verification
  % Small benchmark（如适用）

\section{Conclusion}                            [0.2-0.3 页]
  % Summary + open questions
```

**页数分布**：Preliminaries 1 + Main Results 2.5 + Experiments 0.5 + Intro 1 + Conclusion 0.2 ≈ 5.2 页。理论型论文通常写得比页数限制短是正常的。

---

## 三、类型 2: 模型/方法型大纲

```
\section{Introduction}                          [1.0-1.5 页]
  % ① Task + application
  % ② Pain points（each with 技术原因 + 量化代价）
  % ③ (可选) Background/insight
  % ④ We propose NAME (teaser Fig. 1)
  % ⑤ Comparison + results preview
  % ⑥ Contributions (3-4 bullet)

\section{Related Work}                          [0.5-1.0 页]
  % 按技术线或任务线组织（2-4 subsection）

\section{Method}                                [1.5-2.5 页]
  \subsection{Overview}
  \subsection{[Module 1]}  % Motivation → Design → Forward → Advantage
  \subsection{[Module 2]}
  \subsection{[Module 3]}
  \subsection{Implementation Details}

\section{Experiments}                           [2.0-2.5 页]
  \subsection{Experimental Setup}
  \subsection{Main Results}
  \subsection{Ablation Study}
  \subsection{Analysis}

\section{Conclusion}                            [0.2-0.4 页]
  % Summary + Limitations + Future work

% --- 以下不计入 7 页正文 ---
% Ethical Statement（如适用）
% Acknowledgments
% References
```

**页数分布**：Intro 1.2 + Related Work 0.8 + Method 2.0 + Experiments 2.3 + Conclusion 0.3 ≈ **6.6 页**（接近上限，注意控制）。

---

## 四、类型 3: 基准/资源型大纲

```
\section{Introduction}                          [1.0-1.5 页]
  % ① Task area + 为什么需要好的数据/基准
  % ② Resource gap（现有资源的具体盲区）
  % ③ We introduce [DATASET/BENCHMARK NAME]
  % ④ Overview of construction + key statistics
  % ⑤ Contributions (3-4 bullet: 资源 + 协议 + 洞见 + 社区价值)

\section{Related Work}                          [0.5-1.0 页]
  % 已有数据集/基准 的对比
  % 该领域的代表性方法

\section{The [NAME] Dataset/Benchmark}          [2.0-3.0 页]
  \subsection{Data Collection}
  \subsection{Annotation Protocol}
  \subsection{Dataset Statistics}
  \subsection{Evaluation Protocol}

\section{Experiments}                           [1.5-2.0 页]
  \subsection{Baselines}
  \subsection{Main Results}
  \subsection{Analysis \& Key Insights}

\section{Conclusion}                            [0.3-0.5 页]
  % Summary + 资源对社区价值 + Limitations
```

**页数分布**：Intro 1.2 + Related Work 0.7 + Dataset 2.5 + Experiments 1.8 + Conclusion 0.4 ≈ **6.6 页**。

---

## 五、类型 4: 应用驱动型大纲

```
\section{Introduction}                          [1.0-1.5 页]
  % ① 应用场景（让外行理解）+ 为什么重要
  % ② Domain AI 难点
  % ③ Our AI solution
  % ④ Core design + domain motivation
  % ⑤ Contributions (3-4 bullet)

\section{Related Work}                          [0.5-0.8 页]
  % AI 方法 + 该领域已有尝试（两个 subsection 常见）

\section{Problem Formulation}                   [0.5-0.8 页]
  % 领域问题 → AI 问题的形式化
  % Notation + 约束 + 目标

\section{Method}                                [1.0-2.0 页]
  \subsection{Overview}
  \subsection{[Domain-Specific Module 1]}
  \subsection{[Domain-Specific Module 2]}
  % (可选) Integration & Deployment

\section{Experiments}                           [1.5-2.0 页]
  \subsection{Experimental Setup}
  \subsection{Main Results（领域指标 + ML 指标）}
  \subsection{Case Studies}
  \subsection{Discussion（局限性 + 真实场景考量）}

\section{Conclusion}                            [0.3-0.5 页]
  % Summary + 领域影响 + Limitations + Future
```

**页数分布**：Intro 1.2 + Related Work 0.7 + Problem Formulation 0.6 + Method 1.5 + Experiments 1.8 + Conclusion 0.4 ≈ **6.2 页**。

---

## 六、大纲生成后的验证清单

生成大纲后逐项检查：

- [ ] 正文 ≤ 7 页（各节预算加总 ≤ 7）
- [ ] Abstract（单独环境，不计入各节页数）已规划
- [ ] 每节有明确的 3-5 bullet 核心信息点
- [ ] Method 的每个 subsection 可追溯到 Intro 的贡献 bullet
- [ ] Experiments 中每个声称的贡献有对应消融/验证
- [ ] Teaser 图在第 1 页可见，Pipeline 图在 Method 开头
- [ ] Related Work 与 Method/Experiments 不抢页数——控制在 1 页以内
- [ ] Conclusion ≤ 0.5 页，不引入新信息
- [ ] 章节顺序遵守 AAAI 规范（Abstract → 正文 → Ethical Statement → Acknowledgments → References）

---

> **下一步**：大纲定稿后，按以下路由开始逐节写作：
> - 确定论文类型 → `paper-types/{theory,model-method,benchmark-resource,application-driven}.md`（类型专属策略）
> - 逐节撰写段落骨架 → `sections/{title,abstract,introduction,related-work,method,experiments,conclusion}.md`（每节按顺序加载）
> - 逐句填模板 → `modules/sentence-craft.md`（句法模板库 + Before/After 改写）
> - 全篇数据参考 → `modules/distilled-patterns.md`（获奖论文定量基准：Abstract 均值 160 词等）
