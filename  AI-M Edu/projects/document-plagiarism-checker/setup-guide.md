# Setup guide — Similarity Radar: Document Similarity Checking

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

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
| *(fallback)* | If neither is set, the jar resolves to the **current working directory** → `<cwd>\.google-cookie`. On a typical Windows shell neither `HOME` nor `USERHOME` is set, so this is the branch that actually runs — **the file is created by the library on the first successful Google request; no `.google-cookie` ships with the repository.** Set `HOME` to a writable path if you want the jar kept out of the project folder |

**Hard-coded settings in `app.py` (change by editing the file, not by environment):**

| Setting | Value | Line |
|---|---|---|
| Upload size cap | `MAX_CONTENT_LENGTH = 16 * 1000 * 1000` (16 MB) | `app.py:16` |
| Session signing key | `SECRET_KEY = 'super secret key'` | `app.py:17` |
| Allowed upload extension | `{'pdf'}` only | `app.py:9`, `app.py:19-21` |
| Search TLD / results / pause | `co.id` / `10` / `2` s | `app.py:55`, `app.py:109` |
| Blocked domains | LinkedIn, YouTube, Instagram, Facebook, Twitter, Reddit, Tokopedia, Bukalapak, Shopee, Blibli | `app.py:66-67` |

> **`SECRET_KEY` is a development placeholder.** It is committed in source and signs the
> Flask session cookie that carries flash messages. Do not deploy this as-is; generate a
> random value before any real use.

---

### 2. Installation and Setup

The repository already ships a working virtualenv (`.venv`, Python 3.12.1, all pins
installed). **Use it as-is:**

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\document-plagiarism-checker"
.\.venv\Scripts\Activate.ps1
```

If PowerShell refuses to run the activation script, allow it for the current session and retry:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Confirm the interpreter and the key packages:

```powershell
python --version
python -m pip list
```

Expected: `Python 3.12.1` and `Flask 2.2.2`, `PyPDF2 2.11.1`, `google 3.0.0`,
`gunicorn 20.1.0`, `pytest 7.0.1`.

**To rebuild the environment from scratch** (only if `.venv` is missing or broken):

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\document-plagiarism-checker"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Runtime directories and files the app expects** (all relative to the working directory):

```powershell
# uploads/ already exists and holds a sample PDF (cek.pdf) — the app writes here.
Test-Path .\uploads
Test-Path .\uploads\cek.pdf
Get-ChildItem .\uploads
```

- `uploads/` — where uploaded PDFs are saved (`UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')`, `app.py:7-8`).
- `word.txt` — scratch file holding the last pasted text (`app.py:30`, `app.py:104`).
- `templates/index.html` — the Jinja template; `templates/index.html.bak` is the preserved original upstream template.
- `static/css/style.css`, `static/js/app.js` — the radar gauge, tabs, counters, drag-and-drop and copy buttons.

**Optional — Docker path** (uses the pinned `python:3.8.2` image from the `Dockerfile`):

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\document-plagiarism-checker"
docker build -t similarity-radar .
docker run --rm -p 5000:5000 similarity-radar
```

**There is no configuration file and no `.env`.** Nothing to edit for a local run.

---

### 3. Launch the Complete Project

**You must start the app from the project root.** `app.py` resolves `uploads/` and
`word.txt` against `os.getcwd()`, and the PDF branch re-opens the file with the *relative*
path `uploads/<file>` (`app.py:88`, `app.py:193`). Starting from any other directory breaks
PDF scans.

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\document-plagiarism-checker"
.\.venv\Scripts\Activate.ps1
python app.py
```

Expected console output:

```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. For production, use a production WSGI server.
 * Running on http://127.0.0.1:5000
 * Running on http://<your-lan-ip>:5000
Press CTRL+C to quit
```

- **Port 5000** — `app.run(host="0.0.0.0", debug=False)` (`app.py:231-232`) uses Flask's
  default port and binds **all interfaces**, so the app is also reachable from other
  machines on your LAN.
- **Front end = back end.** The UI is a Jinja template rendered by Flask. There is no
  separate static server, no CORS, no build step.
- **Open:** <http://127.0.0.1:5000/>
- **Stop:** `Ctrl+C` in the terminal running the app.

**Production-style starts (optional, same code):**

```powershell
# From the Procfile
gunicorn app:app --log-file=-
# From the Dockerfile
python -m flask run --host=0.0.0.0
```

**Typical first-run flow (for reference):**

1. Open <http://127.0.0.1:5000/> — the *Input desk* opens on the **Paste text** tab.
2. Paste a passage. The live counters under the box update (`N characters` / `N sentences`),
   split on `". "` exactly as the backend does.
3. Press **Scan originality** (or `Ctrl`/`⌘` + `Enter`).
4. A scanning overlay appears: *"Each sentence is being quoted into Google (TLD `co.id`,
   10 results, short pause per query). Long texts can take a minute or two — please keep
   this tab open."*
5. The browser is redirected to `/plagiarism/word#hasil` and the **Results** panel renders:
   the status stamp (*Original* / *Minor overlap* / *High overlap*, thresholds 0 % / < 30 % /
   ≥

## Known setup risks

- The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.
