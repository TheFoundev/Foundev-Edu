# Read documented goals mapped to implementation in the source

**Lesson ID:** `airflow-scheduled-etl-dags-module-06-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors dags/orders_dag.py, main.py, src/pipeline.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `dags/orders_dag.py`, `main.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `dags/orders_dag.py`, `from datetime import datetime, timedelta` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from airflow import DAG` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from airflow.operators.python import PythonOperator` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `dags/orders_dag.py`, `from src.pipeline import build_daily, extract_orders, load_warehouse, validate_orders` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def orders_dag():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# Airflow Scheduled ETL DAGs

A dependency-ordered orders ETL job with a tiny Airflow-style DAG.

> Design, deploy and monitor scheduled ETL DAGs with Apache Airflow including backfills, sensors, SLAs and alerting.

## Overview

An original, self-contained implementation of the **Airflow Scheduled ETL DAGs** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A real Airflow DAG in `dags/orders_dag.py`, with the tasks, their
  dependencies, the retries and the schedule
- The local runner does the same work, so the pipeline runs without Airflow
- The order of the tasks comes from the dependency graph, not from the order
  they are written in
- A task that fails is retried, and the tasks that already ran are marked
  as rolled back
- The history of every run in the warehouse: the task, the state, the rows,
  the time and when it finished

## Stack

`Python; Airflow; Docker; PostgreSQL`

The CSV stack is Airflow + Docker + PostgreSQL. This build replaces the scheduler and database with a local runner and SQLite while keeping the same four-stage order pipeline.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
airflow-scheduled-etl-dags/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── dags/orders_dag.py       DAG metadata
```

## Testing

```bash
pytest -q
```

13 tests: the order of the tasks (from the graph, and the errors for a
missing task and a cycle), the files the pipeline writes, the revenue of the
day, the tables of the warehouse, the history, and the failure path (the
retries, the rollback and a task that works the second time).

## Notes and limitations

- There is no scheduler daemon, worker pool or Airflow UI.
- SQLite stands in for PostgreSQL and the raw file lands on local disk.
- Failures stop the run; retries and backfills are not implemented.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

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

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Run a small dependency-ordered orders pipeline.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Run a small dependency-ordered orders pipeline.')
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

This lesson ties its explanation to `README.md`, `dags/orders_dag.py`, `main.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
