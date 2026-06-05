# 学术论文与专利协作平台 (SciPatent)

> 基于 AI Flows 框架孵化的**纯 Agent 编排 (UI-less) 全生命周期科研自治协作系统**。集成 Nature 级学术写作与盲审标准，并提供交叉学科（AI × 煤化工）向专利技术交底书的转化与致命合规漏洞自检。

---

## 🎨 核心特性

*   **⚡ 6-Gate 流程门槛与自适应控制流**
    系统在主控工作流中硬编码了 6 个关键的人工审核门槛与分支分流节点，兼顾了科学的严谨度与流程的控制灵活性：
    1.  🛑 **Gate 1: 立意与文献基线确认** —— 锁定研究创新点与 Research Gap。
    2.  🛑 **Gate 2: 核心证据与数据确认** —— 用户提供真实或仿真数据（**AI 绝不编造实验数据**）。
    3.  🛑 **Gate 2b: 科研图表确认** —— 自动触发绘制符合 Nature 规范的高清矢量图，通过审核才可起草全文。
    4.  🛑 **Gate 3: 盲审结论与修回策略确认** —— 模拟 3 专家严厉盲审，制定 Hedging 与补足修回对策。
    5.  🛑 **Gate 3b: 专利转化自主选择** —— 读取配置文件并读取用户意愿，智能判定是否跳过专利确权步骤。
    6.  🛑 **Gate 4: 专利保护范围确认** —— 抽取权利要求并执行合规排查，确认硬件控制边界。
*   **📈 强制性科研作图贯穿**
    在阶段 2 数据就绪后，系统**无条件且自动地**调用 `nature-figure` 技能，通过 Python 自动生成符合 Nature 出图规范的 3D 温度场、瞬态产率及 OOD 消融高清图表（SVG/PNG 格式，并输出至 `docs/figures/`），以直观数据支撑论文论断。
*   **⚙️ 持久化配置控制层**
    通过项目根目录下的 `scipatent_config.json` 持久化管理用户的流程选择。支持在会话中通过自然语言直接更改配置（如“跳过专利转化”），实现动态、零侵入的分流交互。
*   **📘 领域大脑底座 (Domain base)**
    引入 `ai-coal-chem.md` 交叉学科规则库，为所有引擎强制静默加载背景上下文：
    - **防混淆协议**：规避“神经网络节点代表煤炭”等模糊表述，映射为空间控制体网格与传感器测点。
    - **CNIPA 客体红线**：算法申请专利时，强制绑定物理输入（传感器）与物理输出（流量调节阀），构成硬件反馈闭环以规避“智力活动规则”驳回。
*   **✨ 专利双引擎 (Patent Suite)**
    - **学术转专利** (`patent-trans`)：抽取论文方法，快速翻译为带“其特征在于”引导的法言法语权利要求书。
    - **客体合规自检** (`patent-claim-check`)：深度校验引用断层与不合规项，内部重写直至安全。
*   **❄️ [已冷冻] 备用 Web UI 原型**
    本项目前期的科幻深海蓝玻璃拟态（Vite + Ollama 跨域代理）Web 原型已被就地冻结并作为可视化演示参考进行归档，全面让位于 Agent 自治流水线。

---

## 🏗️ 目录结构说明

```text
paper-patent-assistant/
├── .agents/
│   └── workflows/
│       └── scipatent-lifecycle.md  # 项目主控全生命周期工作流 (6-Gate 神经中枢)
├── docs/
│   ├── ARCHITECTURE.md             # 系统交互与 Mermaid 架构图
│   ├── DELIVERABLES.md             # 成果包、运行状态与交付规范
│   ├── EVIDENCE_POLICY.md          # 数据/引用/实验来源分级规则
│   ├── RUN_STATE.example.json      # 生命周期恢复与审计状态样例
│   ├── RUN_STATE.current.json      # 当前优化与验证状态
│   ├── paper_draft.md              # 经 Nature 润色修回的论文初稿 (Abstract/Methods/Results)
│   ├── patent_draft.md             # 经合规校验生成的独立/从属权利要求书
│   ├── technical_disclosure.md     # CNIPA 格式专利技术交底书
│   ├── ppt_outline.md              # 用于 Journal Club 的学术汇报大纲
│   └── figures/                    # 高清科研图表导出目录 (SVG/PDF/PNG)
│
├── memory/                         # 本项目级记忆与任务跟踪
│   ├── tasks.md                    # 任务追踪清单
│   └── 2026-06-04.md               # 重大重构与控制流优化工作日志
│
├── scripts/                        # 物理与化工仿真作图脚本
│   └── plot_figures.py             # Python 科学计算出图脚本 (matplotlib)
│
├── scipatent_config.json           # 流程运行时分支控制配置文件
│
└── skills/                         # 科研与专利底层规则引擎
    ├── _shared/domain/
    │   └── ai-coal-chem.md        # 煤化工领域大脑底座
    ├── nature-figure/              # Nature 级科研配图设计与生成
    ├── nature-polishing/           # 12 步 Nature 学术润色引擎
    ├── nature-reviewer/            # 三专家盲审评估模型
    ├── patent-trans/               # 学术转专利独立/从属权利要求
    └── patent-claim-check/         # 专利客体与引用缺陷排查
```

---

## 🚀 使用指南

### 1. 触发主控工作流
在 IDE 内或通过本仓库助理，输入以下命令即可一键触发：
```text
/scipatent-lifecycle 帮我探索一个基于图神经网络预测气化炉温度场的工作流
```
Agent 会自动将焦点重定向并载入当前项目的 `scipatent-lifecycle.md`，开始引导您经历阶段一至阶段四。

### 2. 配置分支流向
您可以直接编辑项目根目录下的 [scipatent_config.json](file:///d:/Projects/AI%20Flows/projects/paper-patent-assistant/scipatent_config.json) 控制分支，也可以在会话中随时指示 Agent。

*   **例如选择跳过专利确权**：
    在盲审评估后，如果不想进行专利转化，可在对话中说：
    > *“跳过专利转化分支，直接生成学术成果包。”*
    Agent 会自动将配置文件中的 `"patent_transformation.enabled"` 修改为 `false`，并跳过阶段四，为您直接整理出定稿论文、高清图表与汇报大纲。

### 3. 复现科研图表
在项目目录中运行：

```powershell
pnpm run figures
```

该命令会通过 `uv` 临时解析 `numpy` 与 `matplotlib`，并将图表稳定输出到 `docs/figures/`。模拟数据生成的图表仅用于演示和端到端测试；真实论文或专利交付必须按 `docs/EVIDENCE_POLICY.md` 标注证据等级。

---

## 🤝 致谢

本项目的学术分析、盲审与润色规则底座克隆并适配自上海交通大学袁一哲博士团队的开源仓库 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills.git)。在此向其优秀的学术 Prompt 框架设计表示诚挚致谢！
