#!/usr/bin/env node

/**
 * sync-agents.mjs — 多 Agent 适配文件同步
 *
 * 读取 AGENTS.md，为各 AI 工具生成极简配置文件。
 * 设计原则：只传递指针，不重复内容，节省 token。
 *
 * 用法：
 *   node scripts/sync-agents.mjs           # 同步
 *   node scripts/sync-agents.mjs --check   # 检查（CI 用）
 */

import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = join(__dirname, '..');
const isCheck = process.argv.includes('--check');

function readFile(p) {
  const fp = join(ROOT, p);
  return existsSync(fp) ? readFileSync(fp, 'utf-8') : null;
}

function writeAdapter(p, content) {
  const fp = join(ROOT, p);
  mkdirSync(dirname(fp), { recursive: true });
  writeFileSync(fp, content, 'utf-8');
}

function checkAdapter(p, expected) {
  const fp = join(ROOT, p);
  if (!existsSync(fp)) return 'missing';
  return readFileSync(fp, 'utf-8') === expected ? 'ok' : 'outdated';
}

// ─── 极简适配文件生成 ─────────────────────────────────────────────────────────

const adapters = [
  {
    path: 'CLAUDE.md',
    tool: 'Claude Code',
    content: `# AI Flows — Claude Code

<!-- 自动生成，勿手动编辑 · 运行 node scripts/sync-agents.mjs 更新 -->

@AGENTS.md
@MEMORY.md
`,
  },
  {
    path: 'GEMINI.md',
    tool: 'Gemini CLI',
    content: `# AI Flows — Gemini CLI

<!-- 自动生成，勿手动编辑 · 运行 node scripts/sync-agents.mjs 更新 -->

@AGENTS.md
@MEMORY.md
`,
  },
  {
    path: '.cursor/rules/ai-flows.mdc',
    tool: 'Cursor',
    content: `---
description: AI Flows 项目操作系统核心规则
globs: ["**/*"]
alwaysApply: true
---

<!-- 自动生成，勿手动编辑 · 信息源：AGENTS.md -->

请阅读 \`AGENTS.md\` 和 \`MEMORY.md\` 获取完整上下文。

工作原则：先读取 → 复用优先 → 及时写入 → 最小变更。
项目在 \`projects/<slug>/\` 下孵化。工作流在 \`.agents/workflows/\`。
文档用中文，代码/Git 用英文。
`,
  },
  {
    path: '.windsurf/rules/ai-flows.md',
    tool: 'Windsurf',
    content: `<!-- 自动生成，勿手动编辑 · 信息源：AGENTS.md -->

请阅读 \`AGENTS.md\` 和 \`MEMORY.md\` 获取完整上下文。

工作原则：先读取 → 复用优先 → 及时写入 → 最小变更。
项目在 \`projects/<slug>/\` 下孵化。工作流在 \`.agents/workflows/\`。
文档用中文，代码/Git 用英文。
`,
  },
  {
    path: '.github/copilot-instructions.md',
    tool: 'GitHub Copilot',
    content: `# AI Flows — Copilot 指令

<!-- 自动生成，勿手动编辑 · 信息源：AGENTS.md -->

本仓库是可 fork 的 AI 项目操作系统。规则详见 \`AGENTS.md\`。
文档用中文，代码/Git 用英文。Commit 用 Conventional Commits。
项目在 \`projects/<slug>/\` 下，工作流在 \`.agents/workflows/\`。
`,
  },
];

// ─── 主流程 ────────────────────────────────────────────────────────────────

function main() {
  const agentsContent = readFile('AGENTS.md');
  if (!agentsContent) {
    console.error('❌ 未找到 AGENTS.md');
    process.exit(1);
  }

  if (isCheck) {
    let ok = true;
    for (const a of adapters) {
      const status = checkAdapter(a.path, a.content);
      const icon = status === 'ok' ? '✅' : status === 'missing' ? '❌' : '⚠️';
      console.log(`  ${icon} ${a.path}`);
      if (status !== 'ok') ok = false;
    }
    if (!ok) {
      console.error('\n❌ 适配文件不同步。运行 node scripts/sync-agents.mjs');
      process.exit(1);
    }
    console.log('\n✅ 所有适配文件已同步。');
  } else {
    for (const a of adapters) {
      writeAdapter(a.path, a.content);
      console.log(`  ✅ ${a.path} → ${a.tool}`);
    }
    console.log(`\n✅ 已同步 ${adapters.length} 个适配文件。`);
  }
}

main();
