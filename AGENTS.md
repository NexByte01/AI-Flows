# AGENTS.md — AI Agent 核心定义

本文件是所有 AI agent 的行为规则。每次新对话先读取此文件和 `MEMORY.md`。

---

## 身份

我是本仓库的常驻 AI agent，代号 **{{AGENT_NAME}}**。本仓库是一个**可 fork 的 AI 项目操作系统**。

## 默认读取策略

每次恢复工作时，默认只读取：

1. `AGENTS.md`
2. `MEMORY.md`
3. `projects/registry.yml`
4. 当前主项目的 `projects/<slug>/MEMORY.md`
5. 当前主项目的 `projects/<slug>/memory/tasks.md`

按需读取：

- 当前任务涉及项目规则时，再读 `projects/<slug>/AGENTS.md`。
- 当前任务涉及架构时，再读 `projects/<slug>/docs/ARCHITECTURE.md`。
- 只有需要追溯历史原因时，才读 `memory/YYYY-MM-DD.md`。
- 长参考资料保留链接，执行时按需打开。

## 工作原则

1. **先读取**：`AGENTS.md` → `MEMORY.md` → `projects/registry.yml` → 最新 `memory/YYYY-MM-DD.md`
2. **复用优先**：先查 `.agents/skills/` 和 `.agents/workflows/`
3. **及时写入**：重要信息写入仓库文件，不留在对话中
4. **最小变更**：只改相关文件
5. **Token 预算优先**：恢复上下文时先读最小必要文件；日志、架构和长参考资料只在任务需要时按目标路径或关键词读取
6. **记忆最小化**：长期记忆只保存稳定规则、关键决策和当前状态；过程细节进入日志，易过时事实执行前重新验证
7. **最小可验证变更**：先做 MVP，后做扩展；先证明链路，再做规模化
8. **收尾自动化**：较大任务完成后执行 `/closeout` 的最小收尾检查

## 项目孵化

- 项目创建在 `projects/<slug>/` 下，绝不在根目录
- 默认同一时间一个活跃项目（`registry.yml` 中 `building` 状态）
- 使用 `.agents/templates/` 中的模板初始化
- 新项目必须登记到 `projects/registry.yml`
- 项目级任务写入 `projects/<slug>/memory/tasks.md`，不要混入根级任务

## 任务结束检查

完成一次较大工作后，应检查是否需要更新：

1. 当前项目的 `memory/YYYY-MM-DD.md`
2. 当前项目的 `memory/tasks.md`
3. 根级 `memory/tasks.md`（如有跨项目影响）
4. 当前项目的 `MEMORY.md`（如确立新约定）
5. 当前项目的 `docs/ARCHITECTURE.md`（如有架构变更，运行 `/update-architecture`）
6. `projects/registry.yml`（如项目状态变化）

### 强制更新触发条件

只要一次工作满足以下任一条件，必须更新当前项目的 `memory/YYYY-MM-DD.md`，并检查/更新 `docs/ARCHITECTURE.md`：

- 新增或删除核心模块/服务。
- 新增外部 API 或第三方服务接入。
- 修改核心数据模型或 Schema。
- 新增 CLI 命令或 API 路由。
- 改变关键运行时能力。

较大任务完成后应执行 `/closeout`，确认验证、任务、日志、架构和 Token 预算均已处理。
每周或阶段结束后应执行 `/memory-maintenance`。

## 语言

- 文档：中文 | 代码、Git commit type/scope、分支名、YAML 键名：英文
- Git commit 冒号后的标题和正文默认使用中文

---

*由 {{AGENT_NAME}} 维护 — 版本: 4.0.0*
