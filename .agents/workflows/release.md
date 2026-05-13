---
description: Pre-release readiness check before merging develop into main
---

# 发布就绪检查

适用场景：

- "仓库可以发布/合并到 main 了吗？"
- "发布前需要检查什么？"

## 核心原则

- 本仓库使用 `main + develop + feature/*` — 发布是将 `develop` 合并到 `main`
- 发布检查侧重于"仓库协作完整性"，而非统一构建流水线
- 优先检查：项目结构、记忆文件、模板和 GitHub Actions

## 步骤一：确定版本号

采用语义化版本 `vMAJOR.MINOR.PATCH`：

| 变更类型 | 递增 | 示例 |
|---|---|---|
| 破坏性变更 | MAJOR | v1.0.0 → v2.0.0 |
| 新功能 / 大模块交付 | MINOR | v0.2.0 → v0.3.0 |
| Bug 修复 / 文档小改 | PATCH | v0.2.0 → v0.2.1 |

查看上一个 tag 和本次变更：

// turbo
```
git tag --sort=-v:refname | head -5
```

// turbo
```
git log $(git describe --tags --abbrev=0 2>/dev/null || echo HEAD~10)..develop --oneline
```

## 检查清单

### 1. 仓库级检查

- [ ] `CHANGELOG.md` 是否已将 `[Unreleased]` 中的条目移动到新版本号下？
- [ ] `AGENTS.md`、`MEMORY.md`、`memory/tasks.md` 是否与当前实践一致？
- [ ] 今日重要变更是否记录在 `memory/YYYY-MM-DD.md`？
- [ ] `.gitignore` 是否覆盖本地缓存、环境变量和构建产物？
- [ ] `.github/workflows/` 是否只包含本仓库实际使用的工作流？
- [ ] 生产文件中是否还有 `{{TEMPLATE_VARIABLE}}` 占位符？

### 2. 项目容器检查

- [ ] `projects/registry.yml` 是否与实际项目目录一致？
- [ ] 所有 `building` 状态的项目是否有完整的最小结构？
- [ ] 是否有孤儿项目目录？

### 3. 模板检查

- [ ] 模板 `version.yml` 文件是否存在且版本号有效？
- [ ] 模板中是否有硬编码的品牌名或仓库地址？

### 4. GitHub 自动化检查

- [ ] CI 工作流的触发条件和权限是否仍然有效？

## 步骤二：创建 PR

通过 GitHub 集成创建 PR：

- **head**: `develop`
- **base**: `main`
- **title**: `release: <VERSION> — <一句话总结>`
- **body**: 包含本次发布的主要变更列表

## 步骤三：合并 + 打 Tag

CI 通过后：

1. 合并 PR
2. 本地打 tag 并推送：

```bash
git checkout main && git pull origin main
git tag -a <VERSION> -m "<一句话总结>"
git push origin <VERSION>
git checkout develop
```

## 注意事项

- 不要假设发布意味着运行 `pnpm build` — 本仓库可能没有构建步骤
- 如果仓库有大量未提交变更，将"清理工作目录"列为优先事项
