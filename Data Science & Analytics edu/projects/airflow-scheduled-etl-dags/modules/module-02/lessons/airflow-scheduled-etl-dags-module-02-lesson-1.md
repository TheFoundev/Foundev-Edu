# A beginner's model of orders dag and pipeline

**Lesson ID:** `airflow-scheduled-etl-dags-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [dags/orders_dag.py] and [src/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include orders_dag, PipelineContext, __init__, raw_path, clean_path, daily_path, make_orders, extract_orders, validate_orders; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `dags/orders_dag.py`, `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `dags/orders_dag.py`, `from datetime import datetime, timedelta` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from airflow import DAG` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from airflow.operators.python import PythonOperator` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from src.pipeline import build_daily, extract_orders, load_warehouse, validate_orders` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def orders_dag():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import time` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from datetime import datetime, timezone` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class PipelineContext:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, base, connection):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def raw_path(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def clean_path(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def daily_path(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def make_orders(count=240, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### dags/orders_dag.py

```text
"""The Airflow DAG of the orders pipeline.

The file is a real Airflow DAG: `airflow` is imported at the top, so the file
is only loaded when Airflow is there. The local runner in `src/pipeline.py`
reads the same graph from `src/pipeline.py`, so the pipeline runs without
Airflow installed.

To use it with Airflow:

    export AIRFLOW_HOME=~/airflow
    airflow db init
    cp dags/orders_dag.py $AIRFLOW_HOME/dags/
    airflow dags list
"""

from datetime import datetime, timedelta

try:  # pragma: no cover - only used when Airflow is installed
    from airflow import DAG
    from airflow.operators.python import PythonOperator

    AIRFLOW_INSTALLED = True
except ImportError:  # pragma: no cover - the project runs without Airflow
    DAG = None
    PythonOperator = None
    AIRFLOW_INSTALLED = False


DAG_ID = "orders_etl"
SCHEDULE = "@daily"

#: The tasks of the DAG, and what each of them needs.
TASKS = {
    "extract_orders": [],
    "validate_orders": ["extract_orders"],
    "build_daily": ["validate_orders"],
    "load_warehouse": ["build_daily"],
}


def orders_dag():
    """The DAG of the orders pipeline.

    Every task runs the matching function of the pipeline, so the Airflow run
    and the local run do the same work.
    """
    if not AIRFLOW_INSTALLED:
        raise RuntimeError(
            "Airflow is not installed. Install it with `pip install apache-airflow` "
            "to use this DAG, or run the pipeline with `python main.py run`."
        )

    from src.pipeline import build_daily, extract_orders, load_warehouse, validate_orders

    functions = {
        "extract_orders": extract_orders,
        "validate_orders": validate_orders,
        "build_daily": build_daily,
        "load_warehouse": load_warehouse,
    }

    with DAG(
        DAG_ID,
        description="The daily orders pipeline: extract, validate, aggregate and load.",
        schedule_interval=SCHEDULE,
        start_date=datetime(2026, 1, 1),
        catchup=False,
        tags=["etl", "orders"],
    ) as dag:
        previous = None
        for name, needs in TASKS.items():
            task = PythonOperator(
                task_id=name,
                python_callable=functions[name],
                depends_on=needs or None,
                retries=2,
                retry_delay=timedelta(seconds=30),
            )
            if previous is not None and not needs:
                previous >> task
            previous = task

    return dag


#: The DAG, when Airflow is there.
dag = orders_dag() if AIRFLOW_INSTALLED else None

```

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

This lesson ties its explanation to `dags/orders_dag.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
