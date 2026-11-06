# Signal Style E2ee Chat

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Signal-style E2EE Chat

A chat relay where the server only sees encrypted envelopes.

> An educational end-to-end encrypted chat that implements core Signal Protocol ideas over WebSockets.

## Overview

An original, self-contained implementation of the **Signal-style E2EE Chat** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- X25519 key exchange with HKDF-derived session keys
- AES-256-GCM encryption with authenticated tags
- Hand-rolled WebSocket relay that forwards opaque envelopes
- Browser client that shares a room passphrase for end-to-end encryption

## Stack

`Node.js`
The CSV stack is Node.js.js + WebSockets + libsignal. libsignal is not available, so the project uses node:crypto X25519 and AES-GCM; it is not the Signal protocol and there is no double ratchet.

## Run

```bash
npm start
npm test
```

## Structure

```text
signal-style-e2ee-chat/
├── src/crypto.js           X25519 and AES-GCM helpers
├── src/ws.js               minimal WebSocket server
├── src/server.js            static files and the relay
├── public/index.html        chat page
├── public/app.js            browser key derivation and encryption
├── test/                    crypto and relay tests
└── package.json
```

## Testing

```bash
# see the Run section
```

## Notes and limitations

- There is no forward secrecy per message, prekey bundle or group session.
- The room passphrase is typed into the browser; key distribution is manual.
- The relay keeps no history a

## Actual features and limits

README feature statements (verify each against code before relying on it):
- X25519 key exchange with HKDF-derived session keys
- AES-256-GCM encryption with authenticated tags
- Hand-rolled WebSocket relay that forwards opaque envelopes
- Browser client that shares a room passphrase for end-to-end encryption
- There is no forward secrecy per message, prekey bundle or group session.
- The room passphrase is typed into the browser; key distribution is manual.
- The relay keeps no history and stores nothing, but it is not audited.

The implementation inventory includes 12 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `package.json`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `package.json`
- `public/app.js`
- `src/crypto.js`
- `src/server.js`
- `src/ws.js`
- `test/crypto.test.js`
- `test/relay.test.js`

## Testing

Test-related paths found: test/crypto.test.js, test/relay.test.js. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
