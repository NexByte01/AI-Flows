# {{PROJECT_NAME}} 架构文档

> last_verified: {{CREATED_DATE}}

## 概览

{{PROJECT_GOAL}}

## 技术栈

| 领域 | 选型 | 备注 |
|---|---|---|
| 运行时 | {{TECH_STACK}} | |
| 工具/模型 | | |

## 系统架构

```mermaid
graph TD
    A["输入"] --> B["Agent 核心"]
    B --> C["工具调用"]
    B --> D["输出"]
    C --> E["外部服务"]
```

## 变更日志

| 日期 | 变更 | 影响 |
|---|---|---|
| {{CREATED_DATE}} | 初始化架构文档 | — |
