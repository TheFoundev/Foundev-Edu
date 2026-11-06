# Flask Prediction API and Console: Understand request validation, response, and UI flow

**Lesson ID:** `lesson-05-01`  
**Module:** Flask Prediction API and Console  
**Source focus:** `src/flask_app.py` → `predict_fraud`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FraudGuard: Credit Card Fraud Detection. By the end, you can describe request validation, response, and UI flow, trace the flask prediction api and console implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about request validation, response, and UI flow. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### The response semantics

`predict_proba(X)` returns one row of probabilities per sample; the code keeps `result[1]` — the probability of class 1, i.e. fraud. For a single transaction the payload is wrapped in a one-element list so that both shapes go through the same `predict_proba` call.

**The probability is not the decision.** The service returns the raw probability; the console applies the operator's threshold:

```
score >= t      → HIGH
score >= t / 2  → MEDIUM
otherwise       → LOW
```

This is the "cost-aware thresholding" idea, implemented where the business context lives (the analyst's screen) rather than baked into the model.

Connect this explanation to `src/flask_app.py` and the source focus `predict_fraud`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.

## Step-by-step source investigation

1. Open `src/flask_app.py` and inspect `predict_fraud`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/flask_app.py` (not executed during package generation):

```python
def predict_fraud():
    input_data = request.get_json(silent=True) or {}
    if u"features" not in input_data:
        return json.dumps({u"error": u"No features found in input"}), 400
    if not input_data[u"features"] or not isinstance(input_data[u"features"], list):
        return json.dumps({u"error": u"No feature values available"}), 400
    if app.model is None:
        return json.dumps({
            u"error": u"Model not loaded",
            u"detail": u"models/model.pickle is missing. Train it first: place data/creditcard.csv then run python src/train.py",
        }), 503
    if isinstance(input_data[u"features"][0], list):
        results = app.model.predict_proba(input_data[u"features"]).tolist()
    else:
        results = app.model.predict_proba([input_data[u"features"]]).tolist()
    return json.dumps({u"scores": [result[1] for result in results]}), 200
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For flask prediction api and console, use the repository's own output format and the available test fixture where possible.

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

You can now understand request validation, response, and ui flow, identify its source location, and state a limitation. The key project-specific fact is: Understand request validation, response, and UI flow. In this repository, the claim must be grounded in the documented behavior and source paths: src/flask_app.py; index.html; js/app.js.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
