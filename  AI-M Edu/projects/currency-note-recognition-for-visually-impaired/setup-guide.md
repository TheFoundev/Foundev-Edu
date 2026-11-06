# Setup guide — Note Sense: Currency Note Recognition

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Note Sense (currency-note-recognition-for-visually-impaired) — Setup & Test Workflow

This document covers **how to install, configure, launch and test the complete project**: the OpenCV ORB
recogniser (`Currency Detection using OpenCV in ML/detect.py`), its helper module (`utils.py`), and the
static Note Sense page (`index.html` + `css/style.css` + `js/app.js`, port **8000**).

**Honest scope note up front:**

* **There is no HTTP backend, no API and no model server.** `js/app.js` contains **no `fetch()` call**, no
  `XMLHttpRequest` and no backend URL. Pressing *Identify note* switches the result banner to an honest
  **"Requires backend"** state that explains that recognition happens inside the local OpenCV script and
  shows the exact command to run it.
* **There is no trained model.** The "model" is the set of reference photographs in
  `Currency Detection using OpenCV in ML/files/` (44 JPGs; six of them are the `training_set`).
* **The detector is a desktop GUI script** — it opens OpenCV and matplotlib windows and waits for a key
  press. It **cannot run headless**.
* **The script does not play audio.** `detect.py` builds `audio_file = 'audio/<value>.mp3'` and then
  overwrites it with the literal `"value.mp3"`, and the `playsound(...)` / `gTTS` calls are commented out.
  The **web page** plays the real pre-recorded announcements instead.

---

### 1. Prerequisites

| Requirement | Version / detail | Checked with |
|---|---|---|
| OS | Windows 10/11 (commands below are PowerShell) | `Get-Host` |
| Python | 3.12.1 is present; **the shipped 2020 pins will not build on it** — use the unpinned install in Section 2 | `python --version` |
| opencv-python | ≥ 4.10 (4.13.0 is already installed system-wide here) | `python -c "import cv2; print(cv2.__version__)"` |
| numpy | ≥ 2.0 on 3.12 (2.2.4 already installed) | `python -c "import numpy; print(numpy.__version__)"` |
| matplotlib | ≥ 3.9 (3.11.1 already installed) | `python -c "import matplotlib; print(matplotlib.__version__)"` |
| **playsound** | **Not in `requirements.txt` but imported at the top of `detect.py`** | `python -c "import playsound"` |
| **gTTS** | **Not in `requirements.txt` but imported at the top of `detect.py`** | `python -c "import gtts"` |
| **A display / GUI session** | Required — `utils.display()` calls `cv2.waitKey(0)` and `detect.py` calls `plt.show()` | — |
| Node.js | **Not required** — the page is plain HTML/CSS/JS, no build step | — |
| API keys / network / GPU | **None.** The pipeline is fully offline, CPU-only | — |

Project root (used by every command below):

```powershell
$root = "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\currency-note-recognition-for-visually-impaired"
Set-Location $root
```

> The detector lives in a **subfolder** that uses relative paths, so it must be launched from inside
> `Currency Detection using OpenCV in ML`.

---

### 2. Installation and Setup

#### 2.1 The detector's dependencies

The dependency file ships **inside the detector folder**:
`Currency Detection using OpenCV in ML\requirements.txt`, pinned to 2020 versions:

```
certifi==2020.6.20
cycler==0.10.0
kiwisolver==1.3.1
matplotlib==3.3.2
numpy==1.19.4
opencv-python==4.4.0.46
Pillow==8.0.1
pyparsing==2.4.7
python-dateutil==2.8.1
six==1.15.0
```

> **These pins will not install on Python 3.12** (`numpy==1.19.4`, `matplotlib==3.3.2`, `Pillow==8.0.1`
> have no 3.12 wheels). Also note that `playsound` and `gTTS` are **missing from this file** even though
> `detect.py` imports both at module level.

**Recommended install (Python 3.12, unpinned modern versions):**

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\currency-note-recognition-for-visually-impaired\Currency Detection using OpenCV in ML"

python -m venv .venv
.\.venv\Scripts\Activate.ps1
# If PowerShell blocks the activation script:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

python -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install "opencv-python>=4.10,<5" "numpy>=2.0,<3" "matplotlib>=3.9,<4" "pillow>=10" playsound gTTS
```

Verify:

```powershell
.\.venv\Scripts\python.exe -c "import cv2, numpy, matplotlib, playsound, gtts; print('cv2', cv2.__version__); print('numpy', numpy.__version__); print('matplotlib', matplotlib.__version__); print('playsound + gtts OK')"
```

> **The system Python 3.12.1 already has `cv2` 4.13.0, `numpy` 2.2.4 and `matplotlib` 3.11.1**, but
> **not** `playsound` and **not** `gtts` — verified: `python detect.py` currently fails with
> `ModuleNotFoundError: No module named 'playsound'` (the import on `detect.py` line 4).
> Installing just those two packages is enough to run the detector with the system interpreter:
> ```powershell
> python -m pip install playsound gTTS
> ```

**Legacy path (Python ≤ 3.9, as the upstream file intends):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install playsound gTTS
```

> Linux/macOS: replace `.\.venv\Scripts\Activate.ps1` with `source .venv/bin/activate`.

#### 2.2 Configuration

**There is none.** The code reads no environment variables, no `.env` file, no config file and no
command-line arguments. Everything is hard-coded in `detect.py`:

| Setting | Hard-coded value | Location |
|---|---|---|
| Test image | `files/test_200_1.jpg` | `detect.py:22` (it overrides the `files/test_100_4.jpg` assignment on line 20) |
| Training / reference set | `files/20.jpg`, `files/50.jpg`, `files/100.jpg`, `files/500.jpg`, `files/200.jpg`, `files/test_20_6.jpg` | `detect.py:32` |
| Minimum "good" matches | `max_val = 8` (result printed only when `max_val != 8`, i.e. **strictly more than 8**) | `detect.py:10`, `detect.py:58` |
| Lowe's ratio test | `0.789` (source comment: *"give an arbitrary number"*) | `detect.py:48` |
| Preview scale | `0.4` | `detect.py:25` |
| ORB instance | `cv2.ORB_create()` with default parameters | `detect.py:14` |
| Display window size | `1440 x 900` (hard-coded "MacBook Air" resolution) | `utils.py:171` |

**To test your own photo**, edit one line and drop the file into `files/`:

```python
test_img = read_img('files/my_note.jpg')
```

**Reference images** live in `Currency Detection using OpenCV in ML\files\` — **44 JPGs**:
the denomination references (`10.jpg`, `20.jpg`, `50.jpg`, `100.jpg`, `200.jpg`, `500.jpg`, `2000.jpg`),
extra variants (`10_2.jpg`, `20_2.jpg`, `20_3.jpg`, `100_2.jpg`, `100_3.jpg`, `50_2.jpg`, `50_3.jpg`) and
the `test_*.jpg` photographs.

A second, smaller image set also ships at the project root and is used only by the page's gallery:
`Images\currency_images\` (5 photos: `20_rs`, `50_rs`, `100_rs`, `200_rs`, `500_rs`) and
`Images\testing_images\` (19 photos including `Euro-500.png` and `test_dollar_*.jpg`).

**Audio samples** — `Currency Detection using OpenCV in ML\audio\` contains exactly three files:
`20.mp3`, `50.mp3`, `100.mp3`. There is **no** ₹200 or ₹500 sample.

---

### 3. Launch the Complete Project

#### 3.1 The detector — the only component that produces a denomination

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\currency-note-recognition-for-visually-impaired\Currency Detection using OpenCV in ML"
.\.venv\Scripts\python.exe detect.py
```

> **It must be run from inside `Currency Detection using OpenCV in ML`** — `detect.py` does
> `from utils import *` and opens `files/...` with relative paths.

What happens, step by step:

1. A window titled **`original`** appears showing the resized preview. `utils.disp

## Known setup risks

- There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.
