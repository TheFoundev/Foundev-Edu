# Outlier Detection Benchmark

## Overview and purpose

Compare four outlier detectors on several synthetic datasets.

## Real-world context and scope

Benchmark dozens of outlier detectors (LOF, Isolation Forest, autoencoders) on tabular and credit-fraud data to flag rare anomalous records. Actual implementation note: Gaussian, ring and clustered 2D datasets with labelled outliers

The material describes the repository as supplied. **Implemented behavior** is based on the source README and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

- Gaussian, ring and clustered 2D datasets with labelled outliers
- Z-score, isolation forest, LOF and one-class SVM
- ROC AUC comparison table
- Scatter plot of scores and predictions

### Proposed, absent, or uncertain behavior

- Outliers are injected synthetically; real anomaly data is much messier.
- Hyperparameters are fixed per detector rather than tuned.
- ROC AUC is the only metric; precision at a fixed budget is not evaluated.

## Technology stack

- `Python`
- `Matplotlib`
- `NumPy`
- `scikit-learn`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the setup instructions in the source `README.md` and do not paste credentials into tracked files.

## Architecture and important components

main.py → src/data.py (gaussian, ring, clustered) → src/model.py (zscore_scores, train, demo) → web/api_impl.py (summary)

## Directory structure

Source paths central to the learning material:

- `.github/workflows/ci.yml`
- `README.md`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/model.py`
- `tests/test_pipeline.py`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/console.html`
- `web/index.html`
- `web/server.py`

## Installation, environment, and database

See [`setup-guide.md`](setup-guide.md) for repository-specific commands, environment variables, optional services, and data/model requirements. Database setup is only applicable when the source workflow documents a database.

## Testing

Use only tests and checks present in the source repository. This learning package has not run the source application or trained a model. Expected test behavior and missing coverage are described in the source README and lessons.

## Security, privacy, and responsible use

Treat credentials, uploaded data, biometric data, student/financial records, and generated outputs as sensitive where relevant. Apply data minimization, consent and access controls, retention limits, secure secret handling, documented error handling, and human review. For consequential decisions, model outputs are educational signals only. Project-specific hazards appear in the final project guide and source review report.

## Troubleshooting

Start with missing assets and dependency versions, then validate input shape/schema, check configured API/database/model services, inspect logs, and compare observed behavior with the exact source path described in `architecture.md`. Many repositories contain a static UI or stub that is not wired to the model.

## Expected outcome

Complete the final project to explain and reproduce the repository's actual data-to-output path, demonstrate a tested source-aligned extension, and document its limitations.

## Further learning

See `references.json` for official framework references and the source repository README plus cited files for implementation details.
