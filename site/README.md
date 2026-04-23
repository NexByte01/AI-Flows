# NexByte AI Flows 占位页

> 一个面向 `nexbyte.com.cn` 的临时静态入口页，用来说明这个仓库的定位、当前承载的资产，以及后续正式站点方向。

## 当前定位

`site/` 不是正式主站，而是 **NexByte AI Flows** 的公开说明页。当前阶段它承担三件事：

- 告诉访问者这是什么仓库
- 引导访问主站 <https://nexbyte.com.cn>
- 指向 GitHub 仓库与后续实验项目

## 页面内容

当前页面会展示：

- NexByte AI Flows 的项目定位
- 长期记忆、技能资产、自动化流程、实验项目四类能力
- 主站和 GitHub 仓库入口
- 当前仓库 Star 数量（通过 GitHub API 读取 `NexByte01/AI-Flows`）

## 本地预览

这是一个纯静态页面，不依赖构建流程。

```bash
cd site
python -m http.server 8000
```

然后访问：<http://localhost:8000>

## 目录结构

```text
site/
├── README.md
├── index.html
├── robots.txt
└── sitemap.xml
```

## 部署方式

仓库已配置 GitHub Pages 工作流：

- 推送 `site/**` 到 `main` 时自动触发
- 将 `site/` 作为静态产物部署

对应工作流：

- `../.github/workflows/deploy-pages.yml`

## 后续方向

当前页面是占位页，后续可继续演进为：

- 仓库主页 / 项目导航页
- `nexbyte.com.cn` 的镜像说明页
- AI 工作空间和实验项目的统一入口
