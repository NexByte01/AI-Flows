# Science Workflow 成果包规范

每次完整执行 Science Workflow 后，应形成一个可复核、可交接的成果包。成果包不是聊天记录，而是文件清单、证据状态和人工确认记录。

模板默认按通用学术写作设计；行业包只影响语境、术语和示例，不改变成果包字段结构。

## Journal Package

面向 SCI/期刊论文。

| 类别 | 默认路径 | 说明 |
|---|---|---|
| 运行状态 | `docs/RUN_STATE.current.json` 或本轮实际 run state | 记录当前 Gate、证据等级、输出文件和验证命令 |
| 选题与文献 | `memory/phase1_ideation.md` 或 `outputs/journal/ideation.md` | Research Gap、目标期刊方向、基线文献和核验状态 |
| 引用核验 | `templates/citation_verification.md` 派生文件 | DOI/URL、年份、来源、核验状态 |
| 真实数据说明 | `templates/real_data_intake.md` 派生文件 | 实验/仿真/检测数据来源、责任人、时间和使用边界 |
| 科研图表 | `docs/figures/` 或本轮输出目录 | SVG/PNG/PDF 图表产物，必须标注证据等级 |
| 论文初稿 | `docs/paper_draft.md` 或本轮输出目录 | Title、Abstract、Introduction、Methods、Results、Discussion |
| 模拟审稿 | `memory/reviewer_report.md` 或本轮输出目录 | 三专家审阅、主要问题、证据缺口 |
| 返修行动表 | `templates/revision_action_table.md` 派生文件 | 审稿意见到修改动作的映射 |

## Thesis Package

面向硕博论文。

| 类别 | 默认路径 | 说明 |
|---|---|---|
| 运行状态 | `docs/RUN_STATE.current.json` 或本轮实际 run state | 记录章节、证据等级、导师意见和待确认事项 |
| 开题/章节计划 | `templates/chapter_plan.md` 派生文件 | 研究问题、章节结构、每章证据和交付状态 |
| 文献综述 | 本轮输出目录 | 主题矩阵、代表文献、争议点和研究空白 |
| 数据说明 | `templates/real_data_intake.md` 派生文件 | 原始实验、仿真、检测或工业数据说明 |
| 导师意见响应 | `templates/advisor_response.md` 派生文件 | 导师意见、响应策略、修改状态 |
| 章节草稿 | 本轮输出目录 | 各章草稿、图表、引用和证据标签 |
| 答辩材料 | 本轮输出目录 | 汇报大纲、创新点、问题预案 |

## Patent Extension Package

仅当用户明确选择成果转专利时生成。

| 类别 | 默认路径 | 说明 |
|---|---|---|
| 专利草案 | `docs/patent_draft.md` 或本轮输出目录 | 权利要求书草案与初步自检 |
| 技术交底书 | `docs/technical_disclosure.md` 或本轮输出目录 | 给专利代理人继续加工的材料 |

专利 extension 输出不构成法律意见，必须经发明人和专利代理人复核。

## 收尾检查

- 更新 run state、任务表和项目日志。
- 确认真实论文、图表、导师意见、用户数据和当前 run state 仍被 `.gitignore` 排除。
- 若新增核心能力、模板或工作流，更新 `MEMORY.md` 与 `ARCHITECTURE.md`。
