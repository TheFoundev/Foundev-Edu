# Memory Allocator From Scratch

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Memory Allocator from Scratch

A malloc replacement built on mmap with a coalescing free list.

> A thread-safe malloc/free replacement in C that demonstrates free-list design and fragmentation handling.

## Overview

An original, self-contained implementation of the **Memory Allocator from Scratch** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Single mmap arena with 16-byte alignment
- First-fit allocation and block splitting
- Coalescing free list to limit fragmentation
- realloc, calloc and allocation statistics

## Stack

`C; POSIX`
The CSV stack is C + POSIX. This build implements the allocator with mmap and a free list; there is no thread-local cache or arena per thread.

## Run

```bash
make
./build/app
make test
```

## Structure

```text
memory-allocator-from-scratch/
├── src/allocator.c        mmap allocator implementation
├── src/allocator.h        public API
├── src/main.c             demo program
├── tests/test_main.c      unit tests
└── Makefile
```

## Testing

```bash
make test
```

5 tests (`make test`), up from 2: the allocation, the zeroed memory, the reallocation, the end of the arena and the free of nothing.


## Notes and limitations

- The arena is fixed at four megabytes and never grows.
- There is no locking, so it is not safe across threads.
- Fragmentation handling is a simple first fit with coalescing.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project. The build and test

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Single mmap arena with 16-byte alignment
- First-fit allocation and block splitting
- Coalescing free list to limit fragmentation
- realloc, calloc and allocation statistics
- The arena is fixed at four megabytes and never grows.
- There is no locking, so it is not safe across threads.
- Fragmentation handling is a simple first fit with coalescing.

The implementation inventory includes 14 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Makefile`
- `README.md`
- `src/allocator.c`
- `src/allocator.h`
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
