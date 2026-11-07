# Architecture — Abstractive Document Summarization

## Component map

main.py → src/data.py (split_sentences, load_data) → src/model.py (score_length, search_length, summarize, rouge_l) → app.py (api_summarize)

## Data and control flow

Use the project-specific lessons to trace input → preprocessing → algorithm/model → postprocessing → presentation. Verify each transition against the listed source files.

## Algorithm/model details

The source README and implementation files define the behavior taught here; the lesson cites the selected code path and marks unavailable features explicitly.

## Source inventory

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

- The brief says abstractive, but this implementation is extractive: it selects whole sentences.
- There is no neural encoder-decoder, tokenizer download or generation step.
- Evaluation uses a small hand-written set of documents and reference summaries.
