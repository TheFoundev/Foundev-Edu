# Capture and Identity Records: Validate outputs and identify limitations for capture and identity records

**Lesson ID:** `lesson-01-03`  
**Module:** Capture and Identity Records  
**Source focus:** `AMS_Run.py` → `take_img`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FAMS: Face Recognition Attendance System. By the end, you can describe student registration, image capture, and CSV registry, trace the capture and identity records implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about student registration, image capture, and CSV registry. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 3. Why the registry CSV is part of the model

LBPH only returns an **integer label**. The label is the enrollment number parsed out of the file name (`getImagesAndLabels`: `os.path.split(imagePath)[-1].split(".")[1]`). The human-readable name is joined in at *inference* time from `StudentDetails/StudentDetails.csv` via `df.loc[df['Enrollment'] == Id]['Name'].values`. If a row is missing from that CSV, the recognised enrollment still appears but the name column is empty.

Connect this explanation to `AMS_Run.py` and the source focus `take_img`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app uses Haar + LBPH rather than deep learning. Biometric data and attendance records need consent, access controls, retention rules, and correction paths.

## Step-by-step source investigation

1. Open `AMS_Run.py` and inspect `take_img`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `AMS_Run.py` (not executed during package generation):

```python
def take_img():
    l1 = txt.get()
    l2 = txt2.get()
    if l1 == '':
        err_screen()
    elif l2 == '':
        err_screen()
    else:
        try:
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            Enrollment = txt.get()
            Name = txt2.get()
            sampleNum = 0
            while (True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For capture and identity records, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-03.md`](../exercises/exercise-01-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for capture and identity records, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for capture and identity records. In this repository, the claim must be grounded in the documented behavior and source paths: AMS_Run.py; training.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
