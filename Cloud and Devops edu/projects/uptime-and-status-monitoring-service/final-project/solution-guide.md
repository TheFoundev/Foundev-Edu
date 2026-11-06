# Mentor Solution Guide

## Source findings

The project implements: SQLite database, monitor check function, interval scheduler, transition notifications/webhooks, JSON API, polling dashboard.

Review known limitations:
- README claims TCP, DNS, TLS expiry, and content matching in the aspirational brief; implementation notes say checks are HTTP GET only.
- Dashboard polls; no WebSocket push.
- Notifications and multi-node deployment are limited/out of scope; verify exact retry/alert behavior in source.
- SQLite requires a supported Node runtime; runtime version and database feature support must be checked.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
