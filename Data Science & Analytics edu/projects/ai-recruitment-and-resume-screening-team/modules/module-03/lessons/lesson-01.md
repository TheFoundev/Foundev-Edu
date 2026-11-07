# Test code and evidence boundaries: Begin with the concept

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-03-lesson-01`  
**Module ID:** `ai-recruitment-and-resume-screening-team-module-03`  
**Source focus:** `tests/test_pipeline.py` → `test_the_candidates_are_stored`

## Purpose and learning objectives

Explain test code and evidence boundaries in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Test code and evidence boundaries.

## Beginner explanation

In plain language, test code and evidence boundaries is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `tests/test_pipeline.py` and locate `test_the_candidates_are_stored`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `tests/test_pipeline.py`, `app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `tests/test_pipeline.py` at lines 87–107. Source code was not executed during refinement.

### tests/test_pipeline.py

The excerpt below is the selected implementation focus.
### app.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
assert metrics["shortlisted"] == int(metrics["shortlisted"])


def test_the_candidates_are_stored(tmp_path):
    data = load_data(seed=5, quick=True)
    path = tmp_path / "candidates.db"
    train(data, quick=True, db_path=str(path))

    connection = sqlite3.connect(path)
    rows = connection.execute("SELECT name, years, skills, score, shortlisted FROM candidates").fetchall()
    connection.close()

    assert len(rows) == len(data["test"])
    assert all(0 <= row[3] <= 1 for row in rows)
    assert all(row[4] in (0, 1) for row in rows)


def test_the_candidates_are_ranked(tmp_path):
    data = load_data(seed=5, quick=True)
    model, _ = train(data, quick=True, db_path=str(tmp_path / "candidates.db"))
    ranked = rank_candidates(model, data)
```

First read the signature/declared data shape; then follow the code and caller.

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

You moved from a plain-language model to `test_the_candidates_are_stored` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `test_the_candidates_are_stored` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
