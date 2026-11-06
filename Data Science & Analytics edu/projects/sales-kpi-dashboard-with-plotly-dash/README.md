# Sales Kpi Dashboard With Plotly Dash

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Sales KPI Dashboard with Plotly Dash

A small sales KPI dashboard backed by a local warehouse.

> Build an interactive business-intelligence dashboard with callbacks, drill-downs and KPI cards on top of a relational sales dataset.

## Overview

An original, self-contained implementation of the **Sales KPI Dashboard with Plotly Dash** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Ninety days of synthetic sales orders
- Revenue, orders, average order value and growth KPIs
- Top product and region summaries
- Trend chart and a Flask dashboard

## Stack

`Python; Flask; Matplotlib; NumPy; Pandas`
The CSV stack is Python + Flask + Matplotlib + NumPy + Pandas. Dash and PostgreSQL are not installed, so this build computes KPIs with pandas and serves them through Flask.

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
sales-kpi-dashboard-with-plotly-dash/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── app.py                  Flask KPI dashboard
```

## Testing

```bash
pytest -q
```

3 tests (`pytest -q`), up from 2.


## Notes and limitations

- The data is generated locally, not connected to a business system.
- Growth compares the last thirty days with the previous thirty.
- The dashboard is a single page without user accounts or filters.

## License

MIT. S

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Ninety days of synthetic sales orders
- Revenue, orders, average order value and growth KPIs
- Top product and region summaries
- Trend chart and a Flask dashboard
- The data is generated locally, not connected to a business system.
- Growth compares the last thirty days with the previous thirty.
- The dashboard is a single page without user accounts or filters.

The implementation inventory includes 14 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
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
