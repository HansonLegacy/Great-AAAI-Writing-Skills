# 4 种论文类型详解

## 类型 1: 理论/算法型

**一句话定义**：新定理、新证明、新算法、复杂度分析

**核心贡献形态**：
- 新定理 + 严格证明
- 新算法 + 复杂度分析
- 理论界（上界/下界）

**Method 结构**：
```
§ Preliminaries → § Main Results → § Algorithm → § Experiments (轻量)
```

**关键要求**：
- 定理陈述必须独立可读
- 证明草图给出直觉（完整证明可 defer 到 Appendix）
- 实验可以轻量（概念验证即可）

**AAAI 获奖实例**：Revelations (2025)

## 类型 2: 模型/方法型

**一句话定义**：新架构、新训练方法、新框架

**核心贡献形态**：
- 新网络设计 + benchmark SOTA
- 新训练策略 + 消融分析
- 新框架/系统 + 全面评估

**Method 结构**：
```
§ Overview → § Module 1 → § Module 2 → § Module 3 → § Implementation Details
```

**关键要求**：
- 每个模块 = Motivation → Design → Forward → Advantage
- Pipeline 图是最重要的图
- 实验要求最严格：SOTA 对比 + 全面消融

**AAAI 获奖实例**：LLM2CLIP (2026)

## 类型 3: 基准/资源型

**一句话定义**：新数据集、新 benchmark、系统性实证研究

**核心贡献形态**：
- 新数据集 + 全面 baseline
- 系统性评估 + 洞见
- 评估协议标准化

**Method 结构**：
```
§ Data Collection → § Annotation Protocol → § Dataset Statistics → § Evaluation Protocol
```

**关键要求**：
- 数据采集/标注流程必须透明
- Inter-annotator agreement 必报
- Baseline 覆盖必须全面

## 类型 4: 应用驱动型

**一句话定义**：AI 解决真实世界问题

**核心贡献形态**：
- 问题建模 + 领域验证
- 真实部署效果
- 社会/领域影响

**Method 结构**：
```
§ Problem Formulation → § Method (领域适配) → § Experiments (领域指标 + 案例分析)
```

**关键要求**：
- Problem Formulation 清晰（reviewer 可能不熟悉该领域）
- 每个设计决策解释"为什么对该领域必要"
- 案例/用户研究 > 纯 benchmark 数字

## 选择决策树

```
你的核心贡献是？
├── 定理/证明/算法分析 → 类型 1（理论/算法型）
├── 方法/框架/网络设计
│   ├── 核心是 benchmark SOTA → 类型 2（模型/方法型）
│   └── 核心是解决某个领域实际痛点 → 类型 4（应用驱动型）
└── 数据集/评估协议/系统性实验
    └── 类型 3（基准/资源型）
```
