# Naivecoin

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Naivecoin

A small proof-of-work blockchain with a peer relay.

> A minimal cryptocurrency implementation with a block explorer UI for learning blockchain internals safely.

## Overview

An original, self-contained implementation of the **Naivecoin** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Transactions and blocks hashed with SHA-256
- Proof-of-work mining with a configurable difficulty
- Chain validation that detects tampering
- Wallet balances derived from the chain
- HTTP API and a hand-rolled WebSocket peer relay

## Stack

`Node.js`
The CSV stack is Node.js.js + WebSockets. Node has no built-in WebSocket server, so the project includes a small RFC 6455 handshake and frame parser instead of the ws package.

## Run

```bash
npm start
node src/main.js
npm test
```

## Structure

```text
naivecoin/
├── src/blockchain.js       blocks, transactions and validation
├── src/ws.js               minimal WebSocket server
├── src/node.js             HTTP API and peer relay
├── src/server.js           server entry point
├── src/main.js             local chain demo
├── test/                   node:test suites
└── package.json
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- There is no consensus fork choice, peer discovery or persistence to disk.
- Transactions are not signed and there is no UTXO model.
- The WebSocket layer is minimal: text frames, ping/pong and close only.

## License

Apache-2.0. See `LICENSE`.

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Transactions and blocks hashed with SHA-256
- Proof-of-work mining with a configurable difficulty
- Chain validation that detects tampering
- Wallet balances derived from the chain
- HTTP API and a hand-rolled WebSocket peer relay
- There is no consensus fork choice, peer discovery or persistence to disk.
- Transactions are not signed and there is no UTXO model.
- The WebSocket layer is minimal: text frames, ping/pong and close only.

The implementation inventory includes 18 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `package.json`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `package.json`
- `src/blockchain.js`
- `src/main.js`
- `src/node.js`
- `src/server.js`
- `src/ws.js`
- `test/blockchain.test.js`
- `test/node.test.js`
- `test/ws.test.js`
- `web/assets/app.js`
- `web/server.py`

## Testing

Test-related paths found: test/blockchain.test.js, test/node.test.js, test/ws.test.js. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
