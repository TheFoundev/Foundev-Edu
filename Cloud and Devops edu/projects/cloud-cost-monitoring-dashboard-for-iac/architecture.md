# Architecture

## Implemented system

Plan parser, resource/provider classifier, price tables, per-resource estimates, totals by type/provider, unpriced list, JSON handler.

## Data and control flow

terraform show JSON → planned_values resources → simplified local estimates → aggregate summary → stdout or a precomputed JSON endpoint.

## Module source map

- **Plans and Planned Values:** main.go uses embedded examplePlan unless -plan is provided; ParsePlan reads planned_values.root_module.
- **Decode Resource Values:** ParsePlan type-asserts root/module resources and stringValue/numberValue convert selected fields.
- **Traverse Modules and Nested Data:** childModules reads root child_modules; ParsePlan appends each immediate child's resources but does not recurse.
- **Classify Providers and Resource Types:** providerOf splits the resource type at the first underscore and returns other when absent.
- **Use the Hard-Coded Price Catalog:** instancePrices, googleComputePrices, databasePrices contain fixed sample monthly values.
- **Calculate Estimates and Unknowns:** EstimateResource handles a few AWS/GCP types; zero monthly estimates are appended to Unpriced.
- **Aggregate and Expose JSON:** Handler(summary) encodes Summary; main loads plan before ListenAndServe.

## Boundaries and risks

- ParsePlan traverses root resources and only one child_modules level, not arbitrary nested modules.
- Prices are hard-coded and incomplete; no live cloud pricing or billing data is consulted.
- count=0 defaults to one; database estimate ignores count; S3 storage_gb is a simplified input.
- The HTTP endpoint serves a precomputed summary, not a plan upload/dashboard.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
