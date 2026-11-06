# Auto-Configuring Reverse Proxy with Service Discovery

## Overview and purpose

A Go reverse proxy parses a small config, selects healthy backends, and can discover labeled Docker containers.

## Real-world context

Understand a service registry, routing, round robin, and the privilege boundary around Docker daemon access.

## Implemented features

Line parser, manual health flags, round robin, reverse proxy, Docker list-containers request, label discovery, health route.

## Source findings and limitations

- Parser is a small line parser, not YAML.
- Health is manually marked; there is no active probe loop.
- Docker socket access is powerful and should not be exposed to untrusted users.
- TLS certificate management is absent.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, net/http, httputil, Docker Engine API. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Config/Docker API → service registry → healthy backend selection → prefix rewrite → proxy request.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 8. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
