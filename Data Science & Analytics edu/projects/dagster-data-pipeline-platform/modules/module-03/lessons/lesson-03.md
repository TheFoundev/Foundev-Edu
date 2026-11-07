# Test code and evidence boundaries: Test the boundary

**Lesson ID:** `dagster-data-pipeline-platform-module-03-lesson-03`  
**Module ID:** `dagster-data-pipeline-platform-module-03`  
**Source focus:** `tests/test_pipeline.py` → `test_the_recency_the_frequency_and_the_monetary_are_there`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Test code and evidence boundaries.

## Beginner explanation

In plain language, test code and evidence boundaries is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `tests/test_pipeline.py` and locate `test_the_recency_the_frequency_and_the_monetary_are_there`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `tests/test_pipeline.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `tests/test_pipeline.py` at lines 58–78. Source code was not executed during refinement.

### tests/test_pipeline.py

The excerpt below is the selected implementation focus.
### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
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
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

test assertions; fixtures; limits of test evidence The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `test_the_recency_the_frequency_and_the_monetary_are_there` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `test_the_recency_the_frequency_and_the_monetary_are_there` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
