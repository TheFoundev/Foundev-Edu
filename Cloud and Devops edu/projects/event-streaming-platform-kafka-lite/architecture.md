# Architecture

## Implemented system

Producer, registry client/fake registry, schema validation and DLQ, Kafka Streams topology, windows/sessionization, view server, dashboard.

## Data and control flow

ClickProducer → clicks topic → schema validation/deserializer → ClicksStreamsApp → aggregates/state stores → ViewServer/dashboard; invalid messages route to DLQ.

## Module source map

- **Events, Keys, and Topics:** Producer config keys click events by session_id; deterministic event IDs are described in README.
- **Validate Event Schemas:** SchemaRegistryClient calls external registry with bundled-schema fallback; FakeSchemaRegistry is local.
- **Handle Invalid Events and DLQ:** README describes violations routed to clicks-dlq; inspect headers and error handler for exact behavior.
- **Build the Kafka Streams Topology:** Source builds clean-clicks, page-stats, session-stats with state stores and changelog topics.
- **Filter Bots and Aggregate Windows:** README describes regex bot filtering and one-minute tumbling aggregations.
- **Understand Sessionization and State Stores:** README lists sessionization and changelog-backed state stores.
- **Producer Delivery and Registry Modes:** CLI subcommands include producer, streams, view, fake-registry, and all-local.
- **Serve Materialized Views:** ViewServer exposes stats/pages, stats/sessions, top-referrers, and health routes.
- **Dashboard Origin and Data Flow:** README warns dashboard expects ViewServer same-origin or adjusted fetch URLs.
- **Compose the Stack and Verify Startup:** README shows full stack and separate local verification gate.
- **Delivery Guarantees and Failure Handling:** README claims/mentions exactly-once; verify actual processing.guarantee and transaction settings in source.
- **Read Tests and Limitations:** SchemaRegistryClientTest covers bundled/fake schema resolution; it does not prove a live external Schema Registry integration.

## Boundaries and risks

- This project uses real Kafka components but has an in-process fake registry option; behavior differs between all-local smoke mode and full Compose stack.
- README describes exactly-once semantics; inspect the actual Streams configuration and transaction guarantees before claiming end-to-end exactly once.
- Dashboard may require serving on the same origin or adjusting fetch URLs; opening the file directly is not the same as serving it.
- Schema registry/client compatibility and Compose health/startup behavior need environment verification.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
