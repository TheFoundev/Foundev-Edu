# Setup Guide

## Source scope

Use the local Docker Compose stack. Do not describe fake-registry mode as a production registry or exactly-once guarantees without verifying config.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- This project uses real Kafka components but has an in-process fake registry option; behavior differs between all-local smoke mode and full Compose stack.
- README describes exactly-once semantics; inspect the actual Streams configuration and transaction guarantees before claiming end-to-end exactly once.
- Dashboard may require serving on the same origin or adjusting fetch URLs; opening the file directly is not the same as serving it.
- Schema registry/client compatibility and Compose health/startup behavior need environment verification.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
