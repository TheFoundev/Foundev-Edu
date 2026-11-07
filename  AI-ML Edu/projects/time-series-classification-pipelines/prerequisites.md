# Prerequisites — Time-Series Classification Pipelines

## Skills
- Python functions, modules, exceptions, and virtual environments.
- Reading JSON, CSV, images, API requests, or model artifacts as applicable to the source.
- Basic train/validation/test separation, metrics, and error analysis.
- Command-line navigation and careful handling of sensitive input.

## Project-specific preparation

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

## Readiness check

Before starting, locate the documented entry point, identify any unavailable artifact, and explain what output the repository can produce without that artifact.
