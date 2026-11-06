# Mentor Solution Guide

## Source findings

The project implements: Validation, dry-run/local executors, static metric reader, pre/post checks, event timeline, rollback, memory/file stores.

Review known limitations:
- Local executor may SIGTERM a host process and consume CPU; only use a disposable target.
- Local delay sleeps in Apply and Runner, doubling configured delay.
- Recover is a no-op; killed processes are not restarted.
- Stress magnitude does not scale worker count; static metrics are not Prometheus.
- No Kubernetes/Chaos Mesh API or scheduler is present.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
