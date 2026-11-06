# Self Hosted Bi With Apache Superset

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Self-Hosted BI with Apache Superset

A small SQL-driven BI warehouse and dashboard.

> Deploy and model a multi-dataset BI portal in Apache Superset with roles, SQL Lab, datasets and embedded dashboards.

## Overview

An original, self-contained implementation of the **Self-Hosted BI with Apache Superset** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- SQLite warehouse with customers and orders
- Monthly revenue, top products, region mix and repeat-rate SQL
- Saved dashboard JSON and a revenue chart
- Read-only Flask BI page

## Stack

`Python; Flask; Matplotlib; NumPy; Pandas`
The CSV stack is Python + Flask + Matplotlib + NumPy + Pandas. Superset is not installed, so the saved queries run against SQLite and a small Flask page renders the results.

## Run

```bash
pip install -r requirements.txt
python main.py run
python app.py
python main.py demo
pytest -q
```

## Structure

```text
self-hosted-bi-with-apache-superset/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── sql/*.sql                 saved BI queries
├── app.py                    Flask BI page
```

## Testing

```bash
pytest -q
```

4 tests (`pytest -q`), up from 2.


## Notes and limitations

- There is no Superset installation, metadata database or chart editor.
- The warehouse is populated with synthetic orders.
- The dashboard layout is hard-coded around four saved queries.

## L

## Actual features and limits

README feature statements (verify each against code before relying on it):
- SQLite warehouse with customers and orders
- Monthly revenue, top products, region mix and repeat-rate SQL
- Saved dashboard JSON and a revenue chart
- Read-only Flask BI page
- There is no Superset installation, metadata database or chart editor.
- The warehouse is populated with synthetic orders.
- The dashboard layout is hard-coded around four saved queries.

The implementation inventory includes 18 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
- `sql/monthly_revenue.sql`
- `sql/region_share.sql`
- `sql/repeat_rate.sql`
- `sql/top_products.sql`
- `src/__init__.py`
- `src/pipeline.py`
- `tests/test_pipeline.py`
- `web/assets/app.js`

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
