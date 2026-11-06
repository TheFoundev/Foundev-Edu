# Distributed Tracing and APM Platform

## Overview and purpose

A Go in-memory span store groups traces, computes duration/error summaries and service latency percentiles, and exposes JSON handlers.

## Real-world context

Understand span relationships and aggregation while distinguishing a custom tracing demo from an interoperable OpenTelemetry backend.

## Implemented features

Span model/store, trace assembly, p50/p95, custom JSON ingestion, stats and trace lookup handlers.

## Source findings and limitations

- No persistence, sampling, context propagation, or OpenTelemetry SDK/exporter.
- OTLPHandler expects a custom JSON structure and is not mounted in main.go; it is not OTLP JSON/Protobuf compatible.
- Percentile uses floor(p/100*(n-1)) and does not validate p bounds.
- StatsHandler and TraceHandler write JSON without consistent content-type/status helpers.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, net/http, JSON, in-memory store. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

JSON spans → append to memory → group by TraceID → derive root/errors/duration → group by service → calculate percentiles.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 8. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
