# Evaluation, Consent, and Security: Understand biometric privacy, false matches, auditability, and human correction

**Lesson ID:** `lesson-06-01`  
**Module:** Evaluation, Consent, and Security  
**Source focus:** `AMS_Run.py` → `Fillattendances`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FAMS: Face Recognition Attendance System. By the end, you can describe biometric privacy, false matches, auditability, and human correction, trace the evaluation, consent, and security implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about biometric privacy, false matches, auditability, and human correction. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

This project is classical computer vision plus a classical biometric template — there is no neural network anywhere in the repository.

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

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, consent, and security, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-01.md`](../exercises/exercise-06-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand biometric privacy, false matches, auditability, and human correction, identify its source location, and state a limitation. The key project-specific fact is: Understand biometric privacy, false matches, auditability, and human correction. In this repository, the claim must be grounded in the documented behavior and source paths: AMS_Run.py; PROJECT_OVERVIEW.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
