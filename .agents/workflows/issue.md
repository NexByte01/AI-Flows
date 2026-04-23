---
description: Create or manage issues for NexByte01/AI-Flows via the current GitHub connector
---

# 管理 GitHub Issues

## 创建 Issue

根据用户描述，使用 `mcp__codex_apps__github._create_issue` 创建 Issue：

- `repository_full_name`: `NexByte01/AI-Flows`
- `title`: 遵循格式 `[类型] 简要描述`
- `labels`: 根据问题类型和影响目录添加
- `body`: 使用以下模板

### Bug 报告模板

```markdown
## 问题描述

简要描述 Bug 现象。

## 影响范围

- [ ] 仓库工作流 / Git 规范
- [ ] 技能资产（`.agents/skills/`）
- [ ] `site/`
- [ ] `media-platform/`

## 复现步骤

1. 步骤一
2. 步骤二

## 期望行为

描述期望的正确行为。

## 实际行为

描述实际发生的情况。

## 日志 / 截图

- 如有相关输出，请粘贴在这里

## 环境信息

- 浏览器：
- 操作系统：
```

### 功能需求模板

```markdown
## 功能描述

简要描述需要的功能。

## 目标范围

- [ ] 仓库工作流 / Git 规范
- [ ] 技能资产（`.agents/skills/`）
- [ ] `site/`
- [ ] `media-platform/`

## 动机

为什么需要这个功能？解决什么问题？

## 实现建议

如有想法，描述可能的实现方案。

## 验收标准

- [ ] 标准 1
- [ ] 标准 2
```

## 查看 Issues

使用以下当前可用接口：

- `mcp__codex_apps__github._fetch_issue`：查看单个 Issue
- `mcp__codex_apps__github._fetch_issue_comments`：查看 Issue 评论
- `mcp__codex_apps__github._search_issues`：按状态、关键词搜索 Issue

## 关闭 Issue

使用 `mcp__codex_apps__github._update_issue` 关闭已解决的 Issue：
- `repository_full_name`: `NexByte01/AI-Flows`
- `state`: `closed`

## 标签约定

| 标签 | 用途 |
|------|------|
| `bug` | Bug 报告 |
| `enhancement` | 功能需求 |
| `documentation` | 文档改进 |
| `workflow` | Git / GitHub Actions / 仓库流程 |
| `site` | 静态站点相关 |
| `media-platform` | 多媒体平台相关 |
