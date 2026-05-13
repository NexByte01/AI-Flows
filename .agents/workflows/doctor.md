---
description: Health check for repo structure, memory files and project consistency
---

# 仓库健康检查

> 适用场景：
> - "检查仓库是否健康"
> - "跑一次诊断"

## 检查项

### 1. 核心文件

确认存在：`AGENTS.md`、`MEMORY.md`、`memory/tasks.md`、`projects/registry.yml`

### 2. 项目索引一致性

- `projects/registry.yml` 是有效 YAML，`schema_version` ≥ 2
- registry 中的项目在 `projects/` 下有对应目录，反之亦然
- `current_project` 指向有效的 `building` 状态项目

### 3. 适配文件同步

运行 `node scripts/sync-agents.mjs --check`

## 输出格式

```
仓库健康检查
═══════════════════════
✅ 核心文件 ............. 通过
✅ 索引一致性 ........... 通过
✅ 适配文件同步 ......... 通过

总体：健康
```

## 说明

- 此工作流只读不写
- 需要修复时创建单独 commit
