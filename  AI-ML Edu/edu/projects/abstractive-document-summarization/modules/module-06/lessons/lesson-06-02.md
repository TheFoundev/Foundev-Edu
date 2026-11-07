# Inference, Demo, Tests, and Responsible Limits: Inspect the project implementation of inference, demo, tests, and responsible limits

**Lesson ID:** `lesson-06-02`  
**Module:** Inference, Demo, Tests, and Responsible Limits  
**Source focus:** `app.py` → `api_summarize`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Abstractive Document Summarization. By the end, you can describe A demo presents one output; tests and limitations tell you how far that output should be trusted. Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result., trace the inference, demo, tests, and responsible limits implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about A demo presents one output; tests and limitations tell you how far that output should be trusted. Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `api_summarize` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A demo presents one output; tests and limitations tell you how far that output should be trusted. Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The brief says abstractive, but this implementation is extractive: it selects whole sentences.

## Step-by-step source investigation

1. Open `app.py` and inspect `api_summarize`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def api_summarize():
    """The summary of the text of the request."""
    payload = request.get_json(silent=True) or {}
    text = str(payload.get("text") or "")
    length = state()["model"]["max_sentences"]
    return jsonify({
        "summary": summarize(text, max_sentences=length) if text.strip() else "",
        "sentences": length,
    })
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For inference, demo, tests, and responsible limits, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-02.md`](../exercises/exercise-06-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of inference, demo, tests, and responsible limits, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `api_summarize` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A demo presents one output; tests and limitations tell you how far that output should be trusted. Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
