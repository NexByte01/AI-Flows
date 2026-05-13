# AGENTS.md — 项目级规则

本文件定义 `{{PROJECT_NAME}}` 的项目级规则，作为根目录 `AGENTS.md` 的补充。

## 项目上下文

- 项目路径：`projects/{{PROJECT_SLUG}}/`
- 模板：`api-starter` v1.0.0
- 当前阶段：`building`

## 项目级规则

- 项目代码留在本目录 — 不要写回根目录
- 项目任务记录在 `memory/tasks.md`
- 关键决策记录在 `MEMORY.md`
- 根级规则与项目级规则冲突时，根级规则优先

## 开发约束

- 运行时：{{TECH_STACK}}
- API 风格：（REST / GraphQL / RPC）
- 认证方式：（JWT / API keys / OAuth）
- 数据库：（指定）

## 代码风格

- 所有端点保持一致的错误处理模式
- 使用中间件处理横切关注点（认证、日志、验证）
- 保持路由处理器精简 — 业务逻辑放在 services 层
- 为所有公开 API 端点编写测试
