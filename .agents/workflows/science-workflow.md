---
description: 重定向到当前项目的 Science Workflow 主入口
---

# Science Workflow Redirect

当用户调用 `/science-workflow` 时，Agent 必须定位当前活跃项目：

- `projects/paper-patent-assistant/`

并加载项目级工作流：

- `projects/paper-patent-assistant/.agents/workflows/science-workflow.md`

本入口用于 SCI/期刊论文与硕博论文写作。专利能力仅作为 extension，除非用户明确要求“转专利”“技术交底书”“权利要求书”，否则不要进入 `scipatent-lifecycle.md`。
