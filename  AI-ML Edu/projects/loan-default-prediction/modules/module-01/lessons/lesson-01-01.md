# Target Definition and Two-Stage Loss: Understand default probability and loss severity decomposition

**Lesson ID:** `lesson-01-01`  
**Module:** Target Definition and Two-Stage Loss  
**Source focus:** `models.py` → `DefaultClassifier`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Underwriting Desk: Loan Default Risk Modeling. By the end, you can describe default probability and loss severity decomposition, trace the target definition and two-stage loss implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about default probability and loss severity decomposition. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 1. The two-stage decomposition

Let `Y` be the observed loss, `1{Y > 0}` the default indicator, and `S = Y · 1{Y > 0}` the severity paid on default.

The pipeline models:

- `P(default) ≈ f₁(X)` — a binary gradient-boosting classifier.
- `E[S | X] ≈ f₂(X)` — a severity regressor trained **only** on defaulted rows.

The final expectation used for scoring is `E[Y|X] ≈ f₂(X) · 1{f₁(X) > 0.6}`.

This is a hard-threshold approximation of `E[S|X] · P(default|X]`. It is not a probability-consistent product — severity is either fully applied or not applied at all — but it is exactly the quantity the competition wanted, and it is far more stable than regressing the zero-inflated target directly, because `f₂` never wastes capacity learning "this row is zero".

The `0.6` cut is a business decision encoded as a constant. Rows at or below the cut get `loss = 0` regardless of how large `f₂` says the severity would be.

Connect this explanation to `models.py` and the source focus `DefaultClassifier`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The web UI is a heuristic demo, not the trained pipeline. The legacy training path requires missing CSV inputs and porting; no model artifact is supplied. Credit decisions need rigorous fairness, calibration, and legal review.

## Step-by-step source investigation

1. Open `models.py` and inspect `DefaultClassifier`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `models.py` (not executed during package generation):

```python
class DefaultClassifier(object):
    
    def __init__(self, clf):
        self.clf = clf
        
    def fit(self, X, y):
        yy = np.copy(y)
        yy[yy > 0] = 1.0
        self.clf.fit(X, yy)
        
    def predict(self, X):
        return self.clf.predict(X)
    
    def predict_proba(self, X):
        return self.clf.predict_proba(X)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For target definition and two-stage loss, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-01.md`](../exercises/exercise-01-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand default probability and loss severity decomposition, identify its source location, and state a limitation. The key project-specific fact is: Understand default probability and loss severity decomposition. In this repository, the claim must be grounded in the documented behavior and source paths: models.py; train_predict.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
