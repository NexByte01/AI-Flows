"""Semantic Scholar data source for academic search.

Uses the Semantic Scholar Academic Graph API v1.
Docs: https://api.semanticscholar.org/api-docs/graph
"""

import os
import time

import requests

from utils.config import get_config
from utils.errors import DataSourceError

S2_API = "https://api.semanticscholar.org/graph/v1"

# Fields to request from the API
_SEARCH_FIELDS = (
    "paperId,externalIds,title,authors,year,venue,publicationVenue,"
    "citationCount,influentialCitationCount,isOpenAccess,openAccessPdf,"
    "fieldsOfStudy,tldr"
)
_DETAIL_FIELDS = (
    "paperId,externalIds,title,authors,year,venue,publicationVenue,"
    "abstract,citationCount,influentialCitationCount,referenceCount,"
    "isOpenAccess,openAccessPdf,fieldsOfStudy,tldr,publicationTypes,"
    "journal,citationStyles"
)
_CITATION_FIELDS = (
    "paperId,externalIds,title,authors,year,venue,"
    "citationCount,isOpenAccess"
)


class SemanticScholarSource:
    """Semantic Scholar Academic Graph API wrapper with unified result format."""

    SOURCE_NAME = "semantic_scholar"

    def __init__(self):
        config = get_config()
        api_key = (
            os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
            or config._config.get("semantic_scholar", {}).get("api_key", "")
        )
        self._headers = {"User-Agent": "ScienceWorkflow-MCP/1.0"}
        if api_key:
            self._headers["x-api-key"] = api_key
        self._timeout = config._config.get("semantic_scholar", {}).get("timeout", 15)
        # Rate limiting: 1 req/s without key, relaxed with key
        self._has_key = bool(api_key)
        self._last_request_time = 0.0

    # ------------------------------------------------------------------
    # Rate limiting
    # ------------------------------------------------------------------

    def _rate_limit(self) -> None:
        """Enforce rate limiting between requests."""
        min_interval = 0.1 if self._has_key else 1.1
        elapsed = time.time() - self._last_request_time
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self._last_request_time = time.time()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(self, query: str, rows: int = 5) -> dict:
        """Search for papers by keyword.

        Args:
            query: Search keywords.
            rows: Number of results (max 100).

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        self._rate_limit()
        params = {
            "query": query,
            "limit": min(rows, 100),
            "fields": _SEARCH_FIELDS,
        }
        data = self._request("/paper/search", params=params)
        total = data.get("total", 0)
        items = data.get("data", [])
        results = [self._normalize_search_item(item) for item in items]
        return {"total": total, "results": results}

    def get_by_id(self, paper_id: str) -> dict:
        """Get detailed metadata for a paper.

        Args:
            paper_id: Semantic Scholar paper ID, DOI (prefixed with DOI:),
                      arXiv ID (prefixed with ARXIV:), or PMID (prefixed with PMID:).

        Returns:
            Unified detail result dict.
        """
        self._rate_limit()
        data = self._request(f"/paper/{paper_id}", params={"fields": _DETAIL_FIELDS})
        return self._normalize_detail_item(data)

    def get_citations(self, paper_id: str, rows: int = 20) -> dict:
        """Get papers that cite the given paper.

        Args:
            paper_id: Paper identifier.
            rows: Number of results.

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        self._rate_limit()
        params = {"fields": _CITATION_FIELDS, "limit": min(rows, 100)}
        data = self._request(f"/paper/{paper_id}/citations", params=params)
        items = data.get("data", [])
        results = [
            self._normalize_search_item(item.get("citingPaper", {}))
            for item in items
            if item.get("citingPaper")
        ]
        return {"total": len(results), "results": results}

    def get_references(self, paper_id: str, rows: int = 20) -> dict:
        """Get papers referenced by the given paper.

        Args:
            paper_id: Paper identifier.
            rows: Number of results.

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        self._rate_limit()
        params = {"fields": _CITATION_FIELDS, "limit": min(rows, 100)}
        data = self._request(f"/paper/{paper_id}/references", params=params)
        items = data.get("data", [])
        results = [
            self._normalize_search_item(item.get("citedPaper", {}))
            for item in items
            if item.get("citedPaper")
        ]
        return {"total": len(results), "results": results}

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _request(self, path: str, params: dict | None = None) -> dict:
        """Issue GET to Semantic Scholar API and return the JSON payload."""
        url = f"{S2_API}{path}"
        try:
            resp = requests.get(
                url, params=params, headers=self._headers, timeout=self._timeout
            )
            if resp.status_code == 429:
                # Rate limited — wait and retry once
                time.sleep(2.0)
                resp = requests.get(
                    url, params=params, headers=self._headers, timeout=self._timeout
                )
            resp.raise_for_status()
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else "?"
            raise DataSourceError(
                self.SOURCE_NAME,
                f"HTTP {status} from {url}",
                original_error=exc,
            ) from exc
        except requests.RequestException as exc:
            raise DataSourceError(
                self.SOURCE_NAME,
                f"Network error calling {url}: {exc}",
                original_error=exc,
            ) from exc

        return resp.json()

    # ------------------------------------------------------------------
    # Normalization
    # ------------------------------------------------------------------

    @staticmethod
    def _extract_doi(external_ids: dict | None) -> str:
        """Extract DOI from externalIds dict."""
        if not external_ids:
            return ""
        return external_ids.get("DOI", "") or ""

    @staticmethod
    def _extract_authors(authors: list[dict], limit: int = 0) -> list[str]:
        """Convert S2 author entries to name list."""
        subset = authors[:limit] if limit else authors
        names = [a.get("name", "") for a in subset if a.get("name")]
        if limit and len(authors) > limit:
            names.append("et al.")
        return names

    def _normalize_search_item(self, item: dict) -> dict:
        """Map an S2 paper to the unified search result format."""
        external_ids = item.get("externalIds") or {}
        venue = item.get("venue", "")
        pub_venue = item.get("publicationVenue") or {}

        # Prefer publicationVenue.name over venue string
        journal = pub_venue.get("name") or venue or ""

        oa_pdf = item.get("openAccessPdf") or {}

        return {
            "title": item.get("title", ""),
            "authors": self._extract_authors(item.get("authors", []), limit=5),
            "year": item.get("year"),
            "doi": self._extract_doi(external_ids),
            "journal": journal,
            "source": self.SOURCE_NAME,
            "citation_count": item.get("citationCount", 0),
            # Extra S2-specific fields
            "s2_paper_id": item.get("paperId", ""),
            "influential_citation_count": item.get("influentialCitationCount", 0),
            "is_open_access": item.get("isOpenAccess", False),
            "open_access_pdf": oa_pdf.get("url", ""),
            "fields_of_study": item.get("fieldsOfStudy") or [],
            "tldr": (item.get("tldr") or {}).get("text", ""),
        }

    def _normalize_detail_item(self, item: dict) -> dict:
        """Map an S2 paper to the unified detail result format."""
        base = self._normalize_search_item(item)
        external_ids = item.get("externalIds") or {}
        journal_info = item.get("journal") or {}

        base.update({
            "authors": self._extract_authors(item.get("authors", [])),
            "abstract": item.get("abstract", "") or "",
            "volume": journal_info.get("volume", ""),
            "pages": journal_info.get("pages", ""),
            "reference_count": item.get("referenceCount", 0),
            "publication_types": item.get("publicationTypes") or [],
            "pmid": external_ids.get("PubMed", ""),
            "arxiv_id": external_ids.get("ArXiv", ""),
        })
        return base
