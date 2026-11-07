# Setup guide — Weed Species Detection

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Weed Species Detection

Classify synthetic weed species from leaf features.

> Classify eight Australian weed species in pasture imagery with transfer-learned ResNet50 and InceptionV3 models and discuss precision-agriculture deployment on drones.

## Overview

An original, self-contained implementation of the **Weed Species Detection** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Procedurally drawn leaves for four species
- Shape and colour summary features
- Random forest classifier with per-species accuracy
- Sample leaf images saved for inspection

## Stack

`Python; Matplotlib; NumPy; scikit-learn`
The CSV stack is Python + Matplotlib + NumPy + scikit-learn. Pretrained ImageNet weights are not available, so the build uses hand-built features and a random forest.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
weed-species-detection/
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

- Leaves are simple geometric shapes, not field photographs.
- Features are hand-built instead of learned by a CNN.
- There is no augmentation, transfer learning or background variation.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- Leaves are simple geometric shapes, not field photographs.
- Features are hand-built instead of learned by a CNN.
- There is no augmentation, transfer learning or background variation.
