# Woodpecker CI Pipeline Server

## Overview and purpose

A Go service parses a small pipeline format, records builds, and can execute commands using a local HostRunner.

## Real-world context

Understand a minimal CI server's pipeline parse, build lifecycle, runner boundary, and the dangers of executing repository commands.

## Implemented features

Pipeline/Step/Build types, indentation parser, trigger/run/status handlers, HostRunner, in-memory build registry.

## Source findings and limitations

- No OAuth/user accounts, queue worker, retries, cancellation, or container isolation.
- HostRunner executes commands on the server machine; do not run untrusted pipelines.
- README says logs are recorded commands but HostRunner captures actual output; reconcile documentation with the selected runner.
- Pipeline syntax is a tiny custom subset, not full Woodpecker YAML.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, HTTP, custom pipeline parser, os/exec. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

HTTP trigger/config → parse pipeline → create build record → run steps → capture outputs/status → list/query build.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 7. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
