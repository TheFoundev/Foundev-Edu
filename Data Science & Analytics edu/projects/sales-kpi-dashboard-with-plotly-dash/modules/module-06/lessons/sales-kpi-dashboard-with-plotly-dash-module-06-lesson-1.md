# A beginner's model of code review and safe change 6

**Lesson ID:** `sales-kpi-dashboard-with-plotly-dash-module-06-lesson-1`

## Purpose and learning objectives

Use app.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `app.py`, `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `app.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from flask import (Flask, jsonify, render_template_string, send_file,` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from src.pipeline import run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def chart():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_console():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_assets(name):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _kpis() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import matplotlib` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_sales(count=180, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import demo, make_sales, run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_sales_are_made():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_numbers_are_worked_out(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### app.py

```text
"""A compact sales dashboard.

The dashboard of the project is still here, at `/demo`. The home page of the
site of the project, its console and the JSON API live in `web/` and are
served by this same application.
"""
import json
from pathlib import Path

from flask import (Flask, jsonify, render_template_string, send_file,
                   send_from_directory)

from src.pipeline import run

app = Flask(__name__)
run(quick=True, base_dir="artifacts")

WEB = Path(__file__).resolve().parent / "web"

PAGE = """
<!doctype html>
<title>Sales KPIs</title>
<style>
 body { font-family: system-ui, sans-serif; max-width: 900px; margin: 36px auto; color: #1f2937; }
 .cards { display: flex; gap: 14px; flex-wrap: wrap; }
 .card { border: 1px solid #e5e7eb; border-radius: 10px; padding: 14px 18px; min-width: 150px; }
 .card strong { display: block; font-size: 1.5rem; margin-top: 4px; }
 table { border-collapse: collapse; width: 100%; margin-top: 10px; }
 th, td { text-align: left; padding: 7px; border-bottom: 1px solid #e5e7eb; }
 img { max-width: 100%; margin-top: 18px; border: 1px solid #e5e7eb; }
</style>
<h1>Sales KPIs</h1>
<div class="cards">
 <div class="card">Revenue<strong>{{ '%.2f'|format(kpis.revenue) }}</strong></div>
 <div class="card">Orders<strong>{{ kpis.orders }}</strong></div>
 <div class="card">Average order<strong>{{ '%.2f'|format(kpis.aov) }}</strong></div>
 <div class="card">30-day growth<strong>{{ '%.1f'|format(kpis.growth_pct) }}%</strong></div>
</div>
<img src="/chart" alt="Daily revenue trend">
<h2>Revenue by product</h2>
<table><tr><th>Product</th><th>Revenue</th></tr>
{% for row in kpis.products %}<tr><td>{{ row.product }}</td><td>{{ '%.2f'|format(row.revenue) }}</td></tr>{% endfor %}
</table>
"""


@app.route("/demo")
def index():
    kpis = json.loads(Path("artifacts/kpis.json").read_text())
    return render_template_string(PAGE, kpis=kpis)


@app.route("/chart")
def chart():
    return send_file(Path("artifacts/revenue_trend.png"), mimetype="image/png")


# ------------------------------------------------------------------ #
# The web layer of the project                                        #
# ------------------------------------------------------------------ #

@app.route("/")
def site_index():
    """The home page of the site of the project."""
    return send_from_directory(WEB, "index.html")


@app.route("/console.html")
def site_console():
    """The console of the site of the project."""
    return send_from_directory(WEB, "console.html")


@app.route("/assets/<path:name>")
def site_assets(name):
    """The theme and the runtime of the site of the project."""
    return send_from_directory(WEB / "assets", name)


def _kpis() -> dict:
    """The KPIs of the last run of the pipeline."""
    return json.loads(Path("artifacts/kpis.json").read_text())


@app.route("/api/summary")
def api_summary():
    """The KPIs of the running instance and the revenue per product and region."""
    kpis = _kpis()
    revenue = float(kpis["revenue"]) or 1.0
    return jsonify({
        "stats": {
            "revenue": kpis["revenue"],
            "orders": kpis["orders"],
            "aov": kpis["aov"],
            "growth_pct": kpis["growth_pct"],
        },
        "series": [
            {"label": str(row["product"]), "value": float(row["revenue"])}
            for row in kpis["products"]
        ],
```

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Compute and display sales KPIs from synthetic orders.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Compute and display sales KPIs from synthetic orders.')
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

### tests/test_pipeline.py

```text
"""Tests for the KPI dashboard."""
import pandas as pd

from src.pipeline import demo, make_sales, run


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_sales_are_made():
    frame = make_sales(count=30, seed=1)
    assert len(frame) == 30
    assert "revenue" in frame.columns
    assert "order_date" in frame.columns


def test_the_numbers_are_worked_out(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["revenue"] > 0
    assert summary["orders"] > 0

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

This lesson ties its explanation to `app.py`, `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
