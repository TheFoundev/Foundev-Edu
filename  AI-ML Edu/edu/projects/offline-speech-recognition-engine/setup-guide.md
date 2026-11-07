# Setup guide — Offline Speech Recognition Engine

1. Obtain the matching source project and inspect `README.md`, `requirements.txt`, and the cited implementation files.
2. Create a fresh virtual environment using the source's documented Python version. Do not reuse an unknown environment.
3. Install only declared dependencies using the repository's own instructions; compare requirements with actual imports.
4. Prepare datasets, checkpoints, API keys, database, camera, or local model runtime only if the source README or code requires them. Keep secrets out of source control.
5. Start the documented backend/CLI/desktop app in the documented order. A static UI may not connect to a backend.
6. Run source tests only after dependencies and data are present; separately verify the expected interface response and a known example.

## Source setup notes

# Offline Speech Recognition Engine

A command-word recognizer using DTW template matching.

> Engineer a fully offline ASR system with CTC sequence modeling and n-gram language-model rescoring, benchmarking word error rate on LibriSpeech test data.

## Overview

An original, self-contained implementation of the **Offline Speech Recognition Engine** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic command words built from tone sequences
- Frame-level log-band features
- Dynamic time warping against per-word templates
- Accuracy on held-out samples and a demo recording

## Stack

`Python; NumPy`
The CSV stack is Python + NumPy. Those models are not available, so this build implements a small template-matching recognizer with NumPy.

## Run

```bash
pip install -r requirements.txt
python main.py train
python main.py demo
pytest -q
```

## Structure

```text
offline-speech-recognition-engine/
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

5 tests (`pytest -q`), up from 2: the distance, the band and the pipeline.

## Notes and limitations

- Audio is synthetic and limited to eight command words.
- DTW template matching does not scale to a real vocabulary.
- There is no language model; every frame sequence is independent.

## License

MPL-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

## Known setup risks

- Audio is synthetic and limited to eight command words.
- DTW template matching does not scale to a real vocabulary.
- There is no language model; every frame sequence is independent.
