#!/usr/bin/env node

/**
 * AI Flows — 初始化向导
 *
 * 跨平台配置脚本，仅使用 Node.js 内置模块。
 * 运行: node scripts/init.mjs
 */

import { createInterface } from 'node:readline';
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync, mkdirSync } from 'node:fs';
import { join, resolve } from 'node:path';

const ROOT = resolve(import.meta.dirname, '..');

// ─── Colors (ANSI) ───────────────────────────────────────────────────────────

const c = {
  reset: '\x1b[0m',
  bold: '\x1b[1m',
  dim: '\x1b[2m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  magenta: '\x1b[35m',
  red: '\x1b[31m',
};

// ─── Helpers ──────────────────────────────────────────────────────────────────

function banner() {
  console.log(`
${c.cyan}${c.bold}  ┌──────────────────────────────────────────┐
  │       AI Flows — 初始化向导               │
  │   可 fork 的 AI 项目操作系统              │
  └──────────────────────────────────────────┘${c.reset}
`);
}

function ask(rl, question, defaultValue = '') {
  const suffix = defaultValue ? ` ${c.dim}(${defaultValue})${c.reset}` : '';
  return new Promise((resolve) => {
    rl.question(`${c.green}?${c.reset} ${question}${suffix}: `, (answer) => {
      resolve(answer.trim() || defaultValue);
    });
  });
}

function askChoice(rl, question, choices) {
  console.log(`\n${c.green}?${c.reset} ${question}`);
  choices.forEach((ch, i) => {
    console.log(`  ${c.cyan}${i + 1}${c.reset}) ${ch.label}`);
  });
  return new Promise((resolve) => {
    rl.question(`${c.green}>${c.reset} Choose [1-${choices.length}]: `, (answer) => {
      const idx = parseInt(answer, 10) - 1;
      resolve(choices[idx >= 0 && idx < choices.length ? idx : 0].value);
    });
  });
}

function replaceInFile(filePath, replacements) {
  if (!existsSync(filePath)) return;
  let content = readFileSync(filePath, 'utf-8');
  for (const [search, replace] of Object.entries(replacements)) {
    content = content.replaceAll(search, replace);
  }
  writeFileSync(filePath, content, 'utf-8');
}

function walkFiles(dir, files = []) {
  if (!existsSync(dir)) return files;
  for (const entry of readdirSync(dir)) {
    const full = join(dir, entry);
    const stat = statSync(full);
    if (stat.isDirectory()) {
      if (entry === '.git' || entry === 'node_modules') continue;
      walkFiles(full, files);
    } else if (/\.(md|yml|yaml|json|mjs|js|ts|html|txt)$/i.test(entry)) {
      files.push(full);
    }
  }
  return files;
}

function todayISO() {
  return new Date().toISOString().slice(0, 10);
}

// ─── Main ─────────────────────────────────────────────────────────────────────

async function main() {
  banner();

  const rl = createInterface({ input: process.stdin, output: process.stdout });

  try {
    // ── Step 1: 收集配置信息 ───────────────────────────────────────────────

    console.log(`${c.bold}开始配置你的 AI Flows 工作空间。${c.reset}\n`);

    const brandName = await ask(rl, '项目 / 品牌名称', 'AI Flows');
    const agentName = await ask(rl, 'AI Agent 代号', 'Agent');
    const repoFullName = await ask(rl, 'GitHub 仓库地址 (owner/repo)', '');
    const lang = await askChoice(rl, '文档和日志的主要语言', [
      { label: '中文 (推荐)', value: 'zh' },
      { label: 'English', value: 'en' },
    ]);

    const today = todayISO();

    console.log(`\n${c.cyan}${c.bold}配置摘要${c.reset}`);
    console.log(`  品牌名称:   ${c.magenta}${brandName}${c.reset}`);
    console.log(`  Agent 代号: ${c.magenta}${agentName}${c.reset}`);
    console.log(`  仓库地址:   ${c.magenta}${repoFullName || '(未设置)'}${c.reset}`);
    console.log(`  主要语言:   ${c.magenta}${lang === 'zh' ? '中文' : 'English'}${c.reset}`);
    console.log(`  日期:       ${c.magenta}${today}${c.reset}`);

    const confirm = await ask(rl, '\n确认使用以上配置？(y/n)', 'y');
    if (confirm.toLowerCase() !== 'y') {
      console.log(`\n${c.yellow}已取消。${c.reset} 准备好后重新运行。\n`);
      rl.close();
      process.exit(0);
    }

    // ── Step 2: Replace variables ───────────────────────────────────────────

    console.log(`\n${c.cyan}正在应用配置...${c.reset}`);

    const replacements = {
      '{{AGENT_NAME}}': agentName,
      '{{REPO_FULL_NAME}}': repoFullName || 'owner/repo',
      '{{BRAND_NAME}}': brandName,
      '{{LANG}}': lang,
      '{{INIT_DATE}}': today,
      '{{PROJECT_NAME}}': '{{PROJECT_NAME}}',  // preserve project-level vars
    };

    // Files to process (include adapter files for multi-agent support)
    const targetFiles = [
      join(ROOT, 'AGENTS.md'),
      join(ROOT, 'MEMORY.md'),
      join(ROOT, 'README.md'),
      join(ROOT, 'CONTRIBUTING.md'),
      join(ROOT, 'CLAUDE.md'),
      join(ROOT, 'GEMINI.md'),
      ...walkFiles(join(ROOT, '.agents')),
      ...walkFiles(join(ROOT, '.cursor')),
      ...walkFiles(join(ROOT, '.windsurf')),
      ...walkFiles(join(ROOT, 'memory')),
      ...walkFiles(join(ROOT, 'projects')),
    ];

    let processed = 0;
    for (const file of targetFiles) {
      replaceInFile(file, replacements);
      processed++;
    }

    console.log(`  ${c.green}✓${c.reset} 已处理 ${processed} 个文件`);

    // ── Step 3: Create first daily log ──────────────────────────────────────

    const logDir = join(ROOT, 'memory');
    if (!existsSync(logDir)) mkdirSync(logDir, { recursive: true });

    const logFile = join(logDir, `${today}.md`);
    if (!existsSync(logFile)) {
      const logContent = lang === 'zh'
        ? `# ${today} 工作日志\n\n## 今日完成\n\n- 初始化 AI Flows 工作空间\n- 品牌名称：${brandName}\n- AI 助手代号：${agentName}\n- 仓库地址：${repoFullName || '(未设置)'}\n\n## 下一步\n\n- 使用 \`/incubate-project\` 孵化第一个项目\n`
        : `# ${today} Work Log\n\n## Completed Today\n\n- Initialized AI Flows workspace\n- Brand name: ${brandName}\n- AI agent codename: ${agentName}\n- Repository: ${repoFullName || '(not set)'}\n\n## Next Steps\n\n- Use \`/incubate-project\` to incubate the first project\n`;

      writeFileSync(logFile, logContent, 'utf-8');
      console.log(`  ${c.green}✓${c.reset} 已创建每日日志: memory/${today}.md`);
    }

    // ── Step 4: Reset tasks ─────────────────────────────────────────────────

    const tasksFile = join(logDir, 'tasks.md');
    const tasksContent = lang === 'zh'
      ? `# 任务追踪\n\n本文件记录跨对话任务状态。\n\n状态标记：\`[ ]\` 待办 | \`[~]\` 进行中 | \`[x]\` 完成\n\n---\n\n## 进行中\n\n*(暂无)*\n\n---\n\n## 待办\n\n- [ ] 使用 \`/incubate-project\` 创建第一个项目\n\n---\n\n## 已完成（近期）\n\n- [x] **${today}** 初始化 AI Flows 工作空间\n\n---\n\n*最后更新：${today}*\n`
      : `# Task Tracking\n\nThis file tracks task status across conversations.\n\nStatus markers: \`[ ]\` todo | \`[~]\` in progress | \`[x]\` completed\n\n---\n\n## In Progress\n\n*(none)*\n\n---\n\n## Todo\n\n- [ ] Use \`/incubate-project\` to create the first project\n\n---\n\n## Recently Completed\n\n- [x] **${today}** Initialized AI Flows workspace\n\n---\n\n*Last updated: ${today}*\n`;

    writeFileSync(tasksFile, tasksContent, 'utf-8');
    console.log(`  ${c.green}✓${c.reset} 已重置任务: memory/tasks.md`);

    // ── Step 5: Reset registry ──────────────────────────────────────────────

    const registryFile = join(ROOT, 'projects', 'registry.yml');
    const registryContent = `schema_version: 2\ncurrent_project: null\nprojects: []\n`;
    writeFileSync(registryFile, registryContent, 'utf-8');
    console.log(`  ${c.green}✓${c.reset} 已重置项目索引`);

    // ── Step 6: Sync multi-agent adapter files ──────────────────────────────

    console.log(`\n${c.cyan}正在同步多 Agent 适配文件...${c.reset}`);

    try {
      const { execSync } = await import('node:child_process');
      execSync('node scripts/sync-agents.mjs', { cwd: ROOT, stdio: 'pipe' });
      console.log(`  ${c.green}✓${c.reset} 已为 10+ 个 AI 工具生成适配文件`);
    } catch {
      console.log(`  ${c.yellow}⚠${c.reset} 适配文件同步失败，可稍后手动运行: node scripts/sync-agents.mjs`);
    }

    // ── Done ────────────────────────────────────────────────────────────────

    console.log(`
${c.green}${c.bold}✓ AI Flows 工作空间初始化完成！${c.reset}

${c.bold}支持的 AI 工具:${c.reset}
  ${c.cyan}Codex${c.reset} · ${c.cyan}Claude Code${c.reset} · ${c.cyan}Gemini CLI${c.reset} · ${c.cyan}Cursor${c.reset} · ${c.cyan}Windsurf${c.reset} · ${c.cyan}Copilot${c.reset} · ${c.cyan}Open Code${c.reset} · ${c.cyan}Antigravity${c.reset}

${c.bold}下一步:${c.reset}
  1. 使用任何支持的 AI 工具打开本仓库
  2. 说: ${c.cyan}"读取 AGENTS.md 和 MEMORY.md，然后孵化一个新项目"${c.reset}
  3. Agent 将引导你完成项目创建

${c.dim}更多细节请参见 README.md${c.reset}
`);
  } finally {
    rl.close();
  }
}

main().catch((err) => {
  console.error(`${c.red}Error:${c.reset}`, err.message);
  process.exit(1);
});
