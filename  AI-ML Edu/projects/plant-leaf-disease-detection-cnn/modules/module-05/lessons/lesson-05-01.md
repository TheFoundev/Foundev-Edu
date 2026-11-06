# Django Inference Path and Missing Assets: Understand views, predictor, routes, stub tests, and absent production model

**Lesson ID:** `lesson-05-01`  
**Module:** Django Inference Path and Missing Assets  
**Source focus:** `home/views.py` → `predict`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by LeafLens: Plant Leaf Disease Image Classification. By the end, you can describe views, predictor, routes, stub tests, and absent production model, trace the django inference path and missing assets implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about views, predictor, routes, stub tests, and absent production model. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `predict` in `home/views.py`. Use the excerpt below to trace the actual inputs, transformation, and output for views, predictor, routes, stub tests, and absent production model. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Training notebook/code and Django interface exist, but required trained model artifacts are missing; current tests are stubs and do not prove inference. Field photos differ from curated data; diagnosis requires expert confirmation.

## Step-by-step source investigation

1. Open `home/views.py` and inspect `predict`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `home/views.py` (not executed during package generation):

```python
def predict(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only", "ready": _ensure_backend()}, status=405)
    if "leaf_image" not in request.FILES:
        return JsonResponse({"error": "no leaf_image uploaded", "ready": _ensure_backend()}, status=400)
    upload = request.FILES["leaf_image"]
    try:
        result = predict_leaf(upload.read())
    except RuntimeError as exc:
        return JsonResponse({"error": str(exc), "ready": False}, status=503)
    except Exception as exc:  # noqa: BLE001
        return JsonResponse({"error": str(exc), "ready": True}, status=500)
    result["ready"] = True
    return JsonResponse(result)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For django inference path and missing assets, use the repository's own output format and the available test fixture where possible.

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

You can now understand views, predictor, routes, stub tests, and absent production model, identify its source location, and state a limitation. The key project-specific fact is: Understand views, predictor, routes, stub tests, and absent production model. In this repository, the claim must be grounded in the documented behavior and source paths: home/views.py; home/urls.py; home/predictor.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
