# Prerequisites — PlateSight: Vehicle Number Plate Recognition

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# PlateSight (vehicle-number-plate-recognition) — Setup & Test Workflow

### 1. Prerequisites

- **OS**: Windows (PowerShell)
- **Python**: `runtime.txt` specifies Python 3.7; context is 3.12.1. **Old pins may not install on Python 3.12** (see deps). A conda/env with Python 3.7 is safer for exact pins.
- **Webcam** (optional): For webcam branch in `app.py` (`cv2.VideoCapture(0)`).
- **Internet**: **Required on first run** — `torch.hub.load("ultralytics/yolov5","custom", path="model/last.pt")` will fetch YOLOv5 repo if not cached.
- **Node.js**: v22.15.0 (static landing page only)

### 2. Installation and Setup

From `N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\vehicle-number-plate-recognition\`:

#### Option A: Full pinned install (may be problematic on Python 3.12)
```powershell
py -3.7 -m venv .venv37  # preferred per runtime.txt
.\.venv37\Scripts\Activate.ps1
pip install -r requirements.txt
```
Note: `requirements.txt` is a 105-line freeze including Windows-only packages (`pywin32`, `pywinpty`) and full Jupyter stack.

#### Option B: Reduced runtime install (often works better)
```powershell
py -3.7 -m venv .venv37
.\.venv37\Scripts\Activate.ps1
pip install torch==1.8.1 torchvision==0.9.1
pip install streamlit==1.9.0 opencv-python==4.5.5.64 Pillow==9.1.0 numpy==1.21.6
```

**Ground truth:**
- Weights shipped: `model/last.pt` (14.4 MB custom YOLOv5 plate detector).
- Sample images: `uploads/` (7), outputs: `downloads/`.
- Static banners: `static/`.
- `app.py` is Streamlit backend/app. Vendored YOLOv5 in `utils/` and `models/` (not imported by `app.py`).
- Inference is **detection only** (no OCR).
- No tests, no training script/dataset.

### 3. Launch the Complete Project

#### Component 1: Streamlit app (primary backend/UI) — port 8501
```powershell
streamlit run app.py
```
Open [http://localhost:8501/](http://localhost:8501/). On first run with internet, YOLOv5 repo may be downloaded via `torch.hub`. Supports image upload and webcam branch (`cv2.VideoCapture(0)`). **Detection only.**

#### Component 2: Static landing page (optional)
```powershell
py -m http.server 8000
```
Open [http://localhost:8000/](http://localhost:8000/). `index.html` + `js/` provide image intake/docs; inference runs in **Streamlit** (no `fetch()` to API in static files).

#### Component 3: Docker (optional)
`Dockerfile`, `Procfile`, `setup.sh` present for container/deployment.

### 4. Test the Project

**Automated tests:** None.

**Manual verification:**
| Component | How to test | Expected |
|---|---|---|
| Streamlit app | `streamlit run app.py` | App

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
