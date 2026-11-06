# Signals and Eye Aspect Ratio: Understand facial landmarks and geometric signal

**Lesson ID:** `lesson-01-01`  
**Module:** Signals and Eye Aspect Ratio  
**Source focus:** `blinkDetect.py` → `eye_aspect_ratio`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Cockpit: Driver Drowsiness Detection. By the end, you can describe facial landmarks and geometric signal, trace the signals and eye aspect ratio implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about facial landmarks and geometric signal. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.1 Eye Aspect Ratio (dlib version)

```python
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])   # vertical distance, pair 1
    B = dist.euclidean(eye[2], eye[4])   # vertical distance, pair 2
    C = dist.euclidean(eye[0], eye[3])   # horizontal distance (eye width)
    ear = (A + B) / (2.0 * C)
    return ear
```

Properties that make this the standard metric (Soukupová & Čech, 2016):

- **Scale invariant** — `C` normalises for face size and distance.
- **Aspect-based** — only the *ratio* of vertical to horizontal extent matters.
- **Monotone in eye openness** — the value falls smoothly as the lids close, which is
  what allows a single threshold to separate open from closed.
- **Cheap** — three Euclidean distances per eye, i.e. six per frame.

`eye` here is the convex hull of the six dlib eye points: `leftEyeIndex = [36..41]`,
`rightEyeIndex = [42..47]`. The per-eye values are averaged:
`ear = (leftEAR + rightEAR) / 2.0` (`blinkDetect.py:145-148`).

Connect this explanation to `blinkDetect.py` and the source focus `eye_aspect_ratio`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.

## Step-by-step source investigation

1. Open `blinkDetect.py` and inspect `eye_aspect_ratio`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `blinkDetect.py` (not executed during package generation):

```python
def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)

    return ear
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For signals and eye aspect ratio, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-01.md`](../exercises/exercise-01-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand facial landmarks and geometric signal, identify its source location, and state a limitation. The key project-specific fact is: Understand facial landmarks and geometric signal. In this repository, the claim must be grounded in the documented behavior and source paths: blinkDetect.py; PROJECT_OVERVIEW.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
