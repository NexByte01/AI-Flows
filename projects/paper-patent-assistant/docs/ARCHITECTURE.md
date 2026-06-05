# 学术论文与专利协作平台 架构文档 (SciPatent Architecture)

> last_verified: 2026-06-04

## 概览

学术论文与专利协作平台是一个**纯 Agent 编排 (UI-less) 的全生命周期科研协作系统**。它将学术写作润色、模拟盲审、学术转专利、以及专利合规性校验深度整合，专门针对**人工智能 × 计算机科学 × 煤化工**交叉学科领域。

## 技术栈与交互架构

系统放弃了传统的 Web 前端，全面转向**自治 Agent 工作流与底层技能包（Skills）相结合的编排模式**。

| 层级 | 选型 | 作用与职责 |
|---|---|---|
| **主控神经中枢 (Workflow)** | `scipatent-lifecycle.md` | 全生命周期科研流水线，串联各 Phase，硬编码 6 个人工确认与分支选择门槛 (Gates) |
| **配置控制层 (Config)** | `scipatent_config.json` | 存储运行时控制标志（如绘图后端、是否启用专利转化），支持分支控制流的持久化状态与交互式流向更新 |
| **证据治理层 (Evidence)** | `docs/EVIDENCE_POLICY.md` | 区分 Mock、Described、Verified、Real 四类证据，约束论文、图表和专利文本的可信边界 |
| **产物追踪层 (Deliverables)** | `docs/DELIVERABLES.md` + `RUN_STATE.current.json` | 记录每轮生命周期的 Gate 状态、输入证据、输出文件、验证命令和待人工确认事项 |
| **底层功能引擎 (Skills)** | Markdown Skills (Router & Static Fragments) | 提供学术检索、作图、润色、写作、盲审、专利翻译及权利要求校验的提示词/逻辑组件 |
| **领域专属大脑 (Domain)** | `_shared/domain/ai-coal-chem.md` | 提供交叉学科的防混淆协议与专利客体审查红线，作为所有引擎的强制性背景上下文 |

## 系统架构与数据流

```mermaid
graph TD
    User["用户 (User via Chat)"] <--> |指令与数据交互 / 6大 Gates 审批| MasterWorkflow["主控工作流 (scipatent-lifecycle.md)"]
    Config["控制配置 (scipatent_config.json)"] <--> |读取/更新状态| MasterWorkflow
    Evidence["证据规则 (EVIDENCE_POLICY.md)"] --> |约束数据等级| MasterWorkflow
    RunState["运行状态 (RUN_STATE)"] <--> |记录 Gate / 产物 / 验证| MasterWorkflow

    subgraph Core_Engine [底层科研与专利引擎]
        MasterWorkflow --> |1. 检索与精读| Search["文献检索 (nature-academic-search)"]
        MasterWorkflow --> |2. 骨架与起草| Writing["学术写作 (nature-writing)"]
        MasterWorkflow --> |3. 数据作图 [强制]| Figure["科研作图 (nature-figure)"]
        MasterWorkflow --> |4. 语言润色| Polishing["Nature 级润色 (nature-polishing)"]
        MasterWorkflow --> |5. 模拟盲审| Reviewer["三专家评审 (nature-reviewer)"]

        %% 分支判断
        MasterWorkflow -.-> |Gate 3b: 自主选择专利转化?| Decision{读取 config 决定是否转化?}
        Decision --> |是| PatentTrans["学术转专利 (patent-trans)"]
        Decision --> |是| PatentCheck["权利要求校验 (patent-claim-check)"]
        Decision --> |否| EndWorkflow["直达收尾与大纲 (nature-paper2ppt)"]
    end

    subgraph Shared_Knowledge [共享知识层]
        DomainBase["领域大脑 (ai-coal-chem.md)"] -.-> |强制约束 / 静态导入| Core_Engine
    end
```

## 目录结构

```text
paper-patent-assistant/
├── .agents/
│   └── workflows/
│       └── scipatent-lifecycle.md  # 项目主控全生命周期工作流
├── docs/
│   ├── ARCHITECTURE.md             # 本架构文档
│   ├── EVIDENCE_POLICY.md          # 证据等级与引用核验规则
│   ├── DELIVERABLES.md             # 成果包与运行状态规范
│   ├── RUN_STATE.example.json      # 生命周期状态样例
│   └── RUN_STATE.current.json      # 当前优化与验证状态
├── memory/
│   ├── tasks.md                    # 任务清单
│   ├── 2026-06-01.md               # 初始工作日志
│   └── 2026-06-04.md               # 重大重构与技能改造工作日志
├── scipatent_config.json           # 流程运行时分支控制配置文件
└── skills/
    ├── _shared/
    │   └── domain/
    │       └── ai-coal-chem.md    # AI × CS × 煤化工专属领域知识基座
    ├── nature-academic-search/     # 文献检索与验证
    ├── nature-figure/              # Nature 级科研配图设计与生成
    ├── nature-polishing/           # Nature 级学术润色
    ├── nature-writing/             # Nature 级学术写作与框架
    ├── nature-reviewer/            # 三专家盲审模拟
    ├── nature-response/            # 审稿意见回复
    ├── nature-reader/              # 文献阅读器
    ├── nature-paper2ppt/           # 成果汇报大纲生成
    ├── patent-trans/               # 学术转专利独立/从属权利要求
    └── patent-claim-check/         # 专利客体与合规性审查
```

## 变更日志

| 日期 | 变更 | 影响 |
|---|---|---|
| 2026-06-01 | 搭建 UI 原型与开发环境 | 完成 HTML 页面与 Vite 开发服务器配置（已冷冻，保留作为备用） |
| 2026-06-04 | 架构彻底重构，全面转为纯 Agent 编排 | 冻结前端开发，新建 `scipatent-lifecycle.md` 工作流与 6 个 Gate 节点，开发 `patent-trans`、`patent-claim-check`，创建交叉学科知识库 `ai-coal-chem.md` 并完成全量 nature 级技能的适配改造 |
| 2026-06-04 | 优化工作流：增加科研绘图与自选分支 | 优化 `scipatent-lifecycle.md`，融入 `nature-figure` 科研作图设计和 Gate 2b 确认门槛；引入 Gate 3b 分支选择，支持用户自由选择是否进入专利翻译和校验阶段 |
| 2026-06-04 | 优化控制流持久化与作图贯穿 | 强制科研作图在数据输入后必经执行并直达 Gate 2b，引入 `scipatent_config.json` 实现专利转化可选分支的状态持久化与动态交互更改 |
| 2026-06-05 | 增加可信协作层 | 补充证据分级、成果包追踪、运行状态样例与绘图复现约束，降低 Mock 数据误用和恢复上下文漂移风险 |
