# Rolling-Origin Evaluation and Leakage: Understand In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time.

**Lesson ID:** `lesson-05-01`  
**Module:** Rolling-Origin Evaluation and Leakage  
**Source focus:** `src/model.py` → `rolling_origin_evaluation`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Multi-Model Time-Series Forecasting. By the end, you can describe In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time., trace the rolling-origin evaluation and leakage implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `rolling_origin_evaluation` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The series is simulated and much cleaner than real sales or traffic data.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `rolling_origin_evaluation`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def rolling_origin_evaluation(data, models, folds=3, horizon=7):
    """The models are measured on a few windows of the history.

    Every window is cut out of the history in turn, so the numbers are not
    the ones of a single lucky split.
    """
    frame = data["train"] if "train" in data else data
    total = len(frame)
    results = {name: [] for name in models}

    for fold in range(folds):
        end = total - fold * horizon
        start = max(0, end - horizon * 6)
        if end <= start:
            break
        history = frame.iloc[start:end]
        truth = frame["value"].to_numpy()[end:end + horizon]
        if len(truth) < horizon:
            continue
        for name, function in models.items():
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For rolling-origin evaluation and leakage, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-01.md`](../exercises/exercise-05-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand in a rolling-origin evaluation, each forecast is made using only observations available before that forecast time., identify its source location, and state a limitation. The key project-specific fact is: Understand In a rolling-origin evaluation, each forecast is made using only observations available before that forecast time.. In this repository, the claim must be grounded in the documented behavior and source paths: src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
