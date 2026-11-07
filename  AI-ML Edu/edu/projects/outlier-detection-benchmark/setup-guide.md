# Setup guide — Outlier Detection Benchmark

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Outlier Detection Benchmark

Compare four outlier detectors on several synthetic datasets.

> Benchmark dozens of outlier detectors (LOF, Isolation Forest, autoencoders) on tabular and credit-fraud data to flag rare anomalous records.

## Overview

An original, self-contained implementation of the **Outlier Detection Benchmark** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Gaussian, ring and clustered 2D datasets with labelled outliers
- Z-score, isolation forest, LOF and one-class SVM
- ROC AUC comparison table
- Scatter plot of scores and predictions

## Stack

`Python; Matplotlib; NumPy; scikit-learn`
The CSV stack is Python + Matplotlib + NumPy + scikit-learn. PyOD is not installed, so the benchmark uses scikit-learn detectors directly.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
outlier-detection-benchmark/
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

- Outliers are injected synthetically; real anomaly data is much messier.
- Hyperparameters are fixed per detector rather than tuned.
- ROC AUC is the only metric; precision at a fixed budget is not evaluated.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- Outliers are injected synthetically; real anomaly data is much messier.
- Hyperparameters are fixed per detector rather than tuned.
- ROC AUC is the only metric; precision at a fixed budget is not evaluated.
