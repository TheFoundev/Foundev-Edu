# Setup Guide

## Source scope

Use disposable test data only. Do not trust a backup until a restore drill verifies bytes and keys.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- The repository is local; no object-store transport, scheduling, snapshot history, prune, or replication exists.
- Homegrown PBKDF2 and chunking must be reviewed carefully before production use.
- Chunks are stored as separate files, not pack files; backup names/manifest semantics matter.
- A key/secret loss can make encrypted backups unrecoverable.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
