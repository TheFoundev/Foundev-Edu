# Cowrie

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Cowrie

A tiny SSH-style honeypot that records login attempts and commands.

> A medium-interaction SSH and Telnet honeypot that records attacker behaviour for defensive research.

## Overview

An original, self-contained implementation of the **Cowrie** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A honeypot that answers a line-based shell: the files of a small fake
  system can be read and the directories listed
- The events of every session are collected by the server with a lock, so two
  sessions never write into the same list
- A session that says nothing is closed instead of being kept open
- The log of every session: the user, the password and every command

## Stack

`Python`
The CSV stack is Python. Twisted is not installed, so the server uses the standard library socket server and the project runs directly on the host.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
cowrie/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
```bash
pytest -q
```

8 tests: the answers of the honeypot, the files and the directories of the
fake system, that the events of two sessions do not mix, that the log holds
the logins, the passwords and the commands, and that a session ends when the
client stops ta

## Actual features and limits

README feature statements (verify each against code before relying on it):
- A honeypot that answers a line-based shell: the files of a small fake
- The events of every session are collected by the server with a lock, so two
- A session that says nothing is closed instead of being kept open
- The log of every session: the user, the password and every command
- The protocol is a fake line-based shell, not real SSH, so it cannot be logged into with an SSH client.
- Only localhost is used in the demo; there is no container sandbox.
- The log is plain JSONL with no rotation or alerting.

The implementation inventory includes 18 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

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
