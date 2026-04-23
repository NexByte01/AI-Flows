#!/usr/bin/env bash
# Post-start: launch backend and frontend servers in the background
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "==> Starting Flask backend on port 5000..."
cd "$REPO_ROOT/media-platform/backend"
nohup python app.py > /tmp/backend.log 2>&1 &

echo "==> Starting frontend static server on port 8080..."
cd "$REPO_ROOT/media-platform/frontend"
nohup python -m http.server 8080 > /tmp/frontend.log 2>&1 &

echo "==> Services started. Backend: http://localhost:5000  Frontend: http://localhost:8080"
