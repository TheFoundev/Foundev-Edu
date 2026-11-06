# Dagster Data Pipeline Platform

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Dagster Data Pipeline Platform

An asset-oriented customer pipeline with lineage logging.

> Build a software-defined data platform with Dagster assets, schedules, sensors and lineage for a multi-source analytics pipeline.

## Overview

An original, self-contained implementation of the **Dagster Data Pipeline Platform** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The assets depend on each other, and the materialisation log says which
  asset depends on which and which run it belongs to
- The customers are grouped with the RFM model: how recently they signed up,
  how often they order and what they are worth, scored by their fifth
- The assets are written as Parquet files

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Dagster is not installed, so the asset graph is executed by a small local runner and lineage is stored in SQLite.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
dagster-data-pipeline-platform/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
```bash
pytest -q
```

8 tests: the graph of the assets, that the duplicates are removed, that the
log holds the dependencies and one run id per run, the RFM groups and the
report of the groups.
```

## Notes and limitations

- The asset graph is executed by a plai

## Actual features and limits

README feature statements (verify each against code before relying on it):
- The assets depend on each other, and the materialisation log says which
- The customers are grouped with the RFM model: how recently they signed up,
- The assets are written as Parquet files
- The asset graph is executed by a plain function, not a Dagster daemon.
- SQLite stores lineage metadata; the warehouse tables are local Parquet files.
- There is no scheduling, partitioning or backfill UI.

The implementation inventory includes 22 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

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
