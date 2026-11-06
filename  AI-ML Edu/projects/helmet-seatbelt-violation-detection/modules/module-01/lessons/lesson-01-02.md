# Detection Versus Violation Decision: Inspect the project implementation of detection versus violation decision

**Lesson ID:** `lesson-01-02`  
**Module:** Detection Versus Violation Decision  
**Source focus:** `source/main_app.py` → `process_detections`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Signal Control Room: Helmet and Seatbelt Detection. By the end, you can describe object detection labels and downstream rules, trace the detection versus violation decision implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about object detection labels and downstream rules. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 1. Object detection — YOLOv8x

`ultralytics.YOLO` runs a single-stage detector over the whole frame. The instance is configured with:

| Parameter | Value | Effect |
|---|---|---|
| `confidence_threshold` | `0.6` | Boxes below 0.6 are discarded — high precision, lower recall |
| `iou_threshold` | `0.45` | Non-maximum-suppression IoU cutoff |
| `device` | `auto` | `cuda` → `mps` → `cpu`, resolved once in `setup_model()` |
| `model_path` | `custom_model_path` if it exists, else `"yolov8x.pt"` | Custom checkpoint wins when supplied |

`setup_model()` also runs a warm-up inference on a 640×640 zero image so the first real frame is not slowed by lazy initialisation.

Connect this explanation to `source/helmet_detection_yolo8_max_accuracy.py` and the source focus `process_detections`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.

## Step-by-step source investigation

1. Open `source/helmet_detection_yolo8_max_accuracy.py` and inspect `process_detections`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `source/helmet_detection_yolo8_max_accuracy.py` (not executed during package generation):

```python
def process_detections(self, detections: List[dict], frame: np.ndarray, camera_id: int) -> List[HelmetViolation]:
        """Process YOLOv8x detections to identify helmet violations"""
        violations = []
        
        if self.using_custom_model:
            violations = self.process_custom_helmet_detections(detections, frame, camera_id)
        else:
            violations = self.process_coco_detections(detections, frame, camera_id)
        
        return violations
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For detection versus violation decision, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-02.md`](../exercises/exercise-01-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of detection versus violation decision, identify its source location, and state a limitation. The key project-specific fact is: ### 1. Object detection — YOLOv8x

`ultralytics.YOLO` runs a single-stage detector over the whole frame. The instance is configured with:

| Parameter | Value | Effect |
|---|---|---|
| `confidence_threshold` | `0.6` | Boxes below 0.6 are discarded — high precision, lower recall |
| `iou_threshold` | `0.45` | Non-maximum-suppression IoU cutoff |
| `device` | `auto` | `cuda` → `mps` → `cpu`, resolved once in `setup_model()` |
| `model_path` | `custom_model_path` if it exists, else `"yolov8x.pt"` | Custom checkpoint wins when supplied |

`setup_model()` also runs a warm-up inference on a 640×640 zero image so the first real frame is not slowed by lazy initialisation.

Connect this explanation to `source/helmet_detection_yolo8_max_accuracy.py` and the source focus `process_detections`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
