# Mentor Solution Guide

## Source findings

The project implements: Pipeline/Step/Build types, indentation parser, trigger/run/status handlers, HostRunner, in-memory build registry.

Review known limitations:
- No OAuth/user accounts, queue worker, retries, cancellation, or container isolation.
- HostRunner executes commands on the server machine; do not run untrusted pipelines.
- README says logs are recorded commands but HostRunner captures actual output; reconcile documentation with the selected runner.
- Pipeline syntax is a tiny custom subset, not full Woodpecker YAML.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
