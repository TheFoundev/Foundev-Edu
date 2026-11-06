# Setup Guide

## Source scope

Run locally. Decide whether store outages should fail open or closed before using a limiter for abuse protection.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- MemoryStore uses token-bucket refill; RedisStore is a fixed-window INCR/PEXPIRE counter, so the storage backends do not implement identical algorithms.
- RedisStore ignores rate during Take; Sweep is a no-op because Redis TTL handles expiry.
- Store errors fail open in Limiter.AllowAt.
- Stats exposes allowed/blocked counters only for MemoryStore; Redis metrics are missing/zero.
- X-Forwarded-For trust is a global boolean, not a trusted-proxy CIDR list.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
