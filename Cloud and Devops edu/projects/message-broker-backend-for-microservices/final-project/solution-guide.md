# Mentor Solution Guide

## Source findings

The project implements: Supervisor tree, connection/topology, publisher confirms/idempotency, consumer prefetch/settlement, order pipeline, retry TTL queues, DLQ, HTTP endpoints, metrics.

Review known limitations:
- Inventory/payment/fulfillment are deterministic simulations in mbb_order, not real services.
- RabbitMQ topology and Docker Compose must be checked against actual environment; README is detailed but tests are unit-focused.
- Retry TTL ladder can produce delayed retries and duplicate processing; idempotency behavior must be understood.
- Credentials/config must be changed before any exposed broker deployment.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
