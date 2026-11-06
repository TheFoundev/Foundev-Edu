# Sniffnet

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Sniffnet

Summarise a packet capture from a simple CSV trace.

> A cross-platform network traffic monitor written in Rust that makes packet capture approachable and visual.

## Overview

An original, self-contained implementation of the **Sniffnet** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Capture records parsed from source, destination, protocol and bytes
- Per-protocol byte totals
- Top talkers ranked by bytes
- Library API with unit tests and a small CLI

## Stack

`Rust`
The CSV stack is Rust. This build has no external crates, so it reads a small CSV trace format instead of a live pcap device, and prints a terminal summary instead of a GUI.

## Run

```bash
cargo run --release
cargo test --offline
```

## Structure

```text
sniffnet/
├── src/lib.rs            capture parsing and statistics
├── src/main.rs           command line summary
└── Cargo.toml
```

## Testing

```bash
cargo test
```

7 tests (`cargo test`), up from 3.


## Notes and limitations

- There is no live capture, network interface access or GUI.
- The parser expects four comma-separated fields per line.
- Statistics are simple totals, not time-series or flow analysis.

## License

MIT. See `LICENSE`.

## About the scope

This is a third-year student project in Rust with no external crates. It is not a production implementation; the notes list what was skipped.

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Capture records parsed from source, destination, protocol and bytes
- Per-protocol byte totals
- Top talkers ranked by bytes
- Library API with unit tests and a small CLI
- There is no live capture, network interface access or GUI.
- The parser expects four comma-separated fields per line.
- Statistics are simple totals, not time-series or flow analysis.

The implementation inventory includes 13 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `the repository dependency/configuration files`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `Cargo.lock`
- `Cargo.toml`
- `README.md`
- `src/lib.rs`
- `src/main.rs`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: none identified. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
