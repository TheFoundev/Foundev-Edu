# A beginner's model of server and pipeline

**Lesson ID:** `streamlit-analytics-web-app-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [web/server.py] and [src/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include summary, handle, db, hash_password, verify_password, init_db, load_secret, sign, _month_index, make_subscriptions, is_active, active_in, mrr_by_month, summary; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `web/server.py`, `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `web/server.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import hashlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import hmac` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/server.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def db() -> sqlite3.Connection:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def hash_password(password: str, salt: bytes | None = None) -> str:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def verify_password(password: str, stored: str) -> bool:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def init_db() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _month_index(month: str) -> int:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def make_subscriptions(count=180, seed=21, churn_rate=0.12):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def is_active(row, month: str) -> bool:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def active_in(frame: pd.DataFrame, month: str) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def mrr_by_month(frame: pd.DataFrame, months=None) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary(frame: pd.DataFrame, month: str = CURRENT_MONTH) -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/server.py

```text
#!/usr/bin/env python3
"""The web server of the project: it serves the site and the JSON API.

    python3 web/server.py [--port 8000]

The routes are:

    GET  /                       the home page
    GET  /console.html           the console
    GET  /login.html             the sign-in portal
    GET  /assets/*               the theme and the runtime
    GET  /api/summary            the state of the instance (stats, series, lists)
    POST /api/session            sign in
    DELETE /api/session          sign out
    GET  /api/<resource>         the read endpoints of the domain
    POST /api/<resource>         the write endpoints of the domain

The data lives in `web/app.db` (SQLite). The session is a signed, http-only
cookie; the password of the demo account is stored as a salted PBKDF2 hash.
"""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import mimetypes
import os
import secrets
import sqlite3
import sys
import time
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))

try:  # the domain logic of the project
    from web.api_impl import handle, summary
except Exception:  # pragma: no cover - the project has no domain module yet
    def summary() -> dict:
        return {"stats": {"status": "running"}, "series": [], "lists": {}}

    def handle(method, path, payload, user):
        return 404, {"error": "not found"}

#: The Streamlit page of the project. It is a product of its own and it runs
#: in its own process, so the site sends the visitor there.
STREAMLIT_URL = os.environ.get("STREAMLIT_URL", "http://127.0.0.1:9013/app")

DB_PATH = HERE / "app.db"
SECRET_PATH = HERE / ".session-secret"
SESSION_COOKIE = "foundev_session"
SESSION_TTL = 8 * 3600
DEMO_USER = "demo"
DEMO_PASSWORD = "[REDACTED]"

SECRET = b""


# --------------------------------------------------------------------------
# the database
# --------------------------------------------------------------------------

def db() -> sqlite3.Connection:
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def hash_password(password: str, salt: bytes | None = None) -> str:
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 120_000)
    return f"pbkdf2$120000${salt.hex()}${digest.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        _, rounds, salt_hex, digest_hex = stored.split("$")
        digest = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt_hex), int(rounds))
        return hmac.compare_digest(digest.hex(), digest_hex)
    except Exception:
        return False


def init_db() -> None:
    connection = db()
    connection.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT, created_at REAL)"
    )
    row = connection.execute("SELECT COUNT(*) AS n FROM users").fetchone()
    if row["n"] == 0:
        connection.execute(
            "INSERT INTO users (username, password, role, created_at) VALUES (?,?,?,?)",
```

### src/pipeline.py

```text
"""Subscription data and the metrics that are worked out from it.

The metrics are defined here, so the numbers on the page mean the same thing
everywhere:

MRR          the monthly fee of the subscriptions that are running in the
             month. It is the sum of the fee of every subscription that has
             started and has not churned yet.
ARR          the MRR of the current month times twelve.
Active       the subscriptions that are running in the current month.
Average fee  the MRR of the month divided by the number of active
             subscriptions (the revenue per customer).
Churn        the subscriptions that ended in the month, as a share of the
             subscriptions that were running at the start of the month.
New MRR      the MRR the new subscriptions of the month brought in.
Expansion    the extra MRR the subscriptions that were already there
             brought in.
Net revenue  the MRR of the subscriptions that were there a year ago, plus
             what they brought since, as a share of what they brought then.
             It is the number that says whether the business grows with the
             customers it already has.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

SEGMENTS = ["student", "starter", "team", "business"]
REGIONS = ["north", "south", "east", "west"]

#: The fee of a plan, before the discount every customer gets.
PLAN_FEE = {"student": 5, "starter": 12, "team": 29, "business": 79}

#: The months the data covers.
MONTHS = ["2025-11", "2025-12", "2026-01", "2026-02", "2026-03", "2026-04"]

#: The month the page is about.
CURRENT_MONTH = "2026-04"


def _month_index(month: str) -> int:
    return MONTHS.index(month)


def make_subscriptions(count=180, seed=21, churn_rate=0.12):
    """A set of subscriptions with a start month and, for some of them, the
    month they churned in."""
    rng = np.random.default_rng(seed)
    plans = rng.choice(SEGMENTS, count, p=[0.3, 0.3, 0.25, 0.15])
    starts = rng.choice(MONTHS[:4], count, p=[0.3, 0.3, 0.2, 0.2])
    fees = np.array([PLAN_FEE[plan] for plan in plans]) * rng.uniform(0.9, 1.2, count)

    frame = pd.DataFrame({
        "customer_id": np.arange(1, count + 1),
        "segment": plans,
        "region": rng.choice(REGIONS, count),
        "start_month": starts,
        "monthly_fee": fees.round(2),
    })

    churned = []
    for start in frame["start_month"]:
        first = _month_index(start)
        room = len(MONTHS) - 1 - first
        if room > 0 and rng.random() < churn_rate:
            churned.append(MONTHS[first + int(rng.integers(1, room + 1))])
        else:
            churned.append(None)
    frame["churn_month"] = churned
    return frame


def is_active(row, month: str) -> bool:
    """True when a subscription is running in a month."""
    if _month_index(row["start_month"]) > _month_index(month):
        return False
    churn = row.get("churn_month")
    if churn is None or (isinstance(churn, float) and np.isnan(churn)):
        return True
    return _month_index(churn) > _month_index(month)


def active_in(frame: pd.DataFrame, month: str) -> pd.DataFrame:
    """The subscriptions that are running in a month."""
    if frame.empty:
        return frame
    mask = frame.apply(lambda row: is_active(row, month), axis=1)
    return frame[mask]


def mrr_by_month(frame: pd.DataFrame, months=None) -> pd.DataFrame:
    """The MRR of every month."""
    months = months or MONTHS
    rows = []
    for month in months:
        active = active_in(frame, month)
        rows.append({
            "month": month,
            "mrr": round(float(active["monthly_fee"].sum()), 2),
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `web/server.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
