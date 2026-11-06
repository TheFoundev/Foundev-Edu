# Encrypted Deduplicated Backup System

## Overview and purpose

A Go prototype chunks data, deduplicates by content hash, encrypts chunks, writes a manifest, and restores files locally.

## Real-world context

Understand content-defined chunking, deduplication, key derivation, authenticated encryption, and restore integrity.

## Implemented features

Content-defined boundaries, chunk hashes, per-chunk encryption, repository manifest, restore path, unit tests.

## Source findings and limitations

- The repository is local; no object-store transport, scheduling, snapshot history, prune, or replication exists.
- Homegrown PBKDF2 and chunking must be reviewed carefully before production use.
- Chunks are stored as separate files, not pack files; backup names/manifest semantics matter.
- A key/secret loss can make encrypted backups unrecoverable.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, SHA-256, PBKDF2-style key derivation, AES-GCM, Filesystem. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Input bytes → rolling-hash chunks → chunk ID → encrypted chunk file → manifest → decrypt and concatenate on restore.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 9. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
