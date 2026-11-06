# KNN Matching and Ratio Test: Inspect the project implementation of knn matching and ratio test

**Lesson ID:** `lesson-03-02`  
**Module:** KNN Matching and Ratio Test  
**Source focus:** `Currency Detection using OpenCV in ML/detect.py` → `knnMatch`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Note Sense: Currency Note Recognition. By the end, you can describe two-nearest-neighbour filtering and 0.789 cutoff, trace the knn matching and ratio test implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about two-nearest-neighbour filtering and 0.789 cutoff. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.3 Lowe's ratio test at 0.789

```python
for (m, n) in all_matches:
    if m.distance < 0.789 * n.distance:
        good.append([m])
```

A match is kept only if the best candidate is **at least ~21 % better** than the runner-up
(`1 − 0.789 ≈ 0.211`). This rejects *ambiguous* points — texture that looks similar to several
places on the reference note — which is exactly the failure mode of texture-matching approaches.
The source itself calls `0.789` “an arbitrary number”, i.e. it is a hand-tuned constant, not a
learned parameter.

Connect this explanation to `Currency Detection using OpenCV in ML/detect.py` and the source focus `knnMatch`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.

## Step-by-step source investigation

1. Open `Currency Detection using OpenCV in ML/detect.py` and inspect `knnMatch`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `Currency Detection using OpenCV in ML/detect.py` (not executed during package generation):

```python
(kp2, des2) = orb.detectAndCompute(train_img, None)

	# brute force matcher
	bf = cv2.BFMatcher()
	all_matches = bf.knnMatch(des1, des2, k=2)

	good = []
	# give an arbitrary number -> 0.789
	# if good -> append to list of good matches
	for (m, n) in all_matches:
		if m.distance < 0.789 * n.distance:
			good.append([m])

	if len(good) > max_val:
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For knn matching and ratio test, use the repository's own output format and the available test fixture where possible.

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

You can now inspect the project implementation of knn matching and ratio test, identify its source location, and state a limitation. The key project-specific fact is: ### 7.3 Lowe's ratio test at 0.789

```python
for (m, n) in all_matches:
    if m.distance < 0.789 * n.distance:
        good.append([m])
```

A match is kept only if the best candidate is **at least ~21 % better** than the runner-up
(`1 − 0.789 ≈ 0.211`). This rejects *ambiguous* points — texture that looks similar to several
places on the reference note — which is exactly the failure mode of texture-matching approaches.
The source itself calls `0.789` “an arbitrary number”, i.e. it is a hand-tuned constant, not a
learned parameter.

Connect this explanation to `Currency Detection using OpenCV in ML/detect.py` and the source focus `knnMatch`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
