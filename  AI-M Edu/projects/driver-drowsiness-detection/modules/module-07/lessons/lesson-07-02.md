# Debugging and Robustness: Inspect the project implementation of debugging and robustness

**Lesson ID:** `lesson-07-02`  
**Module:** Debugging and Robustness  
**Source focus:** `blinkDetect.py` → `getLandmarks`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Cockpit: Driver Drowsiness Detection. By the end, you can describe missing model asset, camera failures, and frame lifecycle, trace the debugging and robustness implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about missing model asset, camera failures, and frame lifecycle. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `getLandmarks` in `blinkDetect.py`. Use the excerpt below to trace the actual inputs, transformation, and output for missing model asset, camera failures, and frame lifecycle. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.

## Step-by-step source investigation

1. Open `blinkDetect.py` and inspect `getLandmarks`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `blinkDetect.py` (not executed during package generation):

```python
def getLandmarks(im):
    imSmall = cv2.resize(im, None, 
                            fx = 1.0/FACE_DOWNSAMPLE_RATIO, 
                            fy = 1.0/FACE_DOWNSAMPLE_RATIO, 
                            interpolation = cv2.INTER_LINEAR)

    rects = detector(imSmall, 0)
    if len(rects) == 0:
        return 0

    newRect = dlib.rectangle(int(rects[0].left() * FACE_DOWNSAMPLE_RATIO),
                            int(rects[0].top() * FACE_DOWNSAMPLE_RATIO),
                            int(rects[0].right() * FACE_DOWNSAMPLE_RATIO),
                            int(rects[0].bottom() * FACE_DOWNSAMPLE_RATIO))

    points = []
    [points.append((p.x, p.y)) for p in predictor(im, newRect).parts()]
    return points
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For debugging and robustness, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-07-02.md`](../exercises/exercise-07-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of debugging and robustness, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `getLandmarks` in `blinkDetect.py`. Use the excerpt below to trace the actual inputs, transformation, and output for missing model asset, camera failures, and frame lifecycle. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
