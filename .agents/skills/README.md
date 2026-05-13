# 技能库

本目录存储可复用的技能，扩展 AI agent 的能力。

## 目录规范

- 路径：`.agents/skills/<skill-name>/`
- 每个技能必须有 `SKILL.md` 作为主入口点

## 使用方式

1. 接到任务时先检查本目录
2. 本地没有则寻找外部来源
3. 新技能保存到 `.agents/skills/<skill-name>/`
4. 安装、迁移或废弃技能后，更新本 README

## 已安装技能

| 技能 | 描述 |
|---|---|
| `UI-UX-PRO-MAX` | Web 和移动端 UI/UX 设计智能 |
| `ai-image-generation` | 使用多种模型生成 AI 图片 |
| `seo-audit` | SEO 审计和诊断 |

## 安装新技能

技能可以来自：
- 外部技能注册表
- 根据项目需求手动创建
- 从其他 AI Flows fork 复制
