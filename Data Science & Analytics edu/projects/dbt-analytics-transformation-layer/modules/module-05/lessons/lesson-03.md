# Api Impl: Test the boundary

**Lesson ID:** `dbt-analytics-transformation-layer-module-05-lesson-03`  
**Module ID:** `dbt-analytics-transformation-layer-module-05`  
**Source focus:** `web/api_impl.py` → `state`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Api Impl.

## Beginner explanation

In plain language, api impl is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `web/api_impl.py` and locate `state`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `web/api_impl.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `web/api_impl.py` at lines 28–48. Source code was not executed during refinement.

### web/api_impl.py

The excerpt below is the selected implementation focus.

```py
_STATE: dict = {}


def state() -> dict:
    """Materialise the models and keep the manifest of the run."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        _STATE["run"] = result
        _STATE["manifest"] = manifest
    return _STATE


def models() -> list:
    """The models of the run, with the models they need and their rows."""
    return [
        {
            "model": model["name"],
            "needs": ", ".join(model["depends_on"]) or "-",
            "rows": model["rows"],
        }
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `state` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `state` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
