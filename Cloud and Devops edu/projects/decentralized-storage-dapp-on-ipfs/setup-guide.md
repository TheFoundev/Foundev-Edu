# Setup Guide

## Source scope

Use nonsensitive local test content. Do not imply public network upload or deletion; this project stores data locally.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- README states no IPFS daemon/network is used; storage is local and not replicated/announced.
- Only raw codec/single-block behavior is modeled; real IPFS UnixFS chunking/DAGs can produce different CIDs.
- A CID is generally not the same as a simple whole-file hash.
- No pinning, quotas, or garbage collection.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
