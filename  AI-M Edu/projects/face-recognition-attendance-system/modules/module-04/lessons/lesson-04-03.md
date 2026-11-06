# Attendance Matching and Persistence: Validate outputs and identify limitations for attendance matching and persistence

**Lesson ID:** `lesson-04-03`  
**Module:** Attendance Matching and Persistence  
**Source focus:** `AMS_Run.py` → `Fillattendances`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FAMS: Face Recognition Attendance System. By the end, you can describe thresholding, CSV attendance, and optional MySQL mirror, trace the attendance matching and persistence implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about thresholding, CSV attendance, and optional MySQL mirror. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 2. Face representation and matching — LBPH

`cv2.face.LBPHFaceRecognizer_create()` implements **Local Binary Pattern Histogram**. For each pixel the LBP operator compares it with its 8 neighbours, producing an 8-bit code. The face crop is divided into a grid of cells (the recognizer's default is 8×8 cells × 16×16 pixels), and a 256-bin histogram of the LBP codes is built per cell. Concatenating the cell histograms gives a compact descriptor that is characteristic of local texture — which is exactly what distinguishes one face from another.

Matching is done with **chi-squared distance**: the recognizer returns the nearest template and a confidence value that is a distance, so **lower is better**. The app's rule `conf < 70` is therefore a *distance* threshold, not a probability. Above the threshold the face is treated as unknown and drawn in red.

Consequences worth understanding:
- The threshold is a single global constant; it is not calibrated per user and there is no ROC analysis in the repo.
- Because the descriptor is a texture signature, training images matter a lot: the ups

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `AMS_Run.py` and the source focus `Fillattendances`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.

## Step-by-step source investigation

1. Open `AMS_Run.py` and inspect `Fillattendances`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `AMS_Run.py` (not executed during package generation):

```python
def Fillattendances():
        sub=tx.get()
        now = time.time()  ###For calculate seconds of video
        future = now + 20
        if time.time() < future:
            if sub == '':
                err_screen1()
            else:
                recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
                try:
                    recognizer.read("TrainingImageLabel\Trainner.yml")
                except:
                    e = 'Model not found,Please train model'
                    Notifica.configure(text=e, bg="red", fg="black", width=33, font=('times', 15, 'bold'))
                    Notifica.place(x=20, y=250)

                harcascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(harcascadePath)
                df = pd.read_csv("StudentDetails\StudentDetails.csv")
                cam = cv2.VideoCapture(0)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For attendance matching and persistence, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-03.md`](../exercises/exercise-04-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for attendance matching and persistence, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for attendance matching and persistence. In this repository, the claim must be grounded in the documented behavior and source paths: AMS_Run.py; testing.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
