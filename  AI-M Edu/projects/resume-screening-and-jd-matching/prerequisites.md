# Prerequisites — TalentMatch Lens: Resume and Job Description Matching

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# TalentMatch Lens (resume-screening-and-jd-matching) — Setup & Test Workflow

### 1. Prerequisites

- **OS:** Windows (PowerShell)
- **Python:** 3.12.1
- **Node:** v22.15.0 (not required)
- **Ports:** Streamlit `8501` (http://localhost:8501)
- **Critical:** `venv/` in repo is a **STUB** (only `venv\Scripts\activate`, no python.exe/pyvenv.cfg/site-packages). **Do NOT use it.** Create a real venv.
- **Models downloaded on first run:** spaCy `en_core_web_sm` and sentence-transformers `all-MiniLM-L6-v2` (~90MB)
- **Data:** `data/sample_job_description.txt` present (LLM/ML Engineer posting). Resumes uploaded via UI.

### 2. Installation and Setup

#### Step 1: Open the project directory
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\resume-screening-and-jd-matching"
```

#### Step 2: Create a REAL virtual environment (do not use stub venv/)
```powershell
py -3.12 -m venv .venv_real
.\.venv_real\Scripts\Activate.ps1
```

#### Step 3: Install dependencies
```powershell
pip install -r requirements.txt
```
Key deps: streamlit, sentence-transformers, torch, scikit-learn, spacy, pdfplumber, python-docx, pandas, numpy

#### Step 4: Download spaCy model (required)
```powershell
python -m spacy download en_core_web_sm
```
**Note:** `app.py` calls `spacy.load("en_core_web_sm")` at import time (`load_models()` cached) — missing model will crash startup.

#### Step 5: (Optional) Static preview UI
```powershell
python -m http.server 8000 --bind 127.0.0.1
```
Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) for the labeled browser demo (`index.html` fetches `data/sample_job_description.txt` only).

### 3. Launch the Complete Project

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\resume-screening-and-jd-matching"
.\.venv_real\Scripts\Activate.ps1
streamlit run app.py
```
Open: [http://localhost:8501](http://localhost:8501)

First run will download `all-MiniLM-L6-v2` (~90MB) and load models (cached after).

### 4. Test the Project

#### Manual tests
1. Load Streamlit app — models load (cached). If spaCy model missing, app crashes at startup.
2. **Job Description:** Paste text or upload file. Sample available at `data/sample_job_description.txt`.
3. **Resumes:** Upload multiple resumes (PDF/DOCX/TXT supported via `src/extractor.py`).
4. Run screening — pipeline: extract → clean → embed → score → rank → explain.
5. Review results dashboard (ranked candidates with explanations).
6. Check static preview UI at 8000 for demo-only behavior.

#### Notes
- No tests present, no .gitignore
- `resum

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
