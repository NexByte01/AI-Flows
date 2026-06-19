# MCP tools and shared modules

Multi-source literature search, citation verification, citation format conversion, and reference management via MCP tools.

## MCP tools (academic-search server)

### Core search — `search_papers`

All 6 sources are queried in parallel by default. Use the `sources` parameter to select specific sources.

| Source | API | Best For |
|--------|-----|----------|
| `crossref` | CrossRef REST API | Cross-disciplinary, DOI resolution |
| `pubmed` | NCBI E-utilities | Biomedical, MeSH, clinical trials |
| `arxiv` | arXiv OAI-PMH | Preprints (physics, math, CS, biology) |
| `openalex` | OpenAlex REST API | All disciplines, impact metrics, OA PDF |
| `semantic_scholar` | Semantic Scholar API | Citation graph, TLDR, influential citations |
| `europepmc` | Europe PMC REST API | OA full-text, biomedical citation graph |

### Paper retrieval — `get_paper_by_id`

| ID Type | Format | Example |
|---------|--------|---------|
| DOI | `10.xxxx/xxxxx` | `10.1038/nature12373` |
| PMID | Numeric | `23903684` |
| arXiv | `YYYY.NNNNN` | `2312.07533` |
| OpenAlex | `WXXXXXXXXXX` | `W2741809807` |
| PMCID | `PMCXXXXXXX` | `PMC8371605` |
| S2 Paper ID | 40-char hex | (Semantic Scholar internal) |

### Full-text and citations

| Tool | Source | Best For |
|------|--------|----------|
| `get_fulltext` | Europe PMC → arXiv → OpenAlex | OA full-text XML/PDF retrieval |
| `get_citation_graph` | Semantic Scholar → Europe PMC | Citing/referenced paper lists |

### Extended search (external MCP servers)

| Tool | Source | Best For |
|------|--------|----------|
| `search_google_scholar` | paper-search MCP | Broad academic search (scraped, T3) |
| `search_biorxiv` | paper-search MCP | Biology preprints |
| `search_medrxiv` | paper-search MCP | Medical preprints |

### PubMed utilities

| Tool | Purpose |
|------|---------|
| `pubmed_fetch_articles` | Full metadata by PMID |
| `pubmed_find_related` | Related article discovery |
| `pubmed_format_citations` | APA / MLA / BibTeX / RIS formatting |
| `pubmed_convert_ids` | DOI ↔ PMID ↔ PMCID conversion |
| `pubmed_lookup_mesh` | MeSH term exploration and hierarchy |
| `pubmed_lookup_citation` | Bibliographic citation → PMID lookup |

## Shared modules

| Module | Purpose |
|--------|---------|
| [Dedup Engine](../../references/dedup-engine.md) | Unified deduplication (WFs 1, 2, 5a) |
| [Citation Parser](../../references/citation-parser.md) | Extract citations from documents (WF 2) |
| [Search Strategy](../../references/search-strategy.md) | Query construction, source selection, ranking |
| [RIS/BibTeX Format](../../references/ris-bibtex-format.md) | Format specifications and field mappings |
| [Format Converter](../../scripts/format-converter.py) | Multi-source .nbib/.ris/.bib downloader |
