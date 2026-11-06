# A beginner's model of pipeline and monthly revenue

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py] and [sql/monthly_revenue.sql]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include make_orders, run, demo; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/pipeline.py`, `sql/monthly_revenue.sql`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_orders(count=500, seed=12):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- The excerpt from `sql/monthly_revenue.sql` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/pipeline.py

```text
"""Build a SQLite warehouse and execute saved BI queries."""
import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

QUERIES = ["monthly_revenue", "top_products", "region_share", "repeat_rate"]
SQL_DIR = Path(__file__).resolve().parent.parent / "sql"


def make_orders(count=500, seed=12):
    rng = np.random.default_rng(seed)
    start = pd.Timestamp("2026-01-01")
    dates = start + pd.to_timedelta(rng.integers(0, 150, count), unit="D")
    frame = pd.DataFrame({
        "order_id": np.arange(1, count + 1),
        "customer_id": rng.integers(1, 80, count),
        "order_date": dates.strftime("%Y-%m-%d"),
        "region": rng.choice(["north", "south", "east", "west"], count),
        "product": rng.choice(["widget", "gadget", "cable", "stand", "sensor"], count),
        "quantity": rng.integers(1, 5, count),
        "unit_price": np.round(rng.uniform(5, 95, count), 2),
        "status": rng.choice(["paid", "paid", "paid", "pending", "refunded"], count),
    })
    return frame


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    orders = make_orders(180 if quick else 700)
    db_path = base / "bi_warehouse.db"
    connection = sqlite3.connect(db_path)
    orders.to_sql("orders", connection, if_exists="replace", index=False)
    connection.commit()

    dashboard = {}
    for name in QUERIES:
        sql = (SQL_DIR / f"{name}.sql").read_text(encoding="utf-8").strip().rstrip(";")
        frame = pd.read_sql_query(sql, connection)
        dashboard[name] = frame.to_dict(orient="records")

    monthly = pd.DataFrame(dashboard["monthly_revenue"])
    if not monthly.empty:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, axis = plt.subplots(figsize=(7, 3.2))
        axis.bar(monthly["month"], monthly["revenue"], color="#7c3aed")
        axis.set_title("Monthly revenue")
        axis.set_ylabel("revenue")
        axis.tick_params(axis="x", rotation=30)
        fig.tight_layout()
        fig.savefig(base / "monthly_revenue.png", dpi=120)
        plt.close(fig)

    repeat = dashboard["repeat_rate"][0]["repeat_rate"] if dashboard["repeat_rate"] else 0
    total = float(orders.loc[orders["status"] == "paid", "quantity"].mul(
        orders.loc[orders["status"] == "paid", "unit_price"]).sum())
    (base / "dashboard.json").write_text(json.dumps(dashboard, indent=2), encoding="utf-8")
    return {
        "queries": len(QUERIES),
        "orders": int(len(orders)),
        "revenue": round(total, 2),
        "repeat_rate": float(repeat or 0),
        "dashboard": str(base / "dashboard.json"),
        "chart": str(base / "monthly_revenue.png"),
    }


def demo(base_dir="artifacts"):
    summary = run(quick=True, base_dir=base_dir)
    dashboard = json.loads((Path(base_dir) / "dashboard.json").read_text())
    for name in QUERIES:
        print(f"\n{name}:")
        print(pd.DataFrame(dashboard[name]).to_string(index=False))
    print(f"\nRevenue: {summary['revenue']:.2f}, repeat rate: {summary['repeat_rate']:.1f}%")

```

### sql/monthly_revenue.sql

```text
SELECT
    substr(order_date, 1, 7) AS month,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM orders
WHERE status = 'paid'
GROUP BY month
ORDER BY month

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

This lesson ties its explanation to `src/pipeline.py`, `sql/monthly_revenue.sql`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
