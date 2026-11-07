# Declared dependencies and runtime configuration: Trace the code

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-04-lesson-02`  
**Module ID:** `reddit-social-media-analytics-with-praw-module-04`  
**Source focus:** `app.py` → `_query`

## Purpose and learning objectives

Trace `_query` in `app.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Declared dependencies and runtime configuration.

## Beginner explanation

In plain language, declared dependencies and runtime configuration is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `_query`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `requirements.txt`, `app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: declared dependencies; configuration keys; safe setup

**Excerpt:** `app.py` at lines 52–72. Source code was not executed during refinement.

### requirements.txt

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### app.py

The excerpt below is the selected implementation focus.

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

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

declared dependencies; configuration keys; safe setup The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-04.md`](../exercises/exercise-04.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

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
