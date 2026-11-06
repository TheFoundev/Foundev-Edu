# Setup Guide

## Source scope

Run only on localhost with trusted test commands. Never expose a host-command runner without authentication, isolation, and authorization.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- No OAuth/user accounts, queue worker, retries, cancellation, or container isolation.
- HostRunner executes commands on the server machine; do not run untrusted pipelines.
- README says logs are recorded commands but HostRunner captures actual output; reconcile documentation with the selected runner.
- Pipeline syntax is a tiny custom subset, not full Woodpecker YAML.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
