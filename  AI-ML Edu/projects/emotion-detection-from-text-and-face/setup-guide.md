# Setup guide — MoodTunes: Emotion Detection and Music Recommendation

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# MoodTunes (emotion-detection-from-text-and-face) — Setup & Test Workflow

**Folder id:** `emotion-detection-from-text-and-face`
**UI name:** MoodTunes
**Stack:** FastAPI 0.104.1 · uvicorn[standard] 0.24.0 · TensorFlow-CPU ≥ 2.15 + `tf-keras` · DeepFace ≥ 0.0.93 · transformers + PyTorch · OpenCV · redis · ddgs · Next.js 16 / React 19 / Tailwind 4 (frontend) · vanilla HTML/CSS/JS (webui)
**Entry point:** `backend/app.py` (FastAPI, `backend.app:app`)

**What it actually is:** a hybrid emotion-to-music API with two front ends.
- **Face mode** (`POST /predict`): uploads an image → DeepFace extracts/aligns the face →
  a custom CNN (Keras `.h5`) classifies the emotion → DuckDuckGo video search returns
  matching YouTube tracks.
- **Text mode** (`POST /predict-text`): a DistilBERT text-classification pipeline
  (`bhadresh-savani/distilbert-base-uncased-emotion`) labels the text → the same music
  lookup runs.
- Results are cached in **Redis** for 24 h when a Redis server is available; the app works
  without Redis (it logs a warning and disables caching).

**Runtime surfaces:**

| Surface | Kind | Port | Notes |
|---|---|---|---|
| `backend/app.py` | FastAPI (uvicorn) | 8000 | The real backend |
| `webui/` | Static page | 8080 | Vanilla JS; talks to `http://127.0.0.1:8000` |
| `frontend/` | Next.js 16 (React 19) | 3000 | `npm run dev`; needs Node 18+ |
| Redis | Optional cache | 6379 | `docker run -d --name moodtunes-redis -p 6379:6379 redis:alpine` |
| `docker compose up --build` | All three | 8000 / 3000 / 6379 | |

---

### 1. Prerequisites

- **Windows 10/11** with PowerShell (commands below are Windows-first).
- **Python 3.10+** — `HOW_TO_RUN.md` states 3.10+ and the backend `Dockerfile` uses
  `python:3.10-slim`.
- **Node.js 18+ and npm** — *only* for the `frontend/` Next.js app. The `webui/` page needs
  no Node at all.
- **~3 GB of free disk** for TensorFlow, PyTorch, the CNN weights and the DistilBERT model.
- **Internet access on first run** — two separate downloads happen lazily:
  - `models/emotion_model.h5` (~200 MB) is fetched from HuggingFace by
    `backend/model_loader.py:11` (`MODEL_URL`) on the first image prediction.
  - `bhadresh-savani/distilbert-base-uncased-emotion` is fetched by HuggingFace
    `transformers` on the first text prediction.
- **Optional:** a webcam for the `webui/` face-capture mode (the browser blocks camera
  access on non-HTTPS/non-localhost origins — `webui/js/app.js:450` says so explicitly).
- **Optional:** Docker Desktop for the compose path and for Redis.
- **No API key** is needed for anything — the music lookup scrapes DuckDuckGo video
  results, not the YouTube Data API.

**Environment variables actually read by the backend:**

| Variable | Default | Read at | Effect |
|---|---|---|---|
| `REDIS_URL` | *(unset)* | `backend/app.py:60` | Full Redis connection URL, including the database index |
| `REDIS_HOST` | `localhost` | `backend/app.py:60` | Used to build `redis://<host>:6379/0` when `REDIS_URL` is unset |
| `NEXT_PUBLIC_API_URL` | `http://127.0.0.1:8000` | `frontend/app/text-music/page.tsx:21`, `frontend/app/system/page.tsx:20` | API base baked into the Next.js bundle at build time |

The `webui/` page's API base is browser-side: `localStorage["mt.apiBase"]`, default
`http://127.0.0.1:8000` (`webui/js/app.js:4,6,40-43`), and it is also editable in the page
itself via the `#apiBase` text input (`webui/index.html:28`).

---

### 2. Installation and Setup

#### 2a. Backend (Python)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\emotion-detection-from-text-and-face"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

> **Important — `requirements.txt` line 16 is not valid pip syntax.**
> It reads `torch --index-url https://download.pytorch.org/whl/cpu`, which pip cannot parse
> (a requirements file takes only `name [extras] version` per line). `pip install -r
> requirements.txt` will fail on that line. Install PyTorch **separately** and then install
> the rest from a filtered copy of the file.

```powershell
# 1. PyTorch (CPU build) — install on its own
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu

# 2. The remaining dependencies, with the broken torch line removed
$req = Get-Content .\requirements.txt | Where-Object { $_ -notmatch '^\s*torch\s+--index-url' }
$req | Set-Content -Path "$env:TEMP\requirements-moodtunes.txt" -Encoding utf8
python -m pip install -r "$env:TEMP\requirements-moodtunes.txt"
```

Confirm the heavy stack imported correctly:

```powershell
python -c "import fastapi, uvicorn, tensorflow, cv2, deepface, transformers, redis, ddgs; print('backend stack ok')"
```

> **Version caveat:** `requirements.txt` pins `numpy>=2.0.0` alongside
> `tensorflow-cpu>=2.15.0`. TensorFlow 2.15–2.19 wheels are built against NumPy 1.x and can
> raise "A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x" at import
> time. If that happens, pin `numpy<2` (e.g. `python -m pip install "numpy<2"`) — the
> backend code does not require NumPy 2.

#### 2b. Frontend A — Next.js (optional)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\emotion-detection-from-text-and-face\frontend"
npm install
```

Node v22.15.0 / npm 11.6.3 are present in this environment. `package.json` pins
`next@^16.2.1`, `react@19.2.3`, `react-dom@19.2.3`, Tailwind 4 and `@tailwindcss/postcss`.

#### 2c. Frontend B — static `webui/` (no build step)

Nothing to install. Serve it from the project root:

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\emotion-detection-from-text-and-face"
python -m http.server 8080 --directory webui
```

#### 2d. Optional — Redis cache

```powershell
docker run -d --name moodtunes-redis -p 6379:6379 redis:alpine
docker ps --filter name=moodtunes-redis
```

Without Redis the API still works — it prints
`WARNING: Redis not connected. Caching disabled. Error: ...` and serves every request from
DuckDuckGo.

#### 2e. Models

| File | Status | Behaviour |
|---|---|---|
| `models/emotion_model.h5` | **Missing** | Auto-downloaded from HuggingFace on the first image prediction (`backend/model_loader.py:14-27`). Needs internet. |
| `models/emotion_labels.json` | **Present** | `{"angry":0,"disgust":1,"fear":2,"happy":3,"neutral":4,"sad":5,"surprise":6}` — index → label map used by `classify_emotion()` |
| DistilBERT text model | **Not a file** | Downloaded into the HuggingFace cache on the first `/predict-text` call |

`backend/model_loader.py` also **permanently patches** the downloaded `.h5` in place to make
it Keras 3 compatible (`patch_h5_file_permanently()`, lines 30-63) — it rewrites
`"batch_shape"` to `"shape"` in the HDF5 `model_config` attribute. This is automatic; no
manual step is needed.

#### 2f. Docker (optional, all-in-one)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\emotion-detection-from-text-and-face"
docker compose up --build
```

`docker-compose.yml` starts three services: `redis` (:6379), `backend` (:8000, built from
`backend/Dockerfile`, `REDIS_HOST=redis`) and `frontend` (:3000,
`NEXT_PUBLIC_API_URL=http://localhost:8000`).

> **Note:** `backend/Dockerfile` does `RUN pip install --no-cache-dir -r requirements.txt`
> on the *root* `requirements.txt`, which still contains the invalid `torch --index-url`
> line. The image build will fail at that step until that line is corrected.

**There is no `.env` file.** Configuration is via the three environment variable

## Known setup risks

- The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.
