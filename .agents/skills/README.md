# 项目级技能库

本目录保存可复用的项目级技能，统一约定如下：

- 路径：`.agents/skills/<skill-name>/`
- 主入口：`SKILL.md`
- 附属脚本、模板、资源文件：与 `SKILL.md` 放在同一目录

## 当前已安装技能

- `UI-UX-PRO-MAX`：来自上游正式技能源，包含 `SKILL.md`、搜索脚本与数据资源  
  入口：`.agents/skills/UI-UX-PRO-MAX/SKILL.md`

- `ai-image-generation`：来自 `inference-sh/skills`，用于生成 README、宣传页和站点所需的 AI 图片资源  
  入口：`.agents/skills/ai-image-generation/SKILL.md`
  附注：使用外部模型 API Key 时仅做临时环境变量注入，不写入仓库
