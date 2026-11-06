# Research Signal and Look-Ahead Bias: Understand rolling mean shifted prior window and historical signal

**Lesson ID:** `lesson-03-01`  
**Module:** Research Signal and Look-Ahead Bias  
**Source focus:** `src/features/build_features.py` → `research`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TrendCast: Stock Price Trend Research. By the end, you can describe rolling mean shifted prior window and historical signal, trace the research signal and look-ahead bias implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about rolling mean shifted prior window and historical signal. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

**The core signal — `research()` (Preis et al. 2014)**

```
research(series, length=3) = series - series.rolling(length).mean().shift(1)
```

i.e. today's keyword interest minus the moving average of the previous *n* periods. The `.shift(1)` is what makes it usable: it is the deviation from trend known *before* today's observation, so the feature never leaks the current value. A positive value means search interest for the keyword is running above its own recent norm.

**The label — `target_binary(series)`**

The DJIA close series is converted to a percentage change and binarised: `1` when the index rose, `0` when it fell. This is a *direction* target — no magnitude information is modelled.

**The other engineered features**

| Function | Definition | Role |
| --- | --- | --- |
| `sma(series, length=6)` | rolling mean | Trend baseline |
| `ema(series, length=6)` | exponential moving average, `span=length`, `adjust=False` | Faster-reacting trend baseline |
| `delta(series, length=3)` | `series.diff(length)` | Absolute change over *n* periods |
| `pct_change(series, length=3)` | percen

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `src/features/build_features.py` and the source focus `research`.

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

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For research signal and look-ahead bias, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand rolling mean shifted prior window and historical signal, identify its source location, and state a limitation. The key project-specific fact is: Understand rolling mean shifted prior window and historical signal. In this repository, the claim must be grounded in the documented behavior and source paths: src/features/build_features.py; notebooks/01-cpj-machine-learning.ipynb.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
