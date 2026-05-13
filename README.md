# AI Flows — AI 项目操作系统

> 一个可 fork 的 AI 协作框架：内置记忆系统、项目孵化、技能库和工作流自动化。

## 30 秒启动

```bash
# 1. Fork 本仓库
# 2. 克隆到本地
git clone https://github.com/<your-username>/AI-Flows.git
cd AI-Flows

# 3. 运行初始化向导
node scripts/init.mjs

# 4. 开始与 AI agent 对话，孵化你的第一个项目
```

## 这是什么？

AI Flows 不是一个普通的代码仓库，而是一个**AI 项目操作系统** — 一个让你和 AI agent 高效协作的标准化框架。

它提供：

- 🧠 **持久记忆**：跨对话的项目记忆、决策追踪和记忆治理
- 🚀 **项目孵化**：通过对话创建和推进项目，自动初始化标准结构
- 🛠️ **技能库**：可复用的 AI 能力模块
- 📋 **工作流**：15 个标准化工作流，覆盖 Git 协作、代码审查、任务拆解、架构同步等
- 📐 **项目模板**：带版本控制的 App / API / Website / Agent 起手模板
- 🔒 **Token 预算**：分层读取策略，控制上下文消耗

## 仓库结构

```
AI-Flows/
├── AGENTS.md                 # Agent 身份和工作规则（v4.0）
├── MEMORY.md                 # 长期记忆
├── CONTRIBUTING.md           # 协作指南
├── scripts/
│   ├── init.mjs              # 初始化向导
│   └── sync-agents.mjs       # 多 Agent 适配同步
├── memory/                   # 根级记忆
│   ├── README.md             # 记忆治理规则
│   ├── tasks.md              # 任务跟踪
│   ├── YYYY-MM-DD.md         # 每日日志
│   └── archive/              # 阶段归档
├── projects/                 # 项目容器
│   ├── registry.yml          # 项目索引（schema v2）
│   └── <slug>/               # 各项目目录
│       ├── AGENTS.md
│       ├── MEMORY.md
│       ├── docs/ARCHITECTURE.md
│       ├── memory/
│       │   ├── tasks.md
│       │   ├── archive/
│       │   └── reviews/
│       └── src/
├── .agents/
│   ├── templates/            # 项目模板（带版本号）
│   ├── workflows/            # 工作流定义（15 个）
│   ├── skills/               # 技能库
│   └── i18n/                 # 语言包
└── .github/                  # GitHub 自动化
```

## 项目生命周期

| 状态 | 含义 |
|---|---|
| `building` | 正在开发中 |
| `paused` | 暂停，上下文保留 |
| `archived` | 不再活跃，保留参考 |
| `migrated` | 已迁移到独立仓库 |

使用 `/lifecycle` 工作流管理状态转换。

## 可用工作流

### 管理层

| 命令 | 用途 |
|---|---|
| `/commit` | 生成规范提交命令（中文 + Scope 映射） |
| `/feature-branch` | 创建工作分支 |
| `/pr` | 创建 Pull Request |
| `/issue` | 管理 GitHub Issue |
| `/release` | 发布就绪检查 |
| `/incubate-project` | 孵化新项目 |
| `/lifecycle` | 项目生命周期管理 |
| `/status` | 审计仓库状态 |
| `/doctor` | 仓库健康检查 |
| `/closeout` | 任务收尾闭环检查 |
| `/memory-maintenance` | 记忆维护和归档 |

### 执行层

| 命令 | 用途 |
|---|---|
| `/task-breakdown` | 从需求拆解原子任务 |
| `/review` | 结构化代码审查 |
| `/gate-check` | 阶段门禁检查 |
| `/update-architecture` | 架构文档同步 |

## 可用模板

| 模板 | 类型 | 适用场景 |
|---|---|---|
| `app-starter` | App | 通用应用、SaaS、工具类产品 |
| `api-starter` | API | REST/GraphQL API、后端服务 |
| `website-starter` | Website | 落地页、文档站、企业官网 |
| `agent-starter` | Agent | AI agent、工作流、自动化系统 |

## 设计理念

1. **文件即记忆**：所有重要信息持久化到仓库文件，而非依赖对话上下文
2. **约定优于配置**：通过标准目录结构和命名约定减少认知负担
3. **渐进式复杂度**：从 fork 到孵化第一个项目，只需几分钟
4. **可组合架构**：技能、模板、工作流可独立演进和复用
5. **Token 预算优先**：分层读取策略，控制上下文消耗
6. **收尾自动化**：每次工作闭环检查，防止遗漏

## 多 Agent 支持

Fork 即用 — 无论你使用哪个 AI 编程工具，都能直接开始工作：

| 工具 | 配置文件 | 状态 |
|---|---|---|
| **Codex (OpenAI)** | `AGENTS.md` | ✅ 原生支持 |
| **Open Code** | `AGENTS.md` | ✅ 原生支持 |
| **Antigravity (Google)** | `AGENTS.md` | ✅ 原生支持 |
| **Claude Code** | `CLAUDE.md` | ✅ 自动生成 |
| **Gemini CLI** | `GEMINI.md` | ✅ 自动生成 |
| **Cursor** | `.cursor/rules/ai-flows.mdc` | ✅ 自动生成 |
| **Windsurf** | `.windsurf/rules/ai-flows.md` | ✅ 自动生成 |
| **GitHub Copilot** | `.github/copilot-instructions.md` | ✅ 自动生成 |

> `AGENTS.md` 是唯一信息源。其他文件由 `scripts/sync-agents.mjs` 自动生成。

## 推荐工具链

| 领域 | 推荐 | 替代方案 |
|---|---|---|
| Node.js 包管理 | [pnpm](https://pnpm.io/) | npm / yarn |
| Python 包管理 | [uv](https://docs.astral.sh/uv/) | pip + venv |
| Node 版本管理 | [fnm](https://github.com/Schniz/fnm) | nvm / volta |

## 语言策略

- **中文为主**：所有文档、说明、模板内容、Git commit 标题使用中文
- **英文为辅**：代码、Git commit type/scope、分支名、技术术语使用英文
- **国际化支持**：通过 `.agents/i18n/` 提供英文语言包

## 许可证

MIT License
