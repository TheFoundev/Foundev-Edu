# A beginner's model of api impl

**Lesson ID:** `airflow-scheduled-etl-dags-module-03-lesson-1`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_pipeline, history, tasks, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import DEPENDENCIES, run  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_pipeline() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def history() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def tasks() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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
"""The API of the project: the numbers of the last run of the pipeline.

The summary comes from the real pipeline: the tasks are run in the order of
the dependency graph, the raw orders, the clean orders and the daily revenue
are written, and the history of the runs is read back from the warehouse.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import DEPENDENCIES, run  # noqa: E402

#: Where the pipeline writes the raw orders, the clean ones and the warehouse.
BASE_DIR = ROOT / "artifacts"
WAREHOUSE = BASE_DIR / "warehouse.db"

#: The summary of the last run, kept for the life of the process.
_STATE: dict = {}


def run_pipeline() -> dict:
    """Run the pipeline and keep the summary of the run."""
    summary = run(quick=False, base_dir=str(BASE_DIR))
    _STATE["summary"] = summary
    return summary


def history() -> list:
    """The history of the runs: the task, its state, its rows and its time."""
    if not WAREHOUSE.exists():
        return []
    connection = sqlite3.connect(WAREHOUSE)
    rows = connection.execute(
        "SELECT task, status, rows, seconds, finished_at FROM task_runs ORDER BY rowid"
    ).fetchall()
    connection.close()
    return [
        {
            "task": row[0],
            "status": row[1],
            "rows": row[2],
            "seconds": round(row[3], 3),
            "finished_at": row[4],
        }
        for row in rows
    ]


def tasks() -> list:
    """The tasks of the DAG with the task each of them needs.

    The state and the rows of a task come from the last run, so the table
    shows what the run really did.
    """
    summary = _STATE.get("summary") or run_pipeline()
    order = summary["order"]
    last = history()[-len(order):] if len(history()) >= len(order) else []
    states = {row["task"]: row for row in last}
    return [
        {
            "task": name,
            "needs": ", ".join(DEPENDENCIES.get(name, [])) or "-",
            "status": states.get(name, {}).get("status", "-"),
            "rows": states.get(name, {}).get("rows", 0),
        }
        for name in order
    ]


def summary() -> dict:
    """The state of the last run: the tasks, the rows and the days."""
    summary = _STATE.get("summary") or run_pipeline()
    task_rows = tasks()
    return {
        "stats": {
            "tasks": summary["tasks"],
            "raw_rows": summary["raw_rows"],
            "clean_rows": summary["clean_rows"],
            "daily_rows": summary["daily_rows"],
        },
        "series": [
            {"label": row["task"], "value": row["rows"]} for row in task_rows
        ],
        "lists": {
            "tasks": task_rows,
            "history": history()[-20:][::-1],
        },
    }


def handle(method, path, payload, user):
    """The read and the write endpoints of the project."""
    if method == "GET" and path == "/api/tasks":
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
