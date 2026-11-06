# Read pipeline in the source

**Lesson ID:** `sales-kpi-dashboard-with-plotly-dash-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include make_sales, run, demo; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `src/pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import matplotlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_sales(count=180, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""Sales KPI calculation and trend chart."""
import json
from pathlib import Path

import numpy as np
import pandas as pd


def make_sales(count=180, seed=42):
    rng = np.random.default_rng(seed)
    start = pd.Timestamp("2026-06-01")
    frame = pd.DataFrame({
        "order_id": np.arange(1, count + 1),
        "order_date": start + pd.to_timedelta(rng.integers(0, 90, count), unit="D"),
        "region": rng.choice(["north", "south", "east", "west"], count),
        "product": rng.choice(["widget", "gadget", "cable", "stand", "sensor"], count),
        "units": rng.integers(1, 6, count),
        "unit_price": np.round(rng.uniform(8, 120, count), 2),
    })
    frame["revenue"] = (frame["units"] * frame["unit_price"]).round(2)
    frame["order_date"] = frame["order_date"].dt.strftime("%Y-%m-%d")
    return frame


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    sales = make_sales(70 if quick else 360)
    sales.to_csv(base / "sales.csv", index=False)
    sales["date"] = pd.to_datetime(sales["order_date"])

    revenue = float(sales["revenue"].sum())
    orders = int(len(sales))
    aov = round(revenue / max(1, orders), 2)
    latest = sales["date"].max()
    recent = sales[sales["date"] > latest - pd.Timedelta(days=30)]
    previous = sales[(sales["date"] <= latest - pd.Timedelta(days=30)) & (sales["date"] > latest - pd.Timedelta(days=60))]
    growth = round((recent["revenue"].sum() - previous["revenue"].sum()) / max(1.0, previous["revenue"].sum()) * 100, 2)

    daily = sales.groupby("date", as_index=False)["revenue"].sum().sort_values("date")
    by_product = sales.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
    by_region = sales.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axis = plt.subplots(figsize=(8, 3.2))
    axis.plot(daily["date"], daily["revenue"], color="#0f766e", linewidth=1.8)
    axis.set_title("Daily revenue")
    axis.set_ylabel("revenue")
    axis.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(base / "revenue_trend.png", dpi=120)
    plt.close(fig)

    kpis = {
        "revenue": round(revenue, 2),
        "orders": orders,
        "aov": aov,
        "growth_pct": growth,
        "top_product": str(by_product.iloc[0]["product"]),
        "top_region": str(by_region.iloc[0]["region"]),
        "products": by_product.round(2).to_dict(orient="records"),
        "regions": by_region.round(2).to_dict(orient="records"),
    }
    (base / "kpis.json").write_text(json.dumps(kpis, indent=2), encoding="utf-8")
    return {
        "revenue": kpis["revenue"],
        "orders": orders,
        "aov": aov,
        "growth_pct": growth,
        "top_product": kpis["top_product"],
        "top_region": kpis["top_region"],
        "chart": str(base / "revenue_trend.png"),
    }


def demo(base_dir="artifacts"):
    summary = run(quick=True, base_dir=base_dir)
    print(f"Revenue: {summary['revenue']:.2f} from {summary['orders']} orders")
    print(f"Average order value: {summary['aov']:.2f}, growth: {summary['growth_pct']:.1f}%")
    print(f"Top product: {summary['top_product']}, top region: {summary['top_region']}")

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

This lesson ties its explanation to `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
