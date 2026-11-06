# Sqlite Like Database Engine

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# SQLite-like Database Engine

A small sorted key-value store with a binary file format.

> A step-by-step C implementation of a SQLite-like database covering a REPL, B-tree and persistence.

## Overview

An original, self-contained implementation of the **SQLite-like Database Engine** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Sorted key array with binary-search lookup
- Insert, overwrite, delete and scan
- Length-prefixed binary persistence
- Command line shell for put, get and delete

## Stack

`C; POSIX`
The CSV stack is C + POSIX. This build keeps an in-memory sorted table and persists it to a file; the index is an array rather than a full B-tree.

## Run

```bash
make
./build/app
make test
```

## Structure

```text
sqlite-like-database-engine/
├── src/db.c               sorted table and file format
├── src/db.h               public API
├── src/main.c             command line shell
├── tests/test_main.c      unit tests
└── Makefile
```

## Testing

```bash
make test
```

4 tests (`make test`), up from 2: the values, the delete, a key that is not there and the database that is written and read back.


## Notes and limitations

- There are no transactions, pages or write-ahead logging.
- The whole table is rewritten on save, so it is not suitable for large data.
- Concurrency and crash recovery are out of scope.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project. The build and tests run locally

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Sorted key array with binary-search lookup
- Insert, overwrite, delete and scan
- Length-prefixed binary persistence
- Command line shell for put, get and delete
- There are no transactions, pages or write-ahead logging.
- The whole table is rewritten on save, so it is not suitable for large data.
- Concurrency and crash recovery are out of scope.

The implementation inventory includes 14 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Makefile`
- `README.md`
- `src/db.c`
- `src/db.h`
- `src/main.c`
- `tests/test_main.c`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: tests/test_main.c. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
