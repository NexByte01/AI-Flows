# 项目容器

本目录包含项目容器。每个项目在独立的子目录中运行，拥有隔离的记忆、任务和代码。

## 工作方式

- 通过 `/incubate-project` 工作流创建新项目
- 每个项目包含：`README.md`、`AGENTS.md`、`MEMORY.md`、`memory/tasks.md`、`memory/YYYY-MM-DD.md`
- `registry.yml` 跟踪所有项目及其生命周期状态
- 默认同一时间只有一个 `building`（活跃）项目

## Registry Schema (v2)

registry 支持：

- **生命周期管理**：`building` → `paused` → `archived` → `migrated`
- **模板版本追踪**：记录创建项目时使用的模板及版本
- **跨仓库引用**：追踪外部仓库中的项目，统一状态视图

## 项目生命周期

| 状态 | 含义 |
|---|---|
| `building` | 正在开发中 |
| `paused` | 暂停，上下文保留 |
| `archived` | 不再活跃，保留参考 |
| `migrated` | 已迁移到独立仓库 |

使用 `/lifecycle` 工作流管理转换。

## 目录规范

```
projects/
├── registry.yml           # 项目索引
├── README.md              # 本文件
└── <slug>/                # 项目容器
    ├── README.md
    ├── AGENTS.md
    ├── MEMORY.md
    ├── memory/
    │   ├── tasks.md
    │   └── YYYY-MM-DD.md
    └── src/               # （或其他代码目录）
```
