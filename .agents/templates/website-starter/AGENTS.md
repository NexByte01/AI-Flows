# AGENTS.md — 项目级规则

本文件定义 `{{PROJECT_NAME}}` 的项目级规则，作为根目录 `AGENTS.md` 的补充。

## 项目上下文

- 项目路径：`projects/{{PROJECT_SLUG}}/`
- 模板：`website-starter` v1.0.0
- 当前阶段：`building`

## 项目级规则

- 项目代码留在本目录 — 不要写回根目录
- 项目任务记录在 `memory/tasks.md`
- 关键决策记录在 `MEMORY.md`
- 根级规则与项目级规则冲突时，根级规则优先

## 开发约束

- 框架：{{TECH_STACK}}
- 目标：静态站 / SSR / SSG
- SEO：必需 — 所有页面必须有正确的 meta 标签
- 性能：Core Web Vitals 应通过

## 设计原则

- 移动优先的响应式设计
- 可访问性（WCAG 2.1 AA 最低要求）
- 快速加载 — 优化图片，最小化 JS
- 一致的排版和间距系统
