# Architecture and source map

## Repository evidence

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

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> # ssh-audit
> 
> Parse an SSH key-exchange packet and flag weak algorithms.
> 
> > An SSH server and client configuration auditor that reveals weak key exchange and cipher choices.
> 
> ## Overview
> 
> An original, self-contained implementation of the **ssh-audit** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.
> 
> ## Features
> 
> - Fake SSH server that sends banner and KEXINIT
> - Binary SSH packet reader
> - Weak algorithm checks against a small blocklist
> - Grade and JSON report
> 
> ## Stack
> 
> `Python`
> The CSV stack is Python. No SSH library is installed, so the project implements the identification and KEXINIT parsing directly for a local fake server.
> 
> ## Run
> 
> ```bash
> pip install -r requirements.txt
> python main.py run
> python main.py demo
> pytest -q
> ```
> 
> ## Structure
> 
> ```text
> ssh-audit/
> ├── main.py                 pipeline CLI
> ├── src/pipeline.py         data pipeline
> ├── tests/test_pipeline.py  smoke test
> ├── requirements.txt
> ```
> 
> ## Testing
> 
> ```bash
> pytest -q
> ```
> 
> **The good server of the test was not good.** It offered `diffie-hellman-group14-sha1`, which is on the weak list, so the audit found a finding in a server that should be clean. The fixture now offers the modern key exchange only.
> - 6 tests (`pytest -q`), up from 2: the encoding, the parsing and the audit of a good and a weak server.
> 
> 
> ## Notes and limitations
> 
> - Only the banner and first KEXINIT packet are inspected.
> - The fake server is a local test fixture, not a real SSH daemon.
> - Host key algorithms are reported but not cryptographically verified.
> 
> ## License
> 
> MIT. See `LICENSE`.
> 
> ## About the scope
> 
> This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.
> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
