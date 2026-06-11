# 任务跟踪

状态标记：`[ ]` 待办 | `[/]` 进行中 | `[x]` 已完成

---

## 进行中

- [/] **Sprint 4：Science Workflow 商业化转向**

---

## 待办

### Sprint 4：Science Workflow 商业化转向
- [x] 新建 `feature/science-workflow` 分支
- [x] 将产品主线改写为通用科研写作 + 可切换行业包
- [x] 将 README、MEMORY、ARCHITECTURE 主定位调整为 Science Workflow
- [x] 将专利能力降为 extension/plugin，不再作为主流程卖点
- [x] 将煤化工/能源化工降为默认示例行业包
- [x] 新增 `science-workflow.md` 项目级主入口
- [x] 新增根级 `/science-workflow` 重定向工作流
- [x] 将 DELIVERABLES 拆分为 Journal Package、Thesis Package、Patent Extension Package
- [x] 扩展 EVIDENCE_POLICY，加入导师意见、引用核验、查重风险和 AI 辅助边界
- [x] 新增真实数据 intake、引用核验、章节计划、导师意见响应、返修行动模板
- [ ] 为 `nature-academic-search` MCP 增加本地测试环境说明，并明确 pytest/依赖安装方式
- [ ] 为 Phase 1 文献基线增加 DOI、年份、来源的逐条核验清单

### Sprint 5：真实用户交付验证
- [ ] 用通用 SCI 论文题目 dry-run 到 Gate 2，确认不生成伪数据
- [ ] 用煤化工 SCI 论文题目 dry-run 到 Gate 2，确认行业包可选接入
- [ ] 用硕士论文题目 dry-run 到章节计划，确认导师意见响应结构可用
- [ ] 将专利 extension 触发条件写入测试说明

---

## 已完成的历史工作

- [x] **2026-06-05** 执行可信协作优化：统一 Gate 规则，修复绘图路径与字体警告，新增证据政策、成果包规范、运行状态样例和 `pnpm run figures` 复现入口。
- [x] **2026-06-04** 架构重大决策：全面放弃 Web UI，改为纯 Agent Workflow 的自治编排架构。
- [x] **2026-06-04** 完成基于图神经网络预测煤气化合成气产率与炉膛温度场的端到端测试。
- [x] **2026-06-04** 研发专利双引擎 Skill：`patent-trans` 与 `patent-claim-check`。
- [x] **2026-06-04** 创建交叉领域核心知识基座 `skills/_shared/domain/ai-coal-chem.md`。

---

*最后更新：2026-06-09*
