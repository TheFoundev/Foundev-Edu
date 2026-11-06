# Evaluation, Reliability, and Teacher Review: Validate outputs and identify limitations for evaluation, reliability, and teacher review

**Lesson ID:** `lesson-06-03`  
**Module:** Evaluation, Reliability, and Teacher Review  
**Source focus:** `content_generate.py` → `sanitize_ollama_json`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe hallucination, curriculum validity, missing dependencies, and approval, trace the evaluation, reliability, and teacher review implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about hallucination, curriculum validity, missing dependencies, and approval. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `sanitize_ollama_json` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for hallucination, curriculum validity, missing dependencies, and approval. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `app.py` and inspect `sanitize_ollama_json`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def sanitize_ollama_json(raw_str):
    """
    Fixes malformed JSON responses from the Ollama model.
    - Removes trailing commas
    - Converts invalid answer objects to lists
    """
    # Fix trailing commas before } or ]
    raw_str = re.sub(r',\s*([\]}])', r'\1', raw_str)

    # Fix malformed 'answers' objects
    def fix_answers_block(match):
        answer_block = match.group(1)
        tokens = re.findall(r'"([^"]+)"', answer_block)
        all_items = []
        for item in tokens:
            all_items.extend([s.strip() for s in item.split(',')])
        unique_items = list(dict.fromkeys(filter(None, all_items)))
        return '"answers": ' + json.dumps(unique_items)

    raw_str = re.sub(r'"answers"\s*:\s*\[({[^}]+})\]', fix_answers_block, raw_str)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, reliability, and teacher review, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-03.md`](../exercises/exercise-06-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for evaluation, reliability, and teacher review, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for evaluation, reliability, and teacher review. In this repository, the claim must be grounded in the documented behavior and source paths: content_generate.py; app.py; PROJECT_OVERVIEW.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
