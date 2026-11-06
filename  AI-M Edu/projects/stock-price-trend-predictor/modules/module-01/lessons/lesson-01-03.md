# Market Series and Prediction Scope: Validate outputs and identify limitations for market series and prediction scope

**Lesson ID:** `lesson-01-03`  
**Module:** Market Series and Prediction Scope  
**Source focus:** `src/features/build_features.py` → `research`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TrendCast: Stock Price Trend Research. By the end, you can describe time series, stock data, and target definitions, trace the market series and prediction scope implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about time series, stock data, and target definitions. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `research` in `src/features/build_features.py`. Use the excerpt below to trace the actual inputs, transformation, and output for time series, stock data, and target definitions. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The source is research-oriented and the UI is static; historical signals do not establish future returns. Avoid look-ahead leakage and never present outputs as investment advice.

## Step-by-step source investigation

1. Open `src/features/build_features.py` and inspect `research`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/features/build_features.py` (not executed during package generation):

```python
def research(series, length=3):
    """
    The feature which is also used in the research paper by Tobias Preis et al.

    Args:
        series (pandas.Series): Series of the Google Trends data.
        length (int, optional): Length of the moving average used in the
            calculation. Defaults to 3.

    Returns:
        pandas.Series: Series containing the feature.

    Raises:
        ValueError: If length is less than 1 or greater than the length of the
            series.
        TypeError: If `series` is not of pandas.Series type or `length` is not an
            integer.

    """
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For market series and prediction scope, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-03.md`](../exercises/exercise-01-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for market series and prediction scope, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for market series and prediction scope. In this repository, the claim must be grounded in the documented behavior and source paths: src/features/build_features.py; README.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
