---
description: Create a working branch from main following this repository's naming convention
---

# 创建功能分支

> ⚠️ 本 workflow 仅输出命令和简要说明，不替用户直接执行分支操作。

用于以下类型的问题：

- “帮我开一个功能分支”
- “这个改动应该起什么分支名”
- “按仓库规范给我分支命令”

## 使用方法

用户应提供任务主题，如 `git-workflow`、`site-refresh`、`media-upload-fix`。

## 步骤

1. 确保从 `main` 开始，且本地主分支已同步远端
```powershell
git checkout main
git pull origin main
```

2. 按任务类型创建分支
```powershell
git checkout -b feature/<name>
```

3. 推送到远程
```powershell
git push -u origin feature/<name>
```

## 分支命名规范

| 类型 | 格式 | 示例 |
|------|------|------|
| 功能开发 | `feature/<name>` | `feature/git-workflow` |
| 缺陷修复 | `fix/<name>` | `fix/media-platform-upload` |
| 文档更新 | `docs/<name>` | `docs/workflow-handbook` |
| 仓库维护 | `chore/<name>` | `chore/github-actions-cleanup` |

## 注意事项

- 任意非纯查看类改动都应新开分支
- 包括文档、workflow、技能、`site/`、`media-platform/` 等改动
- 分支统一从 `main` 创建，不使用 `develop`
- 分支名使用 kebab-case
- 完成后通过 PR 合并回 `main`

## 示例

```powershell
git checkout main
git pull origin main
git checkout -b docs/workflow-handbook
git push -u origin docs/workflow-handbook
```
