# Architecture

## Implemented system

Span model/store, trace assembly, p50/p95, custom JSON ingestion, stats and trace lookup handlers.

## Data and control flow

JSON spans → append to memory → group by TraceID → derive root/errors/duration → group by service → calculate percentiles.

## Module source map

- **Span and Trace Vocabulary:** Span carries trace/span/parent IDs, service, operation, start, duration, and status.
- **Store and Concurrency:** Store.Add locks for append; all returns a copied slice under RLock.
- **Assemble Trace Duration and Root:** Traces groups by TraceID and counts status == error.
- **Calculate Latency Percentiles:** Percentile selects a sorted-value index; Stats converts durations to milliseconds.
- **Ingest Custom Span JSON:** main mounts /spans to IngestHandler.
- **Audit the OTLP-Labeled Handler:** OTLPHandler expects resourceSpans/scopeSpans/spans containing Span-shaped JSON.
- **Query Stats and Trace IDs:** Main registers /stats and /traces/ only when -listen is supplied.
- **Limits and Verification:** OTLPHandler is a local custom handler; the store is memory-backed and main does not mount an official OTLP receiver/exporter.

## Boundaries and risks

- No persistence, sampling, context propagation, or OpenTelemetry SDK/exporter.
- OTLPHandler expects a custom JSON structure and is not mounted in main.go; it is not OTLP JSON/Protobuf compatible.
- Percentile uses floor(p/100*(n-1)) and does not validate p bounds.
- StatsHandler and TraceHandler write JSON without consistent content-type/status helpers.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
