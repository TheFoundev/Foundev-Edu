# Weights, Evaluation, and Error Analysis: Validate outputs and identify limitations for weights, evaluation, and error analysis

**Lesson ID:** `lesson-05-03`  
**Module:** Weights, Evaluation, and Error Analysis  
**Source focus:** `source/helmet_detection_yolo8_max_accuracy.py` → `is_model_ready`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Signal Control Room: Helmet and Seatbelt Detection. By the end, you can describe missing/custom weights, class coverage, and video conditions, trace the weights, evaluation, and error analysis implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about missing/custom weights, class coverage, and video conditions. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 2. Violation inference — custom-model path

`process_custom_helmet_detections()` assumes the class set `person, helmet, no_helmet, motorcycle, bicycle` (exactly the contents of `helmet.names`):

- **Direct rule** — every `no_helmet` box becomes a `no_helmet_detected` violation.
- **Geometric rule** — for each `person`, `is_near_vehicle()` checks whether a motorcycle/bicycle centre is within **120 px**; if so, `has_nearby_helmet()` checks whether a `helmet` box centre is within **100 px** of the person's head point (`x + w/2`, `y + 0.15h`). No nearby helmet ⇒ `person_no_helmet` violation.

The 120 px / 100 px radii are fixed pixel constants, so the rule is **resolution-dependent** — at 1080p the same physical gap maps to more pixels than at 720p.

Connect this explanation to `source/helmet_detection_yolo8_max_accuracy.py` and the source focus `is_model_ready`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.

## Step-by-step source investigation

1. Open `source/helmet_detection_yolo8_max_accuracy.py` and inspect `is_model_ready`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `source/helmet_detection_yolo8_max_accuracy.py` (not executed during package generation):

```python
def is_model_ready(self) -> bool:
        """Check if model is ready for detection"""
        return self.model is not None
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For weights, evaluation, and error analysis, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-03.md`](../exercises/exercise-05-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for weights, evaluation, and error analysis, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for weights, evaluation, and error analysis. In this repository, the claim must be grounded in the documented behavior and source paths: source/helmet_detection_yolo8_max_accuracy.py; WORKFLOW.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
