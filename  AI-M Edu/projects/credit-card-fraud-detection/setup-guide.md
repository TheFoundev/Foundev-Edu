# Setup guide — FraudGuard: Credit Card Fraud Detection

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# FraudGuard Console (credit-card-fraud-detection) — Setup & Test Workflow

This document covers **how to install, configure, launch and test the complete project**: the Flask
prediction service (`src/flask_app.py`, port **5000**) and the static FraudGuard console
(`index.html` + `css/style.css` + `js/app.js`, port **8000**), plus the optional training step that
produces the missing model artefact.

**Honest scope note up front:** the API exists and works, but **the trained model is not shipped** —
`models/model.pickle` is absent and `data/creditcard.csv` (the Kaggle dataset) is absent too. Until you
supply the dataset and run `src/train.py`, `POST /predict` correctly answers **HTTP 503 "Model not
loaded"**, and the console shows that error rather than a fabricated score. The API also has **no
`/health` endpoint** — it exposes exactly two routes: `POST /predict` and `OPTIONS /predict`.

---

### 1. Prerequisites

| Requirement | Version / detail | Checked with |
|---|---|---|
| OS | Windows 10/11 (commands below are PowerShell) | `Get-Host` |
| Python | **3.12.1** (already present as `.venv`) | `.\.venv\Scripts\python.exe --version` |
| Flask | **3.1.3** (already in `.venv`) | `.\.venv\Scripts\python.exe -m pip show flask` |
| scikit-learn | **1.9.1** (already in `.venv`) | `.\.venv\Scripts\python.exe -m pip show scikit-learn` |
| pandas / joblib / numpy | 3.0.6 / 1.6.0 / 2.5.4 (already in `.venv`) | `.\.venv\Scripts\python.exe -m pip list` |
| Node.js | **Not required** — the console is plain HTML/CSS/JS, no build step | — |
| API keys | **None.** The service reads no `.env` and no environment variables | — |
| Internet | Only for `pip install` and for downloading the Kaggle dataset | — |
| **Optional, for real inference** | Kaggle dataset `mlg-ulb/creditcardfraud` → `data/creditcard.csv` (~150 MB) | <https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud> |

Project root (used by every command below):

```powershell
$root = "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\credit-card-fraud-detection"
Set-Location $root
```

---

### 2. Installation and Setup

#### 2.1 The shipped virtual environment

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\credit-card-fraud-detection"
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip list
```

Expected (verified in this checkout):

```
Python 3.12.1
Flask        3.1.3
joblib      1.6.0
numpy       2.5.4
pandas      3.0.6
scikit-learn 1.9.1
```

If you need to rebuild it:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements-modern.txt
```

> **Do not use `requirements.txt`** — it pins 2017 versions (`Flask==0.12.2`, `numpy==1.13.1`,
> `pandas==0.20.3`, `scikit-learn==0.18.2`, `scipy==0.19.1`) that cannot be installed on Python 3.12.
> `requirements-modern.txt` is the supported set: `flask>=2.3`, `scikit-learn>=1.3`, `pandas>=2.0`,
> `joblib>=1.3`.
> `requirements-dev.txt` (`nose==1.3.7`) is also unusable on Python 3.10+ — see
> [Section 4.1](#41-automated--command-line-tests).

**pytest is not installed** in the shipped venv (verified: `No module named pytest`). If you want the
pytest flavour of the test suite, install it once:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
```

#### 2.2 Configuration

**There is none.** The service reads no environment variables and no `.env` file. The only two settings are
file paths hard-coded in `src/settings.py`:

```python
PARENT_DIR_PATH   = os.path.dirname(os.path.realpath(os.path.join(__file__, '..')))
DATASET_FILENAME  = os.path.join(PARENT_DIR_PATH, "data", "creditcard.csv")
MODEL_FILENAME    = os.path.join(PARENT_DIR_PATH, "models", "model.pickle")
```

**Browser-side settings** (`localStorage`, editable in the console's top bar):

| Key | Default | Purpose |
|---|---|---|
| `fraudguard.apiBase` | `http://127.0.0.1:5000` | Base URL of the API; re-probed when you change it |
| `fraudguard.threshold` | `0.50` | Alert threshold for the LOW / MEDIUM / HIGH bands |
| `fraudguard.auditLog` | *(empty)* | The audit trail (max 200 entries) |

The default `apiBase` matches the backend's bind address, so **no editing is required**. The service sets
`Access-Control-Allow-Origin: *` in an `@app.after_request` hook, so a console served from
`http://localhost:8000` can call `http://127.0.0.1:5000` cross-origin.

#### 2.3 Supplying the model (optional but required for real scores)

Both artefact folders currently contain only a `.gitignore` — verified:

```powershell
Get-ChildItem models, data -Force
```

To unlock real inference:

1. **Download the dataset** — Kaggle dataset `mlg-ulb/creditcardfraud` (sign-in required). The archive
   contains `creditcard.csv` (~150 MB, 284 807 rows, columns `Time, V1..V28, Amount, Class`).
2. **Place it as** `data/creditcard.csv`:

   ```powershell
   # after downloading and extracting the archive into your downloads folder
   Copy-Item "$HOME\Downloads\creditcard.csv" ".\data\creditcard.csv"
   Test-Path .\data\creditcard.csv     # -> True
   ```

3. **Train the model** (writes `models/model.pickle`):

   ```powershell
   Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\credit-card-fraud-detection"
   .\.venv\Scripts\python.exe src\train.py
   ```

   `src/train.py` runs a `GridSearchCV` over a `LogisticRegression(class_weight="balanced")` pipeline
   (`C ∈ {1e-4, 1e-2, 1e0, 1e2, 1e4}`, `cv=10`, `scoring="recall_macro"`, `n_jobs=-1`) over an 80/20
   split (`random_state=42`), then `joblib.dump`s the best estimator to `models/model.pickle`.
   **This takes several minutes** on the full dataset and is CPU-heavy.

4. **Restart the API** — the model is loaded once at import time:

   ```python
   app.model = None
   if os.path.exists(MODEL_FILENAME):
       app.model = joblib.load(MODEL_FILENAME)
   ```

   So `POST /predict` only stops returning 503 after a **fresh** start of `src/flask_app.py`.

> **Skipping all of this is a supported state.** The API stays up and returns a structured
> `503 {"error": "Model not loaded", "detail": "models/model.pickle is missing. Train it first: place
> data/creditcard.csv then run python src/train.py"}`, and the console renders that error. This is the
> documented behaviour of the repository as shipped, not a defect.

---

### 3. Launch the Complete Project

#### 3.1 Backend — Flask prediction service on port 5000

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\credit-card-fraud-detection"
.\.venv\Scripts\python.exe src\flask_app.py
```

Expected console output:

```
 * Serving Flask app 'Fraud Detection'
 * Debug mode: off
WARNING: This is a development server. ...
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Stop with `Ctrl+C`.

**Equivalent Flask-CLI invocation** (same port, same behaviour):

```powershell
$env:FLASK_APP = "src/flask_app.py"
.\.venv\Scripts\python.exe -m flask run
```

> `src/flask_app.py` uses the flat import `from settings import MODEL_FILENAME`. Both commands work because
> the script's own directory (`src/`) is placed on `sys.path` automatically.

#### 3.2 Frontend — the FraudGuard console on port 8000

Open a **second** PowerShell window:

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\credit-card-fraud-detection"
python -m http.server 8000
```

Open **http://localhost:8000**. (Opening `index.html` directly also works — all asset paths

## Known setup risks

- A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.
