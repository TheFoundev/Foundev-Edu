# Prerequisites — Underwriting Desk: Loan Default Risk Modeling

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# Underwriting Desk (loan-default-prediction) — Setup & Test Workflow

### 1. Prerequisites

- **OS:** Windows (PowerShell)
- **Python:** 3.12.1 (works for inspection; the original pipeline is legacy)
- **Node:** v22.15.0 (not required — this is a static UI)
- **No data included:** `train_v2.csv` / `test_v2.csv` from Kaggle "Loan Default Prediction" are **not** present. 
- **Notes about legacy code:**
  - `train_predict.py` uses Python 2 syntax (`print` statements) and old scikit-learn APIs
  - `models.py` uses `dict.iteritems()` and `np.float` (removed in modern libraries)
  - `sklearn.preprocessing.Imputer` was removed (replaced by `SimpleImputer`)
  - `GradientBoostingClassifier` loss `'deviance'` / `GradientBoostingRegressor` loss `'ls'` renamed to `'log_loss'` / `'squared_error'`
- **Runtime deps for the legacy pipeline (if ported):** an older pandas/scikit-learn build from ~2015 (README pins commit `884889a4`); modern versions will require code changes.

### 2. Installation and Setup

#### Step 1: Open the project directory
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\loan-default-prediction"
```

#### Step 2: (Optional) Create a virtual environment
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### Step 3: Understand what exists (no install required for UI)
- **Static UI:** `index.html`, `css/style.css`, `js/app.js` (vanilla JS, no backend, no model weights). The UI is a labeled demo scorecard using transparent heuristics.
- **Pipeline code:** `models.py`, `train_predict.py`, `tools/lr_clf.py` (for reference only as-is).
- **No `requirements.txt`**, no `package.json`, no weights, no dataset files.

> **If** you want to attempt running the real pipeline, you must supply Kaggle `train_v2.csv` and `test_v2.csv` to some `<data-folder>` and port the Python 2/legacy APIs first. The UI does **not** require this.

### 3. Launch the Complete Project

The "complete project" as implemented is the static **Underwriting Desk** UI (demo worksheet). The real ML pipeline is not runnable as-is.

#### Launch the UI (recommended)
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\loan-default-prediction"
python -m http.server 8000
```
Open: [http://localhost:8000/](http://localhost:8000/)

#### Attempt the legacy pipeline (only if data + porting available)
```powershell
# After obtaining train_v2.csv and test_v2.csv in <data-folder> and porting code:
python train_predict.py <data-folder>
# Expects: <data-folder>\train_v2.csv and <data-folder>\test_v2.csv
# Writes

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
