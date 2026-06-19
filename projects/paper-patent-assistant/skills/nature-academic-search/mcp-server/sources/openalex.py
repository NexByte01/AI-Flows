"""OpenAlex data source for academic search.

Uses the OpenAlex REST API directly (not the CLI wrapper).
Docs: https://docs.openalex.org/
"""

import os

import requests

from utils.config import get_config
from utils.errors import DataSourceError

OPENALEX_API = "https://api.openalex.org"


class OpenAlexSource:
    """OpenAlex API wrapper with unified result format."""

    SOURCE_NAME = "openalex"

    def __init__(self):
        config = get_config()
        self._api_key = (
            os.environ.get("OPENALEX_API_KEY")
            or config._config.get("openalex", {}).get("api_key", "")
        )
        self._timeout = config._config.get("openalex", {}).get("timeout", 30)
        self._headers = {"User-Agent": "ScienceWorkflow-MCP/1.0"}

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def search(self, query: str, rows: int = 5) -> dict:
        """Search for works by keyword.

        Args:
            query: Search keywords.
            rows: Number of results (max 100).

        Returns:
            {"total": int, "results": [unified_result, ...]}
        """
        params: dict = {
            "search": query,
            "per_page": min(rows, 100),
        }
        data = self._request("/works", params=params)
        total = data.get("meta", {}).get("count", 0)
        items = data.get("results", [])
        results = [self._normalize_search_item(item) for item in items]
        return {"total": total, "results": results}

    def get_by_doi(self, doi: str) -> dict:
        """Get detailed metadata for a work by DOI.

        Args:
            doi: DOI string (e.g. "10.1038/nature12373").

        Returns:
            Unified detail result dict.
        """
        # OpenAlex accepts DOI URLs as identifiers
        doi_url = doi if doi.startswith("http") else f"https://doi.org/{doi}"
        data = self._request(f"/works/{doi_url}")
        return self._normalize_detail_item(data)

    def get_by_id(self, work_id: str) -> dict:
        """Get detailed metadata for a work by OpenAlex ID.

        Args:
            work_id: OpenAlex work ID (e.g. "W2741809807" or full URL).

        Returns:
            Unified detail result dict.
        """
        data = self._request(f"/works/{work_id}")
        return self._normalize_detail_item(data)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _request(self, path: str, params: dict | None = None) -> dict:
        """Issue GET to OpenAlex API and return the JSON payload."""
        url = f"{OPENALEX_API}{path}"
        if params is None:
            params = {}

        # Add API key if available
        if self._api_key:
            params["api_key"] = self._api_key

        try:
            resp = requests.get(
                url, params=params, headers=self._headers, timeout=self._timeout
            )
            if resp.status_code == 429:
                import time
                time.sleep(1.0)
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
    def _extract_authors(authorships: list[dict], limit: int = 0) -> list[str]:
        """Convert OpenAlex authorship entries to name list."""
        subset = authorships[:limit] if limit else authorships
        names = [
            a.get("author", {}).get("display_name", "")
            for a in subset
            if a.get("author", {}).get("display_name")
        ]
        if limit and len(authorships) > limit:
            names.append("et al.")
        return names

    @staticmethod
    def _extract_journal(item: dict) -> str:
        """Extract journal/source name from primary_location."""
        loc = item.get("primary_location") or {}
        source = loc.get("source") or {}
        return source.get("display_name", "")

    @staticmethod
    def _extract_doi(item: dict) -> str:
        """Extract clean DOI from OpenAlex work."""
        doi = item.get("doi", "") or ""
        if doi.startswith("https://doi.org/"):
            doi = doi[len("https://doi.org/"):]
        return doi

    def _normalize_search_item(self, item: dict) -> dict:
        """Map an OpenAlex work to the unified search result format."""
        oa_info = item.get("open_access") or {}

        return {
            "title": item.get("title", "") or item.get("display_name", ""),
            "authors": self._extract_authors(
                item.get("authorships", []), limit=5
            ),
            "year": item.get("publication_year"),
            "doi": self._extract_doi(item),
            "journal": self._extract_journal(item),
            "source": self.SOURCE_NAME,
            "citation_count": item.get("cited_by_count", 0),
            # Extra OpenAlex-specific fields
            "openalex_id": item.get("id", ""),
            "is_open_access": item.get("is_oa", False),
            "oa_url": oa_info.get("oa_url", ""),
            "type": item.get("type", ""),
            "topics": [
                t.get("display_name", "")
                for t in (item.get("topics") or [])[:3]
            ],
        }

    def _normalize_detail_item(self, item: dict) -> dict:
        """Map an OpenAlex work to the unified detail result format."""
        base = self._normalize_search_item(item)

        # Extract richer location data
        loc = item.get("primary_location") or {}
        source_info = loc.get("source") or {}

        base.update({
            "authors": self._extract_authors(item.get("authorships", [])),
            "abstract": self._reconstruct_abstract(item),
            "volume": (item.get("biblio") or {}).get("volume", ""),
            "issue": (item.get("biblio") or {}).get("issue", ""),
            "pages": self._extract_pages(item),
            "publisher": source_info.get("host_organization_name", ""),
            "source_type": source_info.get("type", ""),
            "source_issn": (source_info.get("issn") or [""])[0] if source_info.get("issn") else "",
            "language": item.get("language", ""),
            "referenced_works_count": len(item.get("referenced_works", [])),
        })
        return base

    @staticmethod
    def _reconstruct_abstract(item: dict) -> str:
        """Reconstruct abstract from abstract_inverted_index."""
        aii = item.get("abstract_inverted_index")
        if not aii:
            return ""
        # Invert the index: {word: [positions]} -> [(position, word)]
        pairs: list[tuple[int, str]] = []
        for word, positions in aii.items():
            for pos in positions:
                pairs.append((pos, word))
        pairs.sort(key=lambda p: p[0])
        return " ".join(word for _, word in pairs)

    @staticmethod
    def _extract_pages(item: dict) -> str:
        """Extract page range from biblio."""
        biblio = item.get("biblio") or {}
        first = biblio.get("first_page", "")
        last = biblio.get("last_page", "")
        if first and last:
            return f"{first}-{last}"
        return first or ""
