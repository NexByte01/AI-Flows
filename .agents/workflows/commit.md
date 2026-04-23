---
description: Analyze git status and generate atomic commits for NexByte01/AI-Flows
---

# 生成原子提交命令

用于以下类型的问题：

- “帮我根据当前改动生成提交命令”
- “把这批改动拆成合理的 commit”
- “按 Conventional Commits 输出可复制命令”

请先阅读用户提供的 `git status` 文本，并结合当前对话里的开发时间线，输出适合 `NexByte01/AI-Flows` 的 PowerShell 提交命令。

## 环境约束

- Shell：PowerShell
- 分支策略：`main` 为主分支，日常改动在 `feature/*`、`fix/*`、`docs/*`、`chore/*` 分支完成后通过 PR 合并回 `main`

## 提交策略

- 严禁使用 `git add .` 或 `git add -A`，按功能模块拆分原子提交
- 优先按依赖关系排序：仓库规则/配置 → 自动化/工作流 → 核心代码 → 文档/日志
- 结合对话时间线，还原尽量真实的开发顺序
- 只基于已知文件路径和上下文推断，不擅自虚构不存在的文件

## Commit Message 规范（严格执行）

- 标题 (Header)：`type(scope): 简要说明`
- 正文 (Body)：使用多行模式，用额外 `-m` 参数列出关键文件及改动说明
- type 取值：feat / fix / refactor / chore / docs / style / perf

### 当前仓库的类型建议

- 仓库规则、记忆文件、说明文档：`docs` 或 `chore`
- GitHub Actions、仓库配置、Git 工作流：`chore`
- `site/` 的页面与静态资源：`feat` / `fix`
- `media-platform/` 的功能修复或增强：`feat` / `fix`
- 仅结构整理且不改变行为：`refactor`

## 输出要求

- ⛔ **禁止执行任何命令**：不要运行 `git diff`、`git log`、`git status`、`git show` 或任何其他命令。仅根据用户提供的 git status 文本分析变更、生成提交命令
- ⛔ **禁止要求用户执行额外命令**：不要让用户去跑 diff 或其他命令来补充信息。信息不够就根据文件路径和对话上下文合理推断
- ⛔ **禁止 `#` 注释**：不要在命令块中使用 `# 注释`，在 CMD 中会报错。用空行分隔不同提交组
- 直接输出可一键复制执行的 PowerShell 命令块，不要输出多余的解释文字
- 如需切换或创建分支，可在命令块开头包含分支操作
- 如用户意图是完成一次提交流程，末尾包含 `git push -u origin <branch>`
- 确保用户可以直接复制粘贴执行

## 示例

```powershell
git add .gitignore AGENTS.md memory/2026-04-23.md
git commit -m "chore(workflow): 完善仓库协作规则" -m "- .gitignore: 补充仓库级忽略规则与中文注释" -m "- AGENTS.md: 对齐当前 Git 协作约定" -m "- memory/2026-04-23.md: 记录本次规则调整"

git add .agents/workflows/commit.md .agents/workflows/pr.md .agents/workflows/README.md
git commit -m "docs(workflows): 重建仓库工作流说明" -m "- .agents/workflows/commit.md: 更新提交规范与输出约束" -m "- .agents/workflows/pr.md: 对齐 main + feature PR 流程" -m "- .agents/workflows/README.md: 说明工作流目录定位"

git push -u origin feature/git-workflow
```
