# Architecture — Semantic Segmentation with U-Net and DeepLab

## Component map

main.py → src/data.py (make_sample, load_data) → src/model.py (build_unet, dice_score, train) → web/api_impl.py (summary)

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
- `web/train_run.py`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- Images are simple shapes on a noisy background, not photographs.
- Training is very short; this is a pipeline demonstration, not a strong segmenter.
- There is no augmentation library or pretrained encoder.
