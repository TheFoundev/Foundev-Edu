# Setup Guide

## Source scope

Use test backends locally. Do not expose the Docker socket or Docker TCP API publicly.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Parser is a small line parser, not YAML.
- Health is manually marked; there is no active probe loop.
- Docker socket access is powerful and should not be exposed to untrusted users.
- TLS certificate management is absent.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
