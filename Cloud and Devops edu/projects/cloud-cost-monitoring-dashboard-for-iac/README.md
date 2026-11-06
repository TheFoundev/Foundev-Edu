# Cloud Cost Monitoring Dashboard for IaC

## Overview and purpose

A Go command-line/API tool reads a subset of Terraform plan JSON and estimates selected resource costs from hard-coded price tables.

## Real-world context

Understand the difference between parsing a plan, applying a simplified price model, and producing a trustworthy cloud bill.

## Implemented features

Plan parser, resource/provider classifier, price tables, per-resource estimates, totals by type/provider, unpriced list, JSON handler.

## Source findings and limitations

- ParsePlan traverses root resources and only one child_modules level, not arbitrary nested modules.
- Prices are hard-coded and incomplete; no live cloud pricing or billing data is consulted.
- count=0 defaults to one; database estimate ignores count; S3 storage_gb is a simplified input.
- The HTTP endpoint serves a precomputed summary, not a plan upload/dashboard.

The modules distinguish implemented code from external systems or features that are only described in the README/brief.

## Technology and system requirements

Go, Terraform plan JSON, HTTP JSON. See the repository build files and setup guide for local prerequisites.

## Installation and environment

Follow setup-guide.md and use the project's actual commands. External infrastructure is optional unless a lesson explicitly calls for a disposable test environment.

## Data and persistence

terraform show JSON → planned_values resources → simplified local estimates → aggregate summary → stdout or a precomputed JSON endpoint.

Persistence, external replication, and managed-service behavior are described only where included in source.

## Architecture and testing

See architecture.md. The project contains the following curriculum modules: 7. Follow test commands from the source README; tests do not establish production safety.

## Security and operations

Treat command runners, Docker sockets, cluster credentials, encryption keys, smart contracts, and public endpoints as high-impact boundaries. Use least privilege, test-only credentials, explicit rollback, and cleanup.

## Troubleshooting

Compare README claims with the named source files, inspect logs and test results, and distinguish parser/setup, build, runtime, network, and policy failures.

## Further learning

Use official references in references.json for up-to-date protocol and provider details.
