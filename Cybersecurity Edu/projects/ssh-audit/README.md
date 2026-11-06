# Ssh Audit

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# ssh-audit

Parse an SSH key-exchange packet and flag weak algorithms.

> An SSH server and client configuration auditor that reveals weak key exchange and cipher choices.

## Overview

An original, self-contained implementation of the **ssh-audit** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Fake SSH server that sends banner and KEXINIT
- Binary SSH packet reader
- Weak algorithm checks against a small blocklist
- Grade and JSON report

## Stack

`Python`
The CSV stack is Python. No SSH library is installed, so the project implements the identification and KEXINIT parsing directly for a local fake server.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
ssh-audit/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

**The good server of the test was not good.** It offered `diffie-hellman-group14-sha1`, which is on the weak list, so the audit found a finding in a server that should be clean. The fixture now offers the modern key exchange only.
- 6 tests (`pytest -q`), up from 2: the encoding, the parsing and the audit of a good and a weak server.


## Notes and limitations

- Only the banner and first KEXINIT packet are inspected.
- The fake server is a local test fixture, not a real SSH daemon.
- Host key algorithms are reported but no

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Fake SSH server that sends banner and KEXINIT
- Binary SSH packet reader
- Weak algorithm checks against a small blocklist
- Grade and JSON report
- 6 tests (`pytest -q`), up from 2: the encoding, the parsing and the audit of a good and a weak server.
- Only the banner and first KEXINIT packet are inspected.
- The fake server is a local test fixture, not a real SSH daemon.
- Host key algorithms are reported but not cryptographically verified.

The implementation inventory includes 17 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

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
