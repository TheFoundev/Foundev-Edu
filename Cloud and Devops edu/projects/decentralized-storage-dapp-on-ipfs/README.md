# Decentralized Storage dApp on IPFS

## Overview and purpose

A Node.js project computes raw CIDv1 identifiers and stores bytes in a local content-addressed directory behind an HTTP API.

## Real-world context

Distinguish content identifiers and local integrity from IPFS peer discovery, replication, pinning, and UnixFS DAG storage.

## Implemented features

CID/base32 helpers, local store, API server, optional client, static page, and Node tests.

## Source findings and limitations

- README states no IPFS daemon/network is used; storage is local and not replicated/announced.
- Only raw codec/single-block behavior is modeled; real IPFS UnixFS chunking/DAGs can produce different CIDs.
- A CID is generally not the same as a simple whole-file hash.
- No pinning, quotas, or garbage collection.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Node.js, CIDv1, Multihash, Local filesystem, HTTP. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Bytes → SHA-256 multihash + raw codec + CIDv1 + base32 → local file keyed by CID → retrieve and verify.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 8. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
