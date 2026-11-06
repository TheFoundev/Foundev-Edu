# Prerequisites — YieldSight: County-Level Crop Yield Prediction

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

# YieldSight (crop-yield-prediction) — Setup & Test Workflow

This document covers **how to install, configure, launch and test the complete project**: the static YieldSight
console (`index.html` + `css/style.css` + `js/app.js`, port **8000**) and the PyTorch **command-line
pipeline** (`run.py` → `cyp/`) that actually produces predictions.

**Honest scope note up front — this project has no runnable model in this checkout:**

* **There is no HTTP server and no API.** `js/app.js` contains **no `fetch()` call**, no URL and no port.
  The console renders an explicitly labelled *illustrative sample series* and its **Pipeline** tab lists
  the real commands.
* **No trained weights ship.** `data/models/` does not exist; checkpoints (`<year>_<run>_<time>_gp.pth.tar`)
  are produced by a training run.
* **No model input ships.** `data/img_output/histogram_all_full.npz` is absent; it is produced by the
  `engineer` stage.
* **The flagship workflow needs ≈ 110 GB of MODIS downloads from Google Earth Engine** plus Earth Engine
  authentication and Google Drive — it is **not reproducible** in this environment.
* **No local environment exists.** There is no `.venv`, and the machine's Python 3.12.1 lacks `fire`,
  `ee`, `gdal` and `rasterio`. The dependencies are declared in `environment.yml` (Conda).

So: the **UI is fully runnable today**; the **pipeline is installable and inspectable**, but producing a
real prediction requires the external MODIS data and Earth Engine credentials.

---

### 1. Prerequisites

| Requirement | Version / detail | Checked with |
|---|---|---|
| OS | Windows 10/11 (commands below are PowerShell). Linux/macOS work identically | `Get-Host` |
| **Conda** | Miniconda / Anaconda — **strongly recommended**, `gdal` and `pytorch=1.0.0` have no pip wheels for modern Windows Python | `conda --version` |
| Python (project) | **3.7** per `environment.yml` / upstream README | `conda run -n crop_yield_prediction python --version` |
| Python (system) | 3.12.1 is present but **cannot host this pipeline** | `python --version` |
| **Google Earth Engine account** | Required for the `export` stage | <https://developers.google.com/earth-engine/> |
| **Google Drive** | Earth Engine writes the exports there; you download them into `data/` | — |
| Disk space | **≈ 110 GB** for the MODIS export + **≈ 97 GB** for the processed `.npy` arrays | `Get-PSDrive` |
| GPU | **Optional** — `run.py` defaults to `torch.device("cuda:0" if torch.cuda.is_available() else "cpu")` | `nvidia-smi` |
| Node.js | **Not required** — the console is plain HTML/CSS/JS, no build step | —

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
