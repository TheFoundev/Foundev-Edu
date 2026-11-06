# Distributed Rate Limiter Service

## Overview and purpose

A Go service includes a memory token bucket, Redis fixed-window store, HTTP middleware, trusted-proxy option, and Prometheus text output.

## Real-world context

Compare rate-limiting algorithms, shared storage, client identity, failure policy, and observability.

## Implemented features

Memory token buckets, Redis INCR/PEXPIRE store, key selection, HTTP 429/header middleware, stats exporter, health endpoint.

## Source findings and limitations

- MemoryStore uses token-bucket refill; RedisStore is a fixed-window INCR/PEXPIRE counter, so the storage backends do not implement identical algorithms.
- RedisStore ignores rate during Take; Sweep is a no-op because Redis TTL handles expiry.
- Store errors fail open in Limiter.AllowAt.
- Stats exposes allowed/blocked counters only for MemoryStore; Redis metrics are missing/zero.
- X-Forwarded-For trust is a global boolean, not a trusted-proxy CIDR list.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, HTTP middleware, Redis RESP subset, Prometheus text. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Request → choose API-key/IP key → Store.Take → allow or 429 → update headers/metrics.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 9. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
