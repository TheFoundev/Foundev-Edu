# Chaos Engineering Experiment Platform

## Overview and purpose

A Go experiment runner validates actions, applies a fault executor, evaluates hypotheses, records a timeline, and stores results.

## Real-world context

Design safe experiments with explicit steady-state hypotheses, controlled actions, recovery, rollback, and evidence.

## Implemented features

Validation, dry-run/local executors, static metric reader, pre/post checks, event timeline, rollback, memory/file stores.

## Source findings and limitations

- Local executor may SIGTERM a host process and consume CPU; only use a disposable target.
- Local delay sleeps in Apply and Runner, doubling configured delay.
- Recover is a no-op; killed processes are not restarted.
- Stress magnitude does not scale worker count; static metrics are not Prometheus.
- No Kubernetes/Chaos Mesh API or scheduler is present.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, context, FaultExecutor, MetricReader. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Validate → baseline check → apply → wait/recover → verify → persist or abort.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 10. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
