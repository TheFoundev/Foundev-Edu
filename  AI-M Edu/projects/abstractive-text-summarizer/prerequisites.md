# Prerequisites — FactCheck Studio: Factual Consistency and Summarization

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# FactCheck Studio (abstractive-text-summarizer) — Setup & Test Workflow

This document covers **how to install, configure, launch and test the complete project**: the
Flask consistency service (`src/api.py`), the static browser UI (`index.html` + `css/style.css` +
`js/app.js`), and the optional research CLI (`modeling/run.py`).

**Honest scope note up front:** the shipped backend (`src/api.py`) is a **deterministic lexical-entailment
engine**, not the neural FactCC / FactCCX pointer-BERT model. It reports this itself in every response
(`"engine": "lexical-entailment (heuristic)"`, `"model_checkpoint": false`). The neural path lives in
`modeling/run.py`, requires the pinned 2020 dependency stack and external multi-GB checkpoints, and **cannot
be installed on Python 3.12** — details in [Section 5](#5-troubleshooting).

---

### 1. Prerequisites

| Requirement | Version / detail | Checked with |
|---|---|---|
| OS | Windows 10/11 (commands below are PowerShell) | `Get-Host` |
| Python | **3.12.1** (already present as `.venv`) | `.\.venv\Scripts\python.exe --version` |
| Flask | **3.1.3** (already present in `.venv`) | `.\.venv\Scripts\python.exe -m pip show flask` |
| Node.js | **Not required.** The UI is plain HTML/CSS/JS with no build step | — |
| Network | Only for `pip install`; the app itself runs fully offline | — |
| API keys | **None.** The service reads no `.env`, no environment variables | — |
| Browser | Any modern Chrome/Edge/Firefox (used for the UI + CORS) | — |

> **No API key, no account, no model download is required for the shipped UI + service.**

Project root (used by every command below):

```powershell
$root = "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\abstractive-text-summarizer"
Set-Location $root
```

---

### 2. Installation and Setup

#### 2.1 The shipped service + UI (the supported path)

The repository already contains a ready `.venv` with Flask installed. Verify it:

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\abstractive-text-summarizer"
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip show flask
```

Expected (verified in this checkout):

```
Python 3.12.1
Name: flask
Version: 3.1.3
```

If `.venv` were missing, recreate it:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install "flask>=3.0"
```

> Use the interpreter **directly** (`.venv\Scripts\python.exe …`) as shown above. Activating the venv is
> optional; activation scripts are often block

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
