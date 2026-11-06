# LBPH Face Representation: Understand local binary patterns and trained recognizer

**Lesson ID:** `lesson-03-01`  
**Module:** LBPH Face Representation  
**Source focus:** `AMS_Run.py` → `trainimg`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FAMS: Face Recognition Attendance System. By the end, you can describe local binary patterns and trained recognizer, trace the lbph face representation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about local binary patterns and trained recognizer. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 2. Face representation and matching — LBPH

`cv2.face.LBPHFaceRecognizer_create()` implements **Local Binary Pattern Histogram**. For each pixel the LBP operator compares it with its 8 neighbours, producing an 8-bit code. The face crop is divided into a grid of cells (the recognizer's default is 8×8 cells × 16×16 pixels), and a 256-bin histogram of the LBP codes is built per cell. Concatenating the cell histograms gives a compact descriptor that is characteristic of local texture — which is exactly what distinguishes one face from another.

Matching is done with **chi-squared distance**: the recognizer returns the nearest template and a confidence value that is a distance, so **lower is better**. The app's rule `conf < 70` is therefore a *distance* threshold, not a probability. Above the threshold the face is treated as unknown and drawn in red.

Consequences worth understanding:
- The threshold is a single global constant; it is not calibrated per user and there is no ROC analysis in the repo.
- Because the descriptor is a texture signature, training images matter a lot: the ups

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `AMS_Run.py` and the source focus `trainimg`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.

## Step-by-step source investigation

1. Open `AMS_Run.py` and inspect `trainimg`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `AMS_Run.py` (not executed during package generation):

```python
def trainimg():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    global detector
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    try:
        global faces,Id
        faces, Id = getImagesAndLabels("TrainingImage")
    except Exception as e:
        l='please make "TrainingImage" folder & put Images'
        Notification.configure(text=l, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)

    recognizer.train(faces, np.array(Id))
    try:
        recognizer.save("TrainingImageLabel\Trainner.yml")
    except Exception as e:
        q='Please make "TrainingImageLabel" folder'
        Notification.configure(text=q, bg="SpringGreen3", width=50, font=('times', 18, 'bold'))
        Notification.place(x=350, y=400)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For lbph face representation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand local binary patterns and trained recognizer, identify its source location, and state a limitation. The key project-specific fact is: Understand local binary patterns and trained recognizer. In this repository, the claim must be grounded in the documented behavior and source paths: AMS_Run.py; training.py; TrainingImageLabel/Trainner.yml.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
