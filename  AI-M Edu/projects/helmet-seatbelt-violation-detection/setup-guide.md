# Setup guide — Signal Control Room: Helmet and Seatbelt Detection

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Signal Control Room (helmet-seatbelt-violation-detection) — Setup & Test Workflow

**Folder id:** `helmet-seatbelt-violation-detection`
**UI name:** Signal Control Room
**Stack:** OpenCV · NumPy · Pillow · PyTorch + torchvision · Ultralytics YOLO (YOLOv8x) · SQLite3 · Tkinter (stdlib) · vanilla HTML/CSS/JS (browser companion)
**Entry point:** `source/main_app.py` (Tkinter desktop application)

**What it actually is:** a **desktop** traffic-violation monitoring application. Operators sign
in with a username, password and role, watch up to four camera feeds, and the app detects
riders **without a helmet**, logs each violation into SQLite, and produces reports, statistics
and JSON/CSV exports.

> **Scope honesty — only the helmet detector is implemented.** The seatbelt and roundabout
> detectors are referenced in the UI but their modules are not in this repository: the
> imports are commented out at `source/main_app.py:21-22`, so `self.seatbelt_detector` and
> `self.roundabout_detector` are never assigned. Toggling either switch in the GUI raises
> `AttributeError` inside the camera thread; the generic handler in `update_camera_feed()`
> prints `Camera N error: ...` and ends that camera's thread. **Use the Helmet toggle only.**

The browser page at the project root (`index.html` + `css/style.css` + `js/app.js`) mirrors
the operator console visually, but it is a local, demo-data preview — it never loads a model
and never talks to a server. Its only external write is `localStorage`.

**Runtime surfaces:**

| Surface | Kind | Port | Notes |
|---|---|---|---|
| `source/main_app.py` | Tkinter desktop app | n/a | The real application — **no HTTP server** |
| `source/database_manager.py` (as `__main__`) | Self-test script | n/a | Writes `test_violations.db` |
| `source/user_authentication_v1.py` (as `__main__`) | Self-test script | n/a | Writes `traffic_system.db` |
| `source/helmet_detection_yolo8_max_accuracy.py` (as `__main__`) | Detector smoke test | n/a | Loads the model and warms it up |
| `python -m http.server 8000` | Static server for the browser page | 8000 | Demo data only |

---

### 1. Prerequisites

- **Windows 10/11** with PowerShell (commands below are Windows-first).
- **Python 3.9+** — the code uses `typing` generics and dataclasses; 3.10+ is recommended.
  Python 3.12.1 is fine.
- **A camera** — camera indices `0`–`3` via `cv2.VideoCapture(idx)`. Without one, the app
  still launches, logs in, and lets you record violations manually.
- **Disk space and time for PyTorch** — `torch` + `torchvision` + `ultralytics` are large
  downloads (the CUDA build is ~2–3 GB; the CPU build is smaller).
- **Network access on the first run** — Ultralytics fetches `yolov8x.pt` (~130 MB) from its
  release assets when the file is not already present.
- **Optional:** a custom helmet checkpoint (`.pt`) to replace the COCO model.
- **Node.js is not required** — the browser page is plain static files.
- **No API key** is required for anything.

> **The bundled `quasar/` folder is a Linux virtualenv snapshot** (`bin/`, `lib/`,
> `lib64`, `pyvenv.cfg` pointing at `/home/maqbool/anaconda3/bin`, Python 3.10.16). It
> **cannot be activated on Windows** — the `.exe` shims inside `quasar/lib/python3.10/site-packages/setuptools/`
> are Linux ELF binaries. **Ignore `quasar/` entirely and create your own environment.**

**Hard-coded settings in the source (no `.env`, no config file):**

| Setting | Value | Line |
|---|---|---|
| Violation database | `traffic_violations.db` (CWD-relative) | `source/database_manager.py:15` |
| User database | `traffic_system.db` (CWD-relative) | `source/user_authentication_v1.py:13` |
| Password hashing | SHA-256 hex digest | `source/user_authentication_v1.py:38-40` |
| Model path | the literal string `"yolov8x.pt"` | `source/helmet_detection_yolo8_max_accuracy.py:65`, `:116` |
| Confidence threshold | `0.6` | `source/main_app.py:38` (`create_helmet_detector(confidence_threshold=0.6)`) |
| IoU threshold | `0.45` | `source/helmet_detection_yolo8_max_accuracy.py:45` |
| Device | `auto` → cuda / mps / cpu | `source/helmet_detection_yolo8_max_accuracy.py:121-127` |
| Frame display size | 300 × 200 | `source/main_app.py:346` |
| Roles | `Administrator`, `Traffic Officer`, `Public` | `source/main_app.py:83` |

**Default accounts (created automatically on first run):**

| Username | Password | Role |
|---|---|---|
| `admin` | `admin123` | Administrator |
| `officer1` | `officer123` | Traffic Officer |
| `public` | `public123` | Public |
| `test` | `test` | Traffic Officer |

> These are **development defaults seeded into `traffic_system.db`** and are printed in the
> source (`source/user_authentication_v1.py:317-321`). The stored passwords are SHA-256
> digests, not plaintext — but unsalted SHA-256 is not a production password hash, and the
> default accounts must be changed before any real use.

---

### 2. Installation and Setup

#### 2a. Create the environment

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\helmet-seatbelt-violation-detection"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

> **Do not activate `quasar\`.** It is a Linux venv snapshot and is unusable on Windows.

#### 2b. Install PyTorch (CPU build recommended, then the rest)

`requirements.txt` lists `torch` and `torchvision` **unpinned**, so `pip install -r
requirements.txt` pulls the default CUDA build (several GB). For a CPU-only machine,
install the CPU wheels first:

```powershell
# CPU-only PyTorch (much smaller download)
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# The remaining dependencies
python -m pip install opencv-python numpy pillow ultralytics
```

Or install the whole file, accepting the large CUDA download:

```powershell
python -m pip install -r requirements.txt
```

> **Note on the `tk` entry.** `requirements.txt` lists a package literally named `tk`. This is
> **not** the Tkinter module — Tkinter ships with the Python standard library on Windows
> (`python.org` installer, *tcl/tk and IDLE* component). The PyPI `tk` package is an
> unrelated meta-package that tries to install a Tcl/Tk distribution and commonly fails on
> Windows. **Install everything except `tk`** as shown above; you do not need it.

#### 2c. Verify the environment

```powershell
python --version
python -c "import cv2, numpy, PIL, torch, torchvision, ultralytics, tkinter, sqlite3; print('torch', torch.__version__); print('cv2', cv2.__version__); print('cuda', torch.cuda.is_available())"
```

#### 2d. Model weights — `yolov8x.pt`

`yolov8x.pt` is **not shipped** (`.gitignore` excludes `*.pt` and `*.weights`). Ultralytics
downloads it automatically from its release assets on first use, so the first launch needs
network access. To fetch it ahead of time:

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\helmet-seatbelt-violation-detection"
python -c "from ultralytics import YOLO; m = YOLO('yolov8x.pt'); print('yolov8x.pt ready')"
```

The file lands in your **current working directory** — see Section 3 for why that matters.

**Custom weights are not shipped either.** The detector accepts one via
`create_helmet_detector(custom_model_path=...)`, and the custom-model branch
(`process_custom_helmet_detections()`) understands the classes `person`, `helmet`,
`no_helmet`, `motorcycle`, `bicycle`. There is **no training dataset** in the repository and
no training script — you would have to train one yourself.

#### 2e. Assets: present vs. unu

## Known setup risks

- Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.
