# Setup Guide

## Source scope

Treat as an in-memory educational model, not an OTLP receiver or production APM service.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- No persistence, sampling, context propagation, or OpenTelemetry SDK/exporter.
- OTLPHandler expects a custom JSON structure and is not mounted in main.go; it is not OTLP JSON/Protobuf compatible.
- Percentile uses floor(p/100*(n-1)) and does not validate p bounds.
- StatsHandler and TraceHandler write JSON without consistent content-type/status helpers.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
