# Balanced Logistic Regression: Understand class_weight, decision scores, and thresholding

**Lesson ID:** `lesson-03-01`  
**Module:** Balanced Logistic Regression  
**Source focus:** `src/train.py` → `new_grid_search`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FraudGuard: Credit Card Fraud Detection. By the end, you can describe class_weight, decision scores, and thresholding, trace the balanced logistic regression implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about class_weight, decision scores, and thresholding. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `new_grid_search` in `src/train.py`. Use the excerpt below to trace the actual inputs, transformation, and output for class_weight, decision scores, and thresholding. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.

## Step-by-step source investigation

1. Open `src/train.py` and inspect `new_grid_search`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/train.py` (not executed during package generation):

```python
def new_grid_search():
    """ Create new GridSearch obj with models pipeline """
    pipeline = Pipeline([
        # TODO some smart preproc can be added here
        (u"clf", LogisticRegression(class_weight="balanced")),
    ])
    search_params = {"clf__C": (1e-4, 1e-2, 1e0, 1e2, 1e4)}
    return GridSearchCV(
        estimator=pipeline,
        param_grid=search_params,
        scoring="recall_macro",
        cv=10,
        n_jobs=-1,
        verbose=3,
    )
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For balanced logistic regression, use the repository's own output format and the available test fixture where possible.

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

You can now understand class_weight, decision scores, and thresholding, identify its source location, and state a limitation. The key project-specific fact is: Understand class_weight, decision scores, and thresholding. In this repository, the claim must be grounded in the documented behavior and source paths: src/train.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
