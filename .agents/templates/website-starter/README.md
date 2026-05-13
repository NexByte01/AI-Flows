# {{PROJECT_NAME}}

> 落地页 / 文档站 / 企业官网

## 项目概述

- **目标**：{{PROJECT_GOAL}}
- **目标用户**：{{TARGET_USERS}}
- **模板**：`website-starter` v1.0.0
- **创建日期**：{{CREATED_DATE}}

## 站点架构

| 页面 | 用途 | 优先级 |
|---|---|---|
| `/` | 首页 / 落地页 | P0 |
| `/about` | 关于我们 | P1 |
| `/docs` | 文档 | P1 |

## 技术栈

| 层级 | 选择 | 理由 |
|---|---|---|
| 框架 | {{TECH_STACK}} | |
| 样式 | | |
| CMS | | |
| 部署 | | |

## 项目结构

```text
src/                # 源代码
  pages/            # 页面组件
  components/       # 可复用 UI 组件
  layouts/          # 页面布局
  styles/           # 全局样式和设计 token
  content/          # Markdown / MDX 内容
  assets/           # 图片、字体、图标
public/             # 静态文件
docs/               # 项目文档
memory/             # 项目级任务和每日日志
```

## 快速开始

```bash
# 推荐 pnpm，也可用 npm
pnpm install
pnpm dev
pnpm build
pnpm preview
```

## 关键决策

参见 [MEMORY.md](MEMORY.md) 了解持久决策，[memory/tasks.md](memory/tasks.md) 了解当前进度。
