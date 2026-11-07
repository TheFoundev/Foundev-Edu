# Architecture — Facial Attribute Analysis Kiosk

## Component map

main.py → src/data.py (draw_face, load_data) → src/model.py (train, demo) → app.py (summary)

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
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- The faces are drawn with rectangles and ellipses; there are no photos or real people.
- The model reads pixel patterns from the synthetic generator, not facial structure.
- Glasses and smile are the only two attributes; there is no face detection step.
