# Mentor Solution Guide

## Source findings

The project implements: Check/Ping/AlertChannel/Alert models, cron-like parser, ping/status and CRUD APIs, token checks, background poller, alert channels.

Review known limitations:
- The schedule parser supports a simplified format, not full cron grammar.
- The separate poller must run to detect missed pings; the web process alone is not the scheduler.
- UUID ping URLs are bearer-like secrets; anyone who learns one can spoof a heartbeat.
- Webhook/email delivery and retry guarantees must be checked in core/dispatch.py.
- Production authentication, rate limits, and database operations require operational review.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
