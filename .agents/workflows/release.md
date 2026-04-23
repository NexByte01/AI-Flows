---
description: Run release-readiness checks for NexByte01/AI-Flows without assuming a develop branch
---

# 发布前检查

用于以下类型的问题：

- “这个仓库现在适合发布/提交到主分支吗”
- “上线前还要检查什么”
- “帮我看一下 Pages 和子项目说明是否齐”

## 核心原则

- 本仓库默认只有 `main` 和工作分支，不使用 `develop`
- 发布检查以“仓库协作完整性”为主，不假设统一构建流水线
- 优先检查 GitHub Pages、子项目说明、记忆文件和 GitHub Actions

## 检查清单

### 1. 仓库级检查

- `AGENTS.md`、`MEMORY.md`、`memory/tasks.md` 是否仍与当前工作方式一致
- 当天重要改动是否已记录到 `memory/YYYY-MM-DD.md`
- `.gitignore` 是否覆盖本地缓存、环境变量和运行产物
- `.github/workflows/` 是否只保留当前仓库实际使用的工作流

### 2. `site/` 检查

- `site/index.html` 是否存在
- `site/assets/` 中引用的静态资源是否完整
- `site/README.md` 是否仍准确描述本地预览和 Pages 部署方式
- 如修改了站点内容，确认 `deploy-pages.yml` 的触发路径与目录结构仍匹配

### 3. `media-platform/` 检查

- `media-platform/README.md` 是否仍准确描述依赖、启动步骤和 API
- `media-platform/backend/requirements.txt` 是否和代码依赖一致
- `media-platform/.gitignore` 是否继续忽略 `backend/uploads/`、`backend/outputs/` 和本地数据库
- 如改动了后端代码，至少做一次基础运行或语法检查

### 4. GitHub 自动化检查

- `ai-daily-digest.yml`、`issue-handler.yml`、`deploy-pages.yml` 是否仍符合当前仓库目标
- 如工作流改动涉及 GitHub API，确认仓库权限和事件触发条件仍合理
- 如新增工作流，确认没有与现有 Pages / Issue 自动化重复或冲突

## 输出要求

回答时按以下结构组织：

1. 当前是否适合发布到 `main`
2. 已满足的条件
3. 仍存在的阻塞项或风险
4. 按优先级排序的下一步动作

## 注意事项

- 不要把“发布检查”写死为必须执行 `pnpm build`
- 若某项检查需要联网，优先用 GitHub 连接器，不可用时明确说明限制
- 如仓库仍有大量未提交改动，要把“先整理工作区”列为优先建议
