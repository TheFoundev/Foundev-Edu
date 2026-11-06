# A beginner's model of main and server

**Lesson ID:** `rag-evaluation-harness-with-ragas-module-01-lesson-1`

## Purpose and learning objectives

Study the implementation in [main.py] and [web/server.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include main, summary, handle, db, hash_password, verify_password, init_db, load_secret, sign; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `main.py`, `web/server.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Evaluate a tiny retrieval-augmented QA pipeline.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Evaluate a tiny retrieval-augmented QA pipeline.')
        print("Run `python main.py run` to execute the pipeline.")
        return

    if args.command == "demo":
        demo(base_dir=args.base_dir)
        return

    summary = run(quick=args.quick, base_dir=args.base_dir)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()

```

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
            (DEMO_USER, hash_password(DEMO_PASSWORD), "admin", time.time()),
        )
        connection.commit()
    connection.close()
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

This lesson ties its explanation to `main.py`, `web/server.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
