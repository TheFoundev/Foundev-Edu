# Read staging orders and pipeline in the source

**Lesson ID:** `dbt-analytics-transformation-layer-module-04-lesson-2`

## Purpose and learning objectives

Study the implementation in [models/staging_orders.sql] and [src/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include model_names, dependencies, order_models, render, replace, make_raw, run; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `models/staging_orders.sql`, `src/pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `models/staging_orders.sql` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def model_names():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def dependencies(sql):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def order_models(models=None, sql_dir=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def render(sql, available):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def replace(match):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def make_raw():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### models/staging_orders.sql

```text
SELECT
    order_id,
    customer_id,
    DATE(order_ts) AS order_date,
    quantity,
    unit_price,
    ROUND(quantity * unit_price, 2) AS revenue
FROM raw_orders
WHERE status = 'paid'

```

### src/pipeline.py

```text
"""A tiny SQL model runner with ref substitution.

The order of the models comes from the `{{ ref() }}` calls in the SQL files,
not from a list that is written by hand, and the manifest says which model
depends on which.
"""
import json
import re
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

REF = re.compile(r"\{\{\s*ref\('([^']+)'\)\s*\}\}")
MODEL_DIR = Path(__file__).resolve().parent.parent / "models"


def model_names():
    """The models of the project, from the files in the models directory."""
    return sorted(path.stem for path in MODEL_DIR.glob("*.sql"))


def dependencies(sql):
    """The models a model needs, from the refs in its SQL."""
    return sorted(set(REF.findall(sql)))


def order_models(models=None, sql_dir=None):
    """The models in the order they have to run.

    The order comes from the ref graph, so a model only runs after the models
    it needs. A model that needs a model that is not there, and a cycle, are
    errors.
    """
    models = list(models or model_names())
    sql_dir = Path(sql_dir or MODEL_DIR)

    sql_of = {}
    for name in models:
        path = sql_dir / f"{name}.sql"
        if not path.exists():
            raise ValueError(f"the model {name} has no file")
        sql_of[name] = path.read_text(encoding="utf-8")

    needs = {name: dependencies(sql) for name, sql in sql_of.items()}
    for name, wanted in needs.items():
        for need in wanted:
            if need not in sql_of:
                raise ValueError(f"the model {name} needs {need}, which does not exist")

    ordered = []
    done = set()
    while len(ordered) < len(models):
        progress = False
        for name in models:
            if name in done:
                continue
            if all(need in done for need in needs[name]):
                ordered.append(name)
                done.add(name)
                progress = True
        if not progress:
            raise ValueError("the models have a cycle")
    return ordered


def render(sql, available):
    """The SQL of a model, with the refs replaced by the tables.

    A ref that names a model that is not there is an error, and not a table
    that does not exist.
    """
    def replace(match):
        name = match.group(1)
        if name not in available:
            raise ValueError(f"the model needs {name}, which is not there")
        return name

    return REF.sub(replace, sql).strip().rstrip(";")


def make_raw():
    """The raw tables the models are built from."""
    rng = np.random.default_rng(7)
    customers = pd.DataFrame({
        "customer_id": np.arange(1, 41),
        "country": rng.choice(["CA", "US", "UK", "DE"], 40),
        "signup_date": pd.Timestamp("2025-06-01") + pd.to_timedelta(rng.integers(0, 180, 40), unit="D"),
    })
    orders = pd.DataFrame({
        "order_id": np.arange(1000, 1320),
        "customer_id": rng.integers(1, 41, 320),
        "order_ts": pd.Timestamp("2026-01-01") + pd.to_timedelta(rng.integers(0, 20 * 24 * 60, 320), unit="m"),
        "status": rng.choice(["paid", "paid", "paid", "pending", "refunded"], 320),
        "quantity": rng.integers(1, 4, 320),
        "unit_price": np.round(rng.uniform(6, 70, 320), 2),
    })
    return customers, orders

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

This lesson ties its explanation to `models/staging_orders.sql`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
