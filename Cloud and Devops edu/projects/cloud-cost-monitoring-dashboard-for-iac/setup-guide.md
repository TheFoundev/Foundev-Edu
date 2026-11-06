# Setup Guide

## Source scope

Use synthetic plan JSON. Never treat estimates as an invoice or current cloud pricing; review provider pricing separately.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- ParsePlan traverses root resources and only one child_modules level, not arbitrary nested modules.
- Prices are hard-coded and incomplete; no live cloud pricing or billing data is consulted.
- count=0 defaults to one; database estimate ignores count; S3 storage_gb is a simplified input.
- The HTTP endpoint serves a precomputed summary, not a plan upload/dashboard.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
