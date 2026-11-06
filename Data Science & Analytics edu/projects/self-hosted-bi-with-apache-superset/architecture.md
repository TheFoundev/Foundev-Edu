# Architecture and source map

## Repository evidence

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

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # Self-Hosted BI with Apache Superset
> 
> A small SQL-driven BI warehouse and dashboard.
> 
> > Deploy and model a multi-dataset BI portal in Apache Superset with roles, SQL Lab, datasets and embedded dashboards.
> 
> ## Overview
> 
> An original, self-contained implementation of the **Self-Hosted BI with Apache Superset** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.
> 
> ## Features
> 
> - SQLite warehouse with customers and orders
> - Monthly revenue, top products, region mix and repeat-rate SQL
> - Saved dashboard JSON and a revenue chart
> - Read-only Flask BI page
> 
> ## Stack
> 
> `Python; Flask; Matplotlib; NumPy; Pandas`
> The CSV stack is Python + Flask + Matplotlib + NumPy + Pandas. Superset is not installed, so the saved queries run against SQLite and a small Flask page renders the results.
> 
> ## Run
> 
> ```bash
> pip install -r requirements.txt
> python main.py run
> python app.py
> python main.py demo
> pytest -q
> ```
> 
> ## Structure
> 
> ```text
> self-hosted-bi-with-apache-superset/
> ├── main.py                 pipeline CLI
> ├── src/pipeline.py         data pipeline
> ├── tests/test_pipeline.py  smoke test
> ├── requirements.txt
> ├── sql/*.sql                 saved BI queries
> ├── app.py                    Flask BI page
> ```
> 
> ## Testing
> 
> ```bash
> pytest -q
> ```
> 
> 4 tests (`pytest -q`), up from 2.
> 
> 
> ## Notes and limitations
> 
> - There is no Superset installation, metadata database or chart editor.
> - The warehouse is populated with synthetic orders.
> - The dashboard layout is hard-coded around four saved queries.
> 
> ## License
> 
> Apache-2.0. See `LICENSE`.
> 
> ## About the scope
> 
> This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.
> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
