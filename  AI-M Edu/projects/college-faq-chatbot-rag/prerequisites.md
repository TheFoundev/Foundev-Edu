# Prerequisites — CampusWise: College FAQ Retrieval-Augmented Generation

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# CampusWise (college-faq-chatbot-rag) — Setup & Test Workflow

This document covers **how to install, configure, launch and test the complete project**: the Streamlit RAG
chat application (`app/app.py`, port **8501**), the one-time ChromaDB ingestion (`scripts/ingest.py`), the
evaluation CLIs, and the optional static CampusWise console (`index.html` + `css/` + `js/`, port **8000**).

**Honest scope note up front:** the real chat backend is the **Streamlit app** — there is **no REST API**
(no Flask/FastAPI route, no `/chat` endpoint) and the static console's `js/app.js` contains **no `fetch()`
call**; it shows an offline card and a scripted demo mode. Live answers require a valid **OpenRouter API
key** (used for *both* chat and embeddings) and a populated `chroma_db/`.

---

### 1. Prerequisites

| Requirement | Version / detail | Checked with |
|---|---|---|
| OS | Windows 10/11 (commands below are PowerShell) | `Get-Host` |
| Python | **3.12.1** (already present as `.venv`) | `.\.venv\Scripts\python.exe --version` |
| Streamlit | **1.66.0** (already in `.venv`) | `.\.venv\Scripts\python.exe -m pip show streamlit` |
| ChromaDB | **1.5.9** (already in `.venv`) | `.\.venv\Scripts\python.exe -m pip show chromadb` |
| **OpenRouter API key** | **Required.** Placeholder: `sk-or-v1-<YOUR_KEY>` | <https://openrouter.ai/keys> |
| Internet | Required **only** for the OpenRouter API calls (chat + embeddings) | — |
| Disk | ≈ 500 MB for the venv + a few MB for `chroma_db/` | `Get-PSDrive` |
| Node.js | **Not required** — the UI is plain HTML/CSS/JS, no build step | — |

> The API key is **never** written into this document. Everything below uses placeholders.

Project root (used by every command below):

```powershell
$root = "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\college-faq-chatbot-rag"
Set-Location $root
```

---

### 2. Installation and Setup

#### 2.1 The shipped virtual environment (fastest path)

A complete `.venv` already exists in this checkout — verified contents:

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\college-faq-chatbot-rag"
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip list
```

Key packages actually present (verified):

| Package | Version |
|---|---|
| streamlit | 1.66.0 |
| langchain | 1.4.6 |
| langchain-core | 1.6.12 |
| langchain-community | **0.4.2** |
| langchain-openai | 1.7.2 |
| langchain-chroma | 1.1.0 |
| langchain-text-splitters | 1.1.3 |
| chromadb | 1.5.9 |
| openai | 3.35.1 |
| rank-bm25 | 0.2.2 |
| ragas | 0.3.1 |
| pyd

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
