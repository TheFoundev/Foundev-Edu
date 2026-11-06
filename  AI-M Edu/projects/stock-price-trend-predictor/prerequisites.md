# Prerequisites — TrendCast: Stock Price Trend Research

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# TrendCast (stock-price-trend-predictor) — Setup & Test Workflow

### 1. Prerequisites

- **OS**: Windows (PowerShell)
- **Python**: 3.12.1 (context). **Warning:** `requirements.txt` pins very old packages (pandas==1.0.4, scikit-learn==0.23.1, numpy==1.18.5, yfinance==0.1.54, xgboost==1.1.0) — these may not install cleanly on Python 3.12. Consider a legacy environment or modernizing carefully.
- **Node.js**: v22.15.0 (not required for scripts/UI serving)
- **Browser**: Modern browser
- **GNU Make** (optional): `Makefile` present (Windows may need `mingw32-make`/WSL)

### 2. Installation and Setup

From `N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\stock-price-trend-predictor\`:

```powershell
py -3.12 -m venv .venv  # may need older Python for pinned deps
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Known issues (ground truth):**
- `src/data/make_dataset.py` lines ~73-74 contain an **IndentationError** (`except:` followed by same-indent `i += 1`) — the module **cannot be imported** as-is.
- `scripts/script.py` referenced by CI does **not exist**.
- No trained weight files shipped (notebook save line commented). Data present in `data/raw/*` and `data/processed/*` (includes `daily-rolling-binary-curated.csv`, weekly curated files).
- `test_environment.py` exists to check environment.

### 3. Launch the Complete Project

**No HTTP backend/API.** Components are scripts, notebooks, and a static UI.

#### Option A: Static UI (primary visual)
```powershell
py -m http.server 8000
```
Open [http://localhost:8000/](http://localhost:8000/). `js/app.js` fetches processed CSVs (e.g. `data/processed/daily-rolling-binary-curated.csv`, weekly) and computes Pearson correlations in-browser; charts via Chart.js CDN. Must be served over HTTP.

#### Option B: Environment check
```powershell
python test_environment.py
```
Checks basic environment setup per repo conventions.

#### Option C: Data/scripts/notebooks (investigation)
- `src/data/make_dataset.py` — **broken** due to indentation error (documented). Do not expect import to succeed.
- `src/data/update_data.py`, `src/features/build_features.py` — may have their own deps/expectations.
- Notebooks in `notebooks/` (`01 MLP+XGBoost training`, `02 research`, `03 viz`) — run in Jupyter with deps installed (old pins).

### 4. Test the Project

**Automated tests:** None obvious in repo root; `Makefile` has `test_environment` but no `test` target that runs a pytest suite visible here.

**Manual verification:**
| Component | How to test | Expected |
|---|---|---|
| UI | Serve HTTP,

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
