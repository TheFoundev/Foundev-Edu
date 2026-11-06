# Airflow Scheduled Etl Dags

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Airflow Scheduled ETL DAGs

A dependency-ordered orders ETL job with a tiny Airflow-style DAG.

> Design, deploy and monitor scheduled ETL DAGs with Apache Airflow including backfills, sensors, SLAs and alerting.

## Overview

An original, self-contained implementation of the **Airflow Scheduled ETL DAGs** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A real Airflow DAG in `dags/orders_dag.py`, with the tasks, their
  dependencies, the retries and the schedule
- The local runner does the same work, so the pipeline runs without Airflow
- The order of the tasks comes from the dependency graph, not from the order
  they are written in
- A task that fails is retried, and the tasks that already ran are marked
  as rolled back
- The history of every run in the warehouse: the task, the state, the rows,
  the time and when it finished

## Stack

`Python; Airflow; Docker; PostgreSQL`

The CSV stack is Airflow + Docker + PostgreSQL. This build replaces the scheduler and database with a local runner and SQLite while keeping the same four-stage order pipeline.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
airflow-scheduled-etl-dags/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── dags/orders_dag.py       DAG metadata
```

## Testing

```bash
pytest -q
```

13 tests: the order

## Actual features and limits

README feature statements (verify each against code before relying on it):
- A real Airflow DAG in `dags/orders_dag.py`, with the tasks, their
- The local runner does the same work, so the pipeline runs without Airflow
- The order of the tasks comes from the dependency graph, not from the order
- A task that fails is retried, and the tasks that already ran are marked
- The history of every run in the warehouse: the task, the state, the rows,
- There is no scheduler daemon, worker pool or Airflow UI.
- SQLite stands in for PostgreSQL and the raw file lands on local disk.
- Failures stop the run; retries and backfills are not implemented.

The implementation inventory includes 21 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `README.md`
- `dags/orders_dag.py`
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
