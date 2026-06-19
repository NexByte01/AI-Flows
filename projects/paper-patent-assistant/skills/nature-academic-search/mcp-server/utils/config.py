"""Configuration management for academic search server."""

import os
from pathlib import Path

import toml


class Config:
    def __init__(self, config_path: str | Path | None = None):
        if config_path is None:
            config_path = Path(__file__).parent.parent / "config.toml"
        self._config = toml.load(config_path)

    @property
    def pubmed_email(self) -> str:
        return os.environ.get("PUBMED_EMAIL") or self._config.get("pubmed", {}).get("email", "")

    @property
    def pubmed_api_key(self) -> str:
        return os.environ.get("NCBI_API_KEY") or self._config.get("pubmed", {}).get("api_key", "")

    @property
    def crossref_mailto(self) -> str:
        return self._config.get("crossref", {}).get("mailto", "")

    @property
    def crossref_timeout(self) -> int:
        return self._config.get("crossref", {}).get("timeout", 15)

    @property
    def arxiv_timeout(self) -> int:
        return self._config.get("arxiv", {}).get("timeout", 30)

    @property
    def openalex_api_key(self) -> str:
        return os.environ.get("OPENALEX_API_KEY") or self._config.get("openalex", {}).get("api_key", "")

    @property
    def openalex_timeout(self) -> int:
        return self._config.get("openalex", {}).get("timeout", 30)

    @property
    def semantic_scholar_api_key(self) -> str:
        return os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or self._config.get("semantic_scholar", {}).get("api_key", "")

    @property
    def semantic_scholar_timeout(self) -> int:
        return self._config.get("semantic_scholar", {}).get("timeout", 15)

    @property
    def europepmc_timeout(self) -> int:
        return self._config.get("europepmc", {}).get("timeout", 30)

    @property
    def default_rows(self) -> int:
        return self._config.get("general", {}).get("default_rows", 5)

    @property
    def max_rows(self) -> int:
        return self._config.get("general", {}).get("max_rows", 50)


# Global config instance
_config: Config | None = None


def get_config() -> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config
