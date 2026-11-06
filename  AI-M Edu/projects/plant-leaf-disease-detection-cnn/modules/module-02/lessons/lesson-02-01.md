# Dataset Preparation: Understand folder structure, labels, train/validation/test separation

**Lesson ID:** `lesson-02-01`  
**Module:** Dataset Preparation  
**Source focus:** `prepare_dataset.py` → `spliting data`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by LeafLens: Plant Leaf Disease Image Classification. By the end, you can describe folder structure, labels, train/validation/test separation, trace the dataset preparation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about folder structure, labels, train/validation/test separation. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `spliting data` in `Code.ipynb`. Use the excerpt below to trace the actual inputs, transformation, and output for folder structure, labels, train/validation/test separation. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Training notebook/code and Django interface exist, but required trained model artifacts are missing; current tests are stubs and do not prove inference. Field photos differ from curated data; diagnosis requires expert confirmation.

## Step-by-step source investigation

1. Open `Code.ipynb` and inspect `spliting data`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `Code.ipynb` (not executed during package generation):

```python
print("[INFO] Spliting data to train, test")
x_train, x_test, y_train, y_test = train_test_split(np_image_list, image_labels, test_size=0.2, random_state = 42)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For dataset preparation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-01.md`](../exercises/exercise-02-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand folder structure, labels, train/validation/test separation, identify its source location, and state a limitation. The key project-specific fact is: Understand folder structure, labels, train/validation/test separation. In this repository, the claim must be grounded in the documented behavior and source paths: prepare_dataset.py; Code.ipynb.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
