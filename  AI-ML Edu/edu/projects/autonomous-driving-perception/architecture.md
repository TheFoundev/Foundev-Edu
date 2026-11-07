# Architecture — Autonomous Driving Perception

## Component map

main.py → src/data.py (make_scene, load_data) → src/model.py (lane_iou, detect_vehicles, match_detections, evaluate) → web/api_impl.py (summary)

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

- Scenes are drawn procedurally; there is no real camera or driving dataset.
- Lane and vehicle detection are classical image operations, not a trained network.
- The evaluation is a sanity check, not a benchmark against KITTI or nuScenes.
