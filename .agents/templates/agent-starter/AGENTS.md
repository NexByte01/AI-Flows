# AGENTS.md — 项目级规则

本文件定义 `{{PROJECT_NAME}}` 的项目级规则，作为根目录 `AGENTS.md` 的补充。

## 项目上下文

- 项目路径：`projects/{{PROJECT_SLUG}}/`
- 模板：`agent-starter` v1.0.0
- 当前阶段：`building`

## 项目级规则

- 项目代码留在本目录 — 不要写回根目录
- 项目任务记录在 `memory/tasks.md`
- 关键决策记录在 `MEMORY.md`
- 根级规则与项目级规则冲突时，根级规则优先

## 开发约束

- 运行时：{{TECH_STACK}}
- LLM 提供商：（指定）
- Agent 框架：（如使用则指定）
- 记忆后端：（内存 / 文件 / 向量数据库）

## Agent 设计原则

- 保持 Prompt 模块化和可测试
- 为 LLM API 故障实现完善的错误处理
- 记录所有 agent 决策以便调试和改进
- 将 agent 逻辑与工具集成分离
- Prompt 模板与代码一起版本管理
