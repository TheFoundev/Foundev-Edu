# Architecture — Segment Anything (SAM) Fine-tuning

## Component map

main.py → src/data.py (make_sample, load_data) → src/model.py (encode_image, decode_point, fine_tune, segment) → app.py (_predictions)

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

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- Only one bright shape per image is supported.
- The point prompt must land inside the shape.
- There is no encoder training or mask decoder network.
