# Pipeline and Monthly Revenue: Test the boundary

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-02-lesson-03`  
**Module ID:** `self-hosted-bi-with-apache-superset-module-02`  
**Source focus:** `src/pipeline.py` → `make_orders`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Pipeline and Monthly Revenue.

## Beginner explanation

In plain language, pipeline and monthly revenue is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `make_orders`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/pipeline.py`, `sql/monthly_revenue.sql`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `src/pipeline.py` at lines 10–30. Source code was not executed during refinement.

### src/pipeline.py

The excerpt below is the selected implementation focus.
### sql/monthly_revenue.sql

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
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

You moved from a plain-language model to `make_orders` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `make_orders` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
