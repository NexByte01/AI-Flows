# {{PROJECT_NAME}} 架构文档

> last_verified: {{CREATED_DATE}}

## 概览

{{PROJECT_GOAL}}

## 技术栈

| 领域 | 选型 | 备注 |
|---|---|---|
| 运行时 | {{TECH_STACK}} | |
| 框架 | | |
| 数据库 | | |

## 系统架构

```mermaid
graph TD
    A["API Gateway"] --> B["路由层"]
    B --> C["业务逻辑"]
    C --> D["数据层"]
```

## 变更日志

| 日期 | 变更 | 影响 |
|---|---|---|
| {{CREATED_DATE}} | 初始化架构文档 | — |
