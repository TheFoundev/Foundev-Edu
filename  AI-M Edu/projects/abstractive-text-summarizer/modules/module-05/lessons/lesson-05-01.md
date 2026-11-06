# Shipped Flask Service and Static UI: Understand lexical overlap scoring, request flow, and model_checkpoint=false

**Lesson ID:** `lesson-05-01`  
**Module:** Shipped Flask Service and Static UI  
**Source focus:** `src/api.py` → `verify`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FactCheck Studio: Factual Consistency and Summarization. By the end, you can describe lexical overlap scoring, request flow, and model_checkpoint=false, trace the shipped flask service and static ui implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about lexical overlap scoring, request flow, and model_checkpoint=false. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `verify` in `src/api.py`. Use the excerpt below to trace the actual inputs, transformation, and output for lexical overlap scoring, request flow, and model_checkpoint=false. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The shipped Flask endpoint is deterministic lexical consistency scoring; it does not load a neural checkpoint. The research model code is a separate, older stack and no trained checkpoint is bundled. WORKFLOW statements that contradict the API/UI implementation need review.

## Step-by-step source investigation

1. Open `src/api.py` and inspect `verify`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/api.py` (not executed during package generation):

```python
def verify():
    payload = request.get_json(silent=True) or {}
    source = payload.get("text")
    claim = payload.get("claim")
    if not isinstance(source, str) or not source.strip():
        return jsonify({"error": "'text' (source document) is required and must be a non-empty string"}), 400
    if not isinstance(claim, str) or not claim.strip():
        return jsonify({"error": "'claim' is required and must be a non-empty string"}), 400

    result = analyse(source, claim)
    result["engine"] = "lexical-entailment (heuristic)"
    result["model_checkpoint"] = False
    result["disclaimer"] = ("Heuristic lexical/entailment analysis — NOT a neural "
                            "FactCC checkpoint prediction.")
    return jsonify(result), 200
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For shipped flask service and static ui, use the repository's own output format and the available test fixture where possible.

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

You can now understand lexical overlap scoring, request flow, and model_checkpoint=false, identify its source location, and state a limitation. The key project-specific fact is: Understand lexical overlap scoring, request flow, and model_checkpoint=false. In this repository, the claim must be grounded in the documented behavior and source paths: src/api.py; js/app.js; index.html.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
