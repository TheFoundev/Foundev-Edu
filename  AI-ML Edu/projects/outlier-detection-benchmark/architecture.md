# Architecture — Outlier Detection Benchmark

## Component map

main.py → src/data.py (gaussian, ring, clustered) → src/model.py (zscore_scores, train, demo) → web/api_impl.py (summary)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

- `.github/workflows/ci.yml`
- `README.md`
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

- Outliers are injected synthetically; real anomaly data is much messier.
- Hyperparameters are fixed per detector rather than tuned.
- ROC AUC is the only metric; precision at a fixed budget is not evaluated.
