# Read documented goals mapped to implementation in the source

**Lesson ID:** `luigi-batch-etl-orchestrator-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.py, src/pipeline.py, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `main.py`, `src/pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class Task:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, base, quick=False):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def requires(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def output(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __repr__(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text
# Luigi Batch ETL Orchestrator

A small task graph with outputs, dependencies and a local runner.

> Implement a multi-task batch ETL workflow (extract, transform, load) with Luigi including dependencies, retries, failure handling and a monitoring view.

## Overview

An original, self-contained implementation of the **Luigi Batch ETL Orchestrator** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Task classes for extract, clean, aggregate and load
- Dependency resolution through requires()
- Marker files for task outputs
- SQLite load with category totals

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Luigi is not installed, so task classes and a recursive runner implement the dependency graph locally.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
luigi-batch-etl-orchestrator/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
pytest -q
```

6 tests (`pytest -q`), up from 2.

## Notes and limitations

- There is no central scheduler or visualiser.
- Files are always rewritten; task output checks are shown but not used for skipping.
- SQLite stands in for PostgreSQL.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Execute a small task graph over synthetic sales data.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Execute a small task graph over synthetic sales data.')
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

### src/pipeline.py

```text
"""Task objects with requires/output/run methods."""
import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd


class Task:
    name = "task"

    def __init__(self, base, quick=False):
        self.base = Path(base)
        self.quick = quick

    def requires(self):
        return []

    def output(self):
        return self.base / self.name / "done.json"

    def run(self):
        raise NotImplementedError

    def __repr__(self):
        return f"<{self.name}>"


class Extract(Task):
    name = "extract"

    def run(self):
        rng = np.random.default_rng(11)
        count = 120 if self.quick else 600
        frame = pd.DataFrame({
            "order_id": np.arange(1, count + 1),
            "category": rng.choice(["books", "tools", "garden", "kitchen"], count),
            "quantity": rng.integers(1, 6, count),
            "unit_price": np.round(rng.uniform(4, 55, count), 2),
        })
        target = self.base / "extract" / "orders.csv"
        target.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(target, index=False)
        return int(len(frame))


class Clean(Task):
    name = "clean"

    def requires(self):
        return [Extract(self.base, self.quick)]

    def run(self):
        frame = pd.read_csv(self.base / "extract" / "orders.csv")
        frame = frame[(frame["quantity"] > 0) & (frame["unit_price"] > 0)].copy()
        frame["revenue"] = (frame["quantity"] * frame["unit_price"]).round(2)
        target = self.base / "clean" / "orders_clean.csv"
        target.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(target, index=False)
        return int(len(frame))


class Aggregate(Task):
    name = "aggregate"

    def requires(self):
        return [Clean(self.base, self.quick)]

    def run(self):
        frame = pd.read_csv(self.base / "clean" / "orders_clean.csv")
        summary = (
            frame.groupby("category")
            .agg(orders=("order_id", "count"), units=("quantity", "sum"), revenue=("revenue", "sum"))
            .reset_index()
        )
        summary["revenue"] = summary["revenue"].round(2)
        target = self.base / "aggregate" / "category_summary.csv"
        target.parent.mkdir(parents=True, exist_ok=True)
        summary.to_csv(target, index=False)
        return int(len(summary))


class Load(Task):
    name = "load"

    def requires(self):
        return [Aggregate(self.base, self.quick)]

    def run(self):
        frame = pd.read_csv(self.base / "aggregate" / "category_summary.csv")
        connection = sqlite3.connect(self.base / "warehouse.db")
        frame.to_sql("category_summary", connection, if_exists="replace", index=False)
        connection.commit()
        connection.close()
        return int(len(frame))


def execute(task, executed):
    for dependency in task.requires():
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

This lesson ties its explanation to `README.md`, `main.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
