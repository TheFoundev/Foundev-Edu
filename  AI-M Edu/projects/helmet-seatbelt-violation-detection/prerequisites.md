# Prerequisites — Signal Control Room: Helmet and Seatbelt Detection

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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
  downloads (the CUDA

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
