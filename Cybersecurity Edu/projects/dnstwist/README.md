# Dnstwist

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# dnstwist

Generate typosquatting candidates and check whether they resolve.

> A domain permutation engine that detects typosquatting and brand-impersonation phishing domains.

## Overview

An original, self-contained implementation of the **dnstwist** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The permutations of a domain: a letter left out, a letter written twice,
  the keyboard next door, the homoglyphs, two letters swapped and the other
  top level domains
- The lookup of a host runs in a thread with the time it may take, so the
  timeout belongs to the call and not to the whole process
- The candidates are looked up at the same time, so a hundred of them do not
  take minutes
- The report of every candidate

## Stack

`Python`
The CSV stack is Python. The standard library resolver is used instead of a DNS library, so probes are simple A lookups and there is no WHOIS or certificate data.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
dnstwist/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

12 tests: the permutations (a letter left out, a letter written twice, the
keyboard, the homoglyphs, two letters swapped, the other top level domains),
that the timeout of the lookup d

## Actual features and limits

README feature statements (verify each against code before relying on it):
- The permutations of a domain: a letter left out, a letter written twice,
- The lookup of a host runs in a thread with the time it may take, so the
- The candidates are looked up at the same time, so a hundred of them do not
- The report of every candidate
- DNS probes need network access; offline runs report every candidate as unresolved.
- There is no WHOIS, TLS certificate or screenshot enrichment.
- Homoglyphs are a short hard-coded map, not a full Unicode confusables list.

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
