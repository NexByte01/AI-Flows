# .agents/workflows

本目录保存 **项目级工作流说明**，用于指导 Nex / Codex 在 `NexByte01/AI-Flows` 中按统一方式处理 Git、GitHub 协作、状态汇报和发布检查。

它承担两类职责：

- **AI 操作手册**：告诉助手在这个仓库里应该遵循什么流程
- **半自动模板**：在用户要求生成命令、PR 文案、Issue 内容、状态总结时提供统一模板

## 使用原则

- 只保留当前仓库明确有用的工作流，不保留其他项目的历史残留
- 工作流必须适配当前仓库结构：`AGENTS.md`、`MEMORY.md`、`memory/`、`.agents/skills/`、`site/`、`media-platform/`
- Git 协作默认采用 `main + feature/* + PR`
- 需要调用 GitHub 能力时，统一使用当前会话可用的 `mcp__codex_apps__github.*`

## 当前文件

| 文件 | 作用 |
|---|---|
| `commit.md` | 根据 `git status` 和对话上下文生成原子提交命令 |
| `feature-branch.md` | 按仓库规范创建工作分支 |
| `pr.md` | 生成 PR 说明并约束 PR 检查项 |
| `issue.md` | 通过 GitHub 连接器创建和管理本仓库 Issue |
| `status.md` | 汇总当前仓库阶段、风险与下一步 |
| `release.md` | 做仓库级发布/上线前检查 |

## 维护要求

- 新增工作流前，先确认当前目录中是否已有同类文件可复用
- 如果工作流引用了仓库名、分支模型、工具名，必须与当前仓库一致
- 发现过期内容应优先删除或重写，不保留“未来可能会用”的旧项目说明
