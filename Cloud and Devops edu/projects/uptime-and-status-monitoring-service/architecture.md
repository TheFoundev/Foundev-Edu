# Architecture

## Implemented system

SQLite database, monitor check function, interval scheduler, transition notifications/webhooks, JSON API, polling dashboard.

## Data and control flow

Monitor config → scheduled HTTP GET → check result/latency → persisted status/history → transition alert → API/dashboard.

## Module source map

- **Monitor and Check Data Model:** SQLite schema separates monitors and check history.
- **Perform an HTTP Check:** checkOnce receives an injectable fetch and returns status/latency/result.
- **Schedule Periodic Checks:** startScheduler iterates monitors and uses setInterval; timer.unref is used when available.
- **Detect State Changes:** previousStatus and notificationsFor compare current/previous status to decide notifications.
- **Send Notifications and Webhooks:** notify accepts injectable send function and formats notification payload.
- **Expose API and Static Status Page:** createStatusServer and servePublic implement HTTP/static routes.
- **Understand SQLite Persistence:** openDatabase creates/uses a SQLite database file and tables.
- **Review Monitoring Scope and Tests:** The checkOnce function issues HTTP requests; tests cover checks, scheduling, notifications, transitions, and webhook behavior.

## Boundaries and risks

- README claims TCP, DNS, TLS expiry, and content matching in the aspirational brief; implementation notes say checks are HTTP GET only.
- Dashboard polls; no WebSocket push.
- Notifications and multi-node deployment are limited/out of scope; verify exact retry/alert behavior in source.
- SQLite requires a supported Node runtime; runtime version and database feature support must be checked.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
