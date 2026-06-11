# Science Workflow

> 面向硕博个人的通用科研写作与成果生成 Agent 工作流。首版主线覆盖 SCI/期刊论文与硕博论文；煤化工/能源化工作为可切换行业包，专利能力作为可选 extension 保留。

---

## 核心定位

Science Workflow 不是代写工具，也不是传统 Web SaaS。它是一个基于 AI Flows 的 **UI-less Agent Workflow**，通过可审计的 Gates、证据分级和成果包规范，帮助硕博个人把科研想法、真实数据、文献证据和导师/审稿意见组织成可交付的学术写作资产。

首版商业主线：

1. **Journal Flow**：SCI/期刊论文写作，覆盖选题、文献核验、证据确认、科研图表、初稿、模拟审稿和返修。
2. **Thesis Flow**：硕博论文写作，覆盖开题、文献综述、章节计划、实验/图表、导师意见响应和答辩材料。
3. **Industry Packs**：可切换行业包层，默认提供煤化工/能源化工示例包，沉淀气化、热化学、过程模拟、AI for Science 和工业控制语境。
4. **Patent Extension**：论文成果转专利/技术交底书的可选插件，默认不进入主流程。

---

## 关键原则

- **AI 不伪造数据**：所有论文断言、图表、专利文本必须标注证据等级。
- **用户保留学术责任**：系统只做写作辅助、结构化审阅、证据核验和表达优化，不保证录用、毕业、查重通过或专利授权。
- **通用主线优先，行业包可插拔**：主标题永远是科研写作，煤化工只是默认示例行业包之一。
- **真实产物本地生成**：论文、图表、导师意见、真实数据和 run state 默认不提交到仓库。

---

## 工作流入口

### 1. Science Workflow 主入口

```text
/science-workflow 帮我把这个课题整理成 SCI 论文工作流
```

Agent 会载入 `projects/paper-patent-assistant/.agents/workflows/science-workflow.md`，并先判断用户目标是 `journal` 还是 `thesis`；如需行业语境，再加载对应行业包。

### 2. 专利插件入口

```text
/scipatent-lifecycle 将这篇论文的技术方案转成专利交底书
```

该入口保留为 extension，只在用户明确选择成果转专利时触发。

---

## 目录结构

```text
paper-patent-assistant/
├── .agents/workflows/
│   ├── science-workflow.md         # SCI/硕博论文主工作流
│   └── scipatent-lifecycle.md      # 专利 extension 工作流
├── docs/
│   ├── ARCHITECTURE.md             # 系统架构
│   ├── DELIVERABLES.md             # Journal / Thesis 成果包规范
│   ├── EVIDENCE_POLICY.md          # 证据、引用、查重和 AI 辅助边界
│   └── RUN_STATE.example.json      # 可提交的状态样例
├── templates/
│   ├── real_data_intake.md
│   ├── citation_verification.md
│   ├── chapter_plan.md
│   ├── advisor_response.md
│   └── revision_action_table.md
├── skills/
│   ├── _shared/domain/ai-coal-chem.md   # 默认行业包示例
│   ├── nature-writing/
│   ├── nature-reviewer/
│   ├── nature-figure/
│   ├── patent-trans/               # extension
│   └── patent-claim-check/         # extension
└── scripts/
    └── plot_figures.py
```

---

## 复现科研图表

```powershell
pnpm run figures
```

该命令通过 `uv` 临时解析 `numpy` 与 `matplotlib`，并将图表输出到本地 `docs/figures/`。该目录默认被忽略；正式交付前必须用真实或核验数据替换 mock 数据。

---

## 商业化边界

- 不代写论文，不伪造实验，不承诺录用或毕业。
- 不绕过学校或期刊的学术规范。
- 对导师意见、审稿意见和查重风险只做结构化分析与写作建议。
- 专利 extension 只做初步文本和自检，不构成法律意见。

---

## 致谢

本项目的学术分析、盲审与润色规则底座克隆并适配自上海交通大学袁一哲博士团队的开源仓库 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills.git)。在此向其优秀的学术 Prompt 框架设计表示诚挚致谢。
