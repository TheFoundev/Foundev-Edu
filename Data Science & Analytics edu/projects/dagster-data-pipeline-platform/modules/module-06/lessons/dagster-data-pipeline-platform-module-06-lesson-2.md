# Read code review and safe change 6 in the source

**Lesson ID:** `dagster-data-pipeline-platform-module-06-lesson-2`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `tests/test_pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import ASSET_GRAPH, ASSETS, make_customers, rfm_segment, run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_every_asset_has_its_dependencies():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_duplicates_are_removed():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_log_says_what_every_asset_depends_on(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_rfm_groups_are_the_five_of_the_model():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_recency_the_frequency_and_the_monetary_are_there():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def state() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def assets(run_id: str) -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def segments() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
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

### tests/test_pipeline.py

```text
"""Tests for the asset graph and the RFM grouping."""
import sqlite3

import pandas as pd

from src.pipeline import ASSET_GRAPH, ASSETS, make_customers, rfm_segment, run, demo


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_every_asset_has_its_dependencies():
    """The graph says what every asset needs."""
    assert ASSET_GRAPH["raw_customers"] == []
    assert ASSET_GRAPH["clean_customers"] == ["raw_customers"]
    assert ASSET_GRAPH["segment_report"] == ["customer_segments"]
    # The order of the assets follows the graph.
    for asset, needs in ASSET_GRAPH.items():
        for need in needs:
            assert ASSETS.index(need) < ASSETS.index(asset)


def test_the_duplicates_are_removed():
    raw = make_customers(20, seed=1)
    clean = raw.drop_duplicates(subset=["customer_id"])
    assert len(clean) == len(raw) - 2


def test_the_log_says_what_every_asset_depends_on(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    connection = sqlite3.connect(tmp_path / "lineage.db")
    rows = connection.execute(
        "SELECT asset, run_id, upstream, rows FROM materializations"
    ).fetchall()
    connection.close()

    upstream = {row[0]: row[2] for row in rows}
    assert upstream["raw_customers"] == ""
    assert upstream["clean_customers"] == "raw_customers"
    assert upstream["segment_report"] == "customer_segments"
    assert len({row[1] for row in rows}) == 1, "one run has one id"


def test_the_rfm_groups_are_the_five_of_the_model():
    clean = make_customers(60, seed=2).drop_duplicates(subset=["customer_id"])
    segmented = rfm_segment(clean)
    groups = set(segmented["rfm_group"])

    assert groups
    assert groups <= {"champion", "loyal", "potential", "at_risk", "lost"}
    assert "champion" in groups


def test_the_recency_the_frequency_and_the_monetary_are_there():
    clean = make_customers(40, seed=3).drop_duplicates(subset=["customer_id"])
    segmented = rfm_segment(clean)

    for column in ("recency", "frequency", "monetary", "rfm_group"):
        assert column in segmented.columns
    assert (segmented["recency"] >= 0).all()
    assert (segmented["monetary"] > 0).all()


def test_the_report_counts_the_customers_of_every_group(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    report = pd.read_parquet(tmp_path / "warehouse" / "segment_report.parquet")

    assert report["customers"].sum() == summary["customers"]
    assert set(report["rfm_group"]) <= {"champion", "loyal", "potential", "at_risk", "lost"}


def test_the_assets_are_written_as_parquet(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    for asset in ASSETS:
        assert (tmp_path / "warehouse" / f"{asset}.parquet").exists()

```

### web/api_impl.py

```text
"""The API of the project: the assets of the graph and the RFM groups.

The numbers come from a real run of the asset graph: the assets are
materialised as Parquet files and every materialisation is written into the
lineage log of the run, which is where the console reads them from.
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import ASSET_GRAPH, run  # noqa: E402

#: Where the assets and the lineage log of the run are written.
BASE_DIR = ROOT / "artifacts"
LINEAGE = BASE_DIR / "lineage.db"
WAREHOUSE = BASE_DIR / "warehouse"

#: The summary of the last run, kept for the life of the process.
_STATE: dict = {}


def state() -> dict:
    """Materialise the assets and keep the summary of the run."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        _STATE["run"] = result
        _STATE["assets"] = assets(result["run_id"])
        _STATE["segments"] = segments()
    return _STATE


def assets(run_id: str) -> list:
    """The assets of the run, with the assets they need and their rows."""
    if not LINEAGE.exists():
        return []
    connection = sqlite3.connect(LINEAGE)
    rows = connection.execute(
        "SELECT asset, upstream, rows, materialized_at FROM materializations "
        "WHERE run_id = ? ORDER BY rowid",
        (run_id,),
    ).fetchall()
    connection.close()
    return [
        {
            "asset": row[0],
            "needs": row[1] or "-",
            "rows": row[2],
            "run": run_id,
        }
        for row in rows
    ]


def segments() -> list:
    """The RFM groups with the number of the customers and what they are worth."""
    path = WAREHOUSE / "segment_report.parquet"
    if not path.exists():
        return []
    report = pd.read_parquet(path)
    return [
        {
            "group": row["rfm_group"],
            "customers": int(row["customers"]),
            "avg_value": round(float(row["avg_annual_value"]), 2),
        }
        for _, row in report.iterrows()
    ]


def summary() -> dict:
    """The state of the last run: the assets, the customers and the groups."""
    current = state()
    result = current["run"]
    groups = current["segments"]
    return {
        "stats": {
            "assets": result["assets"],
            "customers": result["customers"],
            "segments": result["segments"],
            "high_value_customers": result["high_value_customers"],
        },
        "series": [
            {"label": group["group"], "value": group["customers"]} for group in groups
        ],
        "lists": {
            "assets": current["assets"],
            "segments": groups,
        },
    }


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
