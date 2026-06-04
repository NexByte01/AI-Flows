# 学术论文与专利协作平台 (SciPatent)

> 基于 AI Flows 框架孵化的“学术 + 专利”双引擎科研加速工作台。集成 Nature 级学术润色规范，并提供学术成果向专利技术交底书的一键转化与校验。

---

## 🎨 核心特性

*   **📘 学术论文加速引擎 (Nature Suite)**
    *   **Nature 级润色**：智能分析单句句长（控制在 30 词内），升级学术专业词汇，校准客观论点强度（Hedging）。
    *   **模拟盲审人评估**：从 3 位不同偏好的 Nature 审稿人视角评估概念创新性、对照实验完整性以及重现性硬伤。
    *   **论文转 PPT 大纲**：自动提取文献核心主线，生成用于组会分享（Journal Club）的幻灯片结构与演讲 Speaker Notes。
*   **📙 专利申请加速引擎 (Patent Suite)**
    *   **学术转专利语言**：将大白话的技术构想或学术描述，快速转化为符合 CNIPA 撰写规范、包含“其特征在于”引导的独立权利要求书。
    *   **权利要求书校验**：深度分析权利要求引证关系，识别“引用未定义前置词”或“术语不一致”等驳回高发瑕疵。
*   **⚡ 本地 AI 流式代理 (Proxy & Streaming)**
    *   **免 Key 安全请求**：配置了本地 Vite 反向代理，支持直连本地运行的 **Ollama** 服务，完全免除云端 API Key 泄露风险。
    *   **双轨制加载机制**：检测到本地 Ollama 启动时将流式打字输出真实 AI 结果；若未启动则在 1 秒内自动降级为 Demo 演示模式，引导本地部署。
*   **✨ 高保真现代 UI**
    *   科幻深海蓝配色体系配合 Glassmorphism 玻璃拟态卡片与动态加载骨架屏，符合 AI 操作系统的高审美标准。

---

## 🏗️ 目录结构说明

```text
paper-patent-assistant/
├── index.html              # 平台主页面入口
├── package.json            # 依赖包及 pnpm onlyBuiltDependencies 配置
├── vite.config.js          # Vite 构建配置（含 /api/ollama 跨域代理）
│
├── src/
│   ├── main.js             # 页面交互、Ollama 流式 fetch 及 Mock 降级引擎
│   └── style.css           # 视觉美化、玻璃拟态卡片及过渡动效
│
├── skills/                 # 学术规则库（克隆自 nature-skills 并清空 git 属性）
│   ├── _shared/            # 跨技能公共道德与措辞账本
│   ├── nature-polishing/   # 12 步润色法规则片段
│   ├── nature-reviewer/    # 三人审稿模板
│   └── ...                 # 其它引文、PPT 生成辅助模块
│
└── memory/                 # 本项目级记忆与任务跟踪
    ├── tasks.md            # 原子开发任务清单
    └── 2026-06-01.md       # 本项目启动日志
```

---

## 🚀 快速开始

### 1. 安装开发依赖
推荐使用 **pnpm** 安装依赖以跳过不必要的构建脚本编译：
```bash
# 进入项目路径
cd projects/paper-patent-assistant

# 使用 ignore-scripts 快速安装
pnpm install --ignore-scripts
```

### 2. 启动本地开发服务
```bash
pnpm dev
```
启动成功后，在浏览器访问：**[http://localhost:5173](http://localhost:5173)**。

### 3. 配置本地 AI 引擎（可选）
若需体验真实的 AI 润色与专利转换能力：
1. 下载并安装 [Ollama](https://ollama.com/)。
2. 启动大模型（例如 Qwen2.5）：
   ```bash
   ollama run qwen2.5
   ```
3. 在网页左侧配置面板中将“Ollama 本地模型名”输入为 `qwen2.5`，点击“开始加速”即可查看流式生成结果。

---

## 🤝 致谢

本项目的学术分析、盲审与润色规则底座克隆自公开开源仓库 [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills.git)（作者：上海交通大学袁一哲博士团队）。在此向其优秀的学术 Prompt 框架设计表示诚挚致谢！
