# Mentor Solution Guide

## Source findings

The project implements: Memory token buckets, Redis INCR/PEXPIRE store, key selection, HTTP 429/header middleware, stats exporter, health endpoint.

Review known limitations:
- MemoryStore uses token-bucket refill; RedisStore is a fixed-window INCR/PEXPIRE counter, so the storage backends do not implement identical algorithms.
- RedisStore ignores rate during Take; Sweep is a no-op because Redis TTL handles expiry.
- Store errors fail open in Limiter.AllowAt.
- Stats exposes allowed/blocked counters only for MemoryStore; Redis metrics are missing/zero.
- X-Forwarded-For trust is a global boolean, not a trusted-proxy CIDR list.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
