# Mentor Solution Guide

## Source findings

The project implements: Preflight and server/agent installation scripts, token helper, verification, uninstall, edge-stateful Helm chart, manifests, systemd health/backup timers, validator and runbook.

Review known limitations:
- README states no cluster was provisioned; offline validation is not an end-to-end cluster test.
- Control plane requires quorum; node-local local-path volumes are not replicated storage.
- Bootstrap/uninstall commands use sudo and alter hosts; never run without disposable, prepared machines.
- Token helper and environment files contain sensitive cluster credentials; keep them out of logs and Git.
- NetworkPolicy requires a CNI that enforces it; validate on the chosen K3s setup.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
