# Setup Guide

## Source scope

Use a local database and test webhook. Protect ping URLs/tokens; do not launch public monitors without reviewing auth and rate limits.

Inspect the project's README, package/build files, and source before running commands. Some README descriptions refer to broader systems than the included implementation.

## Local setup

Use official tools and versions listed in the repository's build files and references. Prefer local simulations, mock services, test chains, and disposable clusters. Run only the project checks explicitly identified in its README.

## Configuration and credentials

Use environment variables or secret stores for credentials. Do not paste real keys into commands that enter shell history, logs, screenshots, or Git. Check whether a feature uses a local simulation or actual external service.

## Known source gaps

- The schedule parser supports a simplified format, not full cron grammar.
- The separate poller must run to detect missed pings; the web process alone is not the scheduler.
- UUID ping URLs are bearer-like secrets; anyone who learns one can spoof a heartbeat.
- Webhook/email delivery and retry guarantees must be checked in core/dispatch.py.
- Production authentication, rate limits, and database operations require operational review.

## Cleanup

Stop local processes and containers, remove disposable state and test resources, revoke temporary credentials, and check cloud/broker/cluster billing before finishing.
