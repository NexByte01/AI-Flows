# SciPatent 全周期科研流水线 (SciPatent Lifecycle)

**Description**: 执行一站式科研生命周期，串联 Google Science Skills 与专利双引擎，涵盖“文献检索 → 论证设计 → 论文盲审 → 专利转化”。
**Triggers**: 当用户请求“走完论文和专利全流程”、“从检索到写专利”或直接调用 `/scipatent` 触发。

## 0. 全局加载要求 (Global Context)
在执行本工作流的任何步骤前，必须静默加载并严格遵守以下领域规则与控制配置：
1. **领域大脑**：`d:\Projects\AI Flows\projects\paper-patent-assistant\skills\_shared\domain\ai-coal-chem.md` （定义交叉学科防混淆协议及专利审查红线）。
2. **流程配置**：`d:\Projects\AI Flows\projects\paper-patent-assistant\scipatent_config.json` （控制工作流分支选择与执行后端）。
   - *注意*：Agent 在每次开始或恢复执行前，必须首先读取该配置文件。如果文件缺失，则初始化创建它，默认启用专利转化 (`"patent_transformation.enabled": true`)。
3. **证据政策**：`d:\Projects\AI Flows\projects\paper-patent-assistant\docs\EVIDENCE_POLICY.md` （定义 Mock / Described / Verified / Real 证据等级）。
4. **成果包规范**：`d:\Projects\AI Flows\projects\paper-patent-assistant\docs\DELIVERABLES.md` （定义每轮输出文件、验证命令与 Gate 状态记录方式）。

执行任何论文、图表或专利生成前，必须明确当前输入数据的证据等级。若证据等级为 `mock`，输出必须标注“仅用于端到端测试或演示”，不得把模拟结果写成真实实验结论。

---

## 阶段 1: 概念化与基线检索 (Phase 1: Ideation & Baseline)

**行动指令**：
1. 分析用户的初始 Query（例如：预测煤气化产率的 GNN 模型）。
2. 调用相关工具（如 `nature-academic-search` 或 Google Science Skills 的文献检索工具）查找近 3 年的 5-10 篇核心顶会/顶刊论文。
3. 提取现存研究的 **Research Gap**。
4. 将关键文献 DOI、年份、来源和检索工具记录为 `verified` 或 `needs_verification`；无法核验的条目不得作为强证据引用。

> 🛑 **Gate 1: 立意与文献基线确认** 
> **停止执行**，向用户输出：
> - 检索到的核心基线文献综述。
> - 拟定的创新点（Gap）与预期解决的化工难题。
> **等待指令**：询问用户“该研究方向与 Gap 是否准确？是否值得继续推演？”
> *用户确认后，进入阶段 2。*

---

## 阶段 2: 论证链与实验设计 (Phase 2: Argument & Design)
 
**行动指令**：
1. 依据确认的 Gap，使用 `nature-writing` 思维模型（不需要生成全文，只需骨架），推演出：
   - **核心断言 (Core Claim)**
   - **所需证据清单 (Required Evidence)**：例如需要哪些基准模型对比图（Baseline Comparison）、哪些物理场分布图（CFD）、哪些参数消融实验。
 
> 🛑 **Gate 2: 核心证据与数据确认** 
> **停止执行**，向用户输出：
> - 所需的实验数据清单和图表逻辑。
> **等待指令**：明确告知用户：“**AI 绝不编造实验数据**。请提供真实的实验结果、仿真数据、或图表的详细文字描述。”
> *用户提供真实数据（或测试模拟数据）后，进入图表绘制阶段。*

2. **科研绘图 (Scientific Plotting) [Mandatory - 强制贯穿]**：
   - **此步骤为强制性的学术核心环节，不能跳过**。默认使用 Python 后端进行绘图。
   - 调用 `nature-figure` 技能，使用 Python 的 matplotlib/seaborn 编写绘图脚本。
   - 在本地环境中强制执行该绘图脚本（使用 `uv run --with numpy --with matplotlib python <script_path>` 或 `pnpm run figures` 运行），将生成的矢量图（SVG/PDF）或位图（PNG）保存至项目指定的输出目录中（默认 `docs/figures/`）。
   - 验证图表的物理化学守恒机制与学术视觉合规性。
   - 记录绘图命令、输入证据等级和输出文件清单；如基于 `mock_dataset.md`，必须在图表说明中保留 Mock 标签。

> 🛑 **Gate 2b: 科研图表确认** 
> **停止执行**，向用户输出：
> - 已生成的图表文件路径与核心视觉结论。
> - 指明科研图表已经成功绘制并贯穿流程。
> **等待指令**：询问用户：“图表设计与质量是否符合要求？是否值得继续进行全文起草？”
> *用户确认后，进入阶段 3。*

---

## 阶段 3: 全量起草与极端盲审 (Phase 3: Draft & Review)
 
**行动指令**：
1. 根据用户确认的图表与喂入的数据，调用 `nature-writing` 结合图表逻辑撰写全文初稿。
2. 调用 `nature-polishing` 进行 Nature 级语言润色与客观度校准（Hedging）。
3. 调用 `nature-reviewer` 对初稿发起 3 专家（煤化工专家、AI算法专家、重现性专家）极端盲审。
 
> 🛑 **Gate 3: 盲审结论与修回策略确认** 
> **停止执行**，向用户输出：
> - 3 位专家的严厉 Critique 报告（必须突出针对 AI 算法与物理/化工系统结合的薄弱环节）。
> **等待指令**：询问用户应对策略：“是补充数据再写，还是调低本文的论点强度（Hedging）？”
> *用户确认修回策略并定稿后，进入分支选择门槛。*

> 🛑 **Gate 3b: 专利转化自主选择 [Branching - 自主分支]**
> **停止执行**，读取 `scipatent_config.json` 中的 `patent_transformation.enabled`：
> - **若为 `true`**（默认）：向用户说明：“当前配置已启用专利转化。系统即将进入阶段 4 提取独立权利要求并生成技术交底书。如果您想跳过专利转化，请在此告知。”
> - **若为 `false`**：向用户说明：“根据您的偏好配置，系统已跳过阶段 4 的专利确权步骤，直接为您整理定稿的学术论文包。”然后直接跳过阶段 4，直达 `[工作流结束]`。
> - *交互支持*：用户若在会话中指示改变意愿（例如“不需要转专利”或“还是转一下专利吧”），Agent 将立即同步修改 `scipatent_config.json` 中对应的布尔值，并根据最新状态分流。

---

## 阶段 4: 专利提取与合规确权 (Phase 4: Patent Generation)
 
**行动指令**：
1. 读取定稿的学术文本，调用 `d:\Projects\AI Flows\projects\paper-patent-assistant\skills\patent-trans` 技能。
2. 生成【方法权利要求】和【系统/装置权利要求】草案。
3. 立即调用 `d:\Projects\AI Flows\projects\paper-patent-assistant\skills\patent-claim-check` 对草案进行致命缺陷排查。如果报红，内部重写直至合规。
 
> 🛑 **Gate 4: 专利保护范围确认** 
> **停止执行**，向用户输出：
> - 独立权利要求 1 的核心文本及合规审查通过证明。
> **等待指令**：询问用户：“针对 AI 算法与化工控制硬件的结合边界，该保护范围是否过窄（易被规避）或过宽（易被无效）？”
> *根据用户的微调意见，输出最终专利技术交底书并转入收尾。*
 
---
## [工作流结束] 
收尾时必须更新运行状态与成果包清单，推荐用户使用 `nature-paper2ppt` 将最终成果生成汇报大纲，并运行 `/closeout` 完成收尾审计。
