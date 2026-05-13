---
description: Manage project lifecycle transitions (building → paused → archived → migrated)
---

# 项目生命周期管理

> 适用场景：
> - "暂停当前项目"
> - "归档这个项目"
> - "将项目迁移到独立仓库"
> - "恢复暂停的项目"
> - "切换到另一个项目"

## 目标

管理 `projects/registry.yml` 中的项目状态转换，确保所有相关记忆和文档一致更新。

## 状态定义

| 状态 | 含义 | 允许的转换 |
|---|---|---|
| `building` | 正在开发中 | → `paused`、`archived`、`migrated` |
| `paused` | 暂停，上下文保留 | → `building`、`archived` |
| `archived` | 不再活跃，保留参考 | → `building`（重新启动） |
| `migrated` | 已迁移到独立仓库 | — （终态） |

## 转换工作流

### 暂停项目（`building` → `paused`）

1. 确认目标项目（通过 slug 或 `current_project`）
2. 更新 `projects/registry.yml`：
   - 设置项目状态为 `paused`
   - 设置 `updated` 为今日日期
   - 如果此项目是 `current_project`，将 `current_project` 设为 `null`
3. 在项目的 `memory/YYYY-MM-DD.md` 中记录：暂停原因
4. 在根级 `memory/YYYY-MM-DD.md` 中记录：项目已暂停
5. 如果相关任务处于进行中，更新根级 `memory/tasks.md`

### 恢复项目（`paused` → `building`）

1. 确认目标项目
2. 如果当前有另一个 `building` 状态的项目，询问用户是否先暂停它
3. 更新 `projects/registry.yml`：
   - 设置项目状态为 `building`
   - 设置 `updated` 为今日日期
   - 设为 `current_project`
4. 读取项目的 `MEMORY.md` 和 `memory/tasks.md` 恢复上下文
5. 在根级 `memory/YYYY-MM-DD.md` 中记录：项目已恢复

### 归档项目（`building`/`paused` → `archived`）

1. 确认目标项目和归档原因
2. 更新 `projects/registry.yml`：
   - 设置项目状态为 `archived`
   - 设置 `updated` 为今日日期
   - 如果此项目是 `current_project`，将 `current_project` 设为 `null`
3. 在项目的 `MEMORY.md` 中记录：归档原因和最终状态
4. 在根级 `memory/YYYY-MM-DD.md` 中记录：项目已归档

### 重新启动已归档项目（`archived` → `building`）

1. 确认目标项目
2. 按"恢复项目"的步骤执行
3. 额外验证项目结构是否完整（对其运行 `/doctor` 检查）

### 迁移项目（`building`/`paused` → `migrated`）

1. 确认目标项目和目标仓库
2. 输出迁移检查清单：
   - [ ] 创建目标仓库
   - [ ] 将项目代码从 `projects/<slug>/` 复制到新仓库
   - [ ] 在新仓库设置独立版本的 AGENTS.md 和 MEMORY.md
   - [ ] 转移项目相关的 GitHub Issue
   - [ ] 验证新仓库可正常构建/运行
   - [ ] 更新所有交叉引用
3. 迁移确认后：
   - 更新 `projects/registry.yml`：
     - 设置状态为 `migrated`
     - 添加 `migrated_to` 字段，填写新仓库地址
     - 设置 `updated` 为今日日期
   - 保留 `projects/<slug>/` 目录，放一个 `README.md` 指向新位置
   - 如果此项目是 `current_project`，将 `current_project` 设为 `null`
4. 在根级 `memory/YYYY-MM-DD.md` 中记录：项目已迁移

### 切换活跃项目

1. 确认目标项目（必须是 `building` 或 `paused` 状态）
2. 如果目标是 `paused`，先恢复它
3. 如果当前活跃项目是 `building`，可选择暂停它
4. 更新 `projects/registry.yml` 中的 `current_project`

## 跨仓库项目引用

对于在 `registry.yml` 中跟踪但托管在外部仓库的项目：

```yaml
projects:
  - slug: external-api
    name: 外部 API 服务
    type: api
    status: building
    external: true
    repository: owner/external-api-repo
    description: "托管在独立仓库的 API 服务"
    created: 2026-01-01
    updated: 2026-01-15
```

跨仓库项目：
- 没有本地 `projects/<slug>/` 目录
- 仅用于引用和状态跟踪
- 可参与生命周期转换
- 记忆和任务在外部仓库管理

## 验收标准

- `projects/registry.yml` 正确更新
- `current_project` 一致（null 或指向有效的 `building` 项目）
- 根级每日日志记录了转换
- 项目级记忆在适用时已更新
