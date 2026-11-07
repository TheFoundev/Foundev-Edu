# Global and Local Explanations: Understand A global explanation summarizes patterns across examples; a local explanation describes one prediction.

**Lesson ID:** `lesson-04-01`  
**Module:** Global and Local Explanations  
**Source focus:** `src/model.py` → `local_explanation`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Model Explainability with SHAP. By the end, you can describe A global explanation summarizes patterns across examples; a local explanation describes one prediction., trace the global and local explanations implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about A global explanation summarizes patterns across examples; a local explanation describes one prediction.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `local_explanation` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A global explanation summarizes patterns across examples; a local explanation describes one prediction.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Permutation importance describes this model on this dataset, not causality.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `local_explanation`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def local_explanation(values, features, row, prediction, baseline):
    """Why one prediction was made.

    The features are listed with the contribution they made: a positive
    number pushed the prediction up, a negative one pulled it down.
    """
    contributions = np.asarray(values)[row]
    order = np.argsort(np.abs(contributions))[::-1]
    # The expected value of the explainer is a number, but some versions
    # hand it over as an array of one.
    baseline_value = float(np.asarray(baseline).reshape(-1)[0])
    return {
        "prediction": round(float(prediction), 4),
        "baseline": round(baseline_value, 4),
        "total": round(float(np.sum(contributions)), 4),
        "contributions": [
            {
                "feature": features[int(index)],
                "value": round(float(contributions[index]), 5),
            }
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For global and local explanations, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-01.md`](../exercises/exercise-04-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand a global explanation summarizes patterns across examples; a local explanation describes one prediction., identify its source location, and state a limitation. The key project-specific fact is: Understand A global explanation summarizes patterns across examples; a local explanation describes one prediction.. In this repository, the claim must be grounded in the documented behavior and source paths: src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
