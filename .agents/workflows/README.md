# .agents/workflows

本目录包含**工作流定义**，指导 AI agent 在本仓库中执行标准化操作。

## 使用原则

- 只保留对本仓库有实际价值的工作流
- 工作流必须与当前仓库结构对齐：`AGENTS.md`、`MEMORY.md`、`memory/`、`projects/`、`.agents/templates/`、`.agents/skills/`
- Git 协作默认使用 `main + develop + feature/*`
- 调用 GitHub 能力时，使用当前会话中可用的任何 GitHub 集成

## 当前工作流

### 管理层工作流

| File | Slash Command | Description |
| --- | --- | --- |
| `commit.md` | `/commit` | Generate atomic commit commands based on git status and conversation context |
| `feature-branch.md` | `/feature-branch` | Create a working branch following repo naming conventions |
| `pr.md` | `/pr` | Create Pull Requests via available GitHub integrations |
| `issue.md` | `/issue` | Create and manage GitHub Issues via available integrations |
| `release.md` | `/release` | Pre-release readiness check before merging develop into main |
| `incubate-project.md` | `/incubate-project` | Incubate a new project under `projects/<slug>/` and initialize project-level memory |
| `lifecycle.md` | `/lifecycle` | Manage project lifecycle transitions (building → paused → archived → migrated) |
| `status.md` | `/status` | Audit repo status, summarize progress, risks and next steps |
| `doctor.md` | `/doctor` | Health check for repo structure, memory files and project consistency |
| `closeout.md` | `/closeout` | Run validation, memory, architecture, task and token budget checks at task completion |
| `memory-maintenance.md` | `/memory-maintenance` | Control local memory growth and prevent stale facts from misleading execution |

### 执行层工作流

| File | Slash Command | Description |
| --- | --- | --- |
| `task-breakdown.md` | `/task-breakdown` | Break down requirements or documents into atomic executable tasks |
| `review.md` | `/review` | Perform structured code and architecture review on project implementation |
| `gate-check.md` | `/gate-check` | Check if the current project meets stage goals and output pass/block report |
| `update-architecture.md` | `/update-architecture` | Sync project ARCHITECTURE.md after code changes |

## 维护规则

- 添加新工作流前，先检查是否有现有工作流可复用
- 如果工作流引用了仓库名、分支模型或工具名，必须与当前设置一致
- 过时内容应删除或重写，不要"以防万一"地保留
- 每个工作流必须包含 YAML frontmatter 中的 `description` 字段
