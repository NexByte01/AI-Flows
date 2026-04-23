# 贡献与协作规范

本仓库默认按 **`main + 工作分支 + PR`** 模式协作。无论是人工协作还是 AI 助手协作，都应尽量遵循本文件。

## 分支规范

所有非只读操作，默认先创建工作分支，再通过 PR 合并回 `main`。

推荐分支前缀：

- `feature/<name>`：功能开发
- `fix/<name>`：问题修复
- `docs/<name>`：文档和说明更新
- `chore/<name>`：仓库维护、脚手架、工作流调整

命名要求：

- 使用 kebab-case
- 分支名应反映任务本身，而不是泛化命名
- 示例：`feature/github-templates`、`docs/readme-refresh`

## Commit 规范

提交信息采用 **Conventional Commits**：

```text
type(scope): 简要说明
```

常用 `type`：

- `feat`
- `fix`
- `docs`
- `chore`
- `refactor`
- `perf`
- `style`

示例：

```text
docs(readme): 重写仓库首页说明
chore(workflow): 补充 issue 模板与 pr 模板
fix(site): 修正占位页外链与元信息
```

约束：

- 尽量原子提交，按功能模块拆分
- 不使用 `git add .` 或 `git add -A`
- 涉及多个领域时，优先拆成多个 commit

## PR 规范

所有常规改动都应通过 PR 合并到 `main`。

PR 标题建议沿用提交风格：

```text
type(scope): 简要说明
```

PR 描述至少应覆盖：

- 本次改动做了什么
- 影响了哪些目录
- 如何验证
- 是否更新了 `memory/YYYY-MM-DD.md`
- 是否存在风险点或后续待办

仓库当前会在 PR 和工作分支推送时运行基础检查：

- 分支命名是否符合约定
- 提交信息是否符合 Conventional Commits
- 关键仓库文件是否存在
- `media-platform/backend` 的 Python 语法是否可通过编译
- GitHub Actions 工作流是否能通过静态检查
- 工作分支推送后是否自动创建 Draft PR
- 非 Draft PR 是否自动尝试启用 auto-merge

## GitHub 仓库侧一次性设置

为了让自动化真正闭环，建议在 GitHub 仓库设置中完成以下一次性配置：

1. `Settings > General`
   开启 `Allow auto-merge`

2. `Settings > Branches`
   为 `main` 添加 branch protection rule，至少包含：
   - Require a pull request before merging
   - Require status checks to pass before merging
   - 将 `Repository Checks` 设为 required check
   - 如果列表刷新较慢，等待最新工作流完成后重新编辑该规则

3. `Settings > Pull Requests`
   建议保留 `Allow squash merge`
   当前自动启用 auto-merge 的工作流默认使用 `SQUASH`

## 文档与记忆要求

以下改动完成后，原则上应同步更新相关文档：

- 仓库规则、协作方式变化：更新 `AGENTS.md` / `README.md`
- 长期定位变化：更新 `MEMORY.md`
- 当天完成的重要工作：更新 `memory/YYYY-MM-DD.md`
- 跨对话任务进度变化：更新 `memory/tasks.md`
- 技能或工作流新增/重构：更新 `.agents/skills/` 或 `.agents/workflows/`

## 按改动类型的验证建议

- `site/`：人工打开页面检查内容、链接和基础展示
- `media-platform/`：至少做基础运行或语法检查
- `.github/workflows/`：做静态审查，确认触发条件、权限和文案
- 纯文档改动：检查链接、路径和仓库术语是否一致

## 相关入口

- 仓库工作流说明：[`/.agents/workflows/README.md`](.agents/workflows/README.md)
- AI 助手身份定义：[`/AGENTS.md`](AGENTS.md)
- 长期记忆：[`/MEMORY.md`](MEMORY.md)
