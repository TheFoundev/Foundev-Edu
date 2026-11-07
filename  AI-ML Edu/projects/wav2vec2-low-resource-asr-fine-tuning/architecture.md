# Architecture — Wav2Vec2 Low-Resource ASR Fine-tuning

## Component map

main.py (main) → src/data.py (word_signal, frame_features, load_data) → src/model.py (decode, word_distance) → demo/output

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
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`
- `web/server.py`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- The audio is synthesized and the 'phonemes' are tone bands.
- The model classifies independent frames; it is not a self-supervised speech model.
- Greedy decoding is simple and has no language model.
