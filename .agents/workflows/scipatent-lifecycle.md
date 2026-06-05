---
description: 执行一站式科研与专利生命周期，串联文献检索、论文写作、模拟盲审及专利转化
---

# SciPatent 全周期科研工作流 (SciPatent Lifecycle)

> 适用场景：
> - “执行论文和专利转化全流程”
> - “从检索到写权利要求书”
> - 使用 `/scipatent-lifecycle` 触发

## 0. 重定向说明

这是一个项目级的工作流。当触发此命令时，Agent 必须重定向并优先加载当前主项目的专属生命周期定义：
- `d:\Projects\AI Flows\projects\paper-patent-assistant\.agents\workflows\scipatent-lifecycle.md`

## 1. 核心流程摘要

本工作流通过设置 **6 个关键的人工审核与分支选择门槛 (Gates)**，确保科研过程的严谨性与控制灵活性：

1. 🛑 **Gate 1: 立意与文献基线确认**：确认 Gap 是否有研究价值。
2. 🛑 **Gate 2: 核心证据与数据确认**：要求用户提供真实数据（AI 绝不编造数据）。
3. 🛑 **Gate 2b: 科研图表确认**：完成强制的学术科研图表绘制，确认图表合规性。
4. 🛑 **Gate 3: 盲审结论与修回策略确认**：3 位审稿人评估，用户决定修改方向并修回。
5. 🛑 **Gate 3b: 专利转化自主选择**：根据配置文件或会话交互，自主选择是否转专利。
6. 🛑 **Gate 4: 专利保护范围确认**：若进行专利转化，在此确认专利独立权利要求的描述，化解客体驳回风险。

## 2. 执行指令

请执行以下指令：
1. 定位到当前活跃项目 `projects/paper-patent-assistant/`。
2. 加载 `projects/paper-patent-assistant/.agents/workflows/scipatent-lifecycle.md`。
3. 按照该项目专属生命周期的 Phase 1 开始执行。
