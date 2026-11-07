# Setup guide — Image Super-Resolution Enhancer

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Image Super-Resolution Enhancer

Upscale small images with bicubic resampling and sharpening.

> Enhance blurry or low-resolution images such as document scans, satellite, or medical imagery with Real-ESRGAN and benchmark quality metrics and runtime on CPU versus GPU.

## Overview

An original, self-contained implementation of the **Image Super-Resolution Enhancer** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic low/high resolution image pairs
- Bicubic upscaling with an unsharp mask
- PSNR and mean absolute error evaluation
- Before/after image saved for inspection

## Stack

`Python; Matplotlib; NumPy; Pillow`
The CSV stack is Python + Matplotlib + NumPy + Pillow. Those packages are not available here, so this is a classical PIL/NumPy baseline with the same CLI.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
image-super-resolution-enhancer/
├── main.py                 train / demo CLI
├── src/data.py             dataset builder
├── src/model.py            model and evaluation
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

6 tests (`pytest -q`), up from 2.

## Notes and limitations

- There is no learned super-resolution network; this is an interpolation baseline.
- The synthetic images are simple shapes, so PSNR is much friendlier than real photos.
- Sharpening parameters are tuned on the generated validation images.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- There is no learned super-resolution network; this is an interpolation baseline.
- The synthetic images are simple shapes, so PSNR is much friendlier than real photos.
- Sharpening parameters are tuned on the generated validation images.
