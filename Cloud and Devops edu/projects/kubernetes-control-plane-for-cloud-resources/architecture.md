# Architecture

## Implemented system

Resource model, schema registry, plan/create/update/delete, reconciliation, desired-state Controller, optimistic versioning, optional JSON FileStore, HTTP handlers.

## Data and control flow

Desired resources → schema validation → plan against current store → reconcile actions → conditions/version updates → JSON API response.

## Module source map

- **Resource Specs and Status:** Resource includes Kind, Name, Spec, Status, Conditions, and ResourceVersion.
- **Register and Validate Schemas:** SchemaRegistry.Validate checks registered schemas; a kind with no schema is accepted.
- **Plan Desired vs Current State:** Plan returns create/update/delete actions and compares specs with sameSpec.
- **Reconcile Actions and Failures:** ReconcileWithSchemas validates writes and returns FailedAction details.
- **Use Resource Versions for Stale Writes:** Store.Update requires incoming ResourceVersion to match and increments it on write.
- **Controller Desired State and Generation:** SetDesired validates and replaces desired resources; Reconcile plans against Store.
- **Persist State with the Optional FileStore:** main.go conditionally loads NewFileStore when state path is nonempty and saves after changes.
- **Expose the JSON Control API:** Server routes /api/resources, /api/desired, /api/plan, /api/reconcile, /healthz.
- **Separate Simulation from Kubernetes:** No Kubernetes API server/provider is contacted; status is set by local reconciliation.

## Boundaries and risks

- The project is not a Kubernetes API server or Crossplane provider and contacts no cloud provider.
- Unknown resource kinds pass when no schema is registered.
- README limitation says resources are in memory, but main.go supports an optional -state JSON FileStore; distinguish default and configured paths.
- ResourceVersion is an in-process model, not Kubernetes API-server concurrency.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
