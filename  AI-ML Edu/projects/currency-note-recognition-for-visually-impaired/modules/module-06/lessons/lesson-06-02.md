# Accessibility, Evaluation, and Safety: Inspect the project implementation of accessibility, evaluation, and safety

**Lesson ID:** `lesson-06-02`  
**Module:** Accessibility, Evaluation, and Safety  
**Source focus:** `Currency Detection using OpenCV in ML/detect.py` → `display`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Note Sense: Currency Note Recognition. By the end, you can describe lighting, note variation, fallback cues, and no trained model, trace the accessibility, evaluation, and safety implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about lighting, note variation, fallback cues, and no trained model. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

> This project contains **no trained model**. It uses a classical computer-vision algorithm
> (**ORB feature matching**) with a nearest-neighbour ratio test. There is no training data, no
> loss function and no evaluation in the repository.

Connect this explanation to `Currency Detection using OpenCV in ML/detect.py` and the source focus `display`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.

## Step-by-step source investigation

1. Open `Currency Detection using OpenCV in ML/detect.py` and inspect `display`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `Currency Detection using OpenCV in ML/detect.py` (not executed during package generation):

```python
test_img = read_img('files/test_200_1.jpg')

# resizing must be dynamic
original = resize_img(test_img, 0.4)
display('original', original)

# keypoints and descriptors
# (kp1, des1) = orb.detectAndCompute(test_img, None)
(kp1, des1) = orb.detectAndCompute(test_img, None)

training_set = ['files/20.jpg', 'files/50.jpg', 'files/100.jpg', 'files/500.jpg','files/200.jpg','files/test_20_6.jpg']

for i in range(0, len(training_set)):
	# train image
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For accessibility, evaluation, and safety, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-02.md`](../exercises/exercise-06-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of accessibility, evaluation, and safety, identify its source location, and state a limitation. The key project-specific fact is: > This project contains **no trained model**. It uses a classical computer-vision algorithm
> (**ORB feature matching**) with a nearest-neighbour ratio test. There is no training data, no
> loss function and no evaluation in the repository.

Connect this explanation to `Currency Detection using OpenCV in ML/detect.py` and the source focus `display`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
