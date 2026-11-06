# A beginner's model of test code and evidence boundaries

**Lesson ID:** `luigi-batch-etl-orchestrator-module-03-lesson-1`

## Purpose and learning objectives

Read test implementations tests/test_pipeline.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import Aggregate, Clean, Extract, Load, Task, demo, execute, run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_task_knows_what_it_needs_and_where_its_output_is(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_tasks_run_in_the_order_of_the_dependencies(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_task_runs_the_tasks_it_needs_first(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_every_task_writes_its_marker(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_output_is_written(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_pipeline.py

```text
"""Tests for the batch pipeline."""
import pandas as pd

from src.pipeline import Aggregate, Clean, Extract, Load, Task, demo, execute, run


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_a_task_knows_what_it_needs_and_where_its_output_is(tmp_path):
    task = Extract(base=str(tmp_path))
    assert isinstance(task.requires(), list)
    assert "extract" in str(task.output())


def test_the_tasks_run_in_the_order_of_the_dependencies(tmp_path):
    done = []
    execute(Load(base=str(tmp_path)), done)
    assert done == ["extract", "clean", "aggregate", "load"]


def test_a_task_runs_the_tasks_it_needs_first(tmp_path):
    done = []
    execute(Aggregate(base=str(tmp_path)), done)
    assert done.index("extract") < done.index("clean") < done.index("aggregate")


def test_every_task_writes_its_marker(tmp_path):
    done = []
    execute(Load(base=str(tmp_path)), done)
    for name in done:
        assert list(tmp_path.rglob(f"{name}/done.json"))


def test_the_output_is_written(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    assert (tmp_path / "warehouse.db").exists()

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

This lesson ties its explanation to `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### src/pipeline.py

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

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
