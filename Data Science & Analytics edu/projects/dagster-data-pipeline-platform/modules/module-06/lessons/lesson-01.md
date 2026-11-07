# Code review and safe change 6: Begin with the concept

**Lesson ID:** `dagster-data-pipeline-platform-module-06-lesson-01`  
**Module ID:** `dagster-data-pipeline-platform-module-06`  
**Source focus:** `tests/test_pipeline.py` → `test_the_recency_the_frequency_and_the_monetary_are_there`

## Purpose and learning objectives

Explain code review and safe change 6 in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Code review and safe change 6.

## Beginner explanation

In plain language, code review and safe change 6 is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `tests/test_pipeline.py` and locate `test_the_recency_the_frequency_and_the_monetary_are_there`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: call graph; failure cases; safe extension

**Excerpt:** `tests/test_pipeline.py` at lines 58–78. Source code was not executed during refinement.

### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### tests/test_pipeline.py

The excerpt below is the selected implementation focus.
### web/api_impl.py

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

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

call graph; failure cases; safe extension The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-06.md`](../exercises/exercise-06.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

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
