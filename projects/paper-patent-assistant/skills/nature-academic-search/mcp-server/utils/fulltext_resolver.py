"""Full-text resolution module.

Resolves the best available full-text for a given paper, using a priority chain
across multiple Open Access sources.

Priority chain:
1. Europe PMC OA XML (structured, best for extraction)
2. arXiv PDF (preprints, always available)
3. OpenAlex OA PDF URL
4. Semantic Scholar open_access_pdf
5. Abstract only (fallback)
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger(__name__)


class FullTextStatus(str, Enum):
    AVAILABLE = "available"
    ABSTRACT_ONLY = "abstract_only"
    FAILED = "failed"


class FullTextFormat(str, Enum):
    XML = "xml"
    PDF_URL = "pdf_url"
    TEXT = "text"
    NONE = "none"


@dataclass
class FullTextResult:
    """Result of a full-text resolution attempt."""
    status: FullTextStatus
    format: FullTextFormat = FullTextFormat.NONE
    content: str = ""
    url: str = ""
    source: str = ""
    paper_id: str = ""
    error: str = ""

    def to_dict(self) -> dict:
        return {
            "status": self.status.value,
            "format": self.format.value,
            "content_length": len(self.content),
            "url": self.url,
            "source": self.source,
            "paper_id": self.paper_id,
            "error": self.error,
        }


class FullTextResolver:
    """Resolves full text for papers using a multi-source priority chain."""

    def __init__(self, europepmc=None, openalex=None, semantic_scholar=None):
        """Initialize with source adapters.

        Args:
            europepmc: EuropePMCSource instance
            openalex: OpenAlexSource instance
            semantic_scholar: SemanticScholarSource instance
        """
        self._europepmc = europepmc
        self._openalex = openalex
        self._s2 = semantic_scholar

    def resolve(
        self,
        doi: str = "",
        pmid: str = "",
        pmcid: str = "",
        arxiv_id: str = "",
        openalex_id: str = "",
    ) -> FullTextResult:
        """Resolve full text using the priority chain.

        Provide as many identifiers as available for best results.

        Returns:
            FullTextResult with the best available full text.
        """
        paper_id = doi or pmid or pmcid or arxiv_id or openalex_id

        # 1. Europe PMC OA XML (best structured format)
        if self._europepmc:
            result = self._try_europepmc(doi=doi, pmid=pmid, pmcid=pmcid)
            if result and result.status == FullTextStatus.AVAILABLE:
                result.paper_id = paper_id
                return result

        # 2. arXiv PDF URL (preprints)
        if arxiv_id:
            return FullTextResult(
                status=FullTextStatus.AVAILABLE,
                format=FullTextFormat.PDF_URL,
                url=f"https://arxiv.org/pdf/{arxiv_id}",
                source="arxiv",
                paper_id=paper_id,
            )

        # 3. OpenAlex OA PDF URL
        if self._openalex and (doi or openalex_id):
            result = self._try_openalex(doi=doi, openalex_id=openalex_id)
            if result and result.status == FullTextStatus.AVAILABLE:
                result.paper_id = paper_id
                return result

        # 4. Semantic Scholar OA PDF
        if self._s2 and doi:
            result = self._try_semantic_scholar(doi=doi)
            if result and result.status == FullTextStatus.AVAILABLE:
                result.paper_id = paper_id
                return result

        # 5. Abstract only
        return FullTextResult(
            status=FullTextStatus.ABSTRACT_ONLY,
            source="none",
            paper_id=paper_id,
            error="No open-access full text found across all sources.",
        )

    def _try_europepmc(
        self, doi: str = "", pmid: str = "", pmcid: str = ""
    ) -> FullTextResult | None:
        """Try Europe PMC for full text."""
        try:
            # If we have a PMCID, go straight to full text
            if pmcid:
                ft = self._europepmc.get_fulltext(pmcid, fmt="text")
                if ft.get("content"):
                    return FullTextResult(
                        status=FullTextStatus.AVAILABLE,
                        format=FullTextFormat.TEXT,
                        content=ft["content"],
                        source="europepmc",
                    )

            # Otherwise search by DOI or PMID to find the PMCID
            if doi:
                query = f"DOI:{doi}"
            elif pmid:
                query = f"EXT_ID:{pmid} AND SRC:MED"
            else:
                return None

            search = self._europepmc.search(query, rows=1)
            results = search.get("results", [])
            if not results:
                return None

            found_pmcid = results[0].get("pmcid", "")
            if not found_pmcid:
                return None

            ft = self._europepmc.get_fulltext(found_pmcid, fmt="text")
            if ft.get("content"):
                return FullTextResult(
                    status=FullTextStatus.AVAILABLE,
                    format=FullTextFormat.TEXT,
                    content=ft["content"],
                    source="europepmc",
                )
        except Exception as exc:
            logger.debug("Europe PMC full text failed: %s", exc)
        return None

    def _try_openalex(
        self, doi: str = "", openalex_id: str = ""
    ) -> FullTextResult | None:
        """Try OpenAlex for OA PDF URL."""
        try:
            if doi:
                work = self._openalex.get_by_doi(doi)
            elif openalex_id:
                work = self._openalex.get_by_id(openalex_id)
            else:
                return None

            oa_url = work.get("oa_url", "")
            if oa_url:
                return FullTextResult(
                    status=FullTextStatus.AVAILABLE,
                    format=FullTextFormat.PDF_URL,
                    url=oa_url,
                    source="openalex",
                )
        except Exception as exc:
            logger.debug("OpenAlex OA URL failed: %s", exc)
        return None

    def _try_semantic_scholar(self, doi: str) -> FullTextResult | None:
        """Try Semantic Scholar for OA PDF URL."""
        try:
            paper = self._s2.get_by_id(f"DOI:{doi}")
            pdf_url = paper.get("open_access_pdf", "")
            if pdf_url:
                return FullTextResult(
                    status=FullTextStatus.AVAILABLE,
                    format=FullTextFormat.PDF_URL,
                    url=pdf_url,
                    source="semantic_scholar",
                )
        except Exception as exc:
            logger.debug("Semantic Scholar OA PDF failed: %s", exc)
        return None
