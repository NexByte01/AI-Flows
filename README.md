# NexByte AI Flows

> 一个面向长期协作的 AI 工作空间：用仓库承载记忆、技能、自动化和实验项目，让 AI 助手持续参与真实工作。

<p align="center">
  <a href="https://github.com/NexByte01/AI-Flows/blob/main/AGENTS.md"><img alt="AI Agent" src="https://img.shields.io/badge/AI%20Agent-Nex-0f172a?style=flat-square"></a>
  <a href="https://github.com/NexByte01/AI-Flows/actions/workflows/deploy-pages.yml"><img alt="GitHub Pages" src="https://img.shields.io/github/actions/workflow/status/NexByte01/AI-Flows/deploy-pages.yml?style=flat-square&label=Pages"></a>
  <a href="https://nexbyte.com.cn"><img alt="Main Site" src="https://img.shields.io/badge/Main%20Site-nexbyte.com.cn-2563eb?style=flat-square"></a>
</p>

---

## 项目简介

**NexByte AI Flows** 不是单一产品仓库，而是一个可长期演化的 AI 工作空间。它把这些能力放在同一个仓库中：

- **长期记忆**：通过 `AGENTS.md`、`MEMORY.md`、`memory/` 持续保存上下文
- **技能资产**：通过 `.agents/skills/` 复用高价值能力
- **自动化流程**：通过 GitHub Actions 运行日报、Issue 处理、Pages 部署等自动任务
- **实验项目**：将站点、工具、原型和子项目逐步沉淀在同一空间内

这个仓库的目标不是“演示模板”，而是成为你自己的 AI 协作主仓。

## 为什么存在

日常使用 AI 时，真正稀缺的不是一次性回答，而是：

- 上下文能否跨对话保留
- 工作流能否沉淀成规范
- 复用能力能否资产化
- 自动化能否和项目本身一起演进

NexByte AI Flows 就是为此设计的：让 AI 助手不只参与一轮任务，而是参与整个仓库的长期建设。

## 快速恢复工作状态

新开一次对话时，告诉助手：

```text
请读取 AGENTS.md 和 MEMORY.md，恢复 Nex 的身份和当前工作状态，然后继续我们的工作。
```

这会让仓库驻留助手 **Nex** 先读取规则和长期记忆，再继续推进后续任务。

## 仓库结构

```text
NexByte AI Flows/
├── AGENTS.md                  # Nex 的身份、规则和协作方式
├── MEMORY.md                  # 长期记忆：项目背景、偏好、持久约定
├── memory/
│   ├── tasks.md               # 跨对话任务追踪
│   └── YYYY-MM-DD.md          # 每日工作日志
├── .agents/
│   ├── skills/                # 项目级技能资产
│   └── workflows/             # 项目级工作流说明与模板
├── site/                      # NexByte AI Flows 临时占位页
├── media-platform/            # 当前保留的实验子项目：多媒体处理平台
└── .github/workflows/         # GitHub 自动化工作流
```

## AI 工作空间机制

| 级别 | 文件位置 | 作用 |
|---|---|---|
| 身份规则 | `AGENTS.md` | 定义 Nex 的身份、工作方式和收尾动作 |
| 长期记忆 | `MEMORY.md` | 记录不会频繁变化的项目事实 |
| 每日日志 | `memory/YYYY-MM-DD.md` | 保存当天完成的任务和关键决策 |
| 任务追踪 | `memory/tasks.md` | 管理待办、进行中、已完成事项 |
| 技能资产 | `.agents/skills/` | 沉淀可复用能力 |
| 工作流资产 | `.agents/workflows/` | 统一 Git、PR、Issue、状态汇报等流程 |

## 当前子项目 / 实验区

### `site/`

一个临时占位页，用于说明：

- 这是 NexByte 的 AI 工作空间仓库
- 主站为 <https://nexbyte.com.cn>
- 当前仓库承载技能、记忆、自动化和实验项目

该站点继续通过 GitHub Pages 自动部署，适合作为公开说明页或仓库入口页。

### `media-platform/`

一个仍在保留和演进中的实验子项目，提供图片、音频、视频的压缩与格式转换能力。

- 技术栈：Python Flask + Vue 3 + SQLite + Pillow + FFmpeg
- 当前定位：AI 辅助孵化的实验项目，而不是模板演示

## 自动化与协作

当前仓库已保留并继续使用以下自动化流程：

- `ai-daily-digest.yml`：定期生成 AI 技术日报 Issue
- `issue-handler.yml`：自动回复 Issue，并在 `bug` 标签场景下尝试交给 Copilot coding agent
- `deploy-pages.yml`：自动部署 `site/` 到 GitHub Pages
- `repo-checks.yml`：在 PR 和工作分支推送时检查分支命名、提交信息、关键文件、Python 语法和 Actions 配置
- `auto-draft-pr.yml`：在工作分支推送后自动创建 Draft PR
- `auto-enable-automerge.yml`：在 PR 进入可合并阶段时自动尝试启用 auto-merge（需仓库设置支持）

Git 协作约定默认采用：

- `main` 为主分支
- 日常改动在 `feature/*`、`fix/*`、`docs/*`、`chore/*` 分支完成
- 通过 PR 合并回 `main`

更具体的操作手册见：

- [`.agents/workflows/README.md`](.agents/workflows/README.md)
- [`CONTRIBUTING.md`](CONTRIBUTING.md)

## 主站与仓库入口

- 主站：<https://nexbyte.com.cn>
- GitHub 仓库：<https://github.com/NexByte01/AI-Flows>
