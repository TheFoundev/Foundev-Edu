# Event Streaming Platform (Kafka-lite)

## Overview and purpose

A Java/Kafka clickstream pipeline validates schemas, runs Kafka Streams aggregations, and serves materialized views.

## Real-world context

Trace events through schema validation, Kafka topics, stream processing, state stores, and query APIs while distinguishing the local fake registry from a real registry.

## Implemented features

Producer, registry client/fake registry, schema validation and DLQ, Kafka Streams topology, windows/sessionization, view server, dashboard.

## Source findings and limitations

- This project uses real Kafka components but has an in-process fake registry option; behavior differs between all-local smoke mode and full Compose stack.
- README describes exactly-once semantics; inspect the actual Streams configuration and transaction guarantees before claiming end-to-end exactly once.
- Dashboard may require serving on the same origin or adjusting fetch URLs; opening the file directly is not the same as serving it.
- Schema registry/client compatibility and Compose health/startup behavior need environment verification.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Java, Apache Kafka 3.7.0, Kafka Streams, Schema Registry, Docker Compose, JUnit. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

ClickProducer → clicks topic → schema validation/deserializer → ClicksStreamsApp → aggregates/state stores → ViewServer/dashboard; invalid messages route to DLQ.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 12. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
