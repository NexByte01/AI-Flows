---
description: Perform structured code and architecture review on project implementation
---

# 代码审查工作流

## 目标

对当前项目的实现进行结构化审查，输出可追踪的审查报告。

## 适用场景

- 完成一个功能模块后，需要审查质量。
- 阶段性 review（如 MVP 完成后）。
- 准备提交 PR 或推进到下一阶段前。
- 用户主动请求代码审查。

## 默认前提

- 已读取根级 `AGENTS.md`、`MEMORY.md`、`projects/registry.yml`。
- 已确认审查范围（哪些文件或模块）。

## 标准步骤

1. **确认审查范围**：
   - 用户指定的文件或目录。
   - 或最近一次提交涉及的变更。
   - 或整个项目（阶段性全量 review）。

2. **读取约束文档**：
   - 项目 `AGENTS.md`：执行边界和禁止事项。
   - 项目 `docs/ARCHITECTURE.md`：架构约束和模块边界。
   - 数据模型/契约定义（如有）。

3. **按维度逐项审查**：

   | 维度 | 检查内容 |
   | --- | --- |
   | 架构边界 | 模块是否按约定分层，依赖方向是否正确 |
   | 类型安全 | 类型定义是否完整，是否有 `any` 逃逸 |
   | 异常处理 | 错误是否被捕获、记录、不吞没 |
   | 安全检查 | API Key 是否泄露到代码/日志/示例中 |
   | 测试覆盖 | 关键路径是否有测试或验证方式 |
   | 性能考量 | 是否有明显的 N+1 查询、内存泄漏等 |
   | 代码风格 | 是否符合项目已有风格和约定 |

4. **生成审查报告**：
   - 按严重度分类：`blocker` / `major` / `minor` / `suggestion`。
   - 每个问题包含：文件路径、行号（如适用）、问题描述、建议修复方式。

5. **输出并归档**：
   - 审查报告写入 `projects/<slug>/memory/reviews/YYYY-MM-DD-review.md`。
   - 如果发现 blocker，在 `memory/tasks.md` 中新增修复任务。
   - 如发现架构文档过时，标记为 `suggestion` 并触发 `/update-architecture`。
   - 审查完成后运行 `/closeout` 的最小收尾检查。

## Token 控制

- 优先审查用户指定范围或本轮变更文件，不默认全仓审查。
- 只读取与审查范围直接相关的架构、契约章节。
- 不复制长代码块到报告；用文件路径、行号和简短描述定位问题。

## 输出格式

```markdown
# Review Report - YYYY-MM-DD

## 概要
- 审查范围：...
- 发现问题：X blocker / Y major / Z minor / W suggestion

## Blocker
### [B1] 问题标题
- 文件：`path/to/file.ts:L42`
- 描述：...
- 建议：...

## Major
...

## Minor
...

## Suggestion
...
```

## 验收标准

- 审查报告存在于 `projects/<slug>/memory/reviews/`。
- 每个问题有明确的文件位置和修复建议。
- blocker 级问题已同步到 `memory/tasks.md`。
- 审查不直接修改被审查的文件（除非用户明确要求）。
