# {{PROJECT_NAME}}

> AI Agent / 工作流 / 自动化系统

## 项目概述

- **目标**：{{PROJECT_GOAL}}
- **目标用户**：{{TARGET_USERS}}
- **模板**：`agent-starter` v1.0.0
- **创建日期**：{{CREATED_DATE}}

## Agent 架构

| 组件 | 描述 | 状态 |
|---|---|---|
| Core Agent | 主 agent 逻辑和路由 | |
| Memory System | 持久记忆管理 | |
| Tool Integration | 外部工具连接 | |
| Workflow Engine | 任务编排 | |

## 技术栈

| 层级 | 选择 | 理由 |
|---|---|---|
| 运行时 | {{TECH_STACK}} | |
| LLM 提供商 | | |
| 向量数据库 | | |
| 编排框架 | | |

## 项目结构

```text
src/                # 源代码
  agent/            # 核心 agent 逻辑
  tools/            # 工具定义和集成
  workflows/        # 工作流定义
  memory/           # Agent 记忆管理
  prompts/          # Prompt 模板
  config/           # 配置
docs/               # 项目文档
tests/              # 测试文件
memory/             # 项目级任务和每日日志（AI Flows 记忆，非 agent 记忆）
```

## 快速开始

**Node.js 项目：**

```bash
# 推荐 pnpm，也可用 npm
pnpm install
cp .env.example .env
# 在 .env 中添加 API keys
pnpm start
pnpm test
```

**Python 项目（推荐 [uv](https://docs.astral.sh/uv/)）：**

```bash
uv init
uv add langchain openai
cp .env.example .env
# 在 .env 中添加 API keys
uv run python main.py
uv run pytest
```

## 关键决策

参见 [MEMORY.md](MEMORY.md) 了解持久决策，[memory/tasks.md](memory/tasks.md) 了解当前进度。
