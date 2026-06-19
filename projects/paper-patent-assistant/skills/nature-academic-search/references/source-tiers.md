# Source Tiers & Reliability

Every academic data source is classified by reliability tier to guide automated fallback routing.

## Tier Definitions

| Tier | Label | API Quality | Fallback Behavior |
|------|-------|-------------|-------------------|
| **T1** | API-backed, structured | Official REST/XML API, stable schema | Use first. If fails → next T1 source. |
| **T2** | API-backed, limited | Official API but narrow coverage or low rate limits | Use when T1 exhausted or insufficient. |
| **T3** | Scraped, unstable | Web scraping, no contract on response format | Last resort. Always warn user: "results may be incomplete or stale". |

## Source Classification

### T1 — API-backed, Structured

| Source | API | Rate Limit | Coverage | Unique Strength |
|--------|-----|------------|----------|-----------------|
| PubMed | E-utilities (XML/JSON) | 3 req/s (10 with key) | Biomedical + life sciences | MeSH indexing, clinical filters |
| CrossRef | REST API (JSON) | 50 req/s (no key needed) | All disciplines | DOI resolution, publication metadata |
| arXiv | OAI-PMH Atom XML | 1 req/3s | Physics, math, CS, biology, econ | Preprint access, PDF download |
| **OpenAlex** | REST API (JSON) | $1/day free budget | **All disciplines (250M+ works)** | Citation counts, OA PDF URLs, topics |
| **Semantic Scholar** | REST API (JSON) | 100 req/s (with key) | All disciplines (200M+ papers) | Citation graph, TLDR, influential citations |
| **Europe PMC** | REST API (JSON/XML) | No key needed | Biomedical + life sciences | **OA full-text XML/PDF retrieval** |

### T2 — API-backed, Limited

| Source | API | Rate Limit | Notes |
|--------|-----|------------|-------|
| Semantic Scholar (no key) | REST API (JSON) | 1 req/s | Falls to T2 without API key |
| bioRxiv | API | Limited metadata | Biology preprints only |
| medRxiv | API | Limited metadata | Medical preprints only |

### T3 — Scraped, Unstable

| Source | Method | Risk |
|--------|--------|------|
| Google Scholar | HTML scrape | CAPTCHA blocks, IP bans |
| Web of Science | Institution proxy required | Access varies |
| Scopus | Institution proxy required | Access varies |
| CNKI / 万方 | No programmatic access | Chinese only, manual download |

## Fallback Routing Rules

For every literature search or citation verification:

```
1. SELECT T1 sources matching the query domain
2. SEARCH all selected T1 sources in parallel
3. DEDUPLICATE results (DOI primary, Title+Author Jaccard fallback)
4. If (result found AND relevance > threshold) → ACCEPT
5. If T1 exhausted or insufficient → ESCALATE to T2
6. If T1+T2 exhausted → ESCALATE to T3 + WARN USER
7. If all exhausted → return partial results + suggest query refinement
```

### Domain → Tier Mapping (6 sources)

| Domain | T1 Primary | T1 Secondary | T2 (if needed) | T3 (last resort) |
|--------|------------|--------------|----------------|-------------------|
| Medical / clinical | PubMed + Europe PMC | OpenAlex + Semantic Scholar | bioRxiv/medRxiv | Google Scholar |
| Engineering / materials / chemistry | CrossRef + OpenAlex | Semantic Scholar | — | Scopus |
| Computer science / AI | arXiv + Semantic Scholar | OpenAlex | — | Google Scholar |
| Social science / economics / humanities | OpenAlex + CrossRef | Semantic Scholar | — | Google Scholar |
| Agriculture / environment | PubMed + OpenAlex | Semantic Scholar | — | — |
| Math / physics | arXiv + CrossRef | OpenAlex | — | — |
| Multi-disciplinary review | OpenAlex + PubMed + CrossRef + arXiv | Semantic Scholar + Europe PMC | bioRxiv/medRxiv | WoS / Scopus |
| Citation verification | CrossRef (DOI) → OpenAlex → PubMed (PMID) | Semantic Scholar | — | Google Scholar |
| Full-text retrieval | Europe PMC (OA XML) → arXiv (PDF) → OpenAlex (OA PDF) | Semantic Scholar (OA PDF) | — | — |
| Chinese literature | — | — | — | CNKI / 万方 (manual) |

## Environment Configuration

| Service | Env Var | Register At | Free Tier |
|---------|---------|-------------|-----------|
| OpenAlex | `OPENALEX_API_KEY` | [openalex.org](https://openalex.org) | $1/day free (30s to register) |
| Semantic Scholar | `SEMANTIC_SCHOLAR_API_KEY` | [api page](https://www.semanticscholar.org/product/api) | 100 req/s with key |
| NCBI E-utilities | `NCBI_API_KEY` | [ncbi.nlm.nih.gov/account](https://ncbi.nlm.nih.gov/account) | 10 req/s with key |

