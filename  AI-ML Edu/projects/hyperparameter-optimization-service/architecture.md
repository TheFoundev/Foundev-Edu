# Architecture — Hyperparameter Optimization Service

## Component map

main.py → src/data.py (load_data) → src/model.py (run_search, ensure_db, train, demo) → app.py (trials)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

- `.github/workflows/ci.yml`
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/model.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`
- `web/server.py`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- The search space is deliberately tiny and runs on one CPU.
- There is no pruning, distributed workers or persistent study server.
- SQLite is used as a simple local trial store.
