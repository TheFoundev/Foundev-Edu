# Mentor Solution Guide

## Source findings

The project implements: Plan parser, resource/provider classifier, price tables, per-resource estimates, totals by type/provider, unpriced list, JSON handler.

Review known limitations:
- ParsePlan traverses root resources and only one child_modules level, not arbitrary nested modules.
- Prices are hard-coded and incomplete; no live cloud pricing or billing data is consulted.
- count=0 defaults to one; database estimate ignores count; S3 storage_gb is a simplified input.
- The HTTP endpoint serves a precomputed summary, not a plan upload/dashboard.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
