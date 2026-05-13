---
description: Generate atomic commit commands based on git status and conversation context
---

# 生成提交命令

## 环境约束

- 仓库结构：多项目孵化中枢
- 分支策略：`main` 为生产分支，`develop` 为开发主线，功能在 `feature/*` 分支开发后合并到 `develop`，稳定后再合并到 `main`

## 项目结构与 Scope 映射

本仓库是多项目 monorepo，提交的 scope 应反映变更所属的层级：

| 变更位置 | scope 取值 | 示例 |
| --- | --- | --- |
| 根级规则/记忆 | `root` | `docs(root): 更新 MEMORY.md` |
| `.agents/workflows/` | `workflow` | `chore(workflow): 新增收尾工作流` |
| `.agents/templates/` | `template` | `feat(template): 添加架构文档模板` |
| `.agents/skills/` | `skill` | `feat(skill): 新增 SEO 审查技能` |
| `projects/<slug>/` | `<slug>` | `feat(smart-gas): 添加报警模块` |
| `scripts/` | `script` | `chore(script): 优化初始化向导` |
| `.github/` | `ci` | `chore(ci): 更新 CI 触发条件` |
| 其他/跨项目 | `root` | `chore(root): 整理根目录结构` |

> 当一次提交涉及多个项目时，优先按功能模块拆分为独立提交；如确实不可拆分，scope 用最核心的那个。

## ⚠️ PowerShell 路径转义（Windows 用户必须遵守）

路径中包含空格、`()`、`[]` 或中文等特殊字符时，`git add` 必须用双引号包裹：

```powershell
# ❌ 错误
git add docs/DSLC Scheme/03-开发.md

# ✅ 正确
git add "docs/DSLC Scheme/03-开发.md"
```

## 前置条件

- 工作目录有未提交的变更
- 已确认当前分支（日常开发在 `develop`，不在 `main` 上直接提交）

## 步骤

1. 检查当前状态

// turbo
```
git status
```

2. 按逻辑单元分组变更

- 每个 commit 只包含一个逻辑变更
- 如果有多个不相关的变更，拆分为多个 commit

3. 生成 commit 命令

## Commit Message 规范

- 标题 (Header)：`type(scope): 简要说明`
- **语言默认使用中文**：`type(scope)` 保持英文 Conventional Commit，冒号后的标题和正文说明默认写中文
- 正文 (Body)：必须使用多行模式，用额外 `-m` 参数详细列出该提交涉及的每个文件相对路径，并说明具体改动
- type 取值：`feat` / `fix` / `refactor` / `chore` / `docs` / `style` / `perf` / `init`
  - `init`：仅用于仓库初始化或新项目脚手架搭建
- scope 取值：见上方「项目结构与 Scope 映射」

## 提交排序规则

按依赖关系排序：根级规则/配置 → 工作流/模板 → 项目代码 → 项目记忆/索引

## 输出要求

- ⛔ **禁止运行 `git diff`、`git log`、`git show`**：信息不够就根据文件路径和对话上下文合理推断
- 直接输出可一键复制执行的命令块
- 严禁使用 `git add .` 或 `git add -A`
- 末尾包含 push 命令

## 示例

```bash
# [1] 根级规则与记忆
git add AGENTS.md MEMORY.md
git commit -m "docs(root): 建立项目操作系统规则" -m "- AGENTS.md: 定义多项目协作规则" -m "- MEMORY.md: 初始化长期约定"

# [2] 工作流
git add ".agents/workflows/closeout.md" ".agents/workflows/review.md"
git commit -m "chore(workflow): 添加收尾和审查工作流" -m "- closeout.md: 任务结束闭环检查" -m "- review.md: 结构化代码审查流程"

# [3] 推送
git push origin develop
```

## 规则

- Commit message 冒号后使用中文
- Scope 使用小写英文
- 不要用 `git add .` 提交所有文件 — 按逻辑分组
- 纯文档变更使用 `docs` 类型，不要归入 `chore`
