# Architecture

## Implemented system

Supervisor tree, connection/topology, publisher confirms/idempotency, consumer prefetch/settlement, order pipeline, retry TTL queues, DLQ, HTTP endpoints, metrics.

## Data and control flow

HTTP order → publisher/exchange → queue → consumer pipeline → ack/retry/DLQ; broker state and health feed HTTP/metrics endpoints.

## Module source map

- **OTP Application and Supervision:** mbb_sup supervises connection, consumer, metrics, and HTTP workers.
- **Manage AMQP Connection and Reconnect:** Connection module owns connection/channel and re-declares topology after reconnect.
- **Declare Exchanges, Queues, and Bindings:** Project defines orders exchange, process/retry/DLQ queues, and service queues.
- **Publish with Confirms and Idempotency:** Publisher uses confirms and order idempotency key as described by README.
- **Consume with Prefetch and Settlement:** Consumer classifies outcomes and settles deliveries; pipeline returns ok/retry/dead_letter.
- **Process and Classify Orders:** validate → reserve inventory → charge → fulfil; integrations are simulated deterministically.
- **Retry Ladder and Dead-Letter Queue:** Retry TTL grows as base × 4^(N-1); x-retry-count and max_retries govern exhaustion.
- **Expose Health, Readiness, and Metrics:** README lists /health, /ready, /metrics, /orders.
- **Run and Configure the Broker Stack:** README specifies broker, schema/config, HTTP, and dashboard/run configuration.
- **Test Failure Paths and Duplication:** Tests cover order outcomes, metrics, and retries; broker integration should be run separately.
- **Inspect Operational and Security Limits:** The process/1 function uses deterministic inventory and charge functions; they stand in for real network service adapters.
- **Build a Safe Local Verification Plan:** README documents rebar tests, Compose stack, and limitations.

## Boundaries and risks

- Inventory/payment/fulfillment are deterministic simulations in mbb_order, not real services.
- RabbitMQ topology and Docker Compose must be checked against actual environment; README is detailed but tests are unit-focused.
- Retry TTL ladder can produce delayed retries and duplicate processing; idempotency behavior must be understood.
- Credentials/config must be changed before any exposed broker deployment.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
