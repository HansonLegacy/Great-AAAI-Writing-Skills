# Example: Theory Paper — OptimalRegret

> 虚构案例，展示 AAAI Writing Skill 为理论型论文的特化流程。
> 论文类型：**类型 1（理论/算法型）**

---

## 初始需求

```
User: 我在做在线学习（Online Learning）的 regret bound 分析。
      我给经典的 Follow-the-Regularized-Leader (FTRL) 框架提出了一个新的分析技术，
      证明了一个更紧的 regret bound（从 O(sqrt(T)) 改进到 O(sqrt(T log log T)) 的常数因子优化）。
      这在 bandit feedback 设定下成立。
```

---

## Phase 1: 定位

Claude 加载 `modules/paper-taxonomy.md`，判定为**类型 1（理论/算法型）**。

```
Claude: 你的核心贡献形式是？

User:   核心是一个新定理——我们证明了 FTRL 在 bandit 设定下的 regret bound
        可以收紧 log log T 因子。证明用了一种新的 concentration 分析技术。

Claude: 为什么之前没人证明这个更紧的 bound？

User:   之前的标准分析依赖 Azuma-Hoeffding，这在 bandit 设定下会丢失一个
        log T 因子。我们换用一种基于 self-normalized martingale 的技术来避免这个损失。

Claude: 这个结果的意义？

User:   它意味着在 bandit 设定下，FTRL 的理论保证比之前认为的更好——
        而且不需要修改算法本身。这对在线推荐、A/B 测试等场景有直接的理论指导意义。
```

**输出**：
- 论文类型：**1（理论/算法型）**
- 核心贡献：新 regret bound 证明（O(sqrt(T log log T))）+ 新分析技术
- 关键特征：仅理论贡献，实验为概念验证

---

## Phase 2: 大纲

因为是理论型，Method 结构变为 **Preliminaries + Main Results**（无传统"方法"）。

```
Title (候选):
  Sharper Regret Bounds for FTRL under Bandit Feedback via
  Self-Normalized Martingale Analysis

Abstract (理论型五步弧线):
  ① Model: We study the Follow-the-Regularized-Leader (FTRL) framework...
  ② Difficulty: Standard analysis via Azuma-Hoeffding incurs a log T factor loss...
  ③ Core Question: Can tighter regret bounds be obtained for FTRL under bandit feedback?
  ④ Answer: We prove that a self-normalized martingale analysis yields a regret bound of
     O(sqrt(T log log T)), improving the O(sqrt(T log T)) bound from prior work by a factor
     of sqrt(log T / log log T)...
  ⑤ Significance: This shows FTRL is theoretically more efficient than previously believed
     under bandit feedback, without any algorithmic modification.

章节大纲（示例假设具体 event 给出 7 页主文预算；请按目标 event 调整）:
  1. Introduction           (~1.0 页)
  2. Related Work           (~0.7 页) — Online convex optimization / Bandit feedback / FTRL
  3. Preliminaries          (~1.0 页) — Online learning setup / FTRL / Bandit feedback model
  4. Main Results           (~2.0 页) — 定理陈述 + 证明草图 + 紧致性讨论
  5. Experiments            (~0.5 页) — Synthetic bandit 模拟验证 bound 紧致性
  6. Conclusion             (~0.3 页)
  [Appendix]                (完整证明)

验证:
  - [x] 定理陈述独立可读（reviewer 从 theorem 环境即可理解结论）
  - [x] 证明直觉在正文中（完整技术细节在 Appendix）
  - [x] 理论型无需大规模实验——仅轻量验证
```

---

## Phase 3: 逐节撰写（关键差异点）

### Method（理论型的特殊结构）

理论型不用传统的"Method"写法，而是 **Preliminaries + Main Results**：

```latex
\section{Preliminaries}
\subsection{Online Convex Optimization Setup}
\subsection{Follow-the-Regularized-Leader}
\subsection{Bandit Feedback Model}

\section{Main Results}
\subsection{Self-Normalized Martingale Concentration}
% 引理 1: Self-normalized martingale bound
% 引理 2: FTRL 在 bandit 下的 regret 分解

\subsection{Improved Regret Bound for FTRL}
% 定理 1 (主定理): O(sqrt(T log log T)) bound
% 证明草图: 给出直觉，技术细节在 Appendix

\subsection{Tightness and Discussion}
% 下界讨论 / 条件能否放宽 / 与 Azuma-Hoeffding 的对比
```

**关键审查点**：
- 每个定理在正文中给出直觉解释
- 符号在 Preliminaries 中统一定义
- 证明草图让 reviewer 相信证明是对的

### Experiments（轻量验证）

仅 ~0.5 页，概念验证：
```latex
\section{Experiments}
% 在 synthetic bandit 设定下模拟，对比理论 bound 与实际 regret
% 验证 log log T 因子确实出现
```

---

## Phase 4: 整合打磨（理论型特有检查）

| 检查项 | 结果 |
|--------|------|
| 每个定理是否独立可读？ | ✅ |
| 证明直觉是否在正文中？ | ✅ |
| 理论假设是否 explicit？ | ⚠ 边界假设在 §3.1 定义了但 §4.2 用到了未显式引用的假设 |
| 与经典结果的差距是否清楚？ | ✅ §4.3 有对比讨论 |

---

## Phase 5: 合规+自审

- 数学公式字号 ≥ 6.5pt：✅
- 符号全文无重载：✅
- Abstract 无 `\cite`：✅
- 无禁用包/命令：✅

---

## 总结

理论型论文的核心差异：
1. **没有传统 Method** — 用 Preliminaries + Main Results 替代
2. **证明草图是正文核心** — reviewer 需要看到直觉，技术细节 defer 到 Appendix
3. **实验可以轻量** — AAAI 不期望理论论文有大规模实验
4. **符号系统是生命线** — 全文符号一致性检查比方法型更重要
