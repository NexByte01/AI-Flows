---
description: Create Pull Requests via available GitHub integrations
---

# 创建 Pull Request

## 前置条件

- 工作分支的所有提交已推送到远端
- 确认目标分支（通常为 `develop`，发布时为 `main`）
- 变更内容、验证方式和记忆文件更新已审查

## 步骤

1. 确认当前分支和待合并的提交

```bash
git branch --show-current
git log --oneline origin/main..HEAD
```

2. 通过可用的 GitHub 集成创建 PR

参数：
- `repository`：配置的仓库（来自 `MEMORY.md`）
- `title`：遵循 `<type>(<scope>): <description>` 格式
- `head`：当前工作分支名
- `base`：`develop`（发布 PR 用 `main`）
- `body`：使用下方模板

```markdown
## 变更内容

- 变更 1
- 变更 2

## 影响范围

- [ ] `projects/`
- [ ] `.github/workflows/`
- [ ] `.agents/templates/`
- [ ] `.agents/skills/`
- [ ] `.agents/workflows/`
- [ ] 记忆文件（`AGENTS.md` / `MEMORY.md` / `memory/`）

## 测试方式

- [ ] 静态文件变更已手动审查
- [ ] 代码变更已通过语法/类型检查
- [ ] 工作流变更已通过静态审查或 YAML 检查
- [ ] 无需额外测试（说明原因）

## 记忆与文档

- [ ] 已更新 `memory/YYYY-MM-DD.md`
- [ ] 已更新 `projects/registry.yml`（如果项目状态变化）
- [ ] 无需更新记忆文件（说明原因）

## 补充说明

- 相关 Issue：
- 风险点：
- 截图或日志（如有）：
```

3. 创建成功后输出 PR 链接

## PR 规则

- 日常变更走 `feature/*`、`fix/*`、`docs/*`、`chore/*` → `develop`
- 发布时走 `develop` → `main`
- 如果用户要求 PR 副本，使用上方模板输出完整 body
- 仓库支持工作分支推送时自动创建 Draft PR；也支持手动创建
- 当 PR 状态为 `Ready for review` 且仓库设置允许时，自动化将尝试启用 auto-merge
