# Setup Guide

## Source scope

Use throwaway secrets only on localhost. Set a strong password/token, protect the data file, and do not expose the HTTP service publicly.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- Default password is change-me when SECRETS_PASSWORD is absent, and the API token is printed to console at startup.
- One API token provides broad access; no role-based access control or key rotation exists.
- Audit history is capped at 200 records and stored beside secrets; it is not an immutable audit system.
- File writes are direct, not an atomic database transaction; no TLS is provided by the basic Node server.
- Read API reveals plaintext to any holder of the API token.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
