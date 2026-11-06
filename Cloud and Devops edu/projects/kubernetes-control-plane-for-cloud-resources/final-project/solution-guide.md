# Mentor Solution Guide

## Source findings

The project implements: Resource model, schema registry, plan/create/update/delete, reconciliation, desired-state Controller, optimistic versioning, optional JSON FileStore, HTTP handlers.

Review known limitations:
- The project is not a Kubernetes API server or Crossplane provider and contacts no cloud provider.
- Unknown resource kinds pass when no schema is registered.
- README limitation says resources are in memory, but main.go supports an optional -state JSON FileStore; distinguish default and configured paths.
- ResourceVersion is an in-process model, not Kubernetes API-server concurrency.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
