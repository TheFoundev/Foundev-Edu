# Prerequisite Graph and Topic Selection: Inspect the project implementation of prerequisite graph and topic selection

**Lesson ID:** `lesson-02-02`  
**Module:** Prerequisite Graph and Topic Selection  
**Source focus:** `app.py` → `build_prerequisite_tree`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe chapter dependencies and recursive selection, trace the prerequisite graph and topic selection implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about chapter dependencies and recursive selection. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `build_prerequisite_tree` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for chapter dependencies and recursive selection. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `app.py` and inspect `build_prerequisite_tree`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def build_prerequisite_tree(selected_structure):
    import copy

    # Sort class keys by descending class number
    sorted_classes = sorted(
        selected_structure.keys(),
        key=lambda k: int(k.split('_')[1]),
        reverse=True
    )

    if not sorted_classes:
        return {}

    top_class_key = sorted_classes[0]
    result = copy.deepcopy(selected_structure[top_class_key])  # Start with topmost class chapters

    # Add class info to top level chapters
    for subject, chapters in result.items():
        for chapter in chapters:
            chapter["class"] = top_class_key
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For prerequisite graph and topic selection, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-02.md`](../exercises/exercise-02-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of prerequisite graph and topic selection, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `build_prerequisite_tree` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for chapter dependencies and recursive selection. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
