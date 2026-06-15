"""Pytest configuration: make `sources` and `utils` importable without installing.

The source modules use implicit relative imports (`from sources.crossref import …`,
`from utils.config import get_config`). Running `pytest` from this directory should
just work, so we add the package root (the parent of `tests/`) to `sys.path` and
provide a default `PUBMED_EMAIL` env var so config-loading code paths don't blow
up at import time.

No external network calls are made — every test mocks HTTP via `unittest.mock`.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Make `mcp-server/` importable so `import sources`, `import utils`, and
# `import academic_search_server` resolve. Insert at position 0 so the local
# copy takes precedence over anything installed system-wide.
_PKG_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_PKG_ROOT))

# Default values for environment-driven config. Tests that exercise the
# "missing email" path (e.g. TestPubMedSearch.test_search_no_email_raises)
# explicitly clear this and patch the config object, so a default here is safe.
os.environ.setdefault("PUBMED_EMAIL", "test@example.com")
os.environ.setdefault("PUBMED_API_KEY", "")
os.environ.setdefault("CROSSREF_MAILTO", "test@example.com")
