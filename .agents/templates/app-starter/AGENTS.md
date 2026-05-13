# AGENTS.md — 项目级规则

本文件定义 `{{PROJECT_NAME}}` 的项目级规则，作为根目录 `AGENTS.md` 的补充。

## 项目上下文

- 项目路径：`projects/{{PROJECT_SLUG}}/`
- 模板：`app-starter` v1.0.0
- 当前阶段：`building`

## 项目级规则

- 项目代码留在本目录 — 不要写回根目录
- 项目任务记录在 `memory/tasks.md`
- 关键决策记录在 `MEMORY.md`
- 根级规则与项目级规则冲突时，根级规则优先

## 开发约束

- 技术栈：{{TECH_STACK}}
- 目标环境：（指定：web / mobile / desktop / CLI）
- 最低浏览器支持：（如适用则指定）

## 代码风格

- 遵循项目已有的模式
- 优先组合而非继承
- 保持组件聚焦和可复用
- 按根级工作流规范编写 commit message
