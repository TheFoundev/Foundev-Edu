# Mentor Solution Guide

## Source findings

The project implements: Producer, registry client/fake registry, schema validation and DLQ, Kafka Streams topology, windows/sessionization, view server, dashboard.

Review known limitations:
- This project uses real Kafka components but has an in-process fake registry option; behavior differs between all-local smoke mode and full Compose stack.
- README describes exactly-once semantics; inspect the actual Streams configuration and transaction guarantees before claiming end-to-end exactly once.
- Dashboard may require serving on the same origin or adjusting fetch URLs; opening the file directly is not the same as serving it.
- Schema registry/client compatibility and Compose health/startup behavior need environment verification.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
