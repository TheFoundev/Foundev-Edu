# Cron Dead-Man-Switch Monitoring

## Overview and purpose

A Django heartbeat monitor tracks scheduled jobs, late/down transitions, status endpoints, and alert dispatch.

## Real-world context

Understand heartbeat monitoring, simplified schedule parsing, state transitions, authentication, polling, persistence, and notification delivery.

## Implemented features

Check/Ping/AlertChannel/Alert models, cron-like parser, ping/status and CRUD APIs, token checks, background poller, alert channels.

## Source findings and limitations

- The schedule parser supports a simplified format, not full cron grammar.
- The separate poller must run to detect missed pings; the web process alone is not the scheduler.
- UUID ping URLs are bearer-like secrets; anyone who learns one can spoof a heartbeat.
- Webhook/email delivery and retry guarantees must be checked in core/dispatch.py.
- Production authentication, rate limits, and database operations require operational review.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Python, Django, SQLite/PostgreSQL, HTTP webhooks, Docker Compose. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Scheduled job pings → database/state update → poller evaluates deadline → transition to late/down/up → deduplicated alerts → API/UI status.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 10. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
