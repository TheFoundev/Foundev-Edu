# Setup Guide

## Source scope

Run the Compose stack only in a local lab; change example credentials and do not expose the management/broker ports publicly.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Inventory/payment/fulfillment are deterministic simulations in mbb_order, not real services.
- RabbitMQ topology and Docker Compose must be checked against actual environment; README is detailed but tests are unit-focused.
- Retry TTL ladder can produce delayed retries and duplicate processing; idempotency behavior must be understood.
- Credentials/config must be changed before any exposed broker deployment.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
