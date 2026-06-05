# SciPatent 成果包规范

每次完整执行 `scipatent-lifecycle` 后，应形成一个可复核的成果包。成果包不是聊天记录，而是可交接文件清单。

## 必备文件

| 类别 | 默认路径 | 说明 |
|---|---|---|
| 运行状态 | `docs/RUN_STATE.current.json` 或本轮实际 run state | 记录当前 Phase、Gate、证据等级、输出文件和验证命令 |
| 文献与立意 | `memory/phase1_ideation.md` | Research Gap、基线文献与核验状态 |
| 论证与数据 | `memory/phase2_argument.md` | 核心断言、所需证据清单、数据缺口 |
| 数据说明 | `memory/mock_dataset.md` 或用户真实数据清单 | 必须标注证据等级 |
| 科研图表 | `docs/figures/` | SVG/PNG/PDF 等图表产物 |
| 论文草稿 | `docs/paper_draft.md` | 学术论文正文草稿 |
| 盲审报告 | `memory/reviewer_report.md` | 三专家模拟评审与修回策略 |
| 专利草案 | `docs/patent_draft.md` | 权利要求书与自检报告 |
| 技术交底书 | `docs/technical_disclosure.md` | 专利代理人可继续加工的交底材料 |
| 汇报大纲 | `docs/ppt_outline.md` | Journal Club 或内部汇报骨架 |

## 运行状态要求

每轮执行至少记录：

- `current_phase`：当前阶段。
- `current_gate`：最近一次人工确认点。
- `evidence_level`：本轮关键数据等级。
- `human_approvals`：各 Gate 是否已确认。
- `artifacts`：输出文件路径、用途和证据等级。
- `verification`：实际运行过的验证命令与结果。
- `open_risks`：仍需用户、实验人员、专利代理人或领域专家确认的风险。

## 收尾检查

完整工作流结束后，应更新 `memory/tasks.md` 和项目日志。如果新增核心模块、外部依赖、数据模型或运行能力，也要同步更新 `MEMORY.md` 与 `docs/ARCHITECTURE.md`。
