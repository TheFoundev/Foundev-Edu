# Documented goals mapped to implementation: Begin with the concept

**Lesson ID:** `data-quality-gates-with-great-expectations-module-05-lesson-01`  
**Module ID:** `data-quality-gates-with-great-expectations-module-05`  
**Source focus:** `src/pipeline.py` → `Check`

## Purpose and learning objectives

Explain documented goals mapped to implementation in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Documented goals mapped to implementation.

## Beginner explanation

In plain language, documented goals mapped to implementation is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `Check`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `README.md`, `main.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: documentation claims; implementation mapping; limitations

**Excerpt:** `src/pipeline.py` at lines 25–45. Source code was not executed during refinement.

### README.md

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

The excerpt below is the selected implementation focus.

```py
EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class Check:
    """One quality check.

    The check knows what it looks at and how bad it is when it fails, so the
    number of the failures and the rows that are thrown away are both worked
    out from it.
    """

    def __init__(self, name, severity, description=""):
        self.name = name
        self.severity = severity
        self.description = description

    def evaluate(self, frame):
        """The rows that fail the check, with the reason."""
        raise NotImplementedError
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

You moved from a plain-language model to `Check` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `Check` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
