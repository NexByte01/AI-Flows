# Search Strategy Guide

## Query Construction

### From topic to query
1. Extract core concepts from the research question
2. Identify synonyms and alternate spellings for each concept
3. For biomedical topics: map concepts to MeSH terms via `pubmed_lookup_mesh`
4. Assemble Boolean query: `(concept1 OR synonym1) AND (concept2 OR synonym2)`
5. Add field qualifiers for precision: `[Title/Abstract]`, `[MeSH Terms]`, `[Journal]`
6. Test and refine — if >500 results, add filters; if <10, broaden terms

### Query templates by domain

| Domain | Template |
|--------|----------|
| Medical | `("disease"[MeSH] OR "disease"[tiab]) AND ("treatment"[MeSH] OR "treatment"[tiab])` |
| Molecular | `("gene"[tiab] OR "protein"[tiab]) AND ("pathway"[tiab] OR "mechanism"[tiab])` |
| Epidemiology | `("condition"[MeSH]) AND (incidence OR prevalence OR "risk factor")` |
| Methods | `("method"[tiab]) AND ("application"[tiab]) AND (validation OR comparison)` |
| Engineering | `("material" OR "device" OR "system") AND ("performance" OR "efficiency" OR "optimization")` |
| CS / AI | `("model" OR "algorithm" OR "framework") AND ("benchmark" OR "evaluation" OR "dataset")` |
| Social science | `("policy" OR "intervention" OR "impact") AND ("analysis" OR "assessment" OR "evaluation")` |
| Materials | `("synthesis" OR "characterization") AND ("properties" OR "structure" OR "performance")` |

## Source Selection (6 sources)

### Decision tree
```
Topic is medical/clinical?
├─ Yes → PubMed + Europe PMC primary, OpenAlex + S2 secondary
└─ No → Topic is CS/AI/math/physics?
    ├─ Yes → arXiv + Semantic Scholar primary, OpenAlex secondary
    └─ No → Topic is engineering/materials/chemistry?
        ├─ Yes → CrossRef + OpenAlex primary, S2 secondary
        └─ No → Topic is social science/economics/humanities?
            ├─ Yes → OpenAlex + CrossRef primary, S2 secondary
            └─ No → OpenAlex + CrossRef primary (catch-all)
```

### Source strengths

| Source | Best For |
|--------|----------|
| PubMed | Biomedical with MeSH filters, clinical trials |
| CrossRef | DOI resolution, cross-disciplinary metadata, journal-level filtering |
| arXiv | CS/AI/physics/math preprints, immediate PDF access |
| OpenAlex | Broad coverage (250M+), impact metrics, OA PDF, topics taxonomy |
| Semantic Scholar | Citation graph traversal, TLDR, influential citations, fields of study |
| Europe PMC | OA full-text XML retrieval, biomedical citation graph |

### Journal scope awareness
- Nature Portfolio journals: use `nature.com` domain filter
- Chinese journals: CNKI/万方 not indexed in PubMed/CrossRef — flag for manual check
- Preprints only: arXiv, bioRxiv, medRxiv — no peer review status available
- Open Access: OpenAlex `is_oa` flag and `oa_url`; Europe PMC `OPEN_ACCESS:y` filter

## Deduplication Logic

See [Dedup Engine](dedup-engine.md) for the unified deduplication strategy shared by Workflows 1, 2, and 5a.

## Result Ranking

### Default: relevance
Use the search engine's default relevance ranking.

### Date-weighted
When user requests "recent" or "latest": sort by publication date descending.

### Citation-weighted
When user cares about impact: sort by citation count descending.
- OpenAlex: `cited_by_count` (comprehensive, all disciplines)
- Semantic Scholar: `citationCount` + `influentialCitationCount` (quality-weighted)
- CrossRef: `is-referenced-by-count`

### Quality-weighted (NEW)
Use the quality assessment module to rank by `quality_tier`:
- `score = relevance * 0.4 + quality_tier * 0.3 + recency * 0.2 + citations * 0.1`
- Demote preprints vs peer-reviewed articles when both are available
- Flag retracted papers via CrossRef retraction notices

### Combined scoring
For systematic reviews: `score = relevance * 0.4 + quality * 0.3 + recency * 0.2 + citations * 0.1`

