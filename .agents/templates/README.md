# 项目模板库

本目录包含用于在 `projects/<slug>/` 下初始化新项目的版本化模板。

## 目录规范

- 路径：`.agents/templates/<template-name>/`
- 每个模板至少包含：
  - `version.yml` — 模板版本和元数据
  - `README.md` — 项目描述模板
  - `CHANGELOG.md` — 变更日志模板
  - `AGENTS.md` — 项目级 agent 规则
  - `MEMORY.md` — 项目级长期记忆
  - `docs/ARCHITECTURE.md` — 架构文档模板（含 Mermaid 图、技术栈表、变更日志）
  - `memory/tasks.md` — 任务跟踪模板
  - `memory/YYYY-MM-DD.md` — 每日日志模板
  - `memory/archive/.gitkeep` — 归档目录
  - `memory/reviews/.gitkeep` — 审查报告目录
  - `.gitignore` — 类型适配的忽略规则

## 可用模板

| 模板 | 类型 | 描述 | 版本 |
|---|---|---|---|
| `app-starter` | App | 通用应用、SaaS、工具类产品 | 1.0.0 |
| `api-starter` | API | REST/GraphQL API、后端服务 | 1.0.0 |
| `website-starter` | Website | 落地页、文档站、企业官网 | 1.0.0 |
| `agent-starter` | Agent | AI agent、工作流、自动化系统 | 1.0.0 |

## 版本管理

每个模板的 `version.yml` 包含：

```yaml
version: "1.0.0"
type: app
description: "模板描述"
updated: "2026-01-01"
```

使用模板创建项目时，版本号会记录在 `projects/registry.yml` 中，便于追溯。

## 使用规则

- 模板是起点，不是最终项目结构
- 复制模板后，替换所有 `{{PLACEHOLDER}}` 变量为实际值
- 如果没有完全匹配的模板，从最接近的开始调整
- 模板中不允许硬编码品牌名、仓库地址或过时内容
- 模板升级应递增版本号
