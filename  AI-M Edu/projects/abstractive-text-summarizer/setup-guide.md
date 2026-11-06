# Setup guide — FactCheck Studio: Factual Consistency and Summarization

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

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
> optional; activation scripts are often blocked by the Windows execution policy.

#### 2.2 Configuration

**There is none.** `src/api.py` reads no environment variables, no `.env` file and no config file. Its
host/port are hard-coded at the bottom of the file:

```python
app.run(host="127.0.0.1", port=5000, debug=False)
```

The **browser** side has exactly one optional override, read in `js/app.js:10`:

```javascript
var API_BASE = (window.FACTCC_API_BASE || "http://127.0.0.1:5000").replace(/\/+$/, "");
```

So the default UI → backend pairing works with no editing. To point the UI at a different backend, set
`window.FACTCC_API_BASE` before `js/app.js` loads.

The service sends `Access-Control-Allow-Origin: *` on every response (`src/api.py:151-156`), so the UI
served from `http://localhost:8000` can call `http://127.0.0.1:5000` cross-origin without any proxy.

#### 2.3 Optional: the neural research CLI (`modeling/run.py`)

`modeling/run.py` is a **training / evaluation script**, not a server. It needs:

* Python **3.6/3.7** and the pins in `requirements.txt` — `pytorch_transformers==1.0.0`,
  `torch==1.3.1`, `spacy==2.2.3`, `scipy==1.3.0`, `numpy==1.17.4`, `apex==0.9.10dev`, `protobuf==3.11.2`,
  `scikit_learn==0.22.1`, `google-cloud-translate==1.6.0`, `tqdm==4.32.1`.
* `wandb` (imported at module scope; `wandb.init()` runs at import time).
* External data + checkpoints (multi-GB downloads listed in `README.md`).

```powershell
# Only meaningful on Python 3.6/3.7 — the pins do NOT build on 3.12
conda create -n factcc python=3.7 -y
conda activate factcc
pip install -r requirements.txt
pip install wandb
```

**Not runnable in this checkout on Python 3.12.1** — see [Section 5](#5-troubleshooting). Treat the
CLI as an optional, documented-but-unreproducible path.

---

### 3. Launch the Complete Project

Two processes are needed: the **backend** and the **static UI server**.

#### 3.1 Backend — Flask consistency service on port 5000

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\abstractive-text-summarizer"
.\.venv\Scripts\python.exe src\api.py
```

Expected console output:

```
 * Serving Flask app 'api'
 * Debug mode: off
WARNING: This is a development server. ...
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Keep this window open. Stop with `Ctrl+C`.

#### 3.2 Frontend — static UI on port 8000

Open a **second** PowerShell window:

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\abstractive-text-summarizer"
python -m http.server 8000
```

Open **http://localhost:8000** in the browser. (Opening `index.html` directly also works — all asset
paths are relative — but serving over HTTP is more reliable.) Stop with `Ctrl+C`.

#### 3.3 Optional: the research CLI (no server, no port)

```powershell
conda activate factcc
python modeling\run.py --help
```

This writes checkpoints/metrics to `--output_dir`; it never listens on a port.

#### 3.4 Ports summary

| Component | Port | Address |
|---|---|---|
| Flask service (`src/api.py`) | 5000 | `http://127.0.0.1:5000` |
| Static UI (`python -m http.server`) | 8000 | `http://localhost:8000` |
| Research CLI (`modeling/run.py`) | — | no server |

---

### 4. Test the Project

#### 4.1 Automated / command-line tests

There is **no pytest suite in this repository** — the tests below are direct API calls made with
`curl.exe` (available on Windows 10+). Each was executed against `src/api.py` on this machine.

**Test 1 — health check**

```powershell
curl.exe -s http://127.0.0.1:5000/health
```

Expected response (HTTP 200) — verified:

```json
{"engine":"lexical-entailment (heuristic)","model_checkpoint":false,
 "note":"Deterministic lexical engine. The neural FactCC/FactCCX checkpoints are not bundled and require the pinned 2020 dependency stack; this service does not load them.",
 "status":"ok"}
```

**Test 2 — a consistent (source, claim) pair → `CORRECT`**

Send the JSON body from a file (avoids PowerShell quote-mangling):

```powershell
@'
{"text":"Mercury Transit Pharma said its experimental antibody therapy reduced tumor size by 47 percent in a Phase II trial of 320 patients.","claim":"Mercury Transit Pharma said its therapy reduced tumors by 47 percent in a Phase II trial of 320 patients."}
'@ | Set-Content -Path "$env:TEMP\factcc_ok.json" -Encoding utf8

curl.exe -s --data-binary "@$env:TEMP\factcc_ok.json" -H "Content-Type: application/json" http://127.0.0.1:5000/verify
```

Expected (HTTP 200) — verified, `label` = **`CORRECT`**, `confidence` ≈ **0.9792**:

```json
{"confidence":0.9792,
 "diagnostics":{"claim_terms":13,"mean_sentence_overlap":0.7059,"negation_flip":false,
                "numeric_conflicts":[],"source_coverage":0.9231},
 "disclaimer":"Heuristic lexical/entailment analysis — NOT a neural FactCC checkpoint prediction.",
 "engine":"lexical-entailment (heuristic)",
 "inconsistent_spans":[],
 "label":"CORRECT",
 "model_checkpoint":false,
 "supporting_spans":[{"end":131,"start":0,"t

## Known setup risks

- The shipped Flask endpoint is deterministic lexical consistency scoring; it does not load a neural checkpoint. The research model code is a separate, older stack and no trained checkpoint is bundled. WORKFLOW statements that contradict the API/UI implementation need review.
