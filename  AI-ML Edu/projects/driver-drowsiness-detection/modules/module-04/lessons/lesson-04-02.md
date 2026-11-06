# MediaPipe/Streamlit Variants: Inspect the project implementation of mediapipe/streamlit variants

**Lesson ID:** `lesson-04-02`  
**Module:** MediaPipe/Streamlit Variants  
**Source focus:** `streamlit_app/streamlit_app.py` → `calculate_ear`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Cockpit: Driver Drowsiness Detection. By the end, you can describe different landmark indexing and browser-facing workflow, trace the mediapipe/streamlit variants implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about different landmark indexing and browser-facing workflow. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.2 The MediaPipe version is *not* the same pairing

```python
def calculate_ear(landmarks, eye_indices):
    p1, p2 = landmarks[eye_indices[1]], landmarks[eye_indices[5]]
    p3, p4 = landmarks[eye_indices[2]], landmarks[eye_indices[4]]
    p5, p6 = landmarks[eye_indices[0]], landmarks[eye_indices[3]]
    vertical1 = euclidean(p2, p4)   # (1, 4)
    vertical2 = euclidean(p3, p5)   # (2, 0)
    horizontal = euclidean(p1, p6)   # (1, 0)
    return (vertical1 + vertical2) / (2.0 * horizontal)
```

The MediaPipe implementation pairs **(1,4)** and **(2,0)** vertically and uses **(1,0)**
horizontally, whereas the dlib implementation uses **(1,5)**, **(2,4)** and **(0,3)**. The
two landmark sets are also different (68 points vs. 468), so their EAR distributions are
not identical — which is why the web app uses a different threshold (`0.25` instead of
`0.27`). Anyone re-tuning one path should not assume the constants transfer.

Connect this explanation to `streamlit_app/streamlit_app.py` and the source focus `calculate_ear`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.

## Step-by-step source investigation

1. Open `streamlit_app/streamlit_app.py` and inspect `calculate_ear`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `streamlit_app/streamlit_app.py` (not executed during package generation):

```python
def calculate_ear(landmarks, eye_indices):
    # Eye landmarks
    p1, p2 = landmarks[eye_indices[1]], landmarks[eye_indices[5]]
    p3, p4 = landmarks[eye_indices[2]], landmarks[eye_indices[4]]
    p5, p6 = landmarks[eye_indices[0]], landmarks[eye_indices[3]]

    vertical1 = euclidean(p2, p4)
    vertical2 = euclidean(p3, p5)
    horizontal = euclidean(p1, p6)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For mediapipe/streamlit variants, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-02.md`](../exercises/exercise-04-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of mediapipe/streamlit variants, identify its source location, and state a limitation. The key project-specific fact is: ### 7.2 The MediaPipe version is *not* the same pairing

```python
def calculate_ear(landmarks, eye_indices):
    p1, p2 = landmarks[eye_indices[1]], landmarks[eye_indices[5]]
    p3, p4 = landmarks[eye_indices[2]], landmarks[eye_indices[4]]
    p5, p6 = landmarks[eye_indices[0]], landmarks[eye_indices[3]]
    vertical1 = euclidean(p2, p4)   # (1, 4)
    vertical2 = euclidean(p3, p5)   # (2, 0)
    horizontal = euclidean(p1, p6)   # (1, 0)
    return (vertical1 + vertical2) / (2.0 * horizontal)
```

The MediaPipe implementation pairs **(1,4)** and **(2,0)** vertically and uses **(1,0)**
horizontally, whereas the dlib implementation uses **(1,5)**, **(2,4)** and **(0,3)**. The
two landmark sets are also different (68 points vs. 468), so their EAR distributions are
not identical — which is why the web app uses a different threshold (`0.25` instead of
`0.27`). Anyone re-tuning one path should not assume the constants transfer.

Connect this explanation to `streamlit_app/streamlit_app.py` and the source focus `calculate_ear`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
