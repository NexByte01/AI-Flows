#!/usr/bin/env bash
# Post-create: install backend Python dependencies
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "==> Installing backend dependencies..."
pip install --upgrade pip
pip install -r "$REPO_ROOT/media-platform/backend/requirements.txt"

echo "==> Environment ready!"
