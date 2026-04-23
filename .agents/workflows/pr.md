---
description: Create a Pull Request for NexByte01/AI-Flows using the current GitHub connector
---

# 创建 Pull Request

## 前置条件

- 功能分支的所有提交已 push 到远程
- 已确认目标分支为 `main`
- 已整理本次改动涉及的目录、验证方式和记忆文件更新情况

## 步骤

1. 确认当前分支和待合并的提交
```powershell
git branch --show-current
git log --oneline origin/main..HEAD
```

2. 使用当前 GitHub 连接器直接创建 PR

调用 `mcp__codex_apps__github._create_pull_request`，参数如下：
- `repository_full_name`: `NexByte01/AI-Flows`
- `title`: 遵循 `<type>(<scope>): <description>` 格式
- `head`: 当前功能分支名
- `base_branch`: `main`
- `body`: 使用以下模板

```markdown
## 变更内容

- 具体改动 1
- 具体改动 2

## 影响范围

- [ ] `site/`
- [ ] `media-platform/`
- [ ] `.github/workflows/`
- [ ] `.agents/skills/`
- [ ] `.agents/workflows/`
- [ ] 记忆文件（`AGENTS.md` / `MEMORY.md` / `memory/`）

## 测试

- [ ] 静态文件改动已人工检查
- [ ] Python 改动已做基础运行或语法检查
- [ ] 工作流改动已做静态审查或 YAML 校验
- [ ] 无需额外测试（请说明原因）

## 记忆与文档

- [ ] 已更新 `memory/YYYY-MM-DD.md`
- [ ] 无需更新记忆文件（请说明原因）

## 补充说明

- 关联 Issue：
- 风险点：
- 截图或日志（如有）：

```

3. 创建成功后输出 PR 链接

## PR 规则

- 所有常规改动统一走 `feature/*`、`fix/*`、`docs/*`、`chore/*` → `main`
- 不使用 `develop`
- 若用户要求同时生成 PR 文案，优先按上面的模板输出完整正文
- 仓库已支持工作分支推送后自动创建 Draft PR；如用户明确要求，也可以手动创建正式 PR
- 若 PR 已 `Ready for review` 且仓库设置允许 auto-merge，工作流会自动尝试开启 auto-merge
