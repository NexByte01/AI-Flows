# Unified Academic Search MCP Server

统一的学术搜索 MCP 服务器，整合 CrossRef、PubMed、arXiv 三个数据源。

## 工具

| 工具 | 功能 |
|------|------|
| `search_papers` | 统一搜索，支持多数据源并发 |
| `get_paper_by_id` | 按 DOI/PMID/arXiv ID 获取详情 |
| `get_citation` | 格式化引用 (apa/nature/ieee 等) |
| `lookup_mesh` | MeSH 词表查询 |

## 配置

环境变量:
- `PUBMED_EMAIL` - 必填，NCBI 要求
- `NCBI_API_KEY` - 可选，提升速率限制

配置文件: `config.toml`

## 使用

Claude Code 会自动加载此服务器。工具通过 `academic-search` skill 调用。

## 本地测试

测试套件在 `mcp-server/tests/`，**完全 mock 外部 HTTP**，无需联网、无需 API key。

### 前置依赖

- Python ≥ 3.10
- `requests` 和 `toml`（运行时需要）
- `pytest`（测试时需要，**仅测试时**）

`lxml` 列入 `requirements.txt` 是给生产环境备用；本地测试**不需要**它（Windows 上装 `lxml` 需要 C 编译工具链）。

### 安装

```powershell
# 方式 1：传统 venv（推荐用于 IDE 调试）
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt
```

```bash
# 方式 2：uv 一行搞定（不污染全局）
uv run --with-requirements requirements.txt --with-requirements requirements-dev.txt pytest
```

> `tests/conftest.py` 会把 `mcp-server/` 加入 `sys.path`，
> 并写入默认 `PUBMED_EMAIL`/`CROSSREF_MAILTO`，所以 `from sources.crossref import …`
> 不需要 `pip install -e .`。

### 运行

```bash
# 收集并运行全部测试
cd mcp-server
pytest

# 只跑一个测试类
pytest tests/test_sources.py::TestCrossRefSearch

# 详细输出
pytest -v

# 收集但不执行（验证 conftest 路径正确）
pytest --collect-only
```

### 预期结果

- 31 tests collected（4 个测试类：CrossRef / PubMed / arXiv / ID 识别）。
- 全部用例在不到 1 秒内跑完（纯 mock，无网络）。
- 任何模块导入错误都应被 `conftest.py` 兜底；如出现 `ModuleNotFoundError: requests` /
  `toml`，说明 `requirements.txt` 没装全，按上面"安装"补一次。

