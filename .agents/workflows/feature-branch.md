---
description: Create a working branch following repo naming conventions
---

# 创建工作分支

## 前置条件

- 当前在 `develop` 分支上（日常开发从 develop 创建分支）
- 工作目录干净（无未提交的变更）

## 步骤

1. 确认当前状态

```bash
git branch --show-current
git status --short
```

2. 确定分支类型和名称

| 前缀 | 用途 |
|---|---|
| `feature/` | 新功能 |
| `fix/` | 修复 Bug |
| `docs/` | 文档更新 |
| `chore/` | 维护性工作 |

命名规则：
- 全小写英文
- 用连字符分隔单词：`feature/template-versioning`
- 简洁明了，体现工作内容

3. 创建并切换到分支

```bash
git checkout -b <branch-name>
```

4. 推送到远端（可选，建议在第一次提交后推送）

```bash
git push -u origin <branch-name>
```

## 示例

```bash
git checkout -b feature/lifecycle-management
git checkout -b fix/registry-schema-error
git checkout -b docs/contributing-guide
git checkout -b chore/cleanup-stale-templates
```

## 规则

- 不在 `main` 或 `develop` 上直接工作
- 一个分支对应一个逻辑变更单元
- 分支完成后通过 PR 合并到 `develop`，合并后删除分支
