# Encrypted Configuration Management in Git

## Overview and purpose

secretsync is a Python CLI that orchestrates SOPS/age, environment policy, tracked-file scanning, and a hash-chained audit log.

## Real-world context

Understand encrypted configuration workflows, key recipients, CI-only decryption policy, audit integrity, rotation, and their trust boundaries.

## Implemented features

Config loader/YAML subset, real SOPS/age subprocess wrappers, encrypt/decrypt/rotate CLI, CI policy checks, plaintext scanner, audit chain/checkpoint, Git hooks and CI examples.

## Source findings and limitations

- SOPS upstream repository is archived; check maintained releases/forks and current binary provenance.
- Decrypt policy is a guard inside this CLI, not an OS sandbox; CI identity can decrypt its authorized environment.
- Audit hash chain is tamper-evident, not tamper-proof; an attacker able to rewrite records and checkpoint can rewrite history.
- Plaintext scanner is pattern-based and can miss secrets; encrypted sample data and local identities must be handled carefully.
- README says Ansible optional; it is not equivalent to external secret management.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Python, SOPS, age, Git, CI, optional Ansible. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Plain config → SOPS encrypt to age recipients → encrypted file committed → CI identity decrypts → audit records and precommit/CI checks verify hygiene.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 12. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
