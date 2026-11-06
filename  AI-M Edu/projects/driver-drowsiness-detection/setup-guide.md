# Setup guide — Cockpit: Driver Drowsiness Detection

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Cockpit HUD (driver-drowsiness-detection) — Setup & Test Workflow

**Folder id:** `driver-drowsiness-detection`
**UI name:** Cockpit HUD
**Stack:** OpenCV (`opencv-python>=4.5.0,<5.0.0`) · dlib (`>=19.22.0,<20.0.0`) · NumPy `<2.0.0` · SciPy `<2.0.0` · MediaPipe · Streamlit · streamlit-webrtc · playsound · Pillow · aiofiles · Tkinter (stdlib)
**Entry points:** `main.py` (Tkinter launcher), `ui.py` (older Tkinter launcher), `blinkDetect.py`, `face-try.py`, `lanedetection.py`, `streamlit_app/streamlit_app.py`

**What it actually is:** a set of classical computer-vision programs (no trained model) that
measure **Eye Aspect Ratio (EAR)** from facial landmarks to detect eye closure and raise a
drowsiness alarm. The `index.html` + `css/style.css` + `js/app.js` page at the project root
is a **HUD-style instrument view that renders a simulated EAR signal** — it does not open the
camera and there is no backend for it to call.

**Runtime surfaces:**

| Surface | Kind | Port | Notes |
|---|---|---|---|
| `python main.py` | Tkinter launcher | n/a | Spawns `face-try.py` / `blinkDetect.py` as child processes |
| `python blinkDetect.py` | dlib EAR detector | n/a | Needs `models/shape_predictor_68_face_landmarks.dat` (**missing**) |
| `python face-try.py` | Haar face detector | n/a | Runs out of the box — cascade is present |
| `python lanedetection.py` | Lane detector | n/a | |
| `streamlit run streamlit_app/streamlit_app.py` | Streamlit + streamlit-webrtc | 8501 | MediaPipe FaceMesh, **no dlib needed** |
| `python -m http.server 8080` | Static server for the Cockpit HUD | 8080 | Simulated signal only |

---

### 1. Prerequisites

- **Windows 10/11** with PowerShell (commands below are Windows-first).
- **Python 3.10–3.12.** The pins `numpy<2.0.0` / `scipy<2.0.0` are incompatible with
  Python 3.13. `requirements.txt` was *tested* on Python 3.7–3.10; the MediaPipe/Streamlit
  path is the practical route on 3.11/3.12.
- **A webcam** — every detection path reads `cv2.VideoCapture(0)`.
- **A C++ build toolchain** if you intend to use `dlib` on Windows: *Visual Studio Build
  Tools* (Desktop development with C++) and CMake (`pip install cmake`). `dlib` has no
  prebuilt wheel for Windows.
- **A WebRTC-capable browser** (recent Chrome/Edge/Firefox) for the Streamlit app, and the
  browser must be allowed to use the camera.
- **Disk space:** roughly 1.5–3 GB for the full dependency set (MediaPipe, Streamlit, OpenCV, dlib source build).
- **No Node.js, no database, no API key.**

**Two mutually exclusive install paths — pick one:**

| Path | Needs dlib? | Needs VS Build Tools? | Gives you |
|---|---|---|---|
| **A — Desktop detector** | Yes | Yes | `blinkDetect.py` (dlib 68-point landmarks) |
| **B — Browser detector** | **No** | **No** | `streamlit_app/streamlit_app.py` (MediaPipe FaceMesh) + the Haar face detector + the Cockpit HUD |

**Constants the code uses (no env vars, no config file for the Python code):**

| Constant | File | Value | Meaning |
|---|---|---|---|
| `thresh` | `blinkDetect.py:23` | `0.27` | EAR below this ⇒ eyes closed |
| `blinkTime` | `blinkDetect.py:40` | `0.15` s | Closure shorter than this is a false blink |
| `drowsyTime` | `blinkDetect.py:41` | `1.5` s | Sustained closure that raises the alarm |
| `FACE_DOWNSAMPLE_RATIO` | `blinkDetect.py:20` | `1.5` | Face detection runs on a downscaled copy |
| `RESIZE_HEIGHT` | `blinkDetect.py:21` | `460` | Frames are resized to this height |
| `EAR_THRESHOLD` | `streamlit_app/streamlit_app.py:12` | `0.25` | Web-app EAR threshold |
| `CONSEC_FRAMES` | `streamlit_app/streamlit_app.py:13` | `20` | Consecutive closed frames before DROWSY |
| `MAX_EAR` / `THRESH` / `THRESH_ALERT` | `js/app.js:42-44` | `0.45` / `0.27` / `0.25` | Cockpit gauge scale and threshold lines |

Streamlit's own settings live in `streamlit_app/.streamlit/config.toml`:
`enableStaticServing = true`, `enableCORS = false`, theme `primaryColor = "#ff6b6b"`.

---

### 2. Installation and Setup

#### Path A — full desktop detector (needs dlib)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\driver-drowsiness-detection"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install cmake
python -m pip install -r requirements.txt
```

If `pip install dlib` fails on Windows, install *Visual Studio Build Tools* (with the
"C++ desktop development" workload), then retry. The `requirements.txt` header documents
the same fallback.

#### Path B — the browser detector (no dlib, recommended on Windows)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\driver-drowsiness-detection"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install streamlit streamlit-webrtc mediapipe av opencv-python numpy scipy playsound
```

> `av` (PyAV) is required by `streamlit-webrtc` and is imported directly at
> `streamlit_app/streamlit_app.py:6`. The upstream README installs it separately for the
> same reason.

#### The dlib landmark model (required for `blinkDetect.py`)

`models/shape_predictor_68_face_landmarks.dat` is **not shipped** (~100 MB, git-ignored).
`blinkDetect.py` loads it at import time (`blinkDetect.py:28`, `blinkDetect.py:32`), so the
script fails immediately without it.

1. Download <https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2>.
2. Decompress it:

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\driver-drowsiness-detection"
python -c "import bz2,shutil; shutil.copyfileobj(bz2.open('shape_predictor_68_face_landmarks.dat.bz2'), open('models/shape_predictor_68_face_landmarks.dat','wb'))"
```

3. Confirm it landed next to the Haar cascade:

```powershell
Get-ChildItem .\models
```

Expected: `haarcascade_frontalface_default.xml` **and** `shape_predictor_68_face_landmarks.dat`.

#### Verify the environment

```powershell
python --version
python -c "import cv2, numpy, scipy; print('cv2', cv2.__version__); print('numpy', numpy.__version__)"
python -c "import streamlit, mediapipe, av, streamlit_webrtc; print('web stack ok')"
```

#### Files that must be present

| Path | Status | Used by |
|---|---|---|
| `models/haarcascade_frontalface_default.xml` | **Present** | `face-try.py:17` (resolved via `os.path.join(BASE_DIR, 'models', ...)`) |
| `models/shape_predictor_68_face_landmarks.dat` | **Missing** → download it | `blinkDetect.py:28` |
| `models/ML_Models/ResNET+CNN (Tranfer Learning)/` | **Empty** | — no CNN is shipped |
| `models/ML_Models/Using Transformers/` | **Empty** | — no transformer is shipped |
| `alarm.wav` | **Present** (project root) | `sound_path` at `blinkDetect.py:29` |
| `streamlit_app/alarm.mp3` | **Present** | `playsound('alarm.mp3')` at `streamlit_app/streamlit_app.py:19` |
| `streamlit_app/.streamlit/config.toml` | **Present** | Streamlit theme + `enableStaticServing` |
| `streamlit_app/manifest.json`, `sw.js`, `offline.html`, `icons/` | **Present** | PWA assets |

**There is no `.env` file and no environment variables are read by this project.**

---

### 3. Launch the Complete Project

#### 3a. The Cockpit HUD (static page)

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\driver-drowsiness-detection"
.\.venv\Scripts\Activate.ps1
python -m http.server 8080
```

- **Port 8080** in this example; any free port works. Open <http://127.0.0.1:8080/>.
- **How the front end reaches the backend: it doesn't.** The page renders a *simulated* EAR
  signal in the browser and labels it as

## Known setup risks

- No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.
