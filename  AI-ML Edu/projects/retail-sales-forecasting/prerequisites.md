# Prerequisites — DemandSight: Retail Sales Analytics

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# DemandSight (retail-sales-forecasting) — Setup & Test Workflow

### 1. Prerequisites

- **OS**: Windows (PowerShell)
- **Python**: 3.12.1 (tested context)
- **Node.js**: v22.15.0 (not strictly required for runtime; only if you extend tooling)
- **Browser**: Modern browser (Chrome/Edge/Firefox)
- **MySQL** (optional): If you want to run `run_all_queries.py`, a local MySQL instance is needed (script uses hardcoded `root`/`MYSQL` to DB `superstore`). `pymysql` is required but **not listed** in `requirements.txt`.
- **Network**: Not required for static UI. Required if you add CDNs/extensions; current UI uses Chart.js from CDN.

### 2. Installation and Setup

From `N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\retail-sales-forecasting\` in PowerShell:

```powershell
# Create/activate venv (recommended)
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install Python deps (note: pymysql is NOT in requirements.txt)
pip install -r requirements.txt
pip install pymysql  # needed for app.py/run_all_queries.py MySQL usage
```

**Notes (ground truth):**
- `requirements.txt` (unpinned): `pandas`, `numpy`, `matplotlib`, `seaborn`, `sqlalchemy`.
- `app.py` hardcodes `r"E:\Retail Sales Analysis\dataset\Superstore.csv"` (line ~5). You must either update this path to `.\dataset\Superstore.csv` or create that directory/structure if you want to run the ETL script as-is.
- `run_all_queries.py` hardcodes MySQL creds (`root`/`MYSQL`) and DB `superstore`. `sql/retail_analysis.sql` contains 15 SELECT queries.
- Data already present: `dataset\Superstore.csv` (9994 rows), `cleaned dataset\cleaned_superstore.csv`.

### 3. Launch the Complete Project

This project has **no HTTP backend/API**. The real product is the **static UI**. There is an ETL script (`app.py`) and a SQL runner (`run_all_queries.py`) — neither serves the UI.

#### Option A: Launch the static UI (required to view the app)
From the project root:

```powershell
py -m http.server 8000
```

Open: [http://localhost:8000/](http://localhost:8000/) (load `index.html`). The UI reads `dataset/Superstore.csv` client-side via `fetch()` in `js/app.js` (Chart.js from CDN). Serving over HTTP is required (fetch of local CSV is blocked on `file://`).

#### Option B: Run ETL script (optional, MySQL-dependent)
**Known issues:** hardcoded path `E:\...` and will attempt MySQL operations depending on your environment. Edit paths/creds before running.

```powershell
python app.py
```

#### Option C: Run SQL analysis (optional)
Requires MySQL with DB `superstore` and matching creds; ensure `sql/retail_analys

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
