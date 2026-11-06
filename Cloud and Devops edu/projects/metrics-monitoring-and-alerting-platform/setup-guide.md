# Setup Guide

## Source scope

Run locally with synthetic samples. Do not treat the demo as a production monitoring or alerting system.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- No PromQL parser or Prometheus scrape integration; samples are pushed into this process.
- Samples are in memory and not persisted.
- Alerts are logged, not delivered to Alertmanager.
- Rate formula and alert pending-duration behavior are the project's simplified semantics, not full Prometheus semantics.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
