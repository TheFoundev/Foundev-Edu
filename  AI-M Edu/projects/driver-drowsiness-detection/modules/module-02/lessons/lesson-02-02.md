# Drowsiness State Machine: Inspect the project implementation of drowsiness state machine

**Lesson ID:** `lesson-02-02`  
**Module:** Drowsiness State Machine  
**Source focus:** `blinkDetect.py` → `checkEyeStatus`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Cockpit: Driver Drowsiness Detection. By the end, you can describe thresholds, consecutive frames, and alert state, trace the drowsiness state machine implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about thresholds, consecutive frames, and alert state. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.3 The blink/drowsiness state machine (dlib)

```
state  ──eyes closed──▶ state+1
         eyes open  ──▶ state = 0   (and blinkCount += 1 once the closure was a real blink)

if state ≤ falseBlinkLimit              → short closure, ignore
elif falseBlinkLimit ≤ state < drowsyLimit → a genuine blink
else (state ≥ drowsyLimit)              → drowsy: drowsy = 3, add_alert() every frame
```

`falseBlinkLimit = 0.15 / spf` frames, `drowsyLimit = 1.5 / spf` frames.

Two behavioural consequences worth knowing:

- **`drowsy` is a latch.** Once it is set to `3` it is never cleared by the state machine
  — only the `r` key (`blinkDetect.py:361`) sets `drowsy = 0`. So the alert overlay and
  the alarm remain active after the driver opens their eyes again, until `r` is pressed.
- **The two ranges overlap by one frame** (`state <= falseBlinkLimit` versus
  `state >= falseBlinkLimit`), and the first branch wins — harmless, but it means the
  false-blink window is `falseBlinkLimit + 1` frames wide.

Connect this explanation to `blinkDetect.py` and the source focus `checkEyeStatus`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No project-specific drowsiness model is trained; desktop geometry/state logic and the MediaPipe variant differ. A missing landmark asset or camera failure prevents operation. It is a learning prototype, not a safety-certified driver aid.

## Step-by-step source investigation

1. Open `blinkDetect.py` and inspect `checkEyeStatus`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `blinkDetect.py` (not executed during package generation):

```python
def checkEyeStatus(landmarks):
    global session_tracker, current_ear
    mask = np.zeros(frame.shape[:2], dtype = np.float32)
    
    hullLeftEye = []
    for i in range(0, len(leftEyeIndex)):
        hullLeftEye.append((landmarks[leftEyeIndex[i]][0], landmarks[leftEyeIndex[i]][1]))

    cv2.fillConvexPoly(mask, np.int32(hullLeftEye), 255)

    hullRightEye = []
    for i in range(0, len(rightEyeIndex)):
        hullRightEye.append((landmarks[rightEyeIndex[i]][0], landmarks[rightEyeIndex[i]][1]))


    cv2.fillConvexPoly(mask, np.int32(hullRightEye), 255)

    leftEAR = eye_aspect_ratio(hullLeftEye)
    rightEAR = eye_aspect_ratio(hullRightEye)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For drowsiness state machine, use the repository's own output format and the available test fixture where possible.

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

You can now inspect the project implementation of drowsiness state machine, identify its source location, and state a limitation. The key project-specific fact is: ### 7.3 The blink/drowsiness state machine (dlib)

```
state  ──eyes closed──▶ state+1
         eyes open  ──▶ state = 0   (and blinkCount += 1 once the closure was a real blink)

if state ≤ falseBlinkLimit              → short closure, ignore
elif falseBlinkLimit ≤ state < drowsyLimit → a genuine blink
else (state ≥ drowsyLimit)              → drowsy: drowsy = 3, add_alert() every frame
```

`falseBlinkLimit = 0.15 / spf` frames, `drowsyLimit = 1.5 / spf` frames.

Two behavioural consequences worth knowing:

- **`drowsy` is a latch.** Once it is set to `3` it is never cleared by the state machine
  — only the `r` key (`blinkDetect.py:361`) sets `drowsy = 0`. So the alert overlay and
  the alarm remain active after the driver opens their eyes again, until `r` is pressed.
- **The two ranges overlap by one frame** (`state <= falseBlinkLimit` versus
  `state >= falseBlinkLimit`), and the first branch wins — harmless, but it means the
  false-blink window is `falseBlinkLimit + 1` frames wide.

Connect this explanation to `blinkDetect.py` and the source focus `checkEyeStatus`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
