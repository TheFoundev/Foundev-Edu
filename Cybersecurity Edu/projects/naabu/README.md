# Naabu

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Naabu

A TCP connect port scanner with port range parsing.

> A fast Go port scanner that demonstrates asynchronous SYN scanning and pipeline-friendly output for reconnaissance tooling.

## Overview

An original, self-contained implementation of the **Naabu** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Port list and range parsing
- Concurrent TCP connect scans with timeouts
- Open, closed and filtered classification
- JSON results and a short summary

## Stack

`Go`
The CSV stack is Go. Raw SYN scans need privileges and libpcap, so this build uses TCP connect scans from the standard library.

## Run

```bash
go run . -host 127.0.0.1 -ports 22,80,8000-8010
go test ./...
```

## Structure

```text
naabu/
├── main.go                scanner CLI
├── scanner.go             port parsing and connect scan
├── scanner_test.go        unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

5 tests (`go test ./...`), up from 2: the hosts, the networks and the ports.


## Notes and limitations

- Connect scans are slower and noisier than SYN scans.
- Only IPv4 host names are supported.
- There is no service fingerprinting or OS detection.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production service; the notes above list the missing pieces.

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Port list and range parsing
- Concurrent TCP connect scans with timeouts
- Open, closed and filtered classification
- JSON results and a short summary
- Connect scans are slower and noisier than SYN scans.
- Only IPv4 host names are supported.
- There is no service fingerprinting or OS detection.

The implementation inventory includes 17 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `go.mod`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `go.mod`
- `main.go`
- `scanner.go`
- `scanner_test.go`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: scanner_test.go. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
