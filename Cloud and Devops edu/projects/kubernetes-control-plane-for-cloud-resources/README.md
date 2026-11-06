# Kubernetes Control Plane for Cloud Resources

## Overview and purpose

A Go prototype models desired resources, validates schemas, plans actions, reconciles a local store, and exposes JSON endpoints.

## Real-world context

Understand reconciliation and optimistic resource versions while distinguishing a control-plane simulation from Kubernetes or Crossplane.

## Implemented features

Resource model, schema registry, plan/create/update/delete, reconciliation, desired-state Controller, optimistic versioning, optional JSON FileStore, HTTP handlers.

## Source findings and limitations

- The project is not a Kubernetes API server or Crossplane provider and contacts no cloud provider.
- Unknown resource kinds pass when no schema is registered.
- README limitation says resources are in memory, but main.go supports an optional -state JSON FileStore; distinguish default and configured paths.
- ResourceVersion is an in-process model, not Kubernetes API-server concurrency.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, JSON API, custom resource model. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

Desired resources → schema validation → plan against current store → reconcile actions → conditions/version updates → JSON API response.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 9. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
