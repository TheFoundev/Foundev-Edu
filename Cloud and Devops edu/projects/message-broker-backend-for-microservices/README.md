# Message Broker Backend for Microservices

## Overview and purpose

An Erlang/OTP service accepts orders over HTTP, publishes to RabbitMQ, runs a retryable processing pipeline, and exposes metrics.

## Real-world context

Understand supervision, AMQP topology, confirms, consumer acknowledgements, retry ladders, dead letters, and observability.

## Implemented features

Supervisor tree, connection/topology, publisher confirms/idempotency, consumer prefetch/settlement, order pipeline, retry TTL queues, DLQ, HTTP endpoints, metrics.

## Source findings and limitations

- Inventory/payment/fulfillment are deterministic simulations in mbb_order, not real services.
- RabbitMQ topology and Docker Compose must be checked against actual environment; README is detailed but tests are unit-focused.
- Retry TTL ladder can produce delayed retries and duplicate processing; idempotency behavior must be understood.
- Credentials/config must be changed before any exposed broker deployment.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Erlang/OTP, RabbitMQ, AMQP, Docker Compose, Prometheus. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

HTTP order → publisher/exchange → queue → consumer pipeline → ack/retry/DLQ; broker state and health feed HTTP/metrics endpoints.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 12. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
