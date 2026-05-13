# Changelog

本文件记录 AI Flows 的所有重要变更。格式基于 [Keep a Changelog](https://keepachangelog.com/)，版本号遵循 [Semantic Versioning](https://semver.org/)。

## [Unreleased]

## [1.0.0] - 2026-05-13

### Added

- **记忆治理系统**：新增 `memory/README.md`，定义分层读取、易过时事实验证、归档规则和 Token 控制策略
- **收尾自动化工作流** (`/closeout`)：任务结束时执行验证、日志、架构、任务闭环检查
- **记忆维护工作流** (`/memory-maintenance`)：控制记忆增长、归档旧任务、防止过时信息误导
- **任务拆解工作流** (`/task-breakdown`)：从需求或文档中拆解原子可执行任务
- **代码审查工作流** (`/review`)：结构化代码和架构审查，输出可归档报告
- **架构同步工作流** (`/update-architecture`)：代码变更后同步 ARCHITECTURE.md
- **阶段门禁工作流** (`/gate-check`)：检查项目是否满足阶段目标，输出通过/阻塞报告
- **项目架构文档模板**：4 个模板均新增 `docs/ARCHITECTURE.md`（含 Mermaid 图、技术栈表、变更日志）
- **归档和审查目录**：4 个模板均新增 `memory/archive/` 和 `memory/reviews/` 目录

### Changed

- **AGENTS.md 升级至 v4.0**：默认读取策略（5 级分层）、工作原则从 4 条扩充到 8 条、强制更新触发条件
- **Commit 工作流增强**：新增 Scope 映射表、中文 commit message、多行 body、PowerShell 路径转义
- **Status 工作流增强**：新增 Token 控制章节和项目级状态恢复指引
- **Release 工作流更新**：适配 `main + develop + feature/*` 分支策略
- **PR 工作流更新**：base 分支改为 `develop`
- **Feature-branch 工作流更新**：从 `develop` 创建分支
- **分支策略**：从 `main + feature/*` 升级为 `main + develop + feature/*`
- **Commit 语言**：冒号后标题和正文默认使用中文
- **所有工作流 description**：YAML frontmatter 统一为英文，提升 AI 模型解析一致性
- **README.md**：完整重写，反映 v4.0 特性和 15 个工作流
- **CONTRIBUTING.md**：新增记忆治理协作规范、Scope 映射、多行 body 规范
- **模板 README**：更新最小结构列表，包含新增的架构和归档文件
