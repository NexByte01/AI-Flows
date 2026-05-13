# {{PROJECT_NAME}}

> API / 后端服务 / 数据接口

## 项目概述

- **目标**：{{PROJECT_GOAL}}
- **目标用户**：{{TARGET_USERS}}
- **模板**：`api-starter` v1.0.0
- **创建日期**：{{CREATED_DATE}}

## API 设计

| 端点 | 方法 | 描述 | 认证 |
|---|---|---|---|
| `/api/v1/...` | GET | | |
| `/api/v1/...` | POST | | |

## 技术栈

| 层级 | 选择 | 理由 |
|---|---|---|
| 运行时 | {{TECH_STACK}} | |
| 框架 | | |
| 数据库 | | |
| 认证 | | |
| 部署 | | |

## 项目结构

```text
src/                # 源代码
  routes/           # API 路由处理
  middleware/       # 请求中间件
  models/           # 数据模型 / schema
  services/         # 业务逻辑
  utils/            # 共享工具
docs/               # API 文档
tests/              # 测试文件
memory/             # 项目级任务和每日日志
```

## 快速开始

**Node.js 项目：**

```bash
# 推荐 pnpm，也可用 npm
pnpm install
cp .env.example .env
pnpm dev
pnpm test
```

**Python 项目（推荐 [uv](https://docs.astral.sh/uv/)）：**

```bash
# uv 替代 pip + venv + pyenv，速度快 10-100x
uv init
uv add fastapi uvicorn
cp .env.example .env
uv run uvicorn main:app --reload
uv run pytest
```

## 关键决策

参见 [MEMORY.md](MEMORY.md) 了解持久决策，[memory/tasks.md](memory/tasks.md) 了解当前进度。
