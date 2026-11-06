# Evaluation, Generalization, and Farm Safety: Understand class metrics, field shift, expert confirmation, and limits

**Lesson ID:** `lesson-06-01`  
**Module:** Evaluation, Generalization, and Farm Safety  
**Source focus:** `home/tests.py` → `predict`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by LeafLens: Plant Leaf Disease Image Classification. By the end, you can describe class metrics, field shift, expert confirmation, and limits, trace the evaluation, generalization, and farm safety implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about class metrics, field shift, expert confirmation, and limits. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `predict` in `home/predictor.py`. Use the excerpt below to trace the actual inputs, transformation, and output for class metrics, field shift, expert confirmation, and limits. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Training notebook/code and Django interface exist, but required trained model artifacts are missing; current tests are stubs and do not prove inference. Field photos differ from curated data; diagnosis requires expert confirmation.

## Step-by-step source investigation

1. Open `home/predictor.py` and inspect `predict`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `home/predictor.py` (not executed during package generation):

```python
def predict(file_bytes):
    if not _ensure_backend():
        raise RuntimeError("CNN backend is not ready")

    x = decode_image(file_bytes)
    if x is None:
        raise ValueError("could not decode image")

    x = np.array([x], dtype=np.float16) / 225.0
    probs = _model.predict(x, verbose=0)[0]
    idx = int(np.argmax(probs))
    name = str(_label_binarizer.classes_[idx])
    confidence = float(probs[idx])
    healthy = "healthy" in name.lower()

    return {
        "disease": name,
        "healthy": healthy,
        "confidence": confidence,
    }
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, generalization, and farm safety, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-01.md`](../exercises/exercise-06-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand class metrics, field shift, expert confirmation, and limits, identify its source location, and state a limitation. The key project-specific fact is: Understand class metrics, field shift, expert confirmation, and limits. In this repository, the claim must be grounded in the documented behavior and source paths: home/tests.py; home/predictor.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
