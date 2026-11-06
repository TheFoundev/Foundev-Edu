# Mentor Solution Guide

## Source findings

The project implements: Sample store, time-window selection, rate/sum/average, alert rules with for-duration, JSON handlers, Prometheus exporter.

Review known limitations:
- No PromQL parser or Prometheus scrape integration; samples are pushed into this process.
- Samples are in memory and not persisted.
- Alerts are logged, not delivered to Alertmanager.
- Rate formula and alert pending-duration behavior are the project's simplified semantics, not full Prometheus semantics.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
