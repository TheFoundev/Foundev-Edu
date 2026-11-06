# Lightweight Kubernetes Edge Cluster

## Overview and purpose

An operations repository provides scripts, K3s configuration, Helm workloads, systemd units, backups, and an offline validation gate.

## Real-world context

Plan and review a small HA edge cluster while understanding quorum, node joins, local storage, tokens, and destructive operations.

## Implemented features

Preflight and server/agent installation scripts, token helper, verification, uninstall, edge-stateful Helm chart, manifests, systemd health/backup timers, validator and runbook.

## Source findings and limitations

- README states no cluster was provisioned; offline validation is not an end-to-end cluster test.
- Control plane requires quorum; node-local local-path volumes are not replicated storage.
- Bootstrap/uninstall commands use sudo and alter hosts; never run without disposable, prepared machines.
- Token helper and environment files contain sensitive cluster credentials; keep them out of logs and Git.
- NetworkPolicy requires a CNI that enforces it; validate on the chosen K3s setup.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

K3s, Kubernetes, Helm, systemd, Linux, Raspberry Pi/VM. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Preflight → bootstrap first server/etcd → join control-plane peers and agents → deploy chart → verify → monitor/back up → safe teardown.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 12. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
