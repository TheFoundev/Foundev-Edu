# Recognition Task and Reference Images: Understand denomination labels, camera input, and local reference set

**Lesson ID:** `lesson-01-01`  
**Module:** Recognition Task and Reference Images  
**Source focus:** `Currency Detection using OpenCV in ML/detect.py` → `detectAndCompute`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Note Sense: Currency Note Recognition. By the end, you can describe denomination labels, camera input, and local reference set, trace the recognition task and reference images implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about denomination labels, camera input, and local reference set. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `detectAndCompute` in `Currency Detection using OpenCV in ML/detect.py`. Use the excerpt below to trace the actual inputs, transformation, and output for denomination labels, camera input, and local reference set. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.

## Step-by-step source investigation

1. Open `Currency Detection using OpenCV in ML/detect.py` and inspect `detectAndCompute`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `Currency Detection using OpenCV in ML/detect.py` (not executed during package generation):

```python
for i in range(0, len(training_set)):
	# train image
	train_img = cv2.imread(training_set[i])

	(kp2, des2) = orb.detectAndCompute(train_img, None)

	# brute force matcher
	bf = cv2.BFMatcher()
	all_matches = bf.knnMatch(des1, des2, k=2)

	good = []
	# give an arbitrary number -> 0.789
	# if good -> append to list of good matches
	for (m, n) in all_matches:
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For recognition task and reference images, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-01.md`](../exercises/exercise-01-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand denomination labels, camera input, and local reference set, identify its source location, and state a limitation. The key project-specific fact is: Understand denomination labels, camera input, and local reference set. In this repository, the claim must be grounded in the documented behavior and source paths: Currency Detection using OpenCV in ML/detect.py; Currency Detection using OpenCV in ML/utils.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
