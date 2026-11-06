# Mentor Solution Guide

## Source findings

The project implements: Topics/partitions, deterministic key partitioning, publish/fetch, consumer cursor/ack/pending, retention trim, HTTP handlers.

Review known limitations:
- All topics/messages/offsets are in memory; restart loses them.
- There are no durable consumer groups, replication, dead-letter queues, or flow control.
- Acknowledgement semantics and retention boundaries are simple prototype behavior, not Kafka/NATS guarantees.
- README says NATS-like concept but implementation is its own Go HTTP API.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
