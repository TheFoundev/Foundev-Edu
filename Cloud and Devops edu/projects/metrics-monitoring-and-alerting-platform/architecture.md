# Architecture

## Implemented system

Sample store, time-window selection, rate/sum/average, alert rules with for-duration, JSON handlers, Prometheus exporter.

## Data and control flow

Ingest Sample → store → select window at query time → aggregate → evaluate rule state → JSON or exposition response.

## Module source map

- **Sample and Label Data Model:** Sample stores metric/name labels/value/timestamp fields.
- **Store and Select a Time Window:** windowLocked filters by metric and cutoff time.
- **Calculate Rate:** rateLocked uses selected sample values/time behavior from source; inspect exact first/last handling.
- **Calculate Sum and Average:** Store.Sum and Store.Average use windowLocked.
- **Evaluate Alert Rules:** Evaluate compares rule threshold/for duration and returns Alert records.
- **Expose Prometheus Text:** Prometheus(now) generates exposition text; /metrics handler serves it.
- **Use JSON Ingest and Query API:** IngestHandler, QueryHandler, and main route registrations.

## Boundaries and risks

- No PromQL parser or Prometheus scrape integration; samples are pushed into this process.
- Samples are in memory and not persisted.
- Alerts are logged, not delivered to Alertmanager.
- Rate formula and alert pending-duration behavior are the project's simplified semantics, not full Prometheus semantics.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
