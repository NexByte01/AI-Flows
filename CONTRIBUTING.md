# 协作指南

本文件定义了本仓库的协作规范。所有贡献者（包括 AI agent）都应遵循这些约定。

## 分支模型

本仓库使用 `main + develop + feature/*` 分支模型。

### 分支命名规范

| 前缀 | 用途 | 示例 |
|---|---|---|
| `feature/` | 新功能 | `feature/template-versioning` |
| `fix/` | 修复 Bug | `fix/registry-parse-error` |
| `docs/` | 文档更新 | `docs/readme-rewrite` |
| `chore/` | 维护性工作 | `chore/cleanup-stale-files` |

### 分支规则

- `main` 为生产分支，保持稳定
- `develop` 为开发主线，日常提交推到这里
- 功能在 `feature/*` 分支开发后合并到 `develop`
- 稳定后通过 PR 从 `develop` 合并到 `main`
- 分支名使用小写英文和连字符：`feature/my-feature`
- 合并后删除工作分支

## Commit 规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式，**冒号后使用中文**：

```
<type>(<scope>): <中文简要说明>
```

### 类型

| 类型 | 用途 |
|---|---|
| `feat` | 新功能 |
| `fix` | 修复 Bug |
| `docs` | 文档变更 |
| `chore` | 维护性工作 |
| `refactor` | 重构（不改变外部行为） |
| `perf` | 性能优化 |
| `style` | 代码格式（不影响逻辑） |
| `init` | 仓库初始化或新项目脚手架搭建 |

### Scope 映射

| 变更位置 | scope |
|---|---|
| 根级规则/记忆 | `root` |
| `.agents/workflows/` | `workflow` |
| `.agents/templates/` | `template` |
| `projects/<slug>/` | `<slug>` |
| `scripts/` | `script` |
| `.github/` | `ci` |

### 示例

```
feat(template): 为所有模板添加架构文档
fix(smart-gas): 修复报警阈值计算错误
docs(root): 更新语言策略章节
chore(ci): 移除过时的 Python 语法检查
```

### 多行 Body

较大变更应使用多行 body，列出每个文件的改动：

```bash
git commit -m "chore(workflow): 新增收尾和审查工作流" \
  -m "- closeout.md: 任务结束闭环检查" \
  -m "- review.md: 结构化代码审查流程"
```

## Pull Request 规范

### PR 标题

与 commit message 格式一致：`<type>(<scope>): <中文说明>`

### PR 内容

每个 PR 应包含：变更内容说明、影响范围、测试方式、记忆文件更新状态。

## 目录职责

| 目录 | 职责 | 谁来维护 |
|---|---|---|
| 根目录 | 全局规则和控制面文件 | Agent + 用户 |
| `memory/` | 根级记忆和任务 | Agent |
| `projects/` | 项目容器 | Agent + 用户 |
| `.agents/templates/` | 项目模板 | Agent + 用户 |
| `.agents/workflows/` | 工作流定义 | Agent + 用户 |
| `.agents/skills/` | 技能库 | Agent |
| `.agents/i18n/` | 语言包 | Agent + 用户 |
| `.github/` | GitHub 自动化 | Agent + 用户 |
| `scripts/` | 工具脚本 | Agent + 用户 |

## 记忆文件维护

详细规则见 `memory/README.md`。

### 何时更新

- **每次较大工作结束前**：运行 `/closeout` 检查闭环
- **任务状态变化时**：更新 `memory/tasks.md`
- **确立新约定时**：更新 `MEMORY.md`
- **项目状态变化时**：更新 `projects/registry.yml`
- **架构变更时**：运行 `/update-architecture`

### 格式约定

- 任务使用 `[ ]`（待办）、`[~]`（进行中）、`[x]`（已完成）标记
- 每日日志包含：今日完成、关键决策、下一步
- MEMORY.md 只记录跨对话的持久信息，不超过 150 行
- 易过时事实标注 `last_verified` 日期

### 记忆治理

- 已完成任务超过 20 条时，执行 `/memory-maintenance` 归档旧项
- 每周或每个阶段结束后执行一次记忆维护
- 长期记忆不保存一次性输出、临时讨论或未验证猜测

## 推荐工具链

| 领域 | 推荐工具 | 安装方式 |
|---|---|---|
| Node.js 包管理 | [pnpm](https://pnpm.io/) | `npm install -g pnpm` |
| Python 包管理 | [uv](https://docs.astral.sh/uv/) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Node 版本管理 | [fnm](https://github.com/Schniz/fnm) | `cargo install fnm` 或 `winget install Schniz.fnm` |

> 以上为推荐而非强制 — npm / pip / nvm 同样可以正常工作。

## 代码规范

- 遵循项目已有的代码风格
- 涉及项目叙事时，默认以通用主线命名，行业包作为可选扩展，不要把第一垂直领域写进主标题
- 优先组合而非继承
- 保持组件聚焦和可复用
- 不删除与当前变更无关的注释和文档

## 语言规范

- **文档和说明**：中文
- **代码和技术术语**：英文
- **Git commit type/scope**：英文
- **Git commit 标题和正文**：中文
- **分支名**：英文小写
- **YAML 键名**：英文
