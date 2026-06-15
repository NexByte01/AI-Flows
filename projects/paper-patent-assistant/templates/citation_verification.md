# 引用与基线文献核验表

> 本模板用于 Phase J1（选题与文献基线）与 Phase T2（文献综述与证据矩阵）。
> 派生产物路径约定：`outputs/journal/citation_verification.md` 或
> `outputs/thesis/citation_verification.md`；本模板本身不进入提交。

---

## 0. 元信息

| 字段 | 内容 |
|---|---|
| 论文/学位论文题目 |  |
| 研究问题 |  |
| 目标期刊 / 学位层级 |  |
| 行业包（可选） |  |
| 检索工具 |  |
| 检索时间窗 |  |
| 检索关键词 |  |
| 派生文件路径 |  |

---

## 1. 基线文献矩阵（Baseline Literature Matrix）

> 按主题聚类而非按检索顺序。每一条都对应一个具体的论点、对比基线或方法来源。
> 未核验条目不得进入 Part 2 的 Gap 论证。

| 编号 | 主题簇 | 用途 | 标题 | 第一作者 | 年份 | 期刊/会议 | DOI/URL | 来源 | 检索工具 | 核验状态 | 证据等级 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 |  | 背景/方法/对比/数据 |  |  |  |  |  |  | pubmed/crossref/arxiv/其他 | verified / needs_verification / rejected | verified / described |  |
| R2 |  |  |  |  |  |  |  |  |  |  |  |  |
| R3 |  |  |  |  |  |  |  |  |  |  |  |  |

### 1.1 主题簇说明

| 主题簇 | 簇内文献数 | 共同结论 | 簇内争议 | 是否覆盖本研究核心问题 |
|---|---|---|---|---|
| 主题 A |  |  |  | yes / partial / no |
| 主题 B |  |  |  | yes / partial / no |
| 主题 C |  |  |  | yes / partial / no |

---

## 2. Research Gap 与拟用证据

> 在完成 Part 1 核验后填写。Gap 必须能映射到具体文献缺口或方法缺口，
> 并明确"拟用证据等级"——若拟用 `real` 或 `verified`，必须指明对应文献或数据来源。

| Gap 编号 | Gap 描述（现有研究不足） | 现有最近文献 | 拟用证据等级 | 拟用证据来源 | 是否需要补实验/补仿真 | 状态 |
|---|---|---|---|---|---|---|
| G1 |  |  | real / verified / described |  | yes / no | open / closed |
| G2 |  |  |  |  |  |  |
| G3 |  |  |  |  |  |  |

### 2.1 核心创新性依赖的引用清单

> 本研究的核心创新性结论（或拟投稿时 reviewer 最可能追问的"novelty"）
> 所直接依赖的文献必须全部 `verified`，且 `evidence_level = verified`。
> 任何 `needs_verification` / `rejected` 的引用不得出现在此清单。

| 编号 | 用途 | 标题 | DOI/URL | 核验状态 | 与创新点的关系 |
|---|---|---|---|---|---|
| N1 |  |  |  | verified |  |
| N2 |  |  |  | verified |  |
| N3 |  |  |  | verified |  |

---

## 3. 引用核验规则

- **DOI/URL 必须可点击**：所有引用都需提供 DOI 或可访问 URL，二手引用必须回溯到原始来源。
- **核验状态分级**：
  - `verified`：DOI 可解析、作者/期刊/年份/卷期页码与来源一致，摘要与论点对得上。
  - `needs_verification`：仅靠二手描述或预印本/会议摘要，需在 Gate J1/T2 关闭前补核。
  - `rejected`：核验失败、撤稿、重复发表或来源不可信，从基线中剔除。
- **核心创新性约束**：`needs_verification` 与 `rejected` 不得作为创新性依据。
- **二手引用**：若必须引用某观点而无法直接读到原文，需在备注中说明并以最近可核验文献替代。
- **撤稿与更正**：若发现已收录文献被撤稿或发布更正，立即在 `memory/<日期>.md` 记录并同步到本表。
- **数据来源 vs 引用来源**：图表数据来源走 `templates/real_data_intake.md`，本表只处理文献引用。

---

## 4. 收尾检查

- [ ] Part 1 每条引用都有 DOI/URL、年份、来源和核验状态。
- [ ] Part 1.1 主题簇覆盖了核心研究问题，未覆盖的子问题列入 Part 2。
- [ ] Part 2 每个 Gap 都有可指认的现有文献或方法限制。
- [ ] Part 2.1 创新性依赖清单全部 `verified`。
- [ ] 撤稿/更正、错误归属、二手引用等问题已在 `memory/<日期>.md` 记录。
- [ ] run state 的 `evidence_level` 与本表一致；Gate J1/T2 通过前不得进入下一阶段。
