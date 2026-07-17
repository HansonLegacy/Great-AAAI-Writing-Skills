# AAAI 模拟审稿数值评分规则

> 本文件定义本项目内部的诊断量表。`Overall Score` 不是 AAAI 官方分制、录用概率或多位真实审稿人的共识；`Confidence` 只描述当前模拟评估的依据强弱。

## 1. 三类结果必须分离

每次模拟审稿分别输出：

1. **Scientific Overall Score：0–6**，允许一位小数；
2. **Assessment Confidence：0–5**，使用整数；
3. **Compliance / Policy Status**，使用 `ERROR / WARNING / NEEDS_POLICY / NOT_CHECKED / scoped PASS`，不参与科学质量加权。

不得用高 Confidence 拉高论文分，也不得因论文分低而自动提高 Confidence。格式、匿名和 event policy 问题单独报告；只有明确的科学有效性问题可以触发 Overall 上限。

## 2. 评分前先标记信息状态

每个维度只能使用以下一种状态：

| 状态 | 含义 | 是否需要分数 |
|---|---|---:|
| `ASSESSED` | 已有足够材料评价 | 是 |
| `MISSING_IN_PAPER` | 已确认论文自身缺少必要内容 | 是；按缺陷评分 |
| `UNAVAILABLE_TO_REVIEWER` | 当前没有拿到相关章节或附件，不能断言论文缺失 | 否 |
| `NOT_APPLICABLE` | 经说明后确实不适用于该论文 | 否 |

未知信息不得填成 `0`、`3` 或默认平均值。只有论文文本本身证明某项根本失败时，才可给 `0`。

## 3. 七个科学质量维度

按 `criteria.md` 逐维评分：

| ID | 维度 |
|---|---|
| `significance` | 问题重要性与潜在价值 |
| `novelty` | 原创性与实质贡献 |
| `soundness` | 技术正确性与论证深度 |
| `evidence` | 证据与评估可信度；理论论文按证明支持、适用性或必要验证解释 |
| `clarity` | 表达、组织与可理解性 |
| `related_work` | 文献覆盖与工作定位 |
| `reproducibility` | 可复核性、透明度与必要披露 |

### 3.1 通用锚点

维度分只允许 `0, 0.5, 1.0, ... 6.0`。相邻整数之间证据混合时使用半分；禁止 `4.37` 之类的伪精确输入。

| 分数 | 证据锚点 |
|---:|---|
| 0 | 有直接证据表明该维度完全失败，核心工作无法据此评价为有效 |
| 1 | 根本性缺陷占主导，需要重做核心工作 |
| 2 | 重大缺陷明显多于优点，关键主张大部分未建立 |
| 3 | 正反证据混合，存在会影响推荐的主要问题 |
| 4 | 总体扎实，达到可接受水平，剩余问题局部且可修 |
| 5 | 很强且有说服力，只有轻微或非决定性局限 |
| 6 | 罕见的卓越水平，证据充分且无实质性保留意见 |

每个维度必须同时记录：分数、状态、至少一条证据位置、主要保留意见。分数落在半分时，解释为什么不足以进入更高整数锚点。

### 3.2 四类论文权重

这些权重是本模拟器的可版本化启发式配置，不是从 50 篇获奖论文拟合出的录取模型。

| 维度 | 理论型 | 模型方法型 | 基准资源型 | 应用驱动型 |
|---|---:|---:|---:|---:|
| Significance | 0.15 | 0.15 | 0.20 | 0.20 |
| Novelty | 0.20 | 0.20 | 0.12 | 0.15 |
| Soundness | 0.30 | 0.20 | 0.15 | 0.20 |
| Evidence | 0.10 | 0.25 | 0.25 | 0.20 |
| Clarity | 0.10 | 0.08 | 0.08 | 0.10 |
| Related Work | 0.08 | 0.07 | 0.08 | 0.07 |
| Reproducibility | 0.07 | 0.05 | 0.12 | 0.08 |

混合型或类型不确定时，分别用最可能的两个类型计算并报告 sensitivity range；不得暗中选择能得到更高分的类型。

## 4. Overall Score 计算

对已评分且适用的维度重归一化权重：

```text
Raw = sum(weight_i * score_i) / sum(weight_i for assessed applicable dimensions)
Coverage = assessed applicable weight / all applicable weight
Final = round_half_up(min(Raw, all active scientific gate caps), 1)
```

计算规则：

- `Coverage >= 0.80`：正常输出点估计；
- `0.60 <= Coverage < 0.80`：输出 `PROVISIONAL` 点估计和 plausible range；
- `Coverage < 0.60`：Overall 输出 `N/A — Insufficient information`；
- `significance`、`novelty` 或 `soundness` 任一未评分：Overall 输出 `N/A`；
- `NOT_APPLICABLE` 不进入 coverage 分母；`UNAVAILABLE_TO_REVIEWER` 进入分母但不进入分子；
- 先保留未舍入 Raw，应用门控后再用 decimal half-up 保留一位小数。

同一问题指定一个主扣分维度；其他维度只在产生独立后果时扣分，避免重复处罚。

## 5. 科学门控

门控必须显示 `id、cap、reason、evidence/location、resolution condition`。没有定位证据不得触发。

| Gate ID | Final 上限 | 触发条件 |
|---|---:|---|
| `FATAL_VALIDITY` | 1.0 | 核心定理、方法或评估存在已定位的致命无效性，主要结论整体坍塌 |
| `UNSUPPORTED_CENTRAL_CLAIM` | 2.0 | 论文的中心主张缺乏决定性支持，且不是当前材料未提供造成的未知 |
| `CORE_NOVELTY_UNESTABLISHED` | 2.5 | 与最相关工作的核心差异未建立，实质贡献无法成立 |
| `DECISIVE_EVIDENCE_MISSING` | 2.5 | 论文自身缺少其中心经验或理论主张所必需的证据 |

多个门控同时触发时取最低上限。`FORMAT_ERROR`、`ANONYMITY_RISK` 和 `EVENT_POLICY_UNKNOWN` 只进入 Compliance / Policy Status，不默认压低科学分。

## 6. 分数到推荐标签的映射

| Final Score | Recommendation |
|---:|---|
| 0.0–0.4 | Strong Reject |
| 0.5–1.4 | Reject |
| 1.5–2.4 | Weak Reject |
| 2.5–3.4 | Borderline |
| 3.5–4.4 | Weak Accept |
| 4.5–5.4 | Accept |
| 5.5–6.0 | Strong Accept |

该标签是诊断性模拟推荐，不得转换成录用概率。

## 7. Assessment Confidence：0–5

Confidence 使用三个独立整数分量相加：

| 分量 | 范围 | 锚点 |
|---|---:|---|
| `material` | 0–2 | 0=只有摘要/决定性章节不可用；1=已有主要内容但仍缺关键附件或细节；2=全文及所有决策相关材料可访问 |
| `verification` | 0–2 | 0=未做 claim-level 核验；1=已核对全文内部的核心 claim、表格、公式或证明；2=决定性主张及相关对比已在可用来源/产物中进一步核验 |
| `domain_match` | 0–1 | 0=模拟 reviewer profile 未给出或与主题匹配未知；1=显式 profile 与核心主题和方法匹配 |

```text
Confidence = material + verification + domain_match
```

材料门控：`material=0` 时 Confidence 最高为 1；`material=1` 时最高为 3。没有显式 reviewer profile 时不得声称“我是该方向专家”，`domain_match=0`。

| Confidence | Label |
|---:|---|
| 0 | No confidence |
| 1 | Very Low |
| 2 | Low |
| 3 | Medium |
| 4 | High |
| 5 | Very High |

Confidence 必须附 2–3 条依据或限制。Confidence 为 0 时，Overall 必须为 `N/A`，不能把未知解释成 0 分论文。

## 8. 确定性计算器

将维度判断写入 JSON scorecard 后运行：

```bash
python scripts/aaai_review_score.py scorecard.json --format markdown
```

规则源为 `rules/aaai-review-scoring.json`。计算器只验证、聚合、应用门控并映射标签；它不会替 reviewer 臆造维度分。输入 JSON 的字段示例和错误提示可通过：

```bash
python scripts/aaai_review_score.py --help
```

## 9. 强制 Score Footer

完整审稿报告必须以下列两个非空行结束：

```text
Final Overall Score: <x.x / 6.0 — Recommendation | N/A — Insufficient information>
Assessment Confidence: <y / 5 — Confidence label>
```

Footer 的数值和标签必须与前文一致。免责声明、解释、分隔线和 Summary for AC 均须放在 Footer 之前；Footer 之后不得输出任何内容。
