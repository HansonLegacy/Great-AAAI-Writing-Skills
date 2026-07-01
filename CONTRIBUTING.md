# Contributing to AAAI Writing Skill

感谢你的兴趣！这个项目依赖社区贡献来保持规律的准确性。

## 贡献方式

### 🐛 报告问题

如果你发现：
- 写作规律与 AAAI 2027 Author Kit 不符
- 文件之间的引用断裂（`→` 路由指向不存在的文件）
- 获奖论文实例有误
- YAML frontmatter 格式错误

请 [开 Issue](https://github.com/HansonLegacy/aaai-writing/issues/new?template=bug_report.md)。

### 💡 提议新功能

如果你有：
- 新的句法模板（在获奖论文中反复出现但本库未收录）
- 新的审稿红旗词
- 新的论文类型或细分场景

请 [开 Feature Request](https://github.com/HansonLegacy/aaai-writing/issues/new?template=feature_request.md)。

### 📄 贡献论文实例

如果你发现了 AAAI 获奖论文中的优秀写作实例：

请 [开 Paper Instance Issue](https://github.com/HansonLegacy/aaai-writing/issues/new?template=paper_type_request.md)。

### 🔧 提交 PR

1. Fork 本仓库
2. 创建你的 feature 分支：`git checkout -b feat/my-feature`
3. 做出修改
4. 确保符合贡献标准（见下）
5. Commit：`git commit -m "feat: add X template pattern"`
6. Push：`git push origin feat/my-feature`
7. 开 Pull Request

## 贡献标准

### 写作规律贡献

每条新规律必须：
- [ ] 标注来源：`📄`（获奖论文 + 具体论文名）或 `📋`（AAAI Author Kit 具体条款）
- [ ] 有具体的应用场景描述
- [ ] 与已有规律不重复（除非是对已有规律的补充）

### 句法模板贡献

每个新模板必须：
- [ ] 给出填充前/填充后示例
- [ ] 标注适用的论文类型（1-4）
- [ ] 标注适用的章节位置
- [ ] 不引用来路不明的论文

### 文件规范

- Frontmatter：每个 `.md` 文件顶部包含 `name` 和 `description` 字段
- 路由引用：文件末尾的 `→` 引用必须指向实际存在的文件
- 行宽：无硬限制，但建议 ≤ 120 字符
- 语言：写作指导和规律用中文，代码/命令用英文

## Development Setup

```bash
# 克隆
git clone https://github.com/HansonLegacy/aaai-writing.git
cd aaai-writing

# 安装 markdownlint（可选）
npm install -g markdownlint-cli

# Lint
markdownlint '**/*.md' --ignore node_modules
```

## Code of Conduct

本项目遵循 [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md)。

## 问题？

开 Discussion 或者在 Issue 中 @ 维护者。
