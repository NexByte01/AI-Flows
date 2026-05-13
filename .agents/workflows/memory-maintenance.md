---
description: Control local memory growth and prevent stale facts from misleading execution
---

# 记忆维护工作流

## 目标

控制本地记忆增长，减少 Token 消耗，并防止旧事实误导执行。

## 适用场景

- 用户担心记忆越来越多。
- 重大项目结构变化后。
- 阶段结束，需要整理长期决策。
- 发现 `MEMORY.md` 中存在重复、过时或临时内容。
- 每周例行清理，或当前项目 `tasks.md` 已完成区超过 20 条。

## 维护节奏

- **每日收尾**：只追加当天日志和任务状态，不做大规模整理。
- **每周维护**：执行本工作流，清理过时信息、归档已完成任务、检查验证日期。
- **架构变更后**：立即执行 `/closeout` 和必要的 `/update-architecture`，不等周维护。
- **阶段结束后**：做阶段归档，压缩 `tasks.md` 的已完成区。

## 标准步骤

1. 先做结构检查：
   - 查看 `MEMORY.md` 行数和大小。
   - 查看 `memory/tasks.md` 是否有过期任务。
   - 查看 `memory/tasks.md` 的"已完成"是否超过 20 条；超过则归档旧项。
   - 查看 `projects/registry.yml` 是否仍能代表当前主项目。
   - 查看当前项目 `docs/ARCHITECTURE.md` 的 `last_verified` 是否落后于最近架构变更。

2. 先搜索，再读取：
   - 用关键词搜索相关记忆。
   - 只打开命中的文件和当前项目文件。
   - 不默认全文读取所有 `memory/YYYY-MM-DD.md`。

3. 分类处理：
   - 长期规则保留在 `MEMORY.md`。
   - 过程记录移动或保留在 `memory/YYYY-MM-DD.md`。
   - 当前执行项放在 `memory/tasks.md`。
   - 旧完成项移动到 `memory/archive/` 或阶段归档。
   - 项目私有内容放到 `projects/<slug>/MEMORY.md` 或项目任务。

4. 检查易过时事实：
   - 外部路径。
   - 线上地址。
   - Git 状态。
   - 部署、依赖、API、价格、平台规则。
   - 这些内容必须有 `last_verified` 或"执行前重新验证"说明。

5. 合并重复决策：
   - 相同规则只保留一处权威写法。
   - 根级规则写在 `MEMORY.md`。
   - 项目级规则写在对应项目 `MEMORY.md`。

6. 归档任务：
   - `tasks.md` 保留"下一步""暂不做"和最近 10-20 条高价值已完成项。
   - 旧完成项按阶段写入 `memory/archive/YYYY-MM-<phase>.md`。
   - 归档文件顶部写明覆盖范围、归档日期和是否仍需重新验证。

7. 收尾：
   - 更新当天 `memory/YYYY-MM-DD.md`。
   - 更新 `memory/tasks.md`。
   - 如更新了规则或架构，执行 `/closeout` 的最小收尾检查。
   - 不删除历史日志，除非用户明确要求并确认范围。

## 检查命令示例

```bash
# 查看 MEMORY.md 大小
wc -l MEMORY.md 2>/dev/null || (Get-Content -LiteralPath .\MEMORY.md).Count

# 搜索过时信息
grep -r "TODO\|过期\|deprecated\|last_verified" memory/ projects/ 2>/dev/null || rg "TODO|过期|deprecated|last_verified" memory projects
```

## 验收标准

- `MEMORY.md` 只保留长期规则、当前状态和关键路径。
- `memory/tasks.md` 能看出下一步和最近完成事项，旧完成项已归档。
- 易过时事实有验证日期或重新验证提示。
- 没有把一次性日志、长命令输出或未验证猜测写进长期记忆。
- 归档不删除历史，只减少默认读取成本。
