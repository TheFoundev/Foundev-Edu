# Architecture

## Implemented system

Check/Ping/AlertChannel/Alert models, cron-like parser, ping/status and CRUD APIs, token checks, background poller, alert channels.

## Data and control flow

Scheduled job pings → database/state update → poller evaluates deadline → transition to late/down/up → deduplicated alerts → API/UI status.

## Module source map

- **Model Checks, Pings, and Alerts:** Check includes schedule/grace/timeout/status fields; Ping/Alert reference the check.
- **Parse Schedules and Calculate Deadlines:** parse_cron/next_occurrence implement a limited grammar; compute_next_scheduled_at and check_deadline_exceeded use the stored schedule.
- **Reason About State Transitions:** transition_check, should_alert_on_transition, and deadline checks implement new/up/late/down transitions.
- **Receive Heartbeats and Return Status:** check_ping handles GET/HEAD/POST; check_status returns the current status JSON.
- **Authenticate Management APIs:** authenticate_write_token accepts Bearer or X-API-Token; check_ping is designed for unauthenticated secret URLs.
- **CRUD and Summary Endpoints:** checks_list_create, check_detail, summary, and session are separate view functions.
- **Poller and Alert Dispatch:** run_poller evaluates due checks; dispatch_alert handles configured email/webhook/log channels.
- **Database and Environment Configuration:** DATABASE_URL, SECRET_KEY, DEBUG, ALLOWED_HOSTS, EMAIL_*, BASE_URL configure deployment.
- **Webhook Reliability and Alert Deduplication:** Alert history and channel dispatch are implemented in core/dispatch.py; verify retry and mute semantics before relying on them.
- **Threat Model and Test Boundaries:** Tests cover parser/state/API/dispatch cases; no public deployment or load test is implied.

## Boundaries and risks

- The schedule parser supports a simplified format, not full cron grammar.
- The separate poller must run to detect missed pings; the web process alone is not the scheduler.
- UUID ping URLs are bearer-like secrets; anyone who learns one can spoof a heartbeat.
- Webhook/email delivery and retry guarantees must be checked in core/dispatch.py.
- Production authentication, rate limits, and database operations require operational review.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
