# Prerequisites — MoodTunes: Emotion Detection and Music Recommendation

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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
- **No API key** is needed for anything — the music lookup

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
