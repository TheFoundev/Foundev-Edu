# Programmable CI/CD Engine with Dagger

## Overview and purpose

A Go pipeline runner orders steps, hashes inputs/dependencies, caches results, executes host commands, and reports outcomes.

## Real-world context

Understand dependency graphs, cache correctness, executor boundaries, retries/timeouts, and secret redaction without mistaking this host runner for Dagger.

## Implemented features

Pipeline/Step model, DAG ordering/cycle checks, digest cache, host/recording executors, retries/timeouts, environment/secret handling, report.

## Source findings and limitations

- Despite project name and listed stack, this implementation does not import or invoke the Dagger SDK/engine; it simulates container steps with host command execution.
- HostExecutor commands run on the machine and are not isolated containers.
- FileCache is local; no remote artifact/cache service exists.
- Secrets are redacted in output by tests but still require careful environment and process handling.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, context, host process execution, memory/file cache. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Pipeline definitions → dependency order → content/dependency digests → cache or executor → results/logs.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 9. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
