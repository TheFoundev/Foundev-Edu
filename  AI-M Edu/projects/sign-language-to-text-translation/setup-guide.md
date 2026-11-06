# Setup guide — SignBridge: Rule-Based Sign Language Text Translation

1. Obtain the matching source project and inspect `README.md`, `WORKFLOW.md`, `PROJECT_OVERVIEW.md`, and dependency files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source workflow requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# SignBridge Studio (sign-language-to-text-translation) — Setup & Test Workflow

### 1. Prerequisites

- **OS**: Windows (PowerShell)
- **Python**: 3.12.1 works for many packages, but some deps (notably `mediapipe`) historically prefer Python <= 3.11. If you hit mediapipe issues, use `py -3.11`.
- **Poetry** (optional): `poetry.lock` present; you can use `poetry install`.
- **Node.js**: v22.15.0 (not required for CLI; static UI only needs a server)
- **Internet**: Required for first-time weight downloads from GitHub releases (see config). No weights shipped in repo.

### 2. Installation and Setup

Project is a **Python package + Click CLI** (`pyproject.toml`, entry point `slt = sign_language_translator.cli:slt`). Static UI exists but is demo-only.

From `N:\Foundev-Projects\Domain\Artificial Intelligence & Machine Learning\sign-language-to-text-translation\`:

#### Option A: Editable install with venv + pip (recommended on Windows)
```powershell
py -3.11 -m venv .venv  # use 3.11 if mediapipe needed
.\.venv\Scripts\Activate.ps1
pip install -e .
# For tests/dev tools:
pip install -e ".[dev]"
```

#### Option B: Poetry
```powershell
poetry install
poetry shell
# For dev:
poetry install --with dev  # if groups configured
```

#### Option C: requirements.txt (caution)
```powershell
pip install -r requirements.txt
```
**Important:** `requirements.txt` pins different versions than `pyproject.toml` (numpy/torch/matplotlib/click/mediapipe). Prefer `pyproject.toml`/Poetry or editable install to avoid dependency conflicts.

**Notes:** Weights auto-download on demand from GitHub releases per `config/urls.json` with `AUTO_DOWNLOAD=True`. `assets/` may not exist initially. Sign→text model is marked **COMING SOON** upstream.

### 3. Launch the Complete Project

#### Component 1: CLI (`slt`) — primary functionality
After install, verify CLI:
```powershell
slt --help
```
Example translation (rule-based):
```powershell
slt translate --model-code rule-based --text-lang english --sign-lang pk-sl --sign-format video "What is your name?"
```
Other command groups: `slt assets`, `slt complete`, `slt translate`, `slt embed`. First real translation may trigger downloads (internet required).

#### Component 2: Static UI (demo)
```powershell
py -m http.server 8000
```
Open [http://localhost:8000/](http://localhost:8000/). `index.html` + `js/app.js` provide a demo tokenizer/gloss/lexicon; **no `fetch()` calls** — purely client-side demo. **No HTTP backend/API** serves inference.

### 4. Test the Project

#### Automated tests (real suite)
From repo root with venv activated and dev deps installed:
```powershell
python -m pytest
```
Config: `pyproject.toml` has `addopts = "-vv"`, `testpaths = ["tests"]`. Some tests may require `mediapipe` (Python <= 3.11). Install dev extras via `pip install -e ".[dev]"` or Poetry.

#### Manual CLI tests
| Command | Expected |
|---|---|
| `slt --help` | Shows Click command groups. |
| `slt translate --help` | Shows translate options/flags. |
| `slt assets --help` / `slt complete --help` / `slt embed --help` | Group help available. |
| Rule-based translate example above | Runs if deps present; may download assets if missing (internet). |

#### Manual UI tests
| Test | Expected |
|---|---|
| Serve UI and load page | Demo UI renders (no network calls required). |

### 5. Troubleshooting

| Issue | Cause | Fix |
|---|---|---|
| `slt` not found | Not installed/venv not activated | Activate venv and `pip install -e .` |
| `mediapipe` install fails | Python version incompatibility | Use `py -3.11` venv; mediapipe support varies. |
| Dependency conflicts | `requirements.txt` vs `pyproject.toml` versions differ | Prefer editable install from `pyproject.toml`. |
| Asset download fails | No internet / GitHub blocked | Ensure internet; check `config/urls.json`. Downloads happen on demand. |
| "COMING SOON" for sign→text model | Not implemented upstream | Use rule-based or available modes as implemented. |

### 6. Verification Checklist

- [ ] Created/activated venv (recommend Python 3.11 if mediapipe used)
- [ ] Installed package: `pip install -e .` (or Poetry)
- [ ] Dev deps installed for tests: `pip install -e ".[dev]"` (or equivalent)
- [ ] `slt --help` runs successfully
- [ ] `python -m pytest` runs (note any tests needing mediapipe/internet)
- [ ] (Optional) Weights/assets downloaded or handled; internet available if testing real models
- [ ] Static UI served: `py -m http.server 8000` loads demo at `http://localhost:8000/`

## Known setup risks

- The core is rule-based gloss restructuring and token-to-clip mapping, not video recognition or general language translation. Clip coverage and dialect/culture constraints need signer review.
