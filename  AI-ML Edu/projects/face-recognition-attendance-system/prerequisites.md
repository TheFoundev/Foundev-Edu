# Prerequisites — FAMS: Face Recognition Attendance System

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# Roll-Call Kiosk (face-recognition-attendance-system) — Setup & Test Workflow

**Folder id:** `face-recognition-attendance-system`
**UI name:** Roll-Call Kiosk (the Tkinter app's own title is *"FAMS-Face Recognition Based Attendance Management System"*)
**Stack:** OpenCV contrib build (`cv2.face` LBPH) · NumPy · pandas · Pillow · PyMySQL + MySQL (optional) · Tkinter (stdlib) · vanilla HTML/CSS/JS (browser companion)
**Entry point:** `AMS_Run.py` (Tkinter desktop application)

**What it actually is:** a **desktop** face-recognition attendance system. It enrolls students
by capturing webcam samples into `TrainingImage/`, trains an OpenCV **LBPH** recognizer into
`TrainingImageLabel\Trainner.yml`, marks attendance from the webcam over a fixed 20-second
window (accepting a match when the LBPH confidence is `< 70`), writes a per-subject CSV into
`Attendance/`, and optionally mirrors each session into MySQL.

The browser page at the project root (`index.html` + `css/style.css` + `js/app.js`) mirrors
the enrollment / roll-call / CSV-export flows **visually only** — it never opens a camera,
never loads the model and never performs recognition. Its only external read is
`fetch("StudentDetails/StudentDetails.csv")`.

**Runtime surfaces:**

| Surface | Kind | Port | Notes |
|---|---|---|---|
| `python AMS_Run.py` | Tkinter desktop app | n/a | The real application — **no HTTP server** |
| `python testing.py` | Standalone LBPH webcam loop | n/a | Manual model sanity check |
| `python training.py` | Standalone **Fisher** trainer | n/a | ⚠ overwrites the LBPH model file — see Troubleshooting |
| `python -m http.server 8000` | Static server for the browser page | 8000 | Demo data only |

---

### 1. Prerequisites

- **Windows 10/11** — this is effectively a hard requirement. `AMS_Run.py` uses Windows-style
  relative paths such as `TrainingImageLabel\Trainner.yml` and
  `StudentDetails\StudentDetails.csv`; on Linux/macOS the backslashes are not path
  separators and those lookups fail. It also uses `AMS.ico` via `iconbitmap()`.
- **Python 3.x** (written for 3.6; runs on modern 3.x — 3.12.1 is fine). `tkinter` ships
  with the Windows python.org installer; if `import tkinter` fails, reinstall Python and
  enable *tcl/tk and IDLE*.
- **A working webcam** — capture and attendance both use `cv2.VideoCapture(0)`.
- **The OpenCV contrib build** — `opencv-contrib-python`. LBPH lives in the `cv2.face`
  submodule, which the plain `opencv-python` wheel does **not** contain.
- **A local MySQL server** — *optional*. The CSV output works without it; the app catches
  the connectio

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
