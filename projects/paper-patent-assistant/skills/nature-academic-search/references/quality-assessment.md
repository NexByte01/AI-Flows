# Quality Assessment Rules

## Overview

The quality assessment module (`utils/quality_assessor.py`) provides automated multi-dimensional scoring for each retrieved paper, helping users evaluate citation value before including references in their manuscript.

## Scoring Dimensions

| Dimension | Weight | Source | Range |
|-----------|--------|--------|-------|
| Citation impact | 40% | OpenAlex, S2, CrossRef | Age-adjusted log-scale |
| Influential citations | 20% | Semantic Scholar | Ratio of influential/total |
| Peer review status | 25% | Publication type detection | Binary: peer-reviewed vs preprint |
| Recency | 15% | Publication year | Newer = higher |

## Quality Tiers

| Tier | Score Range | Meaning | Recommendation |
|------|------------|---------|----------------|
| **A** | ≥65, peer-reviewed | High-impact, well-cited, peer-reviewed | Strong citation candidate |
| **B** | ≥45 | Good quality, moderate citations | Good candidate, verify relevance |
| **C** | ≥25 | Acceptable, low citations or preprint | Cite with caution |
| **D** | <25 | Low quality, very few citations | Avoid unless no alternatives |

## Domain-Specific Baselines

Citation counts vary dramatically across disciplines. The scoring function uses age-adjusted log-scale rather than absolute thresholds to handle this:

| Domain | Typical "A-tier" citations (5yr paper) | Notes |
|--------|---------------------------------------|-------|
| Biomedical | 50-200+ | High volume, rapid citation |
| Computer science | 100-500+ | Conference papers cite heavily |
| Engineering | 20-80+ | Slower citation cycle |
| Social science | 15-50+ | Smaller community |
| Mathematics | 10-30+ | Very small citation counts are normal |

## Special Rules

### Preprints
- Automatically classified as C-tier minimum, regardless of citations
- Recommendation includes "check if peer-reviewed version exists"
- arXiv, bioRxiv, medRxiv papers detected by source or publication type

### Retracted papers
- If CrossRef retraction notice is detected → auto-downgrade to D-tier
- Recommendation: "RETRACTED — do not cite"
- Detection via CrossRef `update-to` field or Retraction Watch database

### Review articles
- Not penalized but flagged: "Review — not primary evidence"
- Should not be cited as primary support for experimental claims
- Detected via publication type ("review", "Review") in OpenAlex/S2

### Open Access bonus
- Small score bonus for OA papers (full text accessible for verification)
- Not a quality indicator per se, but improves verifiability

## Integration Points

- **search_papers**: Each result includes `quality_tier` and `quality_score`
- **WF1**: Results sorted by quality by default
- **WF2**: Citation verification flags papers below B-tier
- **Science Workflow J1/T2**: Core references must be quality_tier ≥ B
