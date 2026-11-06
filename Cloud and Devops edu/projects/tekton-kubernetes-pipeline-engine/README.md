# Tekton Kubernetes Pipeline Engine

## Overview and purpose

A Go local runner resolves task dependencies, substitutes parameters, executes commands, handles retries/timeouts/final tasks, and reads directory definitions.

## Real-world context

Understand Tekton-like task graphs and execution while distinguishing a local command runner from Tekton CRDs and Pods.

## Implemented features

Task/Pipeline structs, DAG resolver, parameter substitution, workspace/results, runner, retry/timeout/finally logic, directory loader.

## Source findings and limitations

- No Kubernetes API server, Tekton CRDs, Pods, service accounts, or cluster execution are used.
- Commands run on the host; untrusted pipeline definitions can execute arbitrary commands.
- Definitions are Go structs/custom YAML reader rather than Tekton YAML CRDs.
- README's Notes says no retry/timeout/workspace despite earlier features/tests claiming they are implemented; inspect code, which does implement them in the local runner.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, context, os/exec, YAML-like definitions. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Definitions → Resolve DAG → substitute params → host-run steps → workspace/results → statuses.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 10. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
