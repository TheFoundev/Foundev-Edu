# App and Main: Test the boundary

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-01-lesson-03`  
**Module ID:** `reddit-social-media-analytics-with-praw-module-01`  
**Source focus:** `app.py` → `_query`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: App and Main.

## Beginner explanation

In plain language, app and main is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `_query`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `app.py`, `main.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `app.py` at lines 52–72. Source code was not executed during refinement.

### app.py

The excerpt below is the selected implementation focus.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
"""


def _query(sql: str, parameters: tuple = ()) -> list[tuple]:
    """The rows of a query of the analytics database."""
    if not DB_PATH.exists():
        return []
    connection = sqlite3.connect(DB_PATH)
    try:
        return connection.execute(sql, parameters).fetchall()
    finally:
        connection.close()


def summary_payload():
    """The state of the analytics: the database the pipeline wrote.

    The engagement of a post is its score plus twice its number of
    comments, the same way the pipeline weighs it.
    """
    subreddits = _query(
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-01.md`](../exercises/exercise-01.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `_query` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `_query` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
