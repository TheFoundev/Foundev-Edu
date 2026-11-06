# Mentor Solution Guide

## Source findings

The project implements: Span model/store, trace assembly, p50/p95, custom JSON ingestion, stats and trace lookup handlers.

Review known limitations:
- No persistence, sampling, context propagation, or OpenTelemetry SDK/exporter.
- OTLPHandler expects a custom JSON structure and is not mounted in main.go; it is not OTLP JSON/Protobuf compatible.
- Percentile uses floor(p/100*(n-1)) and does not validate p bounds.
- StatsHandler and TraceHandler write JSON without consistent content-type/status helpers.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
