# Setup Guide

## Source scope

Use throwaway keys and sample secrets. Never put real secrets in a teaching repository; CI decrypt access must be least-privilege and environment-scoped.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- SOPS upstream repository is archived; check maintained releases/forks and current binary provenance.
- Decrypt policy is a guard inside this CLI, not an OS sandbox; CI identity can decrypt its authorized environment.
- Audit hash chain is tamper-evident, not tamper-proof; an attacker able to rewrite records and checkpoint can rewrite history.
- Plaintext scanner is pattern-based and can miss secrets; encrypted sample data and local identities must be handled carefully.
- README says Ansible optional; it is not equivalent to external secret management.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
