# Architecture — Speech-to-Text Transcription Service

## Component map

main.py → src/data.py (tone, utterance, features) → src/model.py (segment, transcribe) → app.py (api_transcribe)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

- `.github/workflows/ci.yml`
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/model.py`
- `tests/test_pipeline.py`
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`

## Implemented versus proposed

Implemented behavior is limited to the source entry points and code paths described above.

- No real speech is recorded or recognized.
- The vocabulary is ten digits and the audio is generated from tones.
- A real service needs a trained acoustic model, language model and audio decoding.
