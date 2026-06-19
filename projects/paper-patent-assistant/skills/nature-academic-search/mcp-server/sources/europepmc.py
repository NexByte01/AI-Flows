"""Europe PMC data source for academic search.

Uses the Europe PMC REST API directly.
Docs: https://europepmc.org/RestfulWebService
"""

import requests

from utils.config import get_config
from utils.errors import DataSourceError

EUROPEPMC_API = "https://www.ebi.ac.uk/europepmc/webservices/rest"


class EuropePMCSource:
    """Europe PMC API wrapper with unified result format.

    Specializes in Open Access full-text retrieval and citation graph traversal.
    """

    SOURCE_NAME = "europepmc"

    def __init__(self):
        config = get_config()
        self._timeout = config._config.get("europepmc", {}).get("timeout", 30)
        self._headers = {"User-Agent": "ScienceWorkflow-MCP/1.0"}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(self, query: str, rows: int = 5) -> dict:
        """Search Europe PMC for articles.

        Automatically appends OPEN_ACCESS:y to prioritize OA content.

        Args:
            query: Search query using Europe PMC syntax.
            rows: Number of results (max 100).

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        params = {
            "query": f"{query} OPEN_ACCESS:y",
            "resultType": "core",
            "pageSize": min(rows, 100),
            "format": "json",
        }
        data = self._request("/search", params=params)
        total = data.get("hitCount", 0)
        items = data.get("resultList", {}).get("result", [])
        results = [self._normalize_search_item(item) for item in items]
        return {"total": total, "results": results}

    def get_by_pmcid(self, pmcid: str) -> dict:
        """Get metadata for a paper by PMC ID.

        Args:
            pmcid: PubMed Central ID (e.g. "PMC8371605").

        Returns:
            Unified detail result dict.
        """
        # Search for the specific PMCID
        params = {
            "query": f"PMCID:{pmcid}",
            "resultType": "core",
            "pageSize": 1,
            "format": "json",
        }
        data = self._request("/search", params=params)
        items = data.get("resultList", {}).get("result", [])
        if not items:
            raise DataSourceError(
                self.SOURCE_NAME,
                f"PMCID not found: {pmcid}",
            )
        return self._normalize_detail_item(items[0])

    def get_fulltext(self, pmcid: str, fmt: str = "text") -> dict:
        """Get full text of an OA article.

        Args:
            pmcid: PubMed Central ID.
            fmt: "text" for plain text, "xml" for JATS XML.

        Returns:
            {"pmcid": str, "format": str, "content": str}
        """
        url = f"{EUROPEPMC_API}/{pmcid}/fullTextXML"
        try:
            resp = requests.get(url, headers=self._headers, timeout=self._timeout)
            resp.raise_for_status()
        except requests.HTTPError as exc:
            status = exc.response.status_code if exc.response is not None else "?"
            raise DataSourceError(
                self.SOURCE_NAME,
                f"HTTP {status} fetching full text for {pmcid}",
                original_error=exc,
            ) from exc
        except requests.RequestException as exc:
            raise DataSourceError(
                self.SOURCE_NAME,
                f"Network error fetching full text for {pmcid}: {exc}",
                original_error=exc,
            ) from exc

        content = resp.text
        if fmt == "text":
            # Strip XML tags for plain text
            import re
            content = re.sub(r"<[^>]+>", " ", content)
            content = re.sub(r"\s+", " ", content).strip()

        return {
            "pmcid": pmcid,
            "format": fmt,
            "content": content,
        }

    def get_citations(self, source: str, article_id: str, rows: int = 25) -> dict:
        """Get articles that cite a given paper.

        Args:
            source: Source database ("MED", "PMC", "PPR").
            article_id: Article ID in the source database.
            rows: Number of results.

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        url = f"{EUROPEPMC_API}/{source}/{article_id}/citations"
        params = {"page": 1, "pageSize": min(rows, 100), "format": "json"}
        data = self._request_url(url, params=params)
        total = data.get("hitCount", 0)
        items = data.get("citationList", {}).get("citation", [])
        results = [self._normalize_citation_item(item) for item in items]
        return {"total": total, "results": results}

    def get_references(self, source: str, article_id: str, rows: int = 25) -> dict:
        """Get the bibliography (references) of a given paper.

        Args:
            source: Source database ("MED", "PMC", "PPR").
            article_id: Article ID in the source database.
            rows: Number of results.

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        url = f"{EUROPEPMC_API}/{source}/{article_id}/references"
        params = {"page": 1, "pageSize": min(rows, 100), "format": "json"}
        data = self._request_url(url, params=params)
        total = data.get("hitCount", 0)
        items = data.get("referenceList", {}).get("reference", [])
        results = [self._normalize_citation_item(item) for item in items]
        return {"total": total, "results": results}

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _request(self, path: str, params: dict | None = None) -> dict:
        """Issue GET to Europe PMC API and return the JSON payload."""
        url = f"{EUROPEPMC_API}{path}"
        return self._request_url(url, params)

    def _request_url(self, url: str, params: dict | None = None) -> dict:
        """Issue GET to a URL and return the JSON payload."""
        try:
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

    def _normalize_search_item(self, item: dict) -> dict:
        """Map an EPMC article to the unified search result format."""
        authors = self._extract_authors(item)
        return {
            "title": item.get("title", ""),
            "authors": authors[:5] + (["et al."] if len(authors) > 5 else []),
            "year": self._safe_int(item.get("pubYear")),
            "doi": item.get("doi", "") or "",
            "journal": item.get("journalTitle", "") or "",
            "source": self.SOURCE_NAME,
            "citation_count": self._safe_int(item.get("citedByCount", 0)),
            # Extra EPMC-specific fields
            "pmid": item.get("pmid", "") or "",
            "pmcid": item.get("pmcid", "") or "",
            "is_open_access": item.get("isOpenAccess", "N") == "Y",
            "has_fulltext": item.get("hasTextMinedTerms", "N") == "Y"
                or bool(item.get("pmcid")),
        }

    def _normalize_detail_item(self, item: dict) -> dict:
        """Map an EPMC article to the unified detail result format."""
        base = self._normalize_search_item(item)
        base.update({
            "authors": self._extract_authors(item),
            "abstract": item.get("abstractText", "") or "",
            "volume": item.get("journalVolume", "") or "",
            "issue": item.get("issue", "") or "",
            "pages": item.get("pageInfo", "") or "",
            "publisher": item.get("publisherName", "") or "",
            "publication_type": item.get("pubType", "") or "",
            "language": item.get("language", "") or "",
        })
        return base

    def _normalize_citation_item(self, item: dict) -> dict:
        """Map a citation/reference entry to the unified format."""
        return {
            "title": item.get("title", ""),
            "authors": [item.get("authorString", "")],
            "year": self._safe_int(item.get("pubYear")),
            "doi": item.get("doi", "") or "",
            "journal": item.get("journalAbbreviation", "") or "",
            "source": self.SOURCE_NAME,
            "citation_count": self._safe_int(item.get("citedByCount", 0)),
            "pmid": item.get("id", "") or "",
        }

    @staticmethod
    def _extract_authors(item: dict) -> list[str]:
        """Extract author list from EPMC result."""
        # Try structured author list first
        author_list = item.get("authorList", {}).get("author", [])
        if author_list:
            return [
                a.get("fullName", "") or f"{a.get('lastName', '')} {a.get('firstName', '')}".strip()
                for a in author_list
                if a.get("fullName") or a.get("lastName")
            ]
        # Fall back to author string
        author_str = item.get("authorString", "")
        if author_str:
            return [a.strip() for a in author_str.split(",") if a.strip()]
        return []

    @staticmethod
    def _safe_int(value) -> int | None:
        """Safely convert a value to int."""
        if value is None:
            return None
        try:
            return int(value)
        except (ValueError, TypeError):
            return None
