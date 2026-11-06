# Rag Evaluation Harness With Ragas

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# RAG Evaluation Harness with RAGAS

Measure retrieval and answer quality on a small synthetic QA set.

> Measure and improve retrieval quality with automated metrics for faithfulness, context recall and answer relevancy plus regression tests.

## Overview

An original, self-contained implementation of the **RAG Evaluation Harness with RAGAS** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Synthetic question, answer and context triples
- TF-IDF retrieval with a hit-rate metric
- Token overlap F1 for short answers
- Faithfulness check against the retrieved context

## Stack

`Python; NumPy; Pandas; scikit-learn`
The CSV stack is Python + NumPy + Pandas + scikit-learn. Those packages are not installed, so the evaluation metrics and retrieval are implemented directly with scikit-learn and plain Python.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
rag-evaluation-harness-with-ragas/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

5 tests (`pytest -q`), up from 2.


## Notes and limitations

- Questions and contexts are synthetic and very small in number.
- Retrieval is TF-IDF, not an embedding index.
- The answer extractor picks a sentence from the context, so the evaluation is optimistic.

## License

Apache-2.0. See `LICENSE`.

## Abo

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Synthetic question, answer and context triples
- TF-IDF retrieval with a hit-rate metric
- Token overlap F1 for short answers
- Faithfulness check against the retrieved context
- Questions and contexts are synthetic and very small in number.
- Retrieval is TF-IDF, not an embedding index.
- The answer extractor picks a sentence from the context, so the evaluation is optimistic.

The implementation inventory includes 19 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/pipeline.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/test_pipeline.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
