# Read api impl in the source

**Lesson ID:** `dbt-analytics-transformation-layer-module-05-lesson-2`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include state, models, raw_tables, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def state() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def models() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def raw_tables() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/api_impl.py

```text
"""The API of the project: the models of the run and the manifest.

The numbers come from a real run of the runner: the raw tables are loaded
into SQLite, every model is rendered with its refs replaced by the tables
that are already there, and the manifest of the run is written next to the
warehouse.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import run  # noqa: E402

#: Where the runner writes the warehouse and the manifest.
BASE_DIR = ROOT / "artifacts"
MANIFEST = BASE_DIR / "manifest.json"
WAREHOUSE = BASE_DIR / "warehouse.db"

#: The summary of the last run, kept for the life of the process.
_STATE: dict = {}


def state() -> dict:
    """Materialise the models and keep the manifest of the run."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        _STATE["run"] = result
        _STATE["manifest"] = manifest
    return _STATE


def models() -> list:
    """The models of the run, with the models they need and their rows."""
    return [
        {
            "model": model["name"],
            "needs": ", ".join(model["depends_on"]) or "-",
            "rows": model["rows"],
        }
        for model in state()["manifest"]["models"]
    ]


def raw_tables() -> list:
    """The tables the models are built from, with the rows they hold."""
    if not WAREHOUSE.exists():
        return []
    connection = sqlite3.connect(WAREHOUSE)
    rows = []
    for table in state()["manifest"]["raw_tables"]:
        count = connection.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        rows.append({"table": table, "rows": int(count)})
    connection.close()
    return rows


def summary() -> dict:
    """The state of the last run: the models, the raw orders and the revenue."""
    current = state()
    result = current["run"]
    built = current["manifest"]["models"]
    return {
        "stats": {
            "models": result["models"],
            "raw_orders": result["raw_orders"],
            "staging_rows": result["staging_rows"],
            "revenue": result["revenue"],
        },
        "series": [
            {"label": model["name"], "value": model["rows"]} for model in built
        ],
        "lists": {
            "models": models(),
            "raw_tables": raw_tables(),
        },
    }


def handle(method, path, payload, user):
    """The read and the write endpoints of the project."""
    if method == "GET" and path == "/api/models":
        return 200, {"models": models()}
    if method == "GET" and path == "/api/manifest":
        return 200, state()["manifest"]
    if method == "POST" and path == "/api/run":
        _STATE.pop("run", None)
        _STATE.pop("manifest", None)
        state()
        return 200, summary()["stats"]
    return 404, {"error": "not found"}

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

This lesson ties its explanation to `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
