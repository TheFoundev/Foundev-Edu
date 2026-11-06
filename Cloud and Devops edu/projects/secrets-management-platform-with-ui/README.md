# Secrets Management Platform with UI

## Overview and purpose

A Node.js app derives a key from a master password, encrypts stored values with AES-256-GCM, exposes a token-protected API, and serves a UI.

## Real-world context

Understand authenticated encryption, key derivation, file storage, API authorization, audit behavior, and demo deployment limits.

## Implemented features

Crypto helper, JSON file SecretStore, single-token API, static UI, node:test suite.

## Source findings and limitations

- Default password is change-me when SECRETS_PASSWORD is absent, and the API token is printed to console at startup.
- One API token provides broad access; no role-based access control or key rotation exists.
- Audit history is capped at 200 records and stored beside secrets; it is not an immutable audit system.
- File writes are direct, not an atomic database transaction; no TLS is provided by the basic Node server.
- Read API reveals plaintext to any holder of the API token.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Node.js, node:crypto, AES-256-GCM, PBKDF2, HTTP JSON API. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

HTTP request with token → SecretStore set/get/delete → PBKDF2-derived key → AES-GCM envelope → JSON file and bounded audit list.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 9. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
