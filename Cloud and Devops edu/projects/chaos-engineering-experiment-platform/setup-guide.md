# Setup Guide

## Source scope

DryRunExecutor is the safe default. Do not run local kill/stress against shared or production machines.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Local executor may SIGTERM a host process and consume CPU; only use a disposable target.
- Local delay sleeps in Apply and Runner, doubling configured delay.
- Recover is a no-op; killed processes are not restarted.
- Stress magnitude does not scale worker count; static metrics are not Prometheus.
- No Kubernetes/Chaos Mesh API or scheduler is present.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
