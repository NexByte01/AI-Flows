# MEMORY.md — 长期记忆

## 仓库背景

- **仓库名称**：`{{REPO_FULL_NAME}}`
- **仓库类型**：AI 项目操作系统（可 fork 的模板仓库）
- **默认语言**：中文为主，英文为辅
- **创建时间**：2026-04
- **核心定位**：为开发者提供一个与 AI agent 协作孵化项目的标准化框架

## 用户偏好

- **Agent 代号**：`{{AGENT_NAME}}`
- **语言**：中文（文档、说明、模板），英文（代码、Git 规范、技术术语）
- **Git 协作模型**：`main` + `feature/*` / `fix/*` / `docs/*` / `chore/*` + PR
- **Commit 格式**：Conventional Commits（英文格式，如 `feat(templates): add version support`）
- **分支命名**：`feature/<name>`、`fix/<name>`、`docs/<name>`、`chore/<name>`

## 持久约定

- 项目孵化在 `projects/<slug>/` 下，绝不在根目录
- 默认同一时间只有一个活跃项目
- 模板在 `.agents/templates/` 下，带 `version.yml` 版本追踪
- 工作流在 `.agents/workflows/` 下，以 Markdown 编写
- 技能在 `.agents/skills/` 下，主入口为 `SKILL.md`
- 语言包在 `.agents/i18n/` 下
- `projects/registry.yml` 使用 schema v2，支持生命周期管理和跨仓库引用

## 初始化检查清单

fork 后执行 `node scripts/init.mjs`，该脚本会替换以下变量：

| 变量 | 说明 |
|---|---|
| `{{AGENT_NAME}}` | Agent 代号 |
| `{{REPO_FULL_NAME}}` | 仓库全名（如 `owner/repo`） |
| `{{PROJECT_NAME}}` | 项目名称 |
| `{{PROJECT_SLUG}}` | 项目 slug |
| `{{CREATED_DATE}}` | 创建日期 |
| `{{TECH_STACK}}` | 技术栈 |
| `{{TARGET_USERS}}` | 目标用户 |
| `{{PROJECT_GOAL}}` | 项目目标 |
