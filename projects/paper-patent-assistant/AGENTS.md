# AGENTS.md — 项目级规则

本文件定义 `Science Workflow` 的项目级规则，作为根目录 `AGENTS.md` 的补充。

## 项目上下文

- 项目路径：`projects/paper-patent-assistant/`
- 模板：`app-starter` v1.0.0
- 当前阶段：`building`

## 项目级规则

- 项目代码留在本目录 — 不要写回根目录
- 项目任务记录在 `memory/tasks.md`
- 关键决策记录在 `MEMORY.md`
- **Agent 执行准则**：在处理 SCI/期刊论文或硕博论文指令时，必须优先读取 `.agents/workflows/science-workflow.md` 作为主控工作流。
- **专利扩展准则**：只有用户明确提出“转专利 / 技术交底书 / 权利要求书”时，才进入 `.agents/workflows/scipatent-lifecycle.md` 专利 extension。
- 根级规则与项目级规则冲突时，根级规则优先

## 开发约束

- 技术栈：**纯 Agent 驱动 (Markdown Skills + Prompt Orchestration)**，前端 Web 代码已弃用。
- 领域约束：默认主线保持通用学术写作；当用户明确选择煤化工/能源化工行业包时，加载 `skills/_shared/domain/ai-coal-chem.md`。
- 证据约束：论文、学位论文章节、导师意见响应、图表、专利草案必须标注数据来源等级；模拟数据只能用于集成测试和演示，不得伪装成真实实验结果。
- 产物约束：每轮完整生命周期应维护成果包清单与运行状态，至少记录当前 Gate、输入证据、输出文件、验证命令和待人工确认事项。

## 代码风格

- 遵循项目已有的模式
- 优先组合而非继承
- 保持组件聚焦和可复用
- 按根级工作流规范编写 commit message
