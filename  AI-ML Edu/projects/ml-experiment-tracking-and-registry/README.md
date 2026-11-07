# ML Experiment Tracking and Registry

## Overview and purpose

A tiny experiment tracker and model registry backed by SQLite.

## Real-world context and scope

Operationalize an ML project lifecycle: track experiments, version datasets and models in a registry, and deploy a reproducible REST prediction endpoint. Actual implementation note: Train three model configurations on the same split

The material describes the repository as supplied. **Implemented behavior** is based on the source README and entry points; **proposed or missing functionality** is listed separately below. Do not infer production readiness from a polished interface or project title.

### Verified implementation notes

- Train three model configurations on the same split
- Log parameters, metrics and artefact paths to SQLite
- Best-run lookup and a simple model registry
- FastAPI endpoints for runs and the current best model

### Proposed, absent, or uncertain behavior

- Artefacts are pickled locally; there is no remote store or model server.
- Runs are not nested and there is no UI beyond the JSON API.
- The registry is a table lookup, not a governed production registry.

## Technology stack

- `Python`
- `NumPy`
- `scikit-learn`

## System requirements and setup

Use a supported Python environment appropriate to the source dependency pins. Some projects also require data files, trained weights, external APIs, cameras, GPU resources, a database, or an LLM runtime. These are identified in `setup-guide.md`; they are not assumed to be included. Follow the setup instructions in the source `README.md` and do not paste credentials into tracked files.

## Architecture and important components

main.py → src/data.py (load_data) → src/model.py (candidates, train, best_run, demo) → app.py (run_training)

## Directory structure

Source paths central to the learning material:

- `.github/workflows/ci.yml`
- `README.md`
- `app.py`
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
