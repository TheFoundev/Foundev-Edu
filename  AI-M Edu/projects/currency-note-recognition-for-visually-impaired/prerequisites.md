# Prerequisites — Note Sense: Currency Note Recognition

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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

```powershel

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
