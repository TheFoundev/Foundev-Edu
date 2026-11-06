# Uptime and Status Monitoring Service

## Overview and purpose

A Node.js app uses SQLite and scheduled HTTP GET checks to track monitors and alert on status transitions.

## Real-world context

Understand monitoring records, polling, transitions, persistence, notification delivery, and the difference between HTTP checks and broader monitoring claims.

## Implemented features

SQLite database, monitor check function, interval scheduler, transition notifications/webhooks, JSON API, polling dashboard.

## Source findings and limitations

- README claims TCP, DNS, TLS expiry, and content matching in the aspirational brief; implementation notes say checks are HTTP GET only.
- Dashboard polls; no WebSocket push.
- Notifications and multi-node deployment are limited/out of scope; verify exact retry/alert behavior in source.
- SQLite requires a supported Node runtime; runtime version and database feature support must be checked.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Node.js, node:sqlite, HTTP, node:test. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Monitor config → scheduled HTTP GET → check result/latency → persisted status/history → transition alert → API/dashboard.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 8. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
