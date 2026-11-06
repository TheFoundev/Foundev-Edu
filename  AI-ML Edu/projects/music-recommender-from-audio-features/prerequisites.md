# Prerequisites — Groove Observatory: Audio Feature Music Recommendation

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# Groove Observatory (music-recommender-from-audio-features) — Setup & Test Workflow

### 1. Prerequisites

- **OS:** Windows (PowerShell)
- **Python:** 3.12.1
- **Node:** v22.15.0 (not required)
- **Data:** `data/best_songs_spotify_2000_2023.csv` present (2261 rows after dedup in practice)
- **Environment:** `.venv` already exists with dependencies installed (Flask, pandas, scikit-learn, etc.)
- **Ports:** Backend `5000` (Flask), UI `8000` (static server)

### 2. Installation and Setup

#### Step 1: Open the project directory
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\music-recommender-from-audio-features"
```

#### Step 2: Use the existing virtual environment (recommended)
The repo includes `.venv` with required packages. Activate it:
```powershell
.\.venv\Scripts\Activate.ps1
```

If needed, install API deps (reference):
```powershell
pip install -r requirements-api.txt
```
Contents: `flask>=2.3`, `pandas>=2.0`, `scikit-learn>=1.3`

#### Step 3: Verify files
- `src/api.py` — Flask backend (cosine similarity)
- `index.html`, `css/style.css`, `js/app.js` — static UI (API-first with browser fallback)
- `data/best_songs_spotify_2000_2023.csv` — dataset (semicolon-separated, columns include `danceability ` and `speechiness ` with trailing spaces)

### 3. Launch the Complete Project

**Run both terminals (backend + UI).** The UI probes `http://127.0.0.1:5000/api/health` on load (1.5s timeout); if online it uses the backend, else falls back to identical in-browser cosine engine.

#### Terminal 1: Start the Flask API
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\music-recommender-from-audio-features"
.\.venv\Scripts\python.exe src\api.py
```
Expected: Flask dev server on `http://127.0.0.1:5000` (debug=False)

#### Terminal 2: Start the static UI server
```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\music-recommender-from-audio-features"
python -m http.server 8000
```
Open: [http://localhost:8000/](http://localhost:8000/)

### 4. Test the Project

#### API tests (verified)
```powershell
# Health
curl http://127.0.0.1:5000/api/health
# Expected: {"status":"ok","engine":"cosine-similarity","rows":2261,"features":10}

# Artists
curl http://127.0.0.1:5000/api/artists

# Songs for artist
curl "http://127.0.0.1:5000/api/songs?artist=miley%20cyrus"

# Recommend (example)
curl -X POST http://127.0.0.1:5000/api/recommend -H "Content-Type: application/json" -d "{\"artist\":\"miley cyrus\",\"title\":\"flowers\",\"limit\":3}"
# Expected: recommen

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
