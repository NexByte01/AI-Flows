# WF6 — Full-Text Retrieval

Retrieve full text for papers identified in WF1 (multi-source search) or from user-provided identifiers.

## Trigger

- After WF1 search results, when user needs deep reading
- User provides a list of DOIs or PMIDs for full-text access
- Phase J1/T2 of Science Workflow requests core paper full text

## Steps

### 1. Collect identifiers

From the search results or user input, collect all available identifiers for each paper:
- DOI (universal)
- PMID (biomedical)
- PMCID (OA biomedical)
- arXiv ID (preprints)
- OpenAlex Work ID

### 2. Run full-text resolver

For each paper, call `get_fulltext` MCP tool or use the `FullTextResolver` module:

```
Priority chain:
1. Europe PMC OA XML (structured, best for extraction)
2. arXiv PDF (preprints, always available)
3. OpenAlex OA PDF URL → download
4. Semantic Scholar open_access_pdf → download
5. Fallback: abstract only + flag
```

### 3. Report acquisition results

Generate a summary table:

```
| # | Title | DOI | Status | Format | Source |
|---|-------|-----|--------|--------|--------|
| 1 | Paper A | 10.xxx | ✅ available | xml | europepmc |
| 2 | Paper B | 10.yyy | ✅ available | pdf_url | arxiv |
| 3 | Paper C | 10.zzz | ⚠️ abstract_only | - | - |
```

### 4. Optional: deep reading

For papers with full text available, optionally trigger `nature-reader` skill:
- Extract key findings, methods, and conclusions
- Generate structured reading notes
- Identify quotable passages with page/section references

### 5. Output

- Full-text files saved to `outputs/<run_id>/fulltext/`
- Acquisition report in the workflow output
- Structured reading notes (if step 4 was triggered)

## Integration

- **WF1 → WF6**: After multi-source search, user can select papers for full-text retrieval
- **WF6 → nature-reader**: Full text feeds into the reading skill for deep extraction
- **WF6 → WF2**: Full text enables stronger citation verification (beyond metadata-only)
