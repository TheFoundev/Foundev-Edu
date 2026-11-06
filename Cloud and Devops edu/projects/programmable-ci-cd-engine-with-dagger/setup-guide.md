# Setup Guide

## Source scope

Run only trusted pipeline definitions in a disposable workspace; host-executed steps can modify the local machine.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Despite project name and listed stack, this implementation does not import or invoke the Dagger SDK/engine; it simulates container steps with host command execution.
- HostExecutor commands run on the machine and are not isolated containers.
- FileCache is local; no remote artifact/cache service exists.
- Secrets are redacted in output by tests but still require careful environment and process handling.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
