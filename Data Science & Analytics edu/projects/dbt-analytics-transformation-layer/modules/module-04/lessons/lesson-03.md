# Staging Orders and Pipeline: Test the boundary

**Lesson ID:** `dbt-analytics-transformation-layer-module-04-lesson-03`  
**Module ID:** `dbt-analytics-transformation-layer-module-04`  
**Source focus:** `src/pipeline.py` → `model_names`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Staging Orders and Pipeline.

## Beginner explanation

In plain language, staging orders and pipeline is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/pipeline.py` and locate `model_names`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `models/staging_orders.sql`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `src/pipeline.py` at lines 16–36. Source code was not executed during refinement.

### models/staging_orders.sql

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/pipeline.py

The excerpt below is the selected implementation focus.

```py
MODEL_DIR = Path(__file__).resolve().parent.parent / "models"


def model_names():
    """The models of the project, from the files in the models directory."""
    return sorted(path.stem for path in MODEL_DIR.glob("*.sql"))


def dependencies(sql):
    """The models a model needs, from the refs in its SQL."""
    return sorted(set(REF.findall(sql)))


def order_models(models=None, sql_dir=None):
    """The models in the order they have to run.

    The order comes from the ref graph, so a model only runs after the models
    it needs. A model that needs a model that is not there, and a cycle, are
    errors.
    """
    models = list(models or model_names())
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `model_names` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `model_names` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
