# Data Quality Gates With Great Expectations

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Data Quality Gates with Great Expectations

Data quality gates over a messy customer export.

> Add an automated data-quality layer that profiles datasets, defines expectation suites and blocks bad loads with generated data docs.

## Overview

An original, self-contained implementation of the **Data Quality Gates with Great Expectations** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Every check is written down once: it says what it looks at and how severe
  it is, and both the number of the failures and the cleaning of the table
  come from it
- The report names the rows that failed and the checks they failed, and it
  holds an example of every failure
- The critical failures and the warnings are counted apart, and only the rows
  of a critical check are thrown away

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Great Expectations is not available, so the quality checks are plain pandas functions and the report is JSON.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
data-quality-gates-with-great-expectations/
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

13 tests: every check on its own, the report that names the rows, the
severities that are counted apart, the cleaned table and the agreeme

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Every check is written down once: it says what it looks at and how severe
- The report names the rows that failed and the checks they failed, and it
- The critical failures and the warnings are counted apart, and only the rows
- The checks are hand-written functions instead of an expectation suite.
- The pipeline does not run inside Airflow.
- The report is JSON; there is no data docs site.

The implementation inventory includes 20 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

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
