# Source routing and operations

## Source routing

See [Source Tiers & Reliability](../../references/source-tiers.md) for the complete reliability classification and fallback routing rules. The T1→T2→T3 fallback chain is the standard execution order across all workflows.

Quick guide:

| User need | Primary (T1) | Secondary (T1) | Fallback (T2/T3) |
|-----------|-------------|-----------------|-------------------|
| Medical / clinical | PubMed + Europe PMC | OpenAlex + Semantic Scholar | bioRxiv/medRxiv |
| Engineering / materials / chemistry | CrossRef + OpenAlex | Semantic Scholar | Scopus |
| Computer science / AI | arXiv + Semantic Scholar | OpenAlex | Google Scholar |
| Social science / economics | OpenAlex + CrossRef | Semantic Scholar | Google Scholar |
| Agriculture / environment | PubMed + OpenAlex | Semantic Scholar | — |
| Math / physics | arXiv + CrossRef | OpenAlex | — |
| Multi-disciplinary review | OpenAlex + PubMed + CrossRef + arXiv | S2 + Europe PMC | WoS / Scopus |
| Citation verification | CrossRef (DOI) → OpenAlex → PubMed | Semantic Scholar | — |
| Full-text retrieval | Europe PMC (OA XML) → arXiv (PDF) | OpenAlex (OA PDF) → S2 (OA PDF) | — |
| Chinese literature | — | — | CNKI / 万方 (manual) |

## Environment setup

### API keys (optional but recommended)

| Service | Env Var | Register At | Free Tier |
|---------|---------|-------------|-----------|
| OpenAlex | `OPENALEX_API_KEY` | [openalex.org](https://openalex.org) | $1/day free budget (30s to register) |
| Semantic Scholar | `SEMANTIC_SCHOLAR_API_KEY` | [api page](https://www.semanticscholar.org/product/api) | 100 req/s with key (1/s without) |
| NCBI E-utilities | `NCBI_API_KEY` | [ncbi.nlm.nih.gov/account](https://www.ncbi.nlm.nih.gov/account/) | 10 req/s with key (3/s without) |

Set via `export` or `.env` file:

```bash
export OPENALEX_API_KEY=your_key_here
export SEMANTIC_SCHOLAR_API_KEY=your_key_here
export NCBI_API_KEY=your_key_here
```

### Proxy (if behind firewall)

```bash
export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890
```

### Pre-flight check

```bash
python scripts/preflight.py
```

Run before batch operations to verify API endpoints are reachable.

### Format converter dependencies

The format converter (`scripts/format-converter.py`) uses Python stdlib only — no extra dependencies. Run `python scripts/format-converter.py --test` to verify the conversion pipeline.

## Error handling

- **MCP tool unavailable**: report specific failure, continue with remaining tools.
- **Source timeout or rate limit**: automatically retry with backoff; if persistent, skip source and use alternatives.
- **No results**: broaden terms, try alternative sources, suggest user refine query.
- **Script failure (2x)**: fall back to manual generation from MCP-fetched metadata.

## Limitations

- Google Scholar is scraped (T3) — results may vary due to CAPTCHA blocks.
- Chinese literature (CNKI / 万方) not indexed by any T1/T2 source.
- Citation counts may be delayed: CrossRef updates monthly, OpenAlex weekly, S2 near real-time.
- Full-text retrieval limited to Open Access articles via Europe PMC, arXiv, and publisher OA PDFs.
- Semantic Scholar without API key is rate-limited to 1 req/s (T2 tier).

