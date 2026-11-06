# Heuristic Violation Inference: Inspect the project implementation of heuristic violation inference

**Lesson ID:** `lesson-03-02`  
**Module:** Heuristic Violation Inference  
**Source focus:** `source/helmet_detection_yolo8_max_accuracy.py` → `process_coco_detections`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Signal Control Room: Helmet and Seatbelt Detection. By the end, you can describe COCO-path rules actually used versus custom-model path, trace the heuristic violation inference implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about COCO-path rules actually used versus custom-model path. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 3. Violation inference — COCO path (what actually runs today)

`process_coco_detections()` runs because no custom checkpoint is present:

1. **Rider association** — `find_riders_on_vehicle()` pairs each person with a motorcycle/bicycle when the box IoU exceeds **0.05** (`calculate_overlap()`) *or* when the person's vertical span overlaps the vehicle's (`person_y + person_h >= vehicle_y and person_y <= vehicle_y + vehicle_h`).
2. **Head crop** — `check_helmet_with_cv()` takes the top **25 %** of the rider's box (minimum 10 px tall) as the head region.
3. **Shape test** — `analyze_helmet_shape()` blurs with a 5×5 Gaussian, applies Canny (30, 100), takes the largest external contour, computes circularity `4πA/P²` and treats `> 0.65` as helmet-shaped (helmets are convex and rounded; faces are not).
4. **Colour test** — `analyze_helmet_color()` works in HSV: a low brightness standard deviation (`< 30`) plus moderate saturation (`50 < S < 200`) indicates a smooth, solid-coloured shell.
5. **Combination** — if shape confidence `> 0.7` the shape result wins; else if colour confidence `> 

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `source/helmet_detection_yolo8_max_accuracy.py` and the source focus `process_coco_detections`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Generic COCO weights do not reliably supply dedicated helmet/seatbelt classes; custom model path and deployed behavior differ. No automated output should be treated as enforcement evidence.

## Step-by-step source investigation

1. Open `source/helmet_detection_yolo8_max_accuracy.py` and inspect `process_coco_detections`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `source/helmet_detection_yolo8_max_accuracy.py` (not executed during package generation):

```python
def process_coco_detections(self, detections: List[dict], frame: np.ndarray, camera_id: int) -> List[HelmetViolation]:
        """Process detections from COCO pretrained model using CV analysis"""
        violations = []
        
        # Separate detections by class
        persons = [d for d in detections if d['class_name'] == 'person']
        motorcycles = [d for d in detections if d['class_name'] in ['motorcycle', 'bicycle']]
        
        # Find riders on motorcycles and check for helmets using CV
        for motorcycle in motorcycles:
            riders_on_bike = self.find_riders_on_vehicle(motorcycle, persons)
            
            for rider in riders_on_bike:
                # Use CV methods to check for helmet
                helmet_status = self.check_helmet_with_cv(frame, rider)
                
                if not helmet_status['has_helmet']:
                    violation = HelmetViolation(
                        rider_bbox=rider['bbox'],
                        helmet_bbox=None,
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For heuristic violation inference, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-02.md`](../exercises/exercise-03-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of heuristic violation inference, identify its source location, and state a limitation. The key project-specific fact is: ### 3. Violation inference — COCO path (what actually runs today)

`process_coco_detections()` runs because no custom checkpoint is present:

1. **Rider association** — `find_riders_on_vehicle()` pairs each person with a motorcycle/bicycle when the box IoU exceeds **0.05** (`calculate_overlap()`) *or* when the person's vertical span overlaps the vehicle's (`person_y + person_h >= vehicle_y and person_y <= vehicle_y + vehicle_h`).
2. **Head crop** — `check_helmet_with_cv()` takes the top **25 %** of the rider's box (minimum 10 px tall) as the head region.
3. **Shape test** — `analyze_helmet_shape()` blurs with a 5×5 Gaussian, applies Canny (30, 100), takes the largest external contour, computes circularity `4πA/P²` and treats `> 0.65` as helmet-shaped (helmets are convex and rounded; faces are not).
4. **Colour test** — `analyze_helmet_color()` works in HSV: a low brightness standard deviation (`< 30`) plus moderate saturation (`50 < S < 200`) indicates a smooth, solid-coloured shell.
5. **Combination** — if shape confidence `> 0.7` the shape result wins; else if colour confidence `> 

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `source/helmet_detection_yolo8_max_accuracy.py` and the source focus `process_coco_detections`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
