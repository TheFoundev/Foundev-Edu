# Read documented goals mapped to implementation in the source

**Lesson ID:** `dagster-data-pipeline-platform-module-05-lesson-2`

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
- In `src/pipeline.py`, `import uuid` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from datetime import datetime, timezone` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def make_customers(count=120, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def rfm_segment(clean, today=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def group(row):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _quintile(series, ascending=True):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### README.md

```text
# Dagster Data Pipeline Platform

An asset-oriented customer pipeline with lineage logging.

> Build a software-defined data platform with Dagster assets, schedules, sensors and lineage for a multi-source analytics pipeline.

## Overview

An original, self-contained implementation of the **Dagster Data Pipeline Platform** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The assets depend on each other, and the materialisation log says which
  asset depends on which and which run it belongs to
- The customers are grouped with the RFM model: how recently they signed up,
  how often they order and what they are worth, scored by their fifth
- The assets are written as Parquet files

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Dagster is not installed, so the asset graph is executed by a small local runner and lineage is stored in SQLite.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
dagster-data-pipeline-platform/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
```bash
pytest -q
```

8 tests: the graph of the assets, that the duplicates are removed, that the
log holds the dependencies and one run id per run, the RFM groups and the
report of the groups.
```

## Notes and limitations

- The asset graph is executed by a plain function, not a Dagster daemon.
- SQLite stores lineage metadata; the warehouse tables are local Parquet files.
- There is no scheduling, partitioning or backfill UI.

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
    parser = argparse.ArgumentParser(description='Materialise customer assets and record lineage.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Materialise customer assets and record lineage.')
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
"""A small asset graph with a materialisation log.

The assets depend on each other, the log says which asset depends on which,
and the customers are grouped with the RFM model: how recently they bought,
how often they buy and how much they are worth.
"""
import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

#: The assets of the pipeline and the assets they need.
ASSET_GRAPH = {
    "raw_customers": [],
    "clean_customers": ["raw_customers"],
    "customer_segments": ["clean_customers"],
    "segment_report": ["customer_segments"],
}

#: The assets, in the order they are materialised.
ASSETS = list(ASSET_GRAPH)

#: The score of every RFM group: the number of the group and its share.
RFM_GROUPS = {
    "champion": (1, 0),
    "loyal": (2, 1),
    "potential": (3, 2),
    "at_risk": (4, 3),
    "lost": (5, 4),
}


def make_customers(count=120, seed=42):
    rng = np.random.default_rng(seed)
    countries = np.array(["CA", "US", "UK", "DE", "FR", "unknown"])
    frame = pd.DataFrame({
        "customer_id": np.arange(1, count + 1),
        "country": rng.choice(countries, count, p=[0.35, 0.25, 0.15, 0.1, 0.1, 0.05]),
        "signup_date": pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 420, count), unit="D"),
        "monthly_spend": np.round(rng.gamma(2.2, 24, count), 2),
        "orders_last_year": rng.integers(1, 18, count),
        "churned": rng.choice([0, 1], count, p=[0.78, 0.22]),
    })
    # Add a couple of duplicate rows so the clean asset has work to do.
    return pd.concat([frame, frame.iloc[:2]], ignore_index=True)


def rfm_segment(clean, today=None):
    """The RFM group of every customer.

    The recency is the number of days since the customer signed up, the
    frequency is the number of orders and the monetary value is what they
    spend in a year. Every one of the three is scored from one to five by
    its fifth, and the three scores are put together into the groups of the
    model.
    """
    today = today or pd.Timestamp("2026-04-01")
    frame = clean.copy()
    frame["recency"] = (pd.Timestamp(today) - pd.to_datetime(frame["signup_date"])).dt.days
    frame["frequency"] = frame["orders_last_year"]
    frame["monetary"] = frame["monthly_spend"] * 12

    frame["r_score"] = _quintile(frame["recency"], ascending=False)
    frame["f_score"] = _quintile(frame["frequency"], ascending=True)
    frame["m_score"] = _quintile(frame["monetary"], ascending=True)

    def group(row):
        r, f, m = row["r_score"], row["f_score"], row["m_score"]
        if r >= 4 and f >= 4 and m >= 4:
            return "champion"
        if f >= 3 and m >= 3:
            return "loyal"
        if r >= 4:
            return "potential"
        if r <= 2 and f >= 3:
            return "at_risk"
        return "lost"

    frame["rfm_group"] = frame.apply(group, axis=1)
    return frame


def _quintile(series, ascending=True):
    """The score of every value, from one to five, by its fifth."""
    ranked = series.rank(ascending=ascending, method="dense")
    try:
        groups = pd.qcut(ranked, 5, labels=False, duplicates="drop")
        return pd.Series(groups, index=series.index).fillna(1).astype(int) + 1
    except ValueError:
        # There are fewer values than fifths, so everybody gets the same.
        return pd.Series([3] * len(series), index=series.index)


def run(quick=False, base_dir="artifacts"):
    """Materialise every asset and write the lineage."""
    base = Path(base_dir)
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
