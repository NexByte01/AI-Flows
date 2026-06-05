# 任务跟踪

状态标记：`[ ]` 待办 | `[/]` 进行中 | `[x]` 已完成

---

## 进行中

- [/] **Sprint 1：可信协作与复现链路硬化**

---

## 待办

### Sprint 1：可信协作与复现链路硬化
- [x] 统一项目规则、长期记忆、架构文档与根级重定向工作流中的 6-Gate 表述
- [x] 修复科研绘图脚本的输出路径，使其无论从仓库根目录或项目目录执行都稳定输出到 `docs/figures/`
- [x] 移除图表文本中的特殊字体字符，避免 matplotlib 导出缺字警告
- [x] 增加 `pnpm run figures` 复现入口
- [x] 新增 `docs/EVIDENCE_POLICY.md`，明确 Mock / Described / Verified / Real 证据等级
- [x] 新增 `docs/DELIVERABLES.md` 与 `docs/RUN_STATE.example.json`，定义成果包和运行状态记录方式
- [ ] 为 Phase 1 文献基线增加 DOI、年份、来源的逐条核验清单
- [x] 将本轮实际运行状态固化为 `docs/RUN_STATE.current.json`
- [x] 将 `paper_draft.md`、`patent_draft.md`、`technical_disclosure.md`、`ppt_outline.md` 中基于 mock 数据的结论加上显式证据等级标签
- [ ] 为 `nature-academic-search` MCP 增加本地测试环境说明，并明确 pytest/依赖安装方式

### Sprint 2：真实数据接入与学术可信度
- [ ] 定义真实实验/仿真数据输入模板，包括责任人、时间、仪器/软件、工况和使用边界
- [ ] 增加图表 caption 规范，强制标注数据来源等级和是否可用于正式论文
- [ ] 增加审稿意见到修回动作的映射表，区分“需补实验”“可降调断言”“需删除结论”

### Sprint 3：专利与协作交付
- [ ] 为专利草案增加“初步自检，不构成法律意见”的边界说明
- [ ] 增加新颖性检索和 FTO 风险检查的任务入口
- [ ] 定义多人协作角色：作者、数据提供者、领域专家、专利代理人、Agent

---

## 已完成的端到端测试

### 阶段 1：概念化与基线检索
- [x] 针对“AI × 煤化工”关键词，在 `scipatent-lifecycle` 的 Phase 1 下自动检索近 3 年的 5 篇顶刊文献
- [x] 识别研究缺口 (Research Gap) 并在 Gate 1 暂停输出，等待用户确认

### 阶段 2：论证与实验数据获取
- [x] 根据 Gate 1 的确认，使用 `nature-writing` 推演核心 Assertions
- [x] 汇总并梳理实验需要补充的数据图表，并在 Gate 2 阻断，等待用户填入真实数据

### 阶段 3：草稿撰写、润色与盲审
- [x] 获取数据后生成论文全文草稿，并在 `nature-polishing` 中通过 `ai-coal-chem.md` 开展术语去歧义和润色
- [x] 调用 `nature-reviewer` 执行模拟评审，并在 Gate 3 输出三专家严厉评审意见与 Hedging 策略

### 阶段 4：专利确权与客体校验
- [x] 调用 `patent-trans` 从论文草案中抽提方法与系统独立权利要求，运用法言法语进行转换
- [x] 调用 `patent-claim-check` 对草案执行 CNIPA 第 25 条合规性自检与引用链查错

---

## 最近完成

- [x] **2026-06-05** 执行可信协作优化：统一 6-Gate 规则，修复绘图路径与字体警告，新增证据政策、成果包规范、运行状态样例和 `pnpm run figures` 复现入口。
- [x] **2026-06-04** 优化主生命周期控制流，将科研绘图调整为 Phase 2 收集数据后必须、强制自动执行的步骤；引入项目配置控制文件 `scipatent_config.json` 实现了专利转化分支的持久化状态控制与会话动态选择。
- [x] **2026-06-04** 完成基于图神经网络预测煤气化合成气产率与炉膛温度场的端到端科研全生命周期测试（Phase 1 -> Phase 4，覆盖 6-Gate 主流程并输出最终专利技术交底书）
- [x] **2026-06-04** 对所有核心 `nature-skills` (Polishing, Writing, Reviewer, Response, Reader, Paper2PPT, Figure) 进行交叉领域适配，整合加载 `ai-coal-chem.md` 知识基座
- [x] **2026-06-04** 创建全局重定向工作流 `.agents/workflows/scipatent-lifecycle.md` 以支持根级 `/scipatent-lifecycle` 斜杠命令 of the repo
- [x] **2026-06-04** 研发专利双引擎 Skill：`patent-trans` (学术转专利) 与 `patent-claim-check` (权利要求自检)
- [x] **2026-06-04** 创建交叉领域核心知识基座 `skills/_shared/domain/ai-coal-chem.md`
- [x] **2026-06-04** 架构重大决策：全面放弃 Web UI，改为纯 Agent Workflow (UI-less) 的自治编排架构，更新 MEMORY.md 与 AGENTS.md 约束
- [x] **2026-06-01** 搭建 UI 高保真原型大屏与脚手架环境配置（已冻结/冷缩）

---

*最后更新：2026-06-05*
