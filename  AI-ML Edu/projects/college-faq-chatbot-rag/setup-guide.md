# Setup guide — CampusWise: College FAQ Retrieval-Augmented Generation

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

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
| pydantic / pydantic-settings | 2.14.1 / 2.16.1 |

If you ever need to rebuild it from scratch:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

#### 2.2 Configure the API key (`.env`)

The app reads configuration from `.env` via `pydantic-settings`
(`config/settings.py` → `env_file=PROJECT_ROOT / ".env"`).

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\college-faq-chatbot-rag"

# Create .env from the shipped template (only needed if .env is missing)
Copy-Item .env.example .env

# Open it and replace the placeholder with your real key
notepad .env
```

` .env` must contain (placeholder values shown):

```dotenv
OPENROUTER_API_KEY=sk-or-v1-<YOUR_OPENROUTER_KEY>
OPENROUTER_SITE_URL=http://localhost:8501
OPENROUTER_APP_NAME=College FAQ Chatbot

LLM_MODEL=openai/gpt-4o-mini
EMBEDDING_MODEL=openai/text-embedding-3-small

RETRIEVAL_TOP_K=5
RELEVANCE_SCORE_THRESHOLD=0.20
FETCH_K=20
LAMBDA_MULT=0.5
ADAPTIVE_K_THRESHOLD=0.45

CHUNK_SIZE=500
CHUNK_OVERLAP=100
ENABLE_QUERY_REWRITING=true
```

> **Note:** a `.env` file already exists in this checkout and already contains a non-placeholder value.
> Replace it with **your own** key; never commit a real key. `.env` is git-ignored.

**How the app decides the key is "missing"** (`app/app.py:121-124`):

```python
if not settings.openrouter_api_key or settings.openrouter_api_key == "your_openrouter_api_key_here":
    raise ValueError("OPENROUTER_API_KEY is not set. ...")
```

The value `your_openrouter_api_key_here` (the `.env.example` placeholder) is treated as **unset**, and the
app shows a red error banner.

**Other settings that matter** (`config/settings.py`):

| Setting | Default | Effect |
|---|---|---|
| `LLM_MODEL` | `openai/gpt-4o-mini` | Chat model on OpenRouter |
| `EMBEDDING_MODEL` | `openai/text-embedding-3-small` | Embedding model on OpenRouter |
| `RETRIEVAL_TOP_K` | `5` | Chunks returned by the retriever |
| `RELEVANCE_SCORE_THRESHOLD` | `0.20` | Below this best score the pipeline **refuses** instead of answering |
| `FETCH_K` | `20` | Candidates fetched before the MMR diversity pass |
| `LAMBDA_MULT` | `0.5` | MMR: 0 = max diversity, 1 = max relevance |
| `ADAPTIVE_K_THRESHOLD` | `0.45` | If the best score is below this, retrieval expands to `FETCH_K` |
| `CHUNK_SIZE` / `CHUNK_OVERLAP` | `500` / `100` | Document chunking |
| `ENABLE_QUERY_REWRITING` | `true` | Enables the LLM query rewriter |
| `OPENROUTER_BASE_URL` | `https://openrouter.ai/api/v1` | Hard-coded in `config/settings.py` |

> **Useful trick for testing the failure path without editing `.env`:** real environment variables take
> priority over the `.env` file in `pydantic-settings`. Verified working:
> ```powershell
> $env:OPENROUTER_API_KEY = "your_openrouter_api_key_here"   # forces the "missing key" banner
> Remove-Item Env:\OPENROUTER_API_KEY                        # undo
> ```

#### 2.3 One-time ingestion (creates `chroma_db/`)

`chroma_db/` is git-ignored and **is not present in this checkout** — it must be created once.

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\college-faq-chatbot-rag"
.\.venv\Scripts\python.exe scripts\ingest.py
```

Expected output shape (from `scripts/ingest.py`):

```
Ingestion complete:
  Sections parsed : 57
  Chunks indexed  : <N>
  Persist dir     : N:\...\college-faq-chatbot-rag\chroma_db
```

> The "Sections parsed : 57" figure was verified by loading `data/knowledge_base.docx` directly with
> `src/document_loader.load_docx()` in this checkout. The chunk count depends on `CHUNK_SIZE` /
> `CHUNK_OVERLAP`.

Re-ingest from scratch after editing the `.docx`:

```powershell
.\.venv\Scripts\python.exe scripts\ingest.py --reset
```

**Auto-ingestion:** you can skip the manual step. `src/factory.py:31-33` checks
`collection_is_empty(vector_store)` and runs the ingestion automatically, so the **first** launch of the
Streamlit app embeds the document if `chroma_db/` is empty.

---

### 3. Launch the Complete Project

#### 3.1 Backend — the Streamlit chat app on port 8501

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\college-faq-chatbot-rag"
.\.venv\Scripts\python.exe -m streamlit run app\app.py --server.port 8501 --server.headless true
```

Expected output (verified in this checkout):

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

Open **http://localhost:8501**. Stop with `Ctrl+C`.

**Equivalent convenience launcher** (`run.py` shells out to `streamlit run app/app.py`):

```powershell
.\.venv\Scripts\python.exe run.py
```

> `.streamlit/config.toml` sets `fileWatcherType = "none"` (useful on Windows/network drives) and
> disables usage stats.

#### 3.2 Frontend — the static CampusWise console on port 8000 (optional)

```powershell
Set-Location "N:\Foundev-P

## Known setup risks

- A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.
