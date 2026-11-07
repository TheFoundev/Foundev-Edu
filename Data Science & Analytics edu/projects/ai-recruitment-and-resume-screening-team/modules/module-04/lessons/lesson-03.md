# Declared dependencies and runtime configuration: Test the boundary

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-04-lesson-03`  
**Module ID:** `ai-recruitment-and-resume-screening-team-module-04`  
**Source focus:** `app.py` → `candidates`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Declared dependencies and runtime configuration.

## Beginner explanation

In plain language, declared dependencies and runtime configuration is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `app.py` and locate `candidates`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `requirements.txt`, `app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: declared dependencies; configuration keys; safe setup

**Excerpt:** `app.py` at lines 58–78. Source code was not executed during refinement.

### requirements.txt

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### app.py

The excerpt below is the selected implementation focus.

```py
"""


def candidates():
    """The candidates of the database, the best score first."""
    connection = sqlite3.connect(DB_PATH)
    rows = connection.execute(
        "SELECT name, years, skills, score, shortlisted FROM candidates ORDER BY score DESC"
    ).fetchall()
    connection.close()
    return rows


def interview_questions():
    """The questions of the interview, drafted from the best candidate."""
    ranked = rank_candidates(MODEL, DATA)
    if not ranked:
        return []
    return draft_interview_questions(ranked[0][0], DATA["job_description"])
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

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

You moved from a plain-language model to `candidates` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `candidates` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
