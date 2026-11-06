# Owasp Nodegoat

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# OWASP NodeGoat

A deliberately insecure web app for practising OWASP-style attacks.

> A deliberately insecure Node.js application for learning server-side JavaScript security through guided tutorials.

## Overview

An original, self-contained implementation of the **OWASP NodeGoat** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Login with weak default credentials and a forgeable role cookie
- Search endpoint with a simulated injection flaw
- Unescaped reflected and stored input for XSS practice
- Broken access control on user and admin endpoints

## Stack

`Node.js`
The CSV stack is Node.js.js + Express + MongoDB. This build uses only node:http and in-memory arrays so it runs without a database; the vulnerabilities are kept on purpose.

## Run

```bash
npm start
npm test
```

## Structure

```text
owasp-nodegoat/
├── src/app.js              intentionally vulnerable routes
├── src/store.js            in-memory users and comments
├── src/server.js           server entry point
├── test/app.test.js        checks for each flaw
└── package.json
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- This app is intentionally insecure. Never expose it to a network.
- It is a teaching target, not a template for real applications.
- Persistence is in memory and resets when the process exits.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project. It targets Node's built-in modules

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Login with weak default credentials and a forgeable role cookie
- Search endpoint with a simulated injection flaw
- Unescaped reflected and stored input for XSS practice
- Broken access control on user and admin endpoints
- This app is intentionally insecure. Never expose it to a network.
- It is a teaching target, not a template for real applications.
- Persistence is in memory and resets when the process exits.

The implementation inventory includes 15 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `package.json`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `package.json`
- `src/app.js`
- `src/server.js`
- `src/store.js`
- `test/app.test.js`
- `test/hardened.test.js`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: test/app.test.js, test/hardened.test.js. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
