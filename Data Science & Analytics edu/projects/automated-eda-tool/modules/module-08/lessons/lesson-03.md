# Cleaning CLI and Batch Execution: Test the boundary

**Lesson ID:** `automated-eda-tool-module-08-lesson-03`  
**Module ID:** `automated-eda-tool-module-08`  
**Source focus:** `run_cleaning.py` → `run_cleaning`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Run Cleaning.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `run_cleaning.py` and locate `run_cleaning`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `run_cleaning.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `run_cleaning.py`. source tree absent; excerpt retained from earlier package

### run_cleaning.py

The excerpt below is the selected implementation focus.

```text
from autoeda.null_handler import process_csv

process_csv(
    input_path="notebooks/sample_csv/sample_input.csv",
    output_path="backend/output/cleaned_sample_input.csv"
)


process_csv(
    input_path="notebooks/sample_csv/titanic.csv",
    output_path="backend/output/cleaned_titanic.csv"
)
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-08.md`](../exercises/exercise-08.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `run_cleaning` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `run_cleaning` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
