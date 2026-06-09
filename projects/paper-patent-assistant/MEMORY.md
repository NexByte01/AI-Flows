# MEMORY.md — 项目长期记忆

## 项目背景

- **项目名称**：`Science Workflow`
- **项目 slug**：`paper-patent-assistant`
- **项目类型**：`app`
- **目标用户**：`硕博个人`
- **次级用户**：`高校课题组`
- **第一垂直领域**：`煤化工 / 能源化工`
- **核心目标**：`面向 SCI/期刊论文与硕博论文的科研写作、证据核验、图表生成、模拟审阅与成果包交付 Agent 工作流`
- **创建日期**：`2026-06-01`

## 技术栈决策

| 决策 | 选择 | 理由 | 日期 |
|---|---|---|---|
| 运行框架 | **纯 Agent Workflow (UI-less)** | 摒弃 Web 前端开发，转为通过 Agent 直接编排底层 Markdown Skills，实现科研全生命周期自动化 | 2026-06-04 |
| 商业主线 | **Science Workflow** | 首版聚焦 SCI/期刊论文与硕博论文，煤化工为第一垂直，专利降为可选 extension | 2026-06-05 |
| 交互模式 | 会话驱动 (Chat-based Orchestration) | 用户下达单句指令，Agent 执行主控工作流，并在关键审阅/分支节点暂停人工审批 | 2026-06-04 |
| 证据治理 | Mock / Described / Verified / Real 四级标注 | 防止集成测试数据、用户口述数据和真实实验数据在论文/学位论文/专利产物中混用 | 2026-06-05 |
| 产物追踪 | Run State + Deliverables Manifest | 每轮生命周期必须记录当前 Gate、输入证据、输出文件与验证命令，便于恢复、复核和交接 | 2026-06-05 |

## 持久约定

- 核心功能代码与页面样式保留在 `projects/paper-patent-assistant/` 内，不得向全局根目录溢出。
- 默认主工作流为 `science-workflow.md`，用于 SCI/期刊论文与硕博论文。
- `scipatent-lifecycle.md` 保留为专利 extension，仅在用户明确选择成果转专利时进入。
- 煤化工/能源化工领域包是第一垂直场景，不泛化掉；通用写作内核仍需保持可迁移。
- 遵循 Nature-style 写作与审稿规范开发润色评估提示词。
- 任何论文断言、图表、导师意见响应和专利文本必须标注来源等级；`mock_dataset.md` 仅作为端到端集成测试数据。
- 科研图表默认通过 `uv run --with numpy --with matplotlib python scripts/plot_figures.py` 复现，输出目录固定为项目内 `docs/figures/`。

## 外部依赖

| 依赖 | 用途 | 版本 | 备注 |
|---|---|---|---|
| `vite` | 冻结前端原型的本地热重载和打包构建 | ^5.0.0 | devDependencies |
| `lucide` | 冻结原型中的页面图标渲染 | latest | CDN 引入 |
| `uv` + `numpy` + `matplotlib` | 科研图表复现 | latest on demand | 通过 `uv run --with ...` 临时解析，不固化到前端依赖 |

## 关键决策日志

| 日期 | 决策 | 理由 |
|---|---|---|
| 2026-06-01 | 项目创建 | 整合学术写作润色、模拟盲审、学术转专利语言与权利要求书校验的一站式科研工作台 |
| 2026-06-04 | 架构重构：摒弃 Web UI，转向 Agent Workflow | 前端无法承载庞大的交叉学科规则库，改为利用大模型的系统级调度能力读取并串联 `.md` 技能文件 |
| 2026-06-05 | 可信协作优化 | 统一 Gates，补充证据治理、成果包追踪和绘图复现约束 |
| 2026-06-05 | 商业化转向 Science Workflow | 面向硕博个人，主线改为 SCI/期刊论文与硕博论文；煤化工保留为第一垂直，专利降为插件 |
