# A beginner's model of code review and safe change 6

**Lesson ID:** `out-of-core-dataframes-with-dask-module-06-lesson-1`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def write_partitions(base, chunks=4, rows_per_chunk=2000, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run(quick=False, base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo(base_dir="artifacts"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import demo, run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_summary_counts_the_rows_and_the_partitions(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_summary_is_written(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_top_region_is_the_biggest_one(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import pandas as pd  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import run  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _number(payload, key: str, default: int) -> int:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _read_summary() -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _partitions() -> list[dict]:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Aggregate partitioned CSV data with bounded memory.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Aggregate partitioned CSV data with bounded memory.')
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
"""Chunked groupby over partitioned input files."""
from pathlib import Path

import numpy as np
import pandas as pd


def write_partitions(base, chunks=4, rows_per_chunk=2000, seed=42):
    rng = np.random.default_rng(seed)
    input_dir = base / "input"
    input_dir.mkdir(parents=True, exist_ok=True)
    regions = np.array(["north", "south", "east", "west"])
    products = np.array(["widget", "gadget", "cable", "stand", "sensor"])
    for chunk in range(chunks):
        frame = pd.DataFrame({
            "order_id": np.arange(chunk * rows_per_chunk, (chunk + 1) * rows_per_chunk),
            "region": rng.choice(regions, rows_per_chunk),
            "product": rng.choice(products, rows_per_chunk),
            "quantity": rng.integers(1, 8, rows_per_chunk),
            "unit_price": np.round(rng.uniform(3, 45, rows_per_chunk), 2),
        })
        frame["revenue"] = (frame["quantity"] * frame["unit_price"]).round(2)
        frame.to_csv(input_dir / f"part-{chunk:03d}.csv", index=False)
    return sorted(input_dir.glob("part-*.csv"))


def run(quick=False, base_dir="artifacts"):
    base = Path(base_dir)
    base.mkdir(parents=True, exist_ok=True)
    files = write_partitions(base, 3 if quick else 12, 1500 if quick else 5000)
    partials = []
    total_rows = 0
    for path in files:
        frame = pd.read_csv(path)
        total_rows += len(frame)
        partial = (
            frame.groupby(["region", "product"])
            .agg(orders=("order_id", "count"), revenue=("revenue", "sum"))
            .reset_index()
        )
        partials.append(partial)

    combined = (
        pd.concat(partials, ignore_index=True)
        .groupby(["region", "product"], as_index=False)
        .agg(orders=("orders", "sum"), revenue=("revenue", "sum"))
    )
    combined["revenue"] = combined["revenue"].round(2)
    combined = combined.sort_values("revenue", ascending=False)
    output = base / "summary.parquet"
    try:
        combined.to_parquet(output, index=False)
        output_format = "parquet"
    except Exception:
        output = base / "summary.csv"
        combined.to_csv(output, index=False)
        output_format = "csv"

    top = combined.iloc[0]
    return {
        "input_rows": int(total_rows),
        "partitions": len(files),
        "rows_kept_in_memory": int(len(combined)),
        "top_region": str(top["region"]),
        "top_product": str(top["product"]),
        "total_revenue": round(float(combined["revenue"].sum()), 2),
        "output": str(output),
        "format": output_format,
    }


def demo(base_dir="artifacts"):
    summary = run(quick=True, base_dir=base_dir)
    print(f"Processed {summary['input_rows']} rows in {summary['partitions']} partitions.")
    print(f"Summary rows: {summary['rows_kept_in_memory']} ({summary['format']})")
    print(f"Top product: {summary['top_product']} in the {summary['top_region']} region.")
    sizes = [path.stat().st_size for path in sorted((Path(base_dir) / "input").glob("part-*.csv"))]
    print("Partition sizes (bytes):", sizes)

```

### tests/test_pipeline.py

```text
"""Tests for the out of core aggregation."""
import pandas as pd

from src.pipeline import demo, run


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_summary_counts_the_rows_and_the_partitions(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["input_rows"] > 0
    assert summary["partitions"] > 1
    assert summary["total_revenue"] > 0


def test_the_summary_is_written(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    assert (tmp_path / "summary.csv").exists() or (tmp_path / "summary.parquet").exists()


def test_the_top_region_is_the_biggest_one(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["top_region"]
    assert summary["top_product"]

```

### web/api_impl.py

```text
"""The API of the out-of-core aggregation.

The pipeline of the project really runs: the orders are written as
partitioned CSV files, every partition is read on its own, the group-by is
done per partition and the partial results are merged, so only the small
summary is held in memory. The console reads that summary back from the file
the pipeline wrote.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402

from src.pipeline import run  # noqa: E402

#: The directory the pipeline writes to.
BASE = ROOT / "artifacts"


def _number(payload, key: str, default: int) -> int:
    """One number of the request; a query string arrives as a list."""
    value = (payload or {}).get(key, default)
    if isinstance(value, (list, tuple)):
        value = value[0] if value else default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _read_summary() -> pd.DataFrame:
    """The merged summary the pipeline wrote to disk."""
    parquet = BASE / "summary.parquet"
    if parquet.exists():
        return pd.read_parquet(parquet)
    csv = BASE / "summary.csv"
    if csv.exists():
        return pd.read_csv(csv)
    return pd.DataFrame(columns=["region", "product", "orders", "revenue"])


def _partitions() -> list[dict]:
    """The input partitions with their rows and their size on disk."""
    rows = []
    for path in sorted((BASE / "input").glob("part-*.csv")):
        with path.open() as handle:
            lines = sum(1 for _ in handle) - 1
        rows.append({"partition": path.name, "rows": lines,
                     "bytes": path.stat().st_size})
    return rows


def summary():
    result = run(quick=False, base_dir=str(BASE))
    frame = _read_summary()

    # The revenue per region, summed over the products of the region.
    per_region = frame.groupby("region")["revenue"].sum().sort_values(ascending=False)

    return {
        "stats": {
            "input_rows": result["input_rows"],
            "partitions": result["partitions"],
            "rows_in_memory": result["rows_kept_in_memory"],
            "total_revenue": result["total_revenue"],
        },
        "series": [{"label": str(region), "value": round(float(value), 2)}
                   for region, value in per_region.items()],
        "lists": {
            "summary": [
                {"region": str(row["region"]), "product": str(row["product"]),
                 "orders": int(row["orders"]), "revenue": round(float(row["revenue"]), 2)}
                for _, row in frame.head(10).iterrows()
            ],
            "partitions": _partitions(),
        },
    }


def handle(method, path, payload, user):
    if method == "POST" and path == "/api/run":
        quick = bool((payload or {}).get("quick", False))
        result = run(quick=quick, base_dir=str(BASE))
        return 200, {"run": result, "summary": summary()}

    return 404, {"error": "not found"}

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

This lesson ties its explanation to `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
