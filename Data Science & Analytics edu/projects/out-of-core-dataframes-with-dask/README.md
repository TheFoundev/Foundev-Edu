# Out Of Core Dataframes With Dask

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Out-of-Core Dataframes with Dask

Process a large CSV in chunks without holding it all in memory.

> Analyse a multi-gigabyte public dataset out of core with Dask dataframes, parallel group-bys and a results dashboard.

## Overview

An original, self-contained implementation of the **Out-of-Core Dataframes with Dask** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Partitioned synthetic order files
- Chunked pandas reads with partial aggregation
- Merged summary written to Parquet
- Memory-friendly top-product report

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Dask is not installed, so this build uses chunked pandas reads and writes the aggregate to Parquet.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
out-of-core-dataframes-with-dask/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

4 tests (`pytest -q`), up from 2.


## Notes and limitations

- The chunked loop is a small subset of Dask's scheduler and expression graph.
- Data is synthetic and fits comfortably on a laptop.
- There is no dashboard; the summary is written to disk.

## License

BSD-3-Clause. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Partitioned synthetic order files
- Chunked pandas reads with partial aggregation
- Merged summary written to Parquet
- Memory-friendly top-product report
- The chunked loop is a small subset of Dask's scheduler and expression graph.
- Data is synthetic and fits comfortably on a laptop.
- There is no dashboard; the summary is written to disk.

The implementation inventory includes 30 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

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
