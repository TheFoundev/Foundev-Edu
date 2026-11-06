# Prerequisites — Cockpit: Driver Drowsiness Detection

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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

| Path | Needs dlib? | Needs VS Build Tool

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
