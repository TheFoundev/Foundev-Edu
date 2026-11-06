# Setup, Testing, and Debugging: Understand configuration, API failures, model availability, and tests

**Lesson ID:** `lesson-07-01`  
**Module:** Setup, Testing, and Debugging  
**Source focus:** `WORKFLOW.md` → `fetch_textbooks_list`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe configuration, API failures, model availability, and tests, trace the setup, testing, and debugging implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about configuration, API failures, model availability, and tests. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `fetch_textbooks_list` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for configuration, API failures, model availability, and tests. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `app.py` and inspect `fetch_textbooks_list`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def fetch_textbooks_list(api_url):
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            return response.json()
        logger.error(f"Failed to fetch textbooks: {response.status_code}")
        return None
    except Exception as e:
        logger.error(f"Exception while fetching textbooks: {e}")
        return None
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For setup, testing, and debugging, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-07-01.md`](../exercises/exercise-07-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand configuration, api failures, model availability, and tests, identify its source location, and state a limitation. The key project-specific fact is: Understand configuration, API failures, model availability, and tests. In this repository, the claim must be grounded in the documented behavior and source paths: WORKFLOW.md; app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
