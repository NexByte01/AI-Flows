---
description: Incubate a new project under projects/<slug>/ and initialize project-level memory
---

# 孵化新项目

## 前置条件

- 用户明确要求创建新项目
- 确认 `projects/registry.yml` 中没有其他 `building` 状态的项目（或用户同意暂停当前项目）

## 步骤

### 1. 确认项目信息

向用户确认以下信息：

| 字段 | 说明 | 示例 |
|---|---|---|
| `name` | 项目名称 | 智能气体监测系统 |
| `slug` | 项目目录名（小写英文 + 连字符） | smart-gas |
| `type` | 项目类型 | `app` / `api` / `website` / `agent` |
| `description` | 一句话描述 | 工业气体实时监测和报警平台 |
| `tech_stack` | 技术栈 | Next.js + Supabase |
| `target_users` | 目标用户 | 工厂安全管理人员 |
| `goal` | 核心目标 | 实现气体浓度实时监控和异常报警 |

### 2. 选择模板

根据项目类型选择对应模板：

| 类型 | 模板 |
|---|---|
| `app` | `.agents/templates/app-starter/` |
| `api` | `.agents/templates/api-starter/` |
| `website` | `.agents/templates/website-starter/` |
| `agent` | `.agents/templates/agent-starter/` |

读取模板的 `version.yml` 获取当前版本号。

### 3. 创建项目目录

将模板内容复制到 `projects/<slug>/`，并替换所有占位变量：

| 变量 | 替换为 |
|---|---|
| `{{PROJECT_NAME}}` | 项目名称 |
| `{{PROJECT_SLUG}}` | 项目 slug |
| `{{PROJECT_GOAL}}` | 项目目标 |
| `{{TARGET_USERS}}` | 目标用户 |
| `{{TECH_STACK}}` | 技术栈 |
| `{{CREATED_DATE}}` | 今日日期（YYYY-MM-DD） |

### 4. 更新项目索引

在 `projects/registry.yml` 中添加新项目条目：

```yaml
  - slug: <slug>
    name: <name>
    type: <type>
    status: building
    template: <template-name>
    template_version: "<version>"
    created: <today>
    updated: <today>
    description: "<description>"
    external: false
    repository: ""
    migrated_to: ""
```

将 `current_project` 设置为新项目的 slug。

### 5. 更新根级记忆

- 在 `memory/YYYY-MM-DD.md` 中记录项目孵化
- 在 `memory/tasks.md` 中添加相关任务（如果需要）

### 6. 输出确认

向用户确认：
- 项目已创建在 `projects/<slug>/`
- 使用的模板及版本
- 已注册到 registry
- 建议的下一步操作

## 规则

- 绝不在根目录创建项目代码
- 每次只能有一个 `building` 状态的项目（除非用户明确要求）
- 所有占位变量必须被替换
- 模板版本号必须记录在 registry 中
