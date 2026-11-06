# Prerequisites — FraudGuard: Credit Card Fraud Detection

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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
.\.venv\Scri

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
