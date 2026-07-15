# AAAI 相关工作写作（Related Work）

> 相关工作看似是"引用列表"，实则是**叙事工具**——你选择引用谁、怎么分组、如何"切割"，决定了 reviewer 对你贡献定位的理解。

---

## 一、AAAI 写作与格式注意事项

| 约束 | 说明 |
|------|------|
| **页数规划** | Related Work 可先按 ≤ 1 页规划，再按具体 event 的主文页限缩放；这是写作预算，不是 Author Kit 硬规则 |
| **引用格式** | 文内引用 `(Author Year)`（无逗号），`natbib` 包（不可加选项） |
| **匿名投稿** | 已发表自引保留完整作者与参考文献信息，并按第三人称讨论；移除会直接识别本次投稿的措辞或非匿名资源 |
| **参考文献字号** | 由 `aaai2027.sty` 设置；如确需缩小，最多降到 `\small`（9pt），不得更小 |

---

## 二、三种组织策略

### 策略 A: 按技术线组织（最推荐）

```
\section{Related Work}

\subsection{[Task Name]}
  % 该任务的代表性方法（3-5 篇）
  % 收束到与你的方法的关系：你的方法如何不同

\subsection{[Technical Line 1 — e.g., Self-Attention Mechanisms]}
  % 该技术线的代表方法（3-5 篇）
  % 你的方法在该技术线上推进了什么

\subsection{[Technical Line 2 — e.g., Multi-Modal Fusion]}
  % 同上
```

适用：多技术贡献的论文。每个技术线对应一个 Method subsection。

### 策略 B: 按任务/领域组织

```
\section{Related Work}

\subsection{[Task A]}
\subsection{[Task B]}
\subsection{[Cross-Cutting Techniques]}
```

适用：跨任务/多 benchmark 的论文。

### 策略 C: 单节不分段

```
\section{Related Work}
  % 1-2 个自然段覆盖所有相关工作
  % 每个段落围绕一个主题，不显式分段标题
```

适用：相关工作比较集中的论文（只有一个主线）。视觉上最省空间。

---

## 三、"切割但不树敌"的话术模板

### 3.1 建桥 → 切割 → 离开

模板：
```
[某方法线] has shown promising results in [X].
  （承认贡献——不树敌）

However, these methods typically [do Y / rely on Z],
which [具体限制].
  （明确切割——我们的方法不同在何处）

In contrast, our approach [key difference].
  （离开——不再继续比较）
```

### 3.2 具体话术库

| 目的 | 句式 |
|------|------|
| 承认贡献 | `X has been widely adopted for...` / `Recent work [cite] has made significant progress in...` |
| 指出局限 | `However, these methods typically rely on..., which...` / `While effective for ..., they ...` |
| 明确切割 | `In contrast to [cite], our approach...` / `Unlike methods that..., we...` |
| 整合吸收 | `Building on insights from [cite], we...` / `We adopt the [component] from [cite] and extend it to...` |

### 3.3 避免的写法

| 病灶 | 问题 | 改法 |
|------|------|------|
| `X failed to...` | 太 aggressive | `X focused on a different setting...` |
| `X is limited because...`（没有技术理由） | 空洞批评 | 给具体技术原因 |
| 引用一大堆然后说 "None of them do what we do" | 像在 dismiss 整个领域 | 分组讨论，每组收束到你与该组的差异 |
| 完全没有引用某些明显的相关工作 | Reviewer 会认为你不知道 | 补上；如果确实不相关，用一句解释为什么 |

---

## 四、与 Method 和 Introduction 的呼应

### 4.1 Related Work → Method 的自然过渡

Related Work 的最后一句话应收束到 Method 的入口：
```
"In summary, existing methods [gap summary]. Our method addresses this by [one-sentence preview]."
```

这类似于 Introduction 段②→段④ 的过渡，但更技术化和聚焦。

### 4.2 Introduction 段② vs Related Work 的分工

| | Introduction 段② | Related Work |
|---|---|---|
| **粒度** | 宏观——2-3 个主流方向的概况 | 微观——逐类讨论具体方法 |
| **目的** | 引出**我们要解决的那个痛点** | 全景定位——我们的工作在文献地图中的位置 |
| **引用密度** | 低——每方向 1-3 篇 | 高——每子方向 3-5 篇 |

---

## 五、页数控制策略

Related Work 最容易膨胀。控制策略：

1. **引入 → 一句话评价 → 离开**：不让任何一篇论文占用 > 2 句
2. **用 `\subsection` 分组**（如果 ≥ 3 个子方向）或**单段无分段**（如果 ≤ 2 个方向）——不要介于中间
3. **不追每一个 parallel work**：只引最代表性和你做对比的
4. **Conference 版本**：Related Work 可以比 journal 版本更紧凑——点到为止

---

## 六、写完自查清单

- [ ] Related Work ≤ 1 页？
- [ ] 组织策略明确（按技术线 / 按任务 / 单段）？
- [ ] 每组的最后一句都收束到 "我们与这组的区别"？
- [ ] 没有 "X failed to..." "X is limited" 等空洞批评？
- [ ] 自引已匿名化（匿名投稿时）？
- [ ] Introduction 段② 和 Related Work 不重复（粒度不同）？
- [ ] Related Work 的最后一句话与 Method 的 Overview 有自然衔接？

---

> **句子级模板**（`modules/sentence-craft.md`）：Related Work 的核心句子类型：
> - 每组收束句 → §2.6 对比句 模式 D（"X focuses on A, while we address B"）
> - Related Work → Method 过渡 → §2.7 过渡句 模式 A（gap summary + To address this, we...）
> - 避免空洞批评 → §3 第 2 组（自评 novelty）、第 14 组（主观评价词）
> - 话术库 → 本文件 §三已提供；`sentence-craft.md` 提供更细粒度的句法模板
