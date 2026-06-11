---
description: 面向 SCI/期刊论文与硕博论文的 Science Workflow 主入口
---

# Science Workflow

本工作流是 `paper-patent-assistant` 项目的默认主入口。它服务硕博个人，首版覆盖通用 SCI/期刊论文与硕博论文写作；煤化工/能源化工作为默认示例行业包，按需加载。

## 0. 全局加载要求

执行前必须读取：

1. `docs/EVIDENCE_POLICY.md`
2. `docs/DELIVERABLES.md`
3. `docs/RUN_STATE.example.json`
4. 当用户明确选择煤化工/能源化工行业包时，加载 `skills/_shared/domain/ai-coal-chem.md`

默认不进入专利流程。仅当用户明确要求“转专利”“技术交底书”“权利要求书”时，才切换到 `scipatent-lifecycle.md`。

## 1. 意图分流

先判断用户目标：

- `journal`：SCI/期刊论文。
- `thesis`：硕士/博士论文。
- `extension_patent`：成果转专利，仅在明确触发时进入。

若目标不明确，先询问用户是写期刊论文还是学位论文。

### 1.1 行业包选择（可选）

- 默认不强制加载行业包。
- 如果用户明确指定煤化工/能源化工语境，再加载对应行业包。
- 行业包只影响术语、示例和约束语境，不改变 Gates、证据政策和交付结构。

## 2. Journal Flow

### Phase J1: 选题与文献核验

- 明确研究问题、目标期刊层级、学科方向；如启用行业包，再同步校准行业语境。
- 建立引用核验表，记录 DOI/URL、年份、来源、检索工具和核验状态。
- 输出 Research Gap 与核心贡献假设。

**Gate J1**：用户确认选题、目标期刊方向和核心 Gap。

### Phase J2: 证据与数据确认

- 使用 `templates/real_data_intake.md` 派生真实数据清单。
- 明确哪些数据是 `real`、`verified`、`described` 或 `mock`。
- 禁止用 AI 生成数据替代真实实验或仿真。

**Gate J2**：用户确认数据来源、证据等级和不可编造边界。

### Phase J3: 图表与论文初稿

- 生成图表计划和 caption 草案。
- 调用 `nature-figure` 生成可复现图表，或基于用户真实图表进行结构化描述。
- 调用 `nature-writing` 和 `nature-polishing` 起草论文。

**Gate J3**：用户确认图表、核心论断和初稿方向。

### Phase J4: 模拟审稿与返修

- 调用 `nature-reviewer` 进行领域专家、方法专家和重现性专家审阅。
- 使用 `templates/revision_action_table.md` 映射问题、证据缺口和修回动作。
- 输出 Journal Package。

## 3. Thesis Flow

### Phase T1: 开题与章节计划

- 使用 `templates/chapter_plan.md` 建立学位论文结构。
- 明确研究问题、章节职责、每章证据和预期图表；如启用行业包，再补充对应约束。

**Gate T1**：用户确认论文题目、章节结构和研究边界。

### Phase T2: 文献综述与证据矩阵

- 建立主题矩阵和引用核验表。
- 区分综述性引用、方法引用、数据来源和对比基线。

**Gate T2**：用户确认文献综述范围和引用核验状态。

### Phase T3: 章节写作与导师意见响应

- 分章生成草稿，不越过证据边界。
- 使用 `templates/advisor_response.md` 处理导师意见。
- 标注查重风险、引用密度和需要人工确认的段落。

**Gate T3**：用户确认章节草稿和导师意见响应。

### Phase T4: 答辩材料

- 生成答辩大纲、创新点、图表讲解和问题预案。
- 输出 Thesis Package。

## 4. 收尾

每轮结束必须：

- 更新 run state。
- 更新成果包清单。
- 保留证据等级。
- 不提交真实论文、真实数据、图表、导师意见和当前 run state。
