# A beginner's model of test code and evidence boundaries

**Lesson ID:** `airflow-scheduled-etl-dags-module-04-lesson-1`

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

- In `tests/test_pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pytest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_order_comes_from_the_dependencies():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_order_follows_the_graph_even_when_the_tasks_are_written_in_another_order():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_task_that_needs_a_task_that_is_not_there_is_refused():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_cycle_is_refused():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_pipeline_writes_the_files(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""Tests for the orders pipeline."""
import sqlite3

import pandas as pd
import pytest

from src.pipeline import (
    DEPENDENCIES,
    TASKS,
    FUNCTIONS,
    build_daily,
    extract_orders,
    load_warehouse,
    make_orders,
    order_tasks,
    run,
    validate_orders,
    demo,
)


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


# ---------------------------------------------------------------------------
# The order of the tasks
# ---------------------------------------------------------------------------

def test_the_order_comes_from_the_dependencies():
    order = order_tasks()
    assert order.index("extract_orders") < order.index("validate_orders")
    assert order.index("validate_orders") < order.index("build_daily")
    assert order.index("build_daily") < order.index("load_warehouse")


def test_the_order_follows_the_graph_even_when_the_tasks_are_written_in_another_order():
    tasks = ["load_warehouse", "build_daily", "validate_orders", "extract_orders"]
    order = order_tasks(tasks, DEPENDENCIES)
    assert order[0] == "extract_orders"
    assert order[-1] == "load_warehouse"


def test_a_task_that_needs_a_task_that_is_not_there_is_refused():
    with pytest.raises(ValueError):
        order_tasks(["a"], {"a": ["b"]})


def test_a_cycle_is_refused():
    with pytest.raises(ValueError):
        order_tasks(["a", "b"], {"a": ["b"], "b": ["a"]})


# ---------------------------------------------------------------------------
# What the pipeline writes
# ---------------------------------------------------------------------------

def test_the_pipeline_writes_the_files(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))

    assert (tmp_path / "raw" / "orders.csv").exists()
    assert (tmp_path / "clean" / "orders_clean.csv").exists()
    assert (tmp_path / "clean" / "daily_sales.csv").exists()
    assert summary["clean_rows"] <= summary["raw_rows"]
    assert summary["daily_rows"] > 0


def test_the_clean_orders_are_the_paid_ones(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    raw = pd.read_csv(tmp_path / "raw" / "orders.csv")
    clean = pd.read_csv(tmp_path / "clean" / "orders_clean.csv")

    assert len(clean) == len(raw[raw["status"] == "paid"])
    assert (clean["revenue"] > 0).all()
    assert (clean["quantity"] > 0).all()


def test_the_revenue_of_the_day_is_the_sum_of_its_orders(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    clean = pd.read_csv(tmp_path / "clean" / "orders_clean.csv")
    daily = pd.read_csv(tmp_path / "clean" / "daily_sales.csv")

    expected = clean.groupby("order_date")["revenue"].sum().round(2)
    for _, row in daily.iterrows():
        assert round(row["revenue"], 2) == round(expected[row["order_date"]], 2)


def test_the_warehouse_holds_the_tables(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    connection = sqlite3.connect(tmp_path / "warehouse.db")

    runs = connection.execute("SELECT task, status, rows FROM task_runs").fetchall()
    assert len(runs) == len(TASKS)
    assert all(row[1] == "success" for row in runs)
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
"""A four-task orders pipeline with a DAG definition.

The tasks are ordered by the graph in `DEPENDENCIES`, not by the order they
happen to be written in, and a task that fails is retried before the run is
given up on. Every task is a function of its own, so the Airflow DAG in
`dags/orders_dag.py` and the local runner do the same work.
"""
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

DAG_ID = "orders_etl"
SCHEDULE = "@daily"
TASKS = ["extract_orders", "validate_orders", "build_daily", "load_warehouse"]
DEPENDENCIES = {
    "extract_orders": [],
    "validate_orders": ["extract_orders"],
    "build_daily": ["validate_orders"],
    "load_warehouse": ["build_daily"],
}

#: How often a task is tried again before the run is given up on.
RETRIES = 2

#: How long a task waits before it is tried again, in seconds.
RETRY_BACKOFF = 0.2


class PipelineContext:
    """What the tasks share: the paths, the warehouse and the state."""

    def __init__(self, base, connection):
        self.base = Path(base)
        self.connection = connection
        self.state = {}

    @property
    def raw_path(self):
        return self.base / "raw" / "orders.csv"

    @property
    def clean_path(self):
        return self.base / "clean" / "orders_clean.csv"

    @property
    def daily_path(self):
        return self.base / "clean" / "daily_sales.csv"


def make_orders(count=240, seed=42):
    rng = np.random.default_rng(seed)
    start = pd.Timestamp("2026-01-01")
    return pd.DataFrame({
        "order_id": np.arange(1000, 1000 + count),
        "customer_id": rng.integers(1, 80, count),
        "order_ts": start + pd.to_timedelta(rng.integers(0, 30 * 24 * 60, count), unit="m"),
        "status": rng.choice(["paid", "paid", "paid", "pending", "refunded"], count),
        "quantity": rng.integers(1, 5, count),
        "unit_price": np.round(rng.uniform(8, 90, count), 2),
    })


def extract_orders(context):
    """Read the raw orders."""
    frame = pd.read_csv(context.raw_path)
    context.state["extracted"] = len(frame)
    return len(frame)


def validate_orders(context):
    """Keep the orders that are paid and add the revenue."""
    frame = pd.read_csv(context.raw_path)
    clean = frame[
        (frame["status"] == "paid")
        & (frame["quantity"] > 0)
        & frame["customer_id"].notna()
    ].copy()
    clean["revenue"] = (clean["quantity"] * clean["unit_price"]).round(2)
    clean["order_date"] = pd.to_datetime(clean["order_ts"]).dt.date.astype(str)
    clean.to_csv(context.clean_path, index=False)
    context.state["clean"] = clean
    return len(clean)


def build_daily(context):
    """The revenue of every day."""
    clean = context.state["clean"]
    daily = (
        clean.groupby("order_date")
        .agg(orders=("order_id", "count"), revenue=("revenue", "sum"))
        .reset_index()
    )
    daily["revenue"] = daily["revenue"].round(2)
    daily.to_csv(context.daily_path, index=False)
    context.state["daily"] = daily
    return len(daily)
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
