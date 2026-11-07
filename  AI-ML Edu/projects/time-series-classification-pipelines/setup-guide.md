# Setup guide — Time-Series Classification Pipelines

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Time-Series Classification Pipelines

Classify short time series with summary and frequency features.

> Apply unified time-series pipelines to classification and forecasting tasks such as human activity recognition using sktime's scikit-compatible API.

## Overview

An original, self-contained implementation of the **Time-Series Classification Pipelines** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic sine, square and trending series
- Time-domain and FFT-based features
- Random forest classifier with a confusion matrix
- Single-series prediction in demo mode

## Stack

`Python; Matplotlib; NumPy; scikit-learn`
The CSV stack is Python + Matplotlib + NumPy + scikit-learn. sktime is not installed, so the feature extraction and pipeline are written directly with NumPy and scikit-learn.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
time-series-classification-pipelines/
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

4 tests (`pytest -q`), up from 2.

## Notes and limitations

- Classes are generated from simple formulas with noise.
- The classifier only sees summary features, not the raw sequence.
- There is no temporal cross-validation.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- Classes are generated from simple formulas with noise.
- The classifier only sees summary features, not the raw sequence.
- There is no temporal cross-validation.
