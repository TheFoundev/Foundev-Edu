# Metrics Monitoring and Alerting Platform

## Overview and purpose

A Go in-memory time-series store accepts samples, calculates simple window queries, evaluates threshold alerts, and emits Prometheus text.

## Real-world context

Understand sample timestamps, windows, rate/sum/average, alert duration, and the limits of a tiny metrics engine.

## Implemented features

Sample store, time-window selection, rate/sum/average, alert rules with for-duration, JSON handlers, Prometheus exporter.

## Source findings and limitations

- No PromQL parser or Prometheus scrape integration; samples are pushed into this process.
- Samples are in memory and not persisted.
- Alerts are logged, not delivered to Alertmanager.
- Rate formula and alert pending-duration behavior are the project's simplified semantics, not full Prometheus semantics.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, HTTP JSON, Prometheus text exposition. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Ingest Sample → store → select window at query time → aggregate → evaluate rule state → JSON or exposition response.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 7. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
