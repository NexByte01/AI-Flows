---
description: Create and manage GitHub Issues via available integrations
---

# 管理 GitHub Issue

## 创建 Issue

根据用户描述，通过可用的 GitHub 集成创建 Issue：

- `repository`：配置的仓库（来自 `MEMORY.md`）
- `title`：遵循 `[类型] 简要描述` 格式
- `labels`：根据 Issue 类型和影响范围设置
- `body`：使用对应模板

### Bug 报告模板

```markdown
## 问题描述

简要描述 Bug。

## 影响范围

- [ ] 仓库工作流 / Git 规范
- [ ] 技能资产（`.agents/skills/`）
- [ ] 项目模板（`.agents/templates/`）
- [ ] 项目代码（`projects/`）

## 复现步骤

1. 步骤一
2. 步骤二

## 预期行为

描述正确的预期行为。

## 实际行为

描述实际发生了什么。

## 日志 / 截图

如有相关输出，请粘贴在此。

## 环境信息

- 操作系统：
- 浏览器：
- Node.js 版本：
```

### 功能建议模板

```markdown
## 功能描述

简要描述需要的功能。

## 目标范围

- [ ] 仓库工作流 / Git 规范
- [ ] 技能资产（`.agents/skills/`）
- [ ] 项目模板（`.agents/templates/`）
- [ ] 项目代码（`projects/`）

## 动机

为什么需要这个功能？解决什么问题？

## 实现建议

如果有想法，描述可能的实现方式。

## 验收标准

- [ ] 标准 1
- [ ] 标准 2
```

## 查看 Issue

通过可用的 GitHub 集成：

- 获取单个 Issue 详情
- 查看 Issue 评论
- 按状态或关键词搜索 Issue

## 关闭 Issue

问题解决后，将 Issue 状态更新为 `closed`。

## 标签约定

| 标签 | 用途 |
|---|---|
| `bug` | Bug 报告 |
| `enhancement` | 功能建议 |
| `documentation` | 文档改进 |
| `workflow` | Git / GitHub Actions / 仓库流程 |
| `template` | 项目模板相关 |
| `infrastructure` | 仓库基础设施 |
