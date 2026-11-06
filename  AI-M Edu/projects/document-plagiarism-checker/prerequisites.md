# Prerequisites — Similarity Radar: Document Similarity Checking

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# Similarity Radar (document-plagiarism-checker) — Setup & Test Workflow

**Folder id:** `document-plagiarism-checker`
**UI name:** Similarity Radar
**Stack:** Flask 2.2.2 · Jinja2 3.1.2 · Werkzeug 2.2.2 · PyPDF2 2.11.1 · `google` 3.0.0 (imports as `googlesearch`) · gunicorn 20.1.0 · pytest 7.0.1
**Entry point:** `app.py` (single-file Flask app; no build step, no front-end framework, no JavaScript bundler)

**What it actually is:** a server-rendered web app that splits your text (pasted or extracted
from a PDF) into sentences, quotes each sentence verbatim into a live Google search
(TLD `co.id`, 10 results, 2-second pause), filters out social/marketplace domains, and reports
a similarity index of `matched sentences ÷ total sentences × 100`. It is a *web-presence*
measure, not a semantic/TF-IDF comparison — there is no local corpus and no API key.

**Runtime surfaces:**

| Surface | Kind | Port | Needs internet? |
|---|---|---|---|
| `app.py` → `/` and `/plagiarism/<name>` | Flask web app (server-rendered HTML) | 5000 | **Yes** — every scan queries Google |
| `python -m pytest -q` | Automated smoke test | n/a | No |

---

### 1. Prerequisites

- **Windows 10/11** with PowerShell (all commands below are Windows PowerShell).
- **Python 3.12.1** — the bundled `.venv` was created with it and every pinned package
  installs cleanly on 3.12. The pins (`MarkupSafe==2.1.1`, `zipp==3.10.0`) target the
  3.12-era stack; do **not** use Python 3.13+.
- **An internet connection** — mandatory for any scan. `app.py` calls
  `googlesearch.search(query, tld="co.id", num=10, stop=10, pause=2)` for every sentence.
- **No Node.js, no database, no API key, no Google Custom Search credentials.**
- **Optional:** Docker Desktop, if you prefer the container path.
- **Free disk space:** negligible (< 100 MB); the `.venv` is already present.

Environment variable that matters (read by the `googlesearch` library, not by this repo):

| Variable | Effect |
|---|---|
| `HOME` | Location of the `.google-cookie` cookie jar → `os.path.join(HOME, ".google-cookie")` |
| `USERHOME` | Fallback for `HOME` (note: the library spells it `USERHOME`, **not** `USERPROFILE`) |
| *(fallback)* | If neither is set, the jar resolves to the **current working directory** → `<cwd>\.google-cookie`. On a typical Windows shell neither `HOME` nor `USERHOME` is set, so this is the branch that actually runs — **the file is created by the library on the first successful Google request; no `.google-cookie` ships with the repository.** Set `HOME` to a writable path if you want the jar kept out of the project folder

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
