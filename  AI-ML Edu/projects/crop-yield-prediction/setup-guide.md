# Setup guide — YieldSight: County-Level Crop Yield Prediction

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

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
| Node.js | **Not required** — the console is plain HTML/CSS/JS, no build step | — |
| API keys | None of your own — Earth Engine uses its own OAuth login | — |

Project root (used by every command below):

```powershell
$root = "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\crop-yield-prediction"
Set-Location $root
```

---

### 2. Installation and Setup

#### 2.1 The console (static UI) — nothing to install

The console has **no dependencies at all** — pure HTML/CSS/JS with relative asset paths. Skip to
[Section 3.2](#32-frontend--the-yieldsight-console-static) if you only want the UI.

#### 2.2 The pipeline — Conda environment from `environment.yml`

```powershell
Set-Location "N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\crop-yield-prediction"

# 1. Create the environment exactly as declared (env name: crop_yield_prediction)
conda env create -f environment.yml

# 2. Activate it
conda activate crop_yield_prediction

# 3. Verify the pieces the code imports
python -c "import torch, fire, ee, numpy, pandas, scipy; print('torch', torch.__version__); print('ee ok'); print('fire ok')"

# 4. (optional) the error-map script needs BeautifulSoup, which is NOT in environment.yml
pip install beautifulsoup4
```

`environment.yml` (the shipped file) declares:

```yaml
name: crop_yield_prediction
channels: [pytorch, conda-forge, defaults]
dependencies:
  - pandas
  - numpy
  - gdal
  - matplotlib
  - scipy
  - tqdm
  - fire
  - pytorch=1.0.0
  - earthengine-api
```

> **Expect to relax the pins.** `pytorch=1.0.0` is from 2018 and the code is written against the PyTorch
> 1.0 API. If `conda env create` fails to resolve, install a modern torch into the same environment
> (`conda install pytorch>=1.10 -c pytorch`) and expect small API drift.
> **Never `pip install gdal`** — GDAL is not a pip package on most platforms; use
> `conda install -c conda-forge gdal` and do not mix conda and pip GDAL builds.

**Current state of this checkout (verified):** there is **no `.venv`**, and the system Python 3.12.1
**cannot** run the CLI. `python run.py --help` currently fails with:

```
  File "...\cyp\data\__init__.py", line 1, in <module>
    from .exporting import MODISExporter
  File "...\cyp\data\exporting.py", line 1, in <module>
    import ee
ModuleNotFoundError: No module named 'ee'
```

(`torch` 2.13.0+cpu is installed system-wide, but `fire`, `ee` and `gdal` are not — verified.)

#### 2.3 Earth Engine authentication (only needed for the `export` stage)

```powershell
conda activate crop_yield_prediction
earthengine authenticate

# Verify
python -c "import ee; ee.Initialize(); print('Earth Engine OK')"
```

`earthengine authenticate` opens a browser and stores a refresh token under
`~/.config/earthengine/credentials`. `ee.Initialize()` must succeed before `export` will run.

#### 2.4 Configuration

**There is no `.env` file and no environment variables** are read by this project's own code. The
configuration surface is:

| Mechanism | Value / flags |
|---|---|
| Earth Engine credentials | `earthengine authenticate` → `~/.config/earthengine/credentials` |
| Google Drive | The account signed up to Earth Engine; exports land there |
| Conda environment name | `crop_yield_prediction` (from `environment.yml`) |
| CLI flags | `--export_limit`, `--major_states_only`, `--check_if_done`, `--download_folder`, `--yield_data_path`, `--mask_path`, `--temperature_path`, `--image_path`, `--cleaned_data_path`, `--multiprocessing`, `--processes`, `--parallelism`, `--delete_when_done`, `--num_years`, `--checkpoint`, `--num_bins`, `--max_bin_val`, `--county_data_path`, `--dropout`, `--dense_features`, `--savedir`, `--times`, `--pred_years`, `--num_runs`, `--train_steps`, `--batch_size`, `--starter_learning_rate`, `--weight_decay`, `--l1_weight`, `--patience`, `--use_gp`, `--sigma`, `--r_loc`, `--r_year`, `--sigma_e`, `--sigma_b`, `--device` |

#### 2.5 Data paths the code expects

| Path | Constant / default | Present in this checkout? |
|---|---|---|
| `data/yield_data.csv` | `RunTask.export(yield_data_path=…)` | **Yes** |
| `data/county_data.csv` | `RunTask.engineer(county_data_path=…)` | **Yes** |
| `data/counties.svg` | `plot_county_errors(svg_file=…)` | **Yes** |
| `data/crop_yield-data_image/` | `RunTask.process(image_path=…)` | **No** — exported from Earth Engine |
| `data/crop_yield-data_mask/` | `RunTask.process(mask_path=…)` | **No** — exported from Earth Engine |
| `data/crop_yield-data_temperature/` | `RunTask.process(temperature_path=…)` | **No** — exported from Earth Engine |
| `data/img_output/` | `RunTask.process(cleaned_data_path=…)` | **No** — produced by the process stage |
| `data/img_output/histogram_all_full.npz` | `ModelBase.run(path_to_histogram=…)` | **No** — produced by the engineer stage |
| `data/models/<model_type>/` | `RunTask.train_cnn(savedir=Path("data/models"))` | **No** — produced by training |

---

### 3. Launch the Complete Project

#### 3.1 The pipeline — a four-stage CLI (no server, no port)

```powershell
conda activate crop_yield_predict

## Known setup risks

- The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.
