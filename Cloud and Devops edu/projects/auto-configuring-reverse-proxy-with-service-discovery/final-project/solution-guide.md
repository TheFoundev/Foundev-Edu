# Mentor Solution Guide

## Source findings

The project implements: Line parser, manual health flags, round robin, reverse proxy, Docker list-containers request, label discovery, health route.

Review known limitations:
- Parser is a small line parser, not YAML.
- Health is manually marked; there is no active probe loop.
- Docker socket access is powerful and should not be exposed to untrusted users.
- TLS certificate management is absent.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
