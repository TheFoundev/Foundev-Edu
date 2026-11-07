# Pipeline: Test the boundary

**Lesson ID:** `sales-kpi-dashboard-with-plotly-dash-module-02-lesson-03`  
**Module ID:** `sales-kpi-dashboard-with-plotly-dash-module-02`  
**Source focus:** `src/pipeline.py` → `make_sales`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Pipeline.

## Beginner explanation

In plain language, pipeline is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `make_sales`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `src/pipeline.py` at lines 6–26. Source code was not executed during refinement.

### src/pipeline.py

The excerpt below is the selected implementation focus.

```py
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
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-02.md`](../exercises/exercise-02.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `make_sales` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `make_sales` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
