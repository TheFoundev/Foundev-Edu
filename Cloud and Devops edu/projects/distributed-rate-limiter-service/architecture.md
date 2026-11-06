# Architecture

## Implemented system

Memory token buckets, Redis INCR/PEXPIRE store, key selection, HTTP 429/header middleware, stats exporter, health endpoint.

## Data and control flow

Request → choose API-key/IP key → Store.Take → allow or 429 → update headers/metrics.

## Module source map

- **Token Bucket in Plain Terms:** MemoryStore stores floating tokens and last time, refilling elapsed seconds × rate up to burst.
- **Memory Store Synchronization:** Take, Remaining, Sweep, and Counters lock MemoryStore.mu.
- **HTTP Middleware and Rate Headers:** Blocked path sets Retry-After, X-RateLimit-Limit, and X-RateLimit-Remaining.
- **Choose a Request Identity Key:** KeyFor prefers X-API-Key, then RemoteAddr; first X-Forwarded-For is used only when TrustedProxies is true.
- **Contrast Redis Fixed Window:** RedisStore increments a key and sets PEXPIRE on count==1; Take compares count to burst and does not use rate.
- **Read the RESP Client:** respClient writes arrays/bulk strings and parses simple, error, integer, and bulk replies.
- **Plan for Store Failure:** AllowAt returns true on Store.Take error; Remaining returns zero on error.
- **Metrics and Expiration:** Stats reads Counters only from MemoryStore; RedisStore Sweep returns 0 and relies on key TTL.
- **Tests, Concurrency, and Algorithm Limits:** TestTheLimiterIsSafeUnderLoad exercises concurrent requests against the in-memory limiter; Redis semantics differ.

## Boundaries and risks

- MemoryStore uses token-bucket refill; RedisStore is a fixed-window INCR/PEXPIRE counter, so the storage backends do not implement identical algorithms.
- RedisStore ignores rate during Take; Sweep is a no-op because Redis TTL handles expiry.
- Store errors fail open in Limiter.AllowAt.
- Stats exposes allowed/blocked counters only for MemoryStore; Redis metrics are missing/zero.
- X-Forwarded-For trust is a global boolean, not a trusted-proxy CIDR list.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
