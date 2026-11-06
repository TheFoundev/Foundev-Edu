# Setup Guide

## Source scope

Use local test URLs only. Do not target third-party systems without authorization; configure notification destinations privately.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- README claims TCP, DNS, TLS expiry, and content matching in the aspirational brief; implementation notes say checks are HTTP GET only.
- Dashboard polls; no WebSocket push.
- Notifications and multi-node deployment are limited/out of scope; verify exact retry/alert behavior in source.
- SQLite requires a supported Node runtime; runtime version and database feature support must be checked.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
