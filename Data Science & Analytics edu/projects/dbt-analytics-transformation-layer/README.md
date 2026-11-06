# Dbt Analytics Transformation Layer

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# dbt Analytics Transformation Layer

A mini SQL transformation runner with dbt-style refs and models.

> Develop an analytics-engineering project that transforms raw event data into documented, tested dimensional models using dbt.

## Overview

An original, self-contained implementation of the **dbt Analytics Transformation Layer** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The models are ordered by the `{{ ref() }}` calls in the SQL files, not by
  a list that is written by hand
- A model that needs a model that is not there, and a cycle, are errors
- The manifest says which model depends on which
- The raw tables and the models are materialised into SQLite

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. dbt is not installed, so a small local runner resolves refs and materialises the SQL models in SQLite.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
dbt-analytics-transformation-layer/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── models/*.sql             staging and mart SQL models
```

## Testing

```bash
pytest -q
```

9 tests: the models of the directory, the order that comes from the refs, a
model that is missing, a cycle, the dependencies of a model, the manifest and
the revenue of the day.

## Notes and limitations

- The ru

## Actual features and limits

README feature statements (verify each against code before relying on it):
- The models are ordered by the `{{ ref() }}` calls in the SQL files, not by
- A model that needs a model that is not there, and a cycle, are errors
- The manifest says which model depends on which
- The raw tables and the models are materialised into SQLite
- The runner supports only simple refs, not Jinja, macros or tests.
- SQLite instead of PostgreSQL means some SQL functions differ.
- There is no incremental materialisation or lineage graph UI.

The implementation inventory includes 24 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `main.py`
- `models/customer_value.sql`
- `models/daily_revenue.sql`
- `models/mart_customer_segments.sql`
- `models/segment_summary.sql`
- `models/staging_orders.sql`
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
