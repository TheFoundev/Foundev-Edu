# Detection Output and Unwired OCR Helpers: Validate outputs and identify limitations for detection output and unwired ocr helpers

**Lesson ID:** `lesson-03-03`  
**Module:** Detection Output and Unwired OCR Helpers  
**Source focus:** `utils/helper.py` → `filter_text`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by PlateSight: Vehicle Number Plate Recognition. By the end, you can describe bounding boxes, annotated images, and why the OCR helpers are not called, trace the detection output and unwired ocr helpers implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about bounding boxes, annotated images, and why the OCR helpers are not called. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

**The model: YOLOv5, single-stage object detection.**

YOLOv5 predicts, in one forward pass, a grid of candidate boxes with class probabilities and objectness scores; non-maximum suppression then removes duplicate boxes. The repository uses the `custom` entry point of the hub repo, which loads a checkpoint whose architecture and class map come from the checkpoint itself:

```python
model = torch.hub.load("ultralytics/yolov5", "custom", path="model/last.pt", force_reload=True)
model.eval()
model.conf = 0.5   # minimum confidence to report a detection
model.iou = 0.45   # NMS IoU threshold
results = model(img, size=640)
```

- **`model.eval()`** switches the network to inference mode (no dropout, frozen batch-norm statistics). It is the correct call for a serving path.
- **`conf = 0.5`** is the score threshold: candidates below 0.5 are discarded before NMS. It is a precision-leaning choice — for plate localisation, a missed plate is worse than a spurious box, so 0.5 is on the conservative side for an operator tool.
- **`iou = 0.45`** is the NMS overlap threshold: two boxes overlapping 

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `utils/helper.py` and the source focus `filter_text`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The repository includes YOLOv5 code and Streamlit app but model/checkpoint availability and OCR behavior need verification. Plate data is personal information; protect, minimize, and expire it.

## Step-by-step source investigation

1. Open `utils/helper.py` and inspect `filter_text`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `utils/helper.py` (not executed during package generation):

```python
def filter_text(rectangle_size, ocr_result, region_threshold):
    
    plate = [] 
    for result in ocr_result:
        length = np.sum(np.subtract(result[0][1], result[0][0]))
        height = np.sum(np.subtract(result[0][2], result[0][1]))
        
        if length*height / rectangle_size > region_threshold:
            plate.append(result[1])
    return plate
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For detection output and unwired ocr helpers, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-03.md`](../exercises/exercise-03-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for detection output and unwired ocr helpers, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for detection output and unwired ocr helpers. In this repository, the claim must be grounded in the documented behavior and source paths: utils/helper.py; app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
