---
description: Sync project ARCHITECTURE.md after code changes
---

# 架构文档更新工作流

## 目标

检查当前项目的 `docs/ARCHITECTURE.md` 是否与代码实现一致，输出差异并更新文档。

## 适用场景

- 完成较大重构后（新增模块、服务、API 路由）。
- `/review` 发现架构描述与代码不符。
- 用户主动请求架构图更新。

## 标准步骤

1. **读取现有架构文档**：读取 `projects/<slug>/docs/ARCHITECTURE.md`，记录 `last_verified`。

2. **扫描源码结构**：列出主代码目录，识别新增/删除的核心模块、API 路由、外部集成、数据模型。

3. **对比并生成 diff 摘要**：逐章节检查 Mermaid 图节点与实际文件的对应关系。

4. **更新文档**：只修改有变更的章节，更新 `last_verified`，追加变更日志。**不重写整个文档**。

5. **验证**：确认 Mermaid 语法正确，新增模块有对应说明。

## 强制触发条件

- 新增或删除核心模块/服务。
- 新增外部 API 或第三方服务接入。
- 修改核心数据模型或 Schema。
- 新增 CLI 命令或 API 路由。

## 触发集成

- **`/review`**：架构不一致时标记为 `suggestion`。
- **`/closeout`**：命中触发条件时必须执行。
- **`/commit`**：提交前检查架构收尾。

## 验收标准

- `last_verified` 已更新为当天。
- 变更日志有本次记录。
- Mermaid 图与源码结构对应。
