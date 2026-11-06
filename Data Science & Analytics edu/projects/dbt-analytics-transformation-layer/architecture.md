# Architecture and source map

## Repository evidence

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

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # dbt Analytics Transformation Layer
> 
> A mini SQL transformation runner with dbt-style refs and models.
> 
> > Develop an analytics-engineering project that transforms raw event data into documented, tested dimensional models using dbt.
> 
> ## Overview
> 
> An original, self-contained implementation of the **dbt Analytics Transformation Layer** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.
> 
> ## Features
> 
> - The models are ordered by the `{{ ref() }}` calls in the SQL files, not by
>   a list that is written by hand
> - A model that needs a model that is not there, and a cycle, are errors
> - The manifest says which model depends on which
> - The raw tables and the models are materialised into SQLite
> 
> ## Stack
> 
> `Python; NumPy; Pandas`
> The CSV stack is Python + NumPy + Pandas. dbt is not installed, so a small local runner resolves refs and materialises the SQL models in SQLite.
> 
> ## Run
> 
> ```bash
> pip install -r requirements.txt
> python main.py run
> python main.py demo
> pytest -q
> ```
> 
> ## Structure
> 
> ```text
> dbt-analytics-transformation-layer/
> ├── main.py                 pipeline CLI
> ├── src/pipeline.py         data pipeline
> ├── tests/test_pipeline.py  smoke test
> ├── requirements.txt
> ├── models/*.sql             staging and mart SQL models
> ```
> 
> ## Testing
> 
> ```bash
> pytest -q
> ```
> 
> 9 tests: the models of the directory, the order that comes from the refs, a
> model that is missing, a cycle, the dependencies of a model, the manifest and
> the revenue of the day.
> 
> ## Notes and limitations
> 
> - The runner supports only simple refs, not Jinja, macros or tests.
> - SQLite instead of PostgreSQL means some SQL functions differ.
> - There is no incremental materialisation or lineage graph UI.
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
