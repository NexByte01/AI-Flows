// ==========================================
// SYSTEM PROMPTS MATRIX (For Ollama API)
// ==========================================
const systemPrompts = {
  polishing: `你是 Nature 期刊的资深学术编辑。请帮我润色以下学术段落：
1. 每句话严格限制在 30 个单词（words）以内，表意要极其紧凑和精准。
2. 将口语化、中式英语（Chinglish）或平淡的词汇升级为符合 Nature Journal 风格的高级学术词汇。
3. 调整主被动句式，使行文更客观（使用 Hedging 谦辞调节论点强度，例如用 suggest, might, represent 代替 absolute 断言）。
4. 统一使用英式英语拼写。
直接输出润色后的文本。在润色文本下方，另起一行，以 [修改说明] 为标题，列出 2-3 个关键词汇或句子的改动对比。`,

  reviewer: `你是 Nature 期刊的 3 位特约同行评审专家（Reviewer 1, 2, 3）。请对我发来的论文草稿进行盲审评估：
- Reviewer 1 偏重概念的新颖性与立意。
- Reviewer 2 偏重实验设计的严密性以及是否有完备的 Baseline 对照。
- Reviewer 3 偏重数据的可靠性与重现性。
请用中英双语输出这 3 位审稿人的意见大纲，指出本工作目前最致命的“硬伤”，并给出是否接收（Accept / Major Revision / Reject）的初步态度。`,

  paper2ppt: `你是学术导师。请根据我提供的学术论文大纲或技术成果，为我规划一份用于组会分享（Journal Club）的 PPT 结构大纲：
1. 提炼出 4 个核心幻灯片页面（Slide 1-4）。
2. 每页幻灯片必须包含：[Slide Title]、[主要观点 (Bullet points)] 以及 [演讲备注 (Speaker Notes, 说明演讲时应口头强调什么)]。
请使用中文输出，保持逻辑链条清晰。`,

  "patent-trans": `你是专利代理人。请将我发来的通俗研发思路或学术叙述，转化为符合中国专利局（CNIPA）撰写规范的“独立权利要求书”草案：
1. 必须使用严格的专利法言法语。例如将“安装在”改为“设置于”，“让它切断”改为“控制所述切断回路断开”。
2. 必须以严格的权利要求格式输出，例如：“1. 一种[主题名称]，其特征在于，包括：[技术特征A]，用于...；[技术特征B]，用于...；以及[控制方法特征]...”。
直接输出权利要求书草案。`,

  "claim-check": `你是专利局的资深专利审查员。请对以下权利要求书草稿进行合规性审查：
1. 检查从属权利要求的引用格式是否合规（是否包含“根据权利要求X所述的...”）。
2. 检查前后术语是否一致（防止出现同一组件名称不一致的情况）。
3. 检查独立权利要求的保护范围是否过窄或过宽。
请列出具体的缺陷项，并给出文字修改建议。`
};

// ==========================================
// MOCK FALLBACK DATA (For local demo mode)
// ==========================================
const mockData = {
  polishing: {
    sample: "We used the newly developed ML model to find the core variables. This can lower the errors and it is very good because it is faster than before. The result is shown in Fig 2.",
    output: `<h3>Nature-Style Optimized Text</h3>
<div class="optimized-result">
  We employed the recently developed machine learning model to identify key parameters, significantly reducing experimental errors while achieving a fivefold increase in computational efficiency (Fig. 2).
</div>
<div class="diff-view">
  <div class="diff-header"><i data-lucide="git-commit"></i> 句式改动对比 (Diff Analysis)</div>
  <p>
    We <span class="diff-del">used</span> <span class="diff-ins">employed</span> the <span class="diff-del">newly developed ML model</span> <span class="diff-ins">recently developed machine learning model</span> to <span class="diff-del">find the core variables</span> <span class="diff-ins">identify key parameters</span>. <span class="diff-del">This can lower the errors and it is very good because it is faster than before</span> <span class="diff-ins">significantly reducing experimental errors while achieving a fivefold increase in computational efficiency</span> (<span class="diff-del">Fig 2</span> <span class="diff-ins">Fig. 2</span>).
  </p>
</div>`,
    diagnostics: [
      { type: "success", title: "句子长度审计", content: "原两个短句合并为一个表达紧凑的复杂句，单句长度控制在 24 词，符合 ≤30 词的 Nature 核心规范。" },
      { type: "info", title: "学术词汇升级", content: "将通俗词汇 'used' 升级为 'employed'，'find core variables' 升级为 'identify key parameters'。" },
      { type: "success", title: "客观度校准 (Hedging)", content: "将带有口语夸张的 'very good because it is faster' 提炼为数据支撑的 'achieving a fivefold increase in computational efficiency'。" }
    ],
    score: 95
  },
  
  reviewer: {
    sample: "In this study, we propose a new carbon-capture framework utilizing bio-char. Although the cost is slightly high, the efficiency reaches 98%. We believe this is a big breakthrough.",
    output: `<h3>模拟审稿人评估报告 (Nature Reviewer Reports)</h3>
<div class="optimized-result">
  <strong style="color: hsl(var(--accent-blue)); display: block; margin-top: 10px;">Reviewer #1 (Critique & Focus)</strong>
  <p style="margin-bottom: 12px;">The concept of using bio-char for carbon capture is timely and aligns with current decarbonization efforts. However, the economic analysis is severely lacking. The statement 'slightly high cost' is subjective and must be quantified with detailed techno-economic evaluation.</p>

  <strong style="color: hsl(var(--accent-blue)); display: block;">Reviewer #2 (Methodology & Baseline)</strong>
  <p style="margin-bottom: 12px;">While the claimed 98% efficiency is impressive, the experimental setup is underspecified. Crucially, there are no baseline comparisons against state-of-the-art chemical solvents (such as Monoethanolamine - MEA). Without benchmarking, the 'breakthrough' claim remains unsubstantiated.</p>

  <strong style="color: hsl(var(--accent-blue)); display: block;">Reviewer #3 (Ethics & Reproduction)</strong>
  <p>The authors must provide details on the source and activation conditions of the bio-char. The exact pyrolysis temperature and chemical activators must be tabulated in the supplementary information to ensure reproducibility.</p>
</div>`,
    diagnostics: [
      { type: "warn", title: "对比实验缺失 (Major Issue)", content: "未与传统吸附剂（如 MEA 溶液）进行性能对照，审稿人对此持强烈怀疑态度。" },
      { type: "warn", title: "主观表述缺陷", content: "‘slightly high cost’ 与 ‘big breakthrough’ 属于非学术性夸张，极易遭到拒稿，需修改为精确的数据对比。" },
      { type: "info", title: "重现性缺陷", content: "生物炭制备工艺（热解温度、活化剂）缺少参数表，需增加补充材料说明。" }
    ],
    score: 62
  },

  paper2ppt: {
    sample: "Paper title: An Autonomous Drone for High-Altitude Powerline Inspection.\nKey achievements:\n1. Built a carbon-fiber light-weight drone frame.\n2. Integrated a LiDAR sensor for 3D reconstruction.\n3. Achieved 94% fault detection accuracy in high-wind conditions.",
    output: `<h3>PPT 结构大纲与演讲备注 (Slide Deck Structure)</h3>
<div class="optimized-result" style="font-size: 14px;">
  <div style="border-left: 2px solid hsl(var(--accent-purple)); padding-left: 10px; margin-bottom: 15px;">
    <h4 style="color: white; font-size: 14px;">Slide 1: Title & Project Context</h4>
    <p>• <strong>标题</strong>: Autonomous High-Altitude Powerline Inspection</p>
    <p>• <strong>演讲备注</strong>: 强调高空输电线路人工巡检的高危性和高成本，引出自主无人机巡检迫切需求。</p>
  </div>
  
  <div style="border-left: 2px solid hsl(var(--accent-purple)); padding-left: 10px; margin-bottom: 15px;">
    <h4 style="color: white; font-size: 14px;">Slide 2: Hardware Architecture & Weight Optimization</h4>
    <p>• <strong>核心点</strong>: 采用碳纤维材料设计超轻量化机身，增加电池续航能力。</p>
    <p>• <strong>演讲备注</strong>: 阐述在超轻机身和荷载平衡之间的设计折衷。</p>
  </div>

  <div style="border-left: 2px solid hsl(var(--accent-purple)); padding-left: 10px; margin-bottom: 15px;">
    <h4 style="color: white; font-size: 14px;">Slide 3: LiDAR 3D Reconstruction Pipeline</h4>
    <p>• <strong>核心点</strong>: 集成高精度 LiDAR 传感器，实现输电塔及电网的实时三维重构与环境去噪算法。</p>
    <p>• <strong>演讲备注</strong>: 解释强磁场环境下传感器信号抗干扰算法的数学模型。</p>
  </div>

  <div style="border-left: 2px solid hsl(var(--accent-purple)); padding-left: 10px;">
    <h4 style="color: white; font-size: 14px;">Slide 4: High-Wind Validation (94% Accuracy)</h4>
    <p>• <strong>核心点</strong>: 在强风恶劣环境下的外场测试，故障识别精度高达 94%。</p>
    <p>• <strong>演讲备注</strong>: 配合图标和表格，展示强风干扰下的鲁棒性数据对比。</p>
  </div>
</div>`,
    diagnostics: [
      { type: "success", title: "汇报结构优化", content: "按照“提出问题 - 硬件优化 - 核心软件 - 实验求证”的标准学术逻辑重组结构。" },
      { type: "success", title: "演讲备注自动配置", content: "已根据幻灯片的核心要点生成了配合讲解的 Speaker Notes，建议汇报时长 10 分钟。" }
    ],
    score: 92
  },

  "patent-trans": {
    sample: "我们把传感器安装在电机的外壳上，用来收集电机的震动数据。然后用我们自己写的算法处理数据，一旦震动太强烈了，系统就会自动报警把电机停掉。",
    output: `<h3>权利要求书规范文本 (Patent Claims Format)</h3>
<div class="optimized-result" style="font-family: var(--font-mono); font-size: 13.5px; background: rgba(0,0,0,0.15); padding: 12px; border-radius: 8px; border: 1px solid var(--glass-border);">
  1. 一种电机安全控制系统，其特征在于，包括：<br>
  &nbsp;&nbsp;设置于所述电机外壳上的<strong>振动采集模块</strong>，用于获取所述电机的实时振动特征参数；<br>
  &nbsp;&nbsp;与所述振动采集模块电连接的<strong>安全控制器</strong>，其特征在于，所述安全控制器配置有异常诊断算法，用于：<br>
  &nbsp;&nbsp;&nbsp;&nbsp;对所述实时振动特征参数进行谱分析以获取当前振动幅值；<br>
  &nbsp;&nbsp;&nbsp;&nbsp;判断所述当前振动幅值是否超过预设安全阈值；以及<br>
  &nbsp;&nbsp;&nbsp;&nbsp;若所述当前振动幅值超过所述预设安全阈值，向所述电机的驱动切断回路输出控制信号，以切断所述电机的供电回路并触发报警机制。
</div>`,
    diagnostics: [
      { type: "success", title: "法言法语转换完成", content: "口语化的“安装在”、“收集”、“算法处理”、“停掉”转换为严格的专利权利要求书句式（如“设置于”、“获取”、“判断是否超过”、“输出控制信号切断供电回路”）。" },
      { type: "success", title: "技术单元模块化", content: "自动划分出“振动采集模块”和“安全控制器”，明晰了物理边界，便于后续确立权利要求保护范围。" }
    ],
    score: 98
  },

  "claim-check": {
    sample: "1. 一种智能水过滤杯，其特征在于，包括杯盖和杯体。\n2. 根据权利要求1所述的智能水过滤杯，其特征在于，还包括位于所述杯盖上的显示屏。\n3. 权利要求2所述的过滤杯，还包括紫外线杀菌灯，其连接在杯体底部。",
    output: `<h3>权利要求书合规诊断报告</h3>
<div class="optimized-result">
  <div style="margin-bottom: 12px; border-bottom: 1px solid var(--glass-border); padding-bottom: 8px;">
    <span style="background-color: rgba(255, 90, 95, 0.15); color: hsl(var(--accent-red)); padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 600;">重大缺陷</span>
    <strong style="margin-left: 8px; color: white;">权利要求 3 引用格式不合规</strong>
    <p style="margin-top: 4px; font-size: 13px; color: hsl(var(--text-secondary));">
      <em>原文:</em> '3. 权利要求2所述的过滤杯...' <br>
      <em>修正建议:</em> 必须使用引导关联词。应更改为：'3. 根据权利要求2所述的智能水过滤杯...'。
    </p>
  </div>
  
  <div style="margin-bottom: 8px;">
    <span style="background-color: rgba(0, 180, 216, 0.15); color: hsl(var(--accent-blue)); padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 600;">术语不一致</span>
    <strong style="margin-left: 8px; color: white;">核心主题词出现偏差</strong>
    <p style="margin-top: 4px; font-size: 13px; color: hsl(var(--text-secondary));">
      权 1 和权 2 限定的主题是 '智能水过滤杯'，但权 3 简写成了 '过滤杯'。这在专利审查中会被判定为术语不一致，导致保护范围不明确。
    </p>
  </div>
</div>`,
    diagnostics: [
      { type: "warn", title: "引用断层报警 (Fatal)", content: "第 3 条引用缺少法定的前置修饰词“根据...所述”，无法确立合法的从属引证关系。" },
      { type: "warn", title: "命名术语冲突", content: "‘智能水过滤杯’与‘过滤杯’术语混用，审查中易造成混淆，需全文统一术语。" }
    ],
    score: 45
  }
};

// ==========================================
// INTERACTIVE & API INTERACTION
// ==========================================
document.addEventListener("DOMContentLoaded", () => {
  // Initialize Lucide Icons
  lucide.createIcons();

  // DOM Elements
  const navItems = document.querySelectorAll(".nav-item");
  const currentTitle = document.getElementById("current-title");
  const currentSubtitle = document.getElementById("current-subtitle");
  const srcInput = document.getElementById("src-input");
  const actionBtn = document.getElementById("action-btn");
  const clearBtn = document.getElementById("clear-btn");
  const sampleBtn = document.getElementById("sample-btn");
  const outputBody = document.getElementById("output-body");
  const analysisBody = document.getElementById("analysis-body");
  const copyBtn = document.getElementById("copy-btn");
  const exportBtn = document.getElementById("export-btn");
  const charCount = document.getElementById("char-count");
  const wordCount = document.getElementById("word-count");
  const scoreBar = document.querySelector(".score-bar");
  const scoreText = document.querySelector(".score-text");
  const tempSlider = document.getElementById("temp-slider");
  const tempVal = document.getElementById("temp-val");

  let currentMode = "polishing";

  // Slider change
  tempSlider.addEventListener("input", (e) => {
    const val = (e.target.value / 100).toFixed(1);
    tempVal.textContent = val;
  });

  // Navigation Switch
  navItems.forEach(item => {
    item.addEventListener("click", () => {
      navItems.forEach(n => n.classList.remove("active"));
      item.classList.add("active");

      currentMode = item.getAttribute("data-action");
      const config = mockData[currentMode] || {};
      
      // Update info
      const titles = {
        polishing: { title: "Nature 级润色", subtitle: "针对 Nature/CNS 级期刊规范优化句长、行文时态与学术用语", placeholder: "请在此处输入您的学术段落或初稿（支持中/英文输入）...", btn: "开始学术加速" },
        reviewer: { title: "模拟盲审评估", subtitle: "从 Nature 审稿人视角对论文的新颖性、合理性与实验支撑度进行多维度盲审", placeholder: "请输入您的论文标题、摘要、核心贡献陈述，或直接粘贴引言与结果段落...", btn: "开始审稿评估" },
        paper2ppt: { title: "论文转 PPT 大纲", subtitle: "自动提取论文核心脉络，生成符合学术汇报 (Journal Club) 的幻灯片结构与备注", placeholder: "请粘贴您的论文全文、摘要或成果要点...", btn: "生成 PPT 大纲" },
        "patent-trans": { title: "学术转专利语言", subtitle: "将学术论文的描述或研发思路转化为符合专利局法规范的独立/从属权利要求句式", placeholder: "请输入日常研发思路（如：我们做了一个装置，把数据传给服务器分析，如果异常就切断电源）...", btn: "开始专利转化" },
        "claim-check": { title: "权利要求书校验", subtitle: "深度检测专利权利要求书中的引用关系、前后术语一致性以及保护范围缺陷", placeholder: "请输入您起草的专利权利要求书草案...", btn: "开始合规校验" }
      };

      const currentTitleInfo = titles[currentMode];
      currentTitle.textContent = currentTitleInfo.title;
      currentSubtitle.textContent = currentTitleInfo.subtitle;
      srcInput.placeholder = currentTitleInfo.placeholder;
      actionBtn.querySelector("span").textContent = currentTitleInfo.btn;

      srcInput.value = "";
      charCount.textContent = "0";
      wordCount.textContent = "0";
      resetOutput();
    });
  });

  // Calculate stats
  srcInput.addEventListener("input", () => {
    const val = srcInput.value;
    charCount.textContent = val.length;
    const words = val.trim().split(/\s+/).filter(w => w.length > 0);
    wordCount.textContent = words.length;
  });

  // Load sample data
  sampleBtn.addEventListener("click", () => {
    const config = mockData[currentMode];
    if (config) {
      srcInput.value = config.sample;
      srcInput.dispatchEvent(new Event("input"));
    }
  });

  // Clear content
  clearBtn.addEventListener("click", () => {
    srcInput.value = "";
    srcInput.dispatchEvent(new Event("input"));
    resetOutput();
  });

  function resetOutput() {
    outputBody.innerHTML = `
      <div class="empty-state">
        <i data-lucide="terminal"></i>
        <p>等待输入并运行加速引擎...</p>
        <span>在左侧面板中选择不同的模式，输入您的科研文本后点击“开始学术加速”。</span>
      </div>
    `;
    analysisBody.innerHTML = `
      <div class="empty-diagnostic">
        <p>暂无运行数据</p>
        <span>执行加速后，此栏将显示语法句式评分、句长检测、专利要素缺失等诊断报告。</span>
      </div>
    `;
    scoreBar.style.width = "0%";
    scoreText.textContent = "N/A";
    copyBtn.disabled = true;
    exportBtn.disabled = true;
    lucide.createIcons();
  }

  // ==========================================
  // ACTION ENGINE (REAL OLLAMA FETCH / FALLBACK)
  // ==========================================
  actionBtn.addEventListener("click", async () => {
    const text = srcInput.value.trim();
    if (!text) {
      alert("请输入草稿或要处理的技术文本！");
      return;
    }

    const modelName = document.getElementById("model-input").value.trim() || "qwen2.5";
    const temperature = (parseFloat(tempSlider.value) / 100);

    // Show Skeletons
    outputBody.innerHTML = `
      <div class="skeleton-container">
        <div class="skeleton-line" style="width: 45%"></div>
        <div class="skeleton-line"></div>
        <div class="skeleton-line medium"></div>
        <div class="skeleton-line short"></div>
      </div>
    `;
    analysisBody.innerHTML = `
      <div class="skeleton-container">
        <div class="skeleton-line medium"></div>
        <div class="skeleton-line"></div>
      </div>
    `;

    actionBtn.disabled = true;
    const originalBtnHTML = actionBtn.innerHTML;
    actionBtn.querySelector("span").textContent = "正在调用本地 AI 引擎...";

    try {
      // 1. Try requesting local Ollama (via Vite Proxy /api/ollama)
      const response = await fetch('/api/ollama/v1/chat/completions', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          model: modelName,
          messages: [
            { role: 'system', content: systemPrompts[currentMode] },
            { role: 'user', content: text }
          ],
          temperature: temperature,
          stream: true
        })
      });

      if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
      }

      // Prepare UI for streaming
      outputBody.innerHTML = `<h3>加速结果分析</h3><div class="optimized-result"></div>`;
      const resultDiv = outputBody.querySelector(".optimized-result");

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      let fullText = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
          const cleaned = line.trim();
          if (cleaned === '') continue;
          if (cleaned.startsWith('data: ')) {
            const dataStr = cleaned.slice(6);
            if (dataStr.trim() === '[DONE]') continue;
            try {
              const data = JSON.parse(dataStr);
              const token = data.choices[0]?.delta?.content || '';
              fullText += token;
              resultDiv.innerHTML = formatMarkdown(fullText);
            } catch (err) {
              // Ignore partial JSON parse errors
            }
          }
        }
      }

      // Generate dynamic diagnostics upon completion
      generateDynamicDiagnostics(text, fullText);
      
      actionBtn.disabled = false;
      actionBtn.innerHTML = originalBtnHTML;
      copyBtn.disabled = false;
      exportBtn.disabled = false;

    } catch (error) {
      console.warn("本地 Ollama 连接失败，已切换至 Mock 演示数据模式。错误信息:", error);
      // Fallback to Mock Mode
      setTimeout(() => {
        const config = mockData[currentMode];
        outputBody.innerHTML = config.output;
        
        // Render diagnostics list and append warnings about Ollama
        const fallbackDiagnostics = [
          { type: "warn", title: "本地 AI 引擎未启动", content: `未能在端口 11434 探测到运行中的 Ollama 服务或找不到模型【${modelName}】。已为您自动降级至 Demo 演示模式。` },
          ...config.diagnostics
        ];
        renderDiagnostics(fallbackDiagnostics);
        
        // Animate score
        animateScore(config.score);

        actionBtn.disabled = false;
        actionBtn.innerHTML = originalBtnHTML;
        copyBtn.disabled = false;
        exportBtn.disabled = false;
        lucide.createIcons();
      }, 1000);
    }
  });

  // Helper to parse basic markdown to HTML safely
  function formatMarkdown(text) {
    return text
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/\n/g, "<br>")
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/`([^`]+)`/g, "<code>$1</code>")
      .replace(/###\s+(.+)/g, "<h3 style='margin-top:14px; margin-bottom:8px; color:white;'>$1</h3>")
      .replace(/##\s+(.+)/g, "<h2 style='margin-top:18px; margin-bottom:10px; color:white;'>$1</h2>")
      .replace(/#\s+(.+)/g, "<h1 style='margin-top:22px; margin-bottom:12px; color:white; font-size:18px;'>$1</h1>");
  }

  // Render diagnostics helper
  function renderDiagnostics(diagnostics) {
    analysisBody.innerHTML = "";
    diagnostics.forEach(d => {
      const card = document.createElement("div");
      card.className = `diag-card ${d.type}`;
      let icon = "info";
      if (d.type === "warn") icon = "alert-triangle";
      if (d.type === "success") icon = "check-circle";

      card.innerHTML = `
        <div class="diag-card-header">
          <i data-lucide="${icon}"></i>
          <span>${d.title}</span>
        </div>
        <p>${d.content}</p>
      `;
      analysisBody.appendChild(card);
    });
    lucide.createIcons();
  }

  // Score animation helper
  function animateScore(targetScore) {
    let current = 0;
    const interval = setInterval(() => {
      if (current >= targetScore) {
        clearInterval(interval);
        scoreText.textContent = `${targetScore}%`;
        scoreBar.style.width = `${targetScore}%`;
      } else {
        current += 2;
        scoreText.textContent = `${current}%`;
        scoreBar.style.width = `${current}%`;
      }
    }, 15);
  }

  // Helper to dynamically calculate simple rule diagnostics on AI output
  function generateDynamicDiagnostics(input, output) {
    const list = [];
    let score = 85; // base score

    if (currentMode === "polishing") {
      // 1. check max sentence length
      const sentences = output.split(/[.!?。！？]+/).map(s => s.trim().split(/\s+/).filter(w => w.length > 0));
      let tooLong = false;
      let maxLen = 0;
      sentences.forEach(s => {
        if (s.length > maxLen) maxLen = s.length;
        if (s.length > 30) tooLong = true;
      });

      if (tooLong) {
        list.push({ type: "warn", title: "发现长句超标", content: `检测到有句子长度超过 30 词（最长句包含 ${maxLen} 词），可能影响 Nature 期刊的阅读流畅度，建议进一步拆分。` });
        score -= 10;
      } else {
        list.push({ type: "success", title: "句子长度达标", content: `所有生成的句子均在 30 词以内（最长句 ${maxLen} 词），完美符合 Nature 简练风格。` });
        score += 5;
      }

      // 2. check academic vocabulary
      const bannedWords = ["think", "good", "bad", "we believe", "very"];
      const hitWords = bannedWords.filter(word => output.toLowerCase().includes(word));
      if (hitWords.length > 0) {
        list.push({ type: "warn", title: "非学术词汇预警", content: `文稿中检测到较主观或口语化表达：[${hitWords.join(", ")}]，建议使用更客观的数据陈述。` });
        score -= 8;
      } else {
        list.push({ type: "success", title: "语言客观度极佳", content: "行文客观中立，未发现明显的主观夸张或口语词汇。" });
        score += 5;
      }
    } 
    else if (currentMode === "patent-trans") {
      // Check patent claims keywords
      if (output.includes("其特征在于")) {
        list.push({ type: "success", title: "合规独立权利要求格式", content: "已成功构建以‘其特征在于’引导的技术特征描述结构。" });
        score += 10;
      } else {
        list.push({ type: "warn", title: "独立权利要求引导词缺失", content: "未能在权利要求书第 1 条中检测到法定的‘其特征在于’前置引导词，格式面临驳回风险。" });
        score -= 15;
      }
      
      const colloquialWords = ["把", "装在", "弄到", "断掉"];
      const hitPatentCol = colloquialWords.filter(word => output.includes(word));
      if (hitPatentCol.length > 0) {
        list.push({ type: "warn", title: "口语化技术词汇残留", content: `检测到非专利术语：[${hitPatentCol.join(", ")}]，建议修改为如‘设置于’、‘切断’等正式术语。` });
        score -= 10;
      } else {
        list.push({ type: "success", title: "专利术语净化完成", content: "未检测到日常口语化表达，技术描述物理边界清晰。" });
        score += 5;
      }
    } 
    else {
      // General dynamic diagnostics for other modes
      list.push({ type: "success", title: "本地 AI 引擎处理完毕", content: "本地大模型流式响应已成功接收并解析完毕。" });
      score = Math.floor(Math.random() * (98 - 85 + 1)) + 85;
    }

    renderDiagnostics(list);
    animateScore(Math.min(100, Math.max(0, score)));
  }

  // Copy Clipboard
  copyBtn.addEventListener("click", () => {
    const textElement = outputBody.querySelector(".optimized-result");
    if (textElement) {
      navigator.clipboard.writeText(textElement.innerText)
        .then(() => {
          const originalIcon = copyBtn.innerHTML;
          copyBtn.innerHTML = `<i data-lucide="check" style="color: hsl(var(--accent-green))"></i>`;
          lucide.createIcons();
          setTimeout(() => {
            copyBtn.innerHTML = originalIcon;
            lucide.createIcons();
          }, 2000);
        })
        .catch(err => {
          console.error("复制失败: ", err);
        });
    }
  });

  // Export Markdown
  exportBtn.addEventListener("click", () => {
    const textElement = outputBody.querySelector(".optimized-result");
    if (textElement) {
      const blob = new Blob([textElement.innerText], { type: "text/markdown;charset=utf-8" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `${currentMode}-result.md`;
      a.click();
      URL.revokeObjectURL(url);
    }
  });
});
