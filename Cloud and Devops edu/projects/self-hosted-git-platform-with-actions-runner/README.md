# Self-Hosted Git Platform with Actions Runner

## Overview and purpose

A Go teaching implementation stores Git-like objects, branches and commits, parses a small workflow syntax, and runs host commands.

## Real-world context

Understand content-addressed Git objects and workflow scheduling while recognizing that commands execute directly on the host.

## Implemented features

Blob/tree/commit object store, branches/log/diff, JSON save/load, small YAML-like workflow parser, job/step dependency runner.

## Source findings and limitations

- Objects are stored in a local JSON state, not packed or served over Git protocol.
- Workflow parser supports only a small syntax subset; it is not full YAML or GitHub Actions.
- Runner executes commands on the host without container isolation; never run untrusted workflow files.
- README's wording that steps are recorded conflicts with tests/implementation showing HostRunner executes them; study source, not that sentence.
- Prebuilt executable files are present in the repository; their provenance is not established by source review, so do not run them blindly.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, Git object hashing, custom workflow parser, os/exec. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Files → Git-style objects/commit → branch pointer; workflow text → jobs/steps → dependency gates → host command execution → results.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 10. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
