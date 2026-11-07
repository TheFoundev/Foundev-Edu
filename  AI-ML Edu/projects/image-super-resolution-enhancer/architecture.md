# Architecture — Image Super-Resolution Enhancer

## Component map

main.py → src/data.py (make_image, downsample, load_data) → src/model.py (upscale, psnr, evaluate) → web/api_impl.py (summary)

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

- There is no learned super-resolution network; this is an interpolation baseline.
- The synthetic images are simple shapes, so PSNR is much friendlier than real photos.
- Sharpening parameters are tuned on the generated validation images.
