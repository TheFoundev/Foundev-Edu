# Setup guide — TensorFlow Object Detection API

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# TensorFlow Object Detection API

Detect and classify simple shapes in synthetic images.

> Train and deploy custom object detectors (people, helmets, vehicles) on domain images using the TensorFlow Model Garden detection API with COCO-pretrained checkpoints.

## Overview

An original, self-contained implementation of the **TensorFlow Object Detection API** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic scenes with circles and squares
- Connected-component proposals
- Crop features and a random forest shape classifier
- Box precision, recall and class accuracy

## Stack

`Python; Matplotlib; NumPy; SciPy; scikit-learn`
The CSV stack is Python + Matplotlib + NumPy + SciPy + scikit-learn. Those training pipelines need large downloads, so this is a classical detector with sklearn.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
tensorflow-object-detection-api/
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

3 tests (`pytest -q`), up from 2.

## Notes and limitations

- Only circles and squares on a clean background are supported.
- There are no overlapping objects or real photographs.
- The proposal stage is connected components, not a region proposal network.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- Only circles and squares on a clean background are supported.
- There are no overlapping objects or real photographs.
- The proposal stage is connected components, not a region proposal network.
