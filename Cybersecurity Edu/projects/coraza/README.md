# Coraza

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Coraza

A small web application firewall that inspects requests against rules.

> An open-source Web Application Firewall engine that is embedded to filter HTTP traffic in real time.

## Overview

An original, self-contained implementation of the **Coraza** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Regex rules for SQL injection, XSS, traversal and scanners
- Per-request findings with severity and evidence
- Allow or block decision with a score
- Command line inspection and JSON output

## Stack

`Go`
The CSV stack is Go. This build implements a compact rule engine with Go's regexp package instead of loading the full OWASP Core Rule Set.

## Run

```bash
go run . -path /items -query 'id=1 union select 1'
go test ./...
```

## Structure

```text
coraza/
├── main.go                request inspection CLI
├── waf.go                 rules and decision logic
├── waf_test.go            unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

5 tests (`go test ./...`), up from 2: the middleware, a suspicious request, a request that is written with escapes, the body and the request that is looked at.


## Notes and limitations

- The rule set is tiny and will miss most real attacks.
- Requests are inspected as strings; there is no HTTP middleware or body streaming.
- There is no anomaly scoring across sessions or rule tuning.

## License

Apache-2.0. See `LICENSE`.

## About the

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Regex rules for SQL injection, XSS, traversal and scanners
- Per-request findings with severity and evidence
- Allow or block decision with a score
- Command line inspection and JSON output
- The rule set is tiny and will miss most real attacks.
- Requests are inspected as strings; there is no HTTP middleware or body streaming.
- There is no anomaly scoring across sessions or rule tuning.

The implementation inventory includes 17 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `go.mod`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `go.mod`
- `main.go`
- `waf.go`
- `waf_test.go`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: waf_test.go. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
