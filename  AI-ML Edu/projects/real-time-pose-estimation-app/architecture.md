# Architecture — Real-Time Pose Estimation App

## Component map

main.py → src/data.py (make_frame, load_data) → src/model.py (find_people, fit_ridge, estimate, pck) → app.py (api_summary)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

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
- `web/login.html`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- MediaPipe is not used, so the regressor is a ridge regression over the brightness of a small grid of the person, not a neural network. The detector also assumes bright figures on a dark background.
- The camera needs OpenCV and a camera; without them the simulator and the upload are the inputs.
- The person is found by the bright pixels, so a person on a bright background is not found.
