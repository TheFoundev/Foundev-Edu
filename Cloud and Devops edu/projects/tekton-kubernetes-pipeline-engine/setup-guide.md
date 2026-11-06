# Setup Guide

## Source scope

Run only trusted definitions in a disposable workspace. Do not apply as Kubernetes resources; this project executes locally.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- No Kubernetes API server, Tekton CRDs, Pods, service accounts, or cluster execution are used.
- Commands run on the host; untrusted pipeline definitions can execute arbitrary commands.
- Definitions are Go structs/custom YAML reader rather than Tekton YAML CRDs.
- README's Notes says no retry/timeout/workspace despite earlier features/tests claiming they are implemented; inspect code, which does implement them in the local runner.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
