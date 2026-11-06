# A beginner's model of api impl

**Lesson ID:** `streamlit-analytics-web-app-module-03-lesson-1`

## Purpose and learning objectives

Study the implementation in [web/api_impl.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include _frame, _numbers, _monthly, _segments, _cohorts, summary, handle; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `web/api_impl.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import (  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import summary as pipeline_summary  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _frame():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _numbers():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _monthly() -> list[dict]:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _segments() -> list[dict]:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _cohorts() -> list[dict]:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### web/api_impl.py

```text
"""The API of the subscription analytics.

The numbers are the real ones: the subscriptions are the ones the project
made (or the ones it saved in artifacts/subscriptions.csv) and every number
comes from the functions of src/pipeline.py, the same ones the Streamlit page
of the project uses. The page and this API cannot disagree, because they read
the same table and the same metrics.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.pipeline import (  # noqa: E402
    CURRENT_MONTH,
    MONTHS,
    cohort_retention,
    load,
    mrr_by_month,
)
from src.pipeline import summary as pipeline_summary  # noqa: E402

#: The subscriptions of the project, read once and kept.
_CACHE: dict[str, object] = {}


def _frame():
    """The subscriptions of the project."""
    if "frame" not in _CACHE:
        _CACHE["frame"] = load(base_dir=str(ROOT / "artifacts"))
    return _CACHE["frame"]


def _numbers():
    """The metrics of the current month."""
    return pipeline_summary(_frame(), CURRENT_MONTH)


def _monthly() -> list[dict]:
    """The MRR, the customers, the new and the churned of every month."""
    monthly = mrr_by_month(_frame(), MONTHS)
    return [
        {
            "month": str(row["month"]),
            "mrr": float(row["mrr"]),
            "customers": int(row["customers"]),
            "new": int(row["new"]),
            "churned": int(row["churned"]),
        }
        for _, row in monthly.iterrows()
    ]


def _segments() -> list[dict]:
    """The MRR and the customers of every segment."""
    numbers = _numbers()
    return [
        {
            "segment": str(row["segment"]),
            "customers": int(row["customers"]),
            "mrr": float(row["mrr"]),
        }
        for row in numbers["by_segment"]
    ]


def _cohorts() -> list[dict]:
    """How much of every cohort is still there in every month."""
    cohorts = cohort_retention(_frame(), MONTHS)
    rows = []
    for _, row in cohorts.iterrows():
        entry = {"cohort": str(row["cohort"]), "customers": int(row["customers"])}
        for month in MONTHS:
            value = row.get(month)
            entry[month] = None if value is None or value != value else float(value)
        rows.append(entry)
    return rows


def summary():
    numbers = _numbers()
    monthly = _monthly()

    return {
        "stats": {
            "mrr": numbers["mrr"],
            "arr": numbers["arr"],
            "active": numbers["active"],
            "churn_rate": round(numbers["churn_rate"] * 100, 2),
        },
        "series": [
            {"label": row["month"], "value": row["mrr"]}
            for row in monthly
        ],
        "lists": {
            "monthly": monthly,
            "segments": _segments(),
            "cohorts": _cohorts(),
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

This lesson ties its explanation to `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
