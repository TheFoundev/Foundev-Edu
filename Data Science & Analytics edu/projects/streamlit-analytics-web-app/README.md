# Streamlit Analytics Web App

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Streamlit Analytics Web App

A filterable subscription analytics app without Streamlit.

> Ship a self-service analytics web app with file uploads, filters, charts and shareable reports written entirely in Python.

## Overview

An original, self-contained implementation of the **Streamlit Analytics Web App** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A Streamlit page with filters for the segment, the region and the months
- The MRR, the ARR, the active customers, the average fee, the churn and the
  net revenue retention, with the definitions written down
- The revenue of every month, with the new and the churned customers
- A cohort table: how much of every cohort is still there
- A chart of the revenue by segment
- The table of the customers and a download of it

## Stack

`Python; Streamlit; Pandas; Plotly`

The CSV stack is Streamlit + Pandas, and that is what the project uses: the
page is a Streamlit app, the data comes from a file that is read once and
cached, and the numbers are worked out in `src/pipeline.py` where they can be
tested.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
python main.py demo
pytest -q
```



## Structure

```text
streamlit-analytics-web-app/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── app.py                  the Streamlit page
```

## Testing

```bash
pytest -q
```

15 tests: a s

## Actual features and limits

README feature statements (verify each against code before relying on it):
- A Streamlit page with filters for the segment, the region and the months
- The MRR, the ARR, the active customers, the average fee, the churn and the
- The revenue of every month, with the new and the churned customers
- A cohort table: how much of every cohort is still there
- A chart of the revenue by segment
- The table of the customers and a download of it
- The app is not reactive like Streamlit; filters submit a form.
- Data is generated once per run and stored as CSV.
- There are no charts or user accounts.

The implementation inventory includes 19 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `README.md`
- `app.py`
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
