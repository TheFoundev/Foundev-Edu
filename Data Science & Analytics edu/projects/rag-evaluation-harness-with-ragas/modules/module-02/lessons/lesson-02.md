# Pipeline and Api Impl: Trace the code

**Lesson ID:** `rag-evaluation-harness-with-ragas-module-02-lesson-02`  
**Module ID:** `rag-evaluation-harness-with-ragas-module-02`  
**Source focus:** `web/api_impl.py` → `token_f1`

## Purpose and learning objectives

Trace `token_f1` in `web/api_impl.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Pipeline and Api Impl.

## Beginner explanation

In plain language, pipeline and api impl is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `web/api_impl.py` and locate `token_f1`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/pipeline.py`, `web/api_impl.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `web/api_impl.py` at lines 23–43. Source code was not executed during refinement.

### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### web/api_impl.py

The excerpt below is the selected implementation focus.

```py
extract_answer,
    retrieve,
    run,
    token_f1,
)

#: The directory the pipeline writes to.
BASE = ROOT / "artifacts"


def _number(payload, key: str, default: int) -> int:
    """One number of the request; a query string arrives as a list."""
    value = (payload or {}).get(key, default)
    if isinstance(value, (list, tuple)):
        value = value[0] if value else default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

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

You moved from a plain-language model to `token_f1` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `token_f1` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
