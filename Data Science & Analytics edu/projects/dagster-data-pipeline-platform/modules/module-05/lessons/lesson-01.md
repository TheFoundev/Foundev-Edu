# Documented goals mapped to implementation: Begin with the concept

**Lesson ID:** `dagster-data-pipeline-platform-module-05-lesson-01`  
**Module ID:** `dagster-data-pipeline-platform-module-05`  
**Source focus:** `src/pipeline.py` → `make_customers`

## Purpose and learning objectives

Explain documented goals mapped to implementation in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Documented goals mapped to implementation.

## Beginner explanation

In plain language, documented goals mapped to implementation is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `make_customers`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `README.md`, `main.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: documentation claims; implementation mapping; limitations

**Excerpt:** `src/pipeline.py` at lines 34–54. Source code was not executed during refinement.

### README.md

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

The excerpt below is the selected implementation focus.

```py
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
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

documentation claims; implementation mapping; limitations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-05.md`](../exercises/exercise-05.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `make_customers` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `make_customers` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
