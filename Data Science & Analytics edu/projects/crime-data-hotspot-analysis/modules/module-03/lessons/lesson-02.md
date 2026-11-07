# Declared dependencies and runtime configuration: Trace the code

**Lesson ID:** `crime-data-hotspot-analysis-module-03-lesson-02`  
**Module ID:** `crime-data-hotspot-analysis-module-03`  
**Source focus:** `requirements.txt` → `requirements`

## Purpose and learning objectives

Trace `requirements` in `requirements.txt` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Declared dependencies and runtime configuration.

## Beginner explanation

In plain language, declared dependencies and runtime configuration is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `requirements.txt` and locate `requirements`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `requirements.txt`, `app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: declared dependencies; configuration keys; safe setup

**Excerpt:** `requirements.txt`. source tree absent; excerpt retained from earlier package

### requirements.txt

The excerpt below is the selected implementation focus.
### app.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
streamlit
pandas
numpy
plotly
scikit-learn
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

declared dependencies; configuration keys; safe setup The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `requirements` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `requirements` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
