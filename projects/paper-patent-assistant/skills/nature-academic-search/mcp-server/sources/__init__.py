"""Data source modules for academic search."""

from .crossref import CrossRefSource
from .pubmed import PubMedSource
from .arxiv import ArxivSource
from .openalex import OpenAlexSource
from .semantic_scholar import SemanticScholarSource
from .europepmc import EuropePMCSource

__all__ = [
    "CrossRefSource",
    "PubMedSource",
    "ArxivSource",
    "OpenAlexSource",
    "SemanticScholarSource",
    "EuropePMCSource",
]
