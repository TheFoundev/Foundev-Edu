# Gophish

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# GoPhish

Plan a phishing-awareness campaign and score the results.

> An open-source phishing simulation platform used to run authorised awareness campaigns and staff training.

## Overview

An original, self-contained implementation of the **GoPhish** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Campaign and target models with unique tracking IDs
- Simulated send, open, click and report events
- Per-campaign statistics and rates
- JSON export for a training report

## Stack

`Go`
The CSV stack is Go. This build stores campaigns in memory and simulates delivery, so no mail server, database or tracking web server is required.

## Run

```bash
go run . -targets ana@example.com,bo@example.com
go test ./...
```

## Structure

```text
gophish/
├── main.go                campaign CLI
├── campaign.go            campaign and funnel logic
├── campaign_test.go       unit tests
└── go.mod
```

## Testing

```bash
go test ./...
```

5 tests: the tracking ids, the empty targets, the funnel, the rates and the
unknown tracking id.

## Notes and limitations

- No email is actually sent; events are recorded manually or from the demo.
- The tracking IDs are random strings, not signed tokens.
- Data is not persisted between runs.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project written in Go with the standard library only. It is not a hardened production se

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Campaign and target models with unique tracking IDs
- Simulated send, open, click and report events
- Per-campaign statistics and rates
- JSON export for a training report
- No email is actually sent; events are recorded manually or from the demo.
- The tracking IDs are random strings, not signed tokens.
- Data is not persisted between runs.

The implementation inventory includes 16 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `go.mod`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `campaign.go`
- `campaign_test.go`
- `go.mod`
- `main.go`
- `web/api_impl.py`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: campaign_test.go. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
