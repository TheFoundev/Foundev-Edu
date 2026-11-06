# Setup guide — FAMS: Face Recognition Attendance System

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

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
  the connection error and continues.
- **Node.js is not required** — the browser page is plain static files.
- **Disk space:** ~50 MB (the shipped `Trainner.yml` is 50,332,718 bytes ≈ 48 MiB).

**Hard-coded settings in `AMS_Run.py` (no `.env`, no config file — edit the source):**

| Setting | Value | Line |
|---|---|---|
| MySQL host / user / password | `localhost` / `root` / *(empty)* | `AMS_Run.py:62` (manual), `AMS_Run.py:399` (automatic) |
| Automatic-attendance schema | `Face_reco_fill` | `AMS_Run.py:399` |
| Manual-attendance schema | `manually_fill_attendance` | `AMS_Run.py:62` |
| Model file | `TrainingImageLabel\Trainner.yml` | `AMS_Run.py:329`, `AMS_Run.py:578` |
| Capture folder | `TrainingImage/` (note the **trailing space** in the write path) | `AMS_Run.py:289` |
| Registry CSV | `StudentDetails\StudentDetails.csv` | `AMS_Run.py:304`, `AMS_Run.py:337` |
| Attendance CSV | `Attendance/<Subject>_<date>_<HH-MM-SS>.csv` | `AMS_Run.py:386` |
| Haar cascade | `haarcascade_frontalface_default.xml` | `AMS_Run.py:276`, `AMS_Run.py:335` |
| Recognition accept threshold | `conf < 70` | `AMS_Run.py:350` |
| Attendance capture window | 20 seconds | `AMS_Run.py:322` |
| Admin credential | a literal username/password pair in the source | `AMS_Run.py:489-490` |

**Three absolute paths point into the original author's home directory and must be edited
before the app is usable on your machine:**

| Line | What it does | Current value |
|---|---|---|
| `AMS_Run.py:159` | Writes the manual-attendance CSV | `C:/Users/kusha/PycharmProjects/Attendace managemnt system/Attendance/Manually Attendance/` |
| `AMS_Run.py:213`, `AMS_Run.py:462` | Opens the "Check Sheets" Explorer window | `C:\Users\kusha\PycharmProjects\Attendace managemnt system\Attendance\...` |
| `AMS_Run.py:434`, `AMS_Run.py:498` | Re-opens the attendance CSV and the student register for display | `C:/Users/kusha/PycharmProjects/Attendace managemnt system/...` |

> **The admin login is a hard-coded credential pair in the source** (username `kushal`,
> password `kushal14320`), compared in plain text with no hashing, no lockout and no
> database backing. It exists only to gate a read-only view of `StudentDetails.csv`.
> Treat it as a development placeholder — do not ship it as-is.

---

### 2. Installation and Setup

#### 2a. Create the environment

There is **no `requirements.txt`** in this repository. Install exactly what the source imports:

```powershell
cd "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\face-recognition-attendance-system"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

pip install opencv-contrib-python numpy pandas pillow

# Optional — only if you want the MySQL mirror:
pip install pymysql
```

> **Install only ONE OpenCV distribution.** `opencv-python` and `opencv-contrib-python`
> install the same `cv2` package and conflict. Use `opencv-contrib-python`; if you already
> have `opencv-python` installed, run `pip uninstall -y opencv-python` first.

#### 2b. Verify the environment

```powershell
python --version
python -c "import cv2, numpy, pandas, PIL, tkinter; print('cv2', cv2.__version__); print('has cv2.face:', hasattr(cv2, 'face'))"
```

The second command **must** print `has cv2.face: True`. If it prints `False`, the wrong
OpenCV wheel is installed.

#### 2c. Create the `TrainingImage/` capture folder

`TrainingImage/` does **not** exist in the repository. `trainimg()` catches the failure and
shows *"please make "TrainingImage" folder & put Images"*.

```powershell
New-Item -ItemType Directory -Path .\TrainingImage -Force
Test-Path .\TrainingImage
```

> **Trailing-space bug:** `AMS_Run.py:289` writes to `"TrainingImage/ " + Name + "." +
> Enrollment + "." + str(sampleNum) + ".jpg"` — note the **space after the slash**. On
> Windows this creates a subfolder literally named `" "` (a single space) inside
> `TrainingImage/`, and `getImagesAndLabels()` (`os.listdir`) will still find those files, so
> capture and training do work — but the directory listing looks wrong. You may prefer to
> correct the source string to `"TrainingImage/"`; this workflow does not modify any
> application code.

#### 2d. Optional — MySQL setup

The app creates one table per session at runtime:
`CREATE TABLE <Subject>_<YYYY_MM_DD>_Time_<H>_<M>_<S>` with columns
`ID, ENROLLMENT, NAME, DATE, TIME`. You only need to create the two schemas and grant
access.

```powershell
# Start MySQL, then log in as root and create the two schemas:
mysql -u root -e "CREATE DATABASE IF NOT EXISTS Face_reco_fill;"
mysql -u root -e "CREATE DATABASE IF NOT EXISTS manually_fill_attendance;"
```

Confirm the app can reach them:

```powershell
python -c "import pymysql; c=pymysql.connect(host='localhost',user='root',password='',db='Face_reco_fill'); print(c.cursor().execute('SELECT 1')); c.close()"
```

If this fails, the app still works and writes CSVs — it just prints the connection error.

#### 2e. Assets and files the code expect

## Known setup risks

- The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.
