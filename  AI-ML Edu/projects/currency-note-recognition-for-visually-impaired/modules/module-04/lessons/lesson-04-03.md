# Winner Voting and Filename Labels: Validate outputs and identify limitations for winner voting and filename labels

**Lesson ID:** `lesson-04-03`  
**Module:** Winner Voting and Filename Labels  
**Source focus:** `Currency Detection using OpenCV in ML/detect.py` → `max_val`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Note Sense: Currency Note Recognition. By the end, you can describe per-reference evidence and denomination extraction, trace the winner voting and filename labels implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about per-reference evidence and denomination extraction. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.4 Winner-takes-all voting

The number of surviving matches is a vote for that reference. Because the test photo and the
reference are photographs of the *same physical design* (same printing, same guilloche, same
portrait), the keypoints are largely repeatable, so the correct reference accumulates far more
consistent matches than the wrong ones.

The decision rule is `len(good) > max_val` with `max_val` initialised to **8**, so a reference
must produce **more than 8** good matches to be accepted — otherwise the script prints
`No Matches`.

Connect this explanation to `Currency Detection using OpenCV in ML/detect.py` and the source focus `max_val`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: There is no trained CNN or connected web API: the detector uses ORB matching against reference images; the page is static. README claims about server/detector paths conflict with the actual tree. Hard-coded paths and optional speech dependencies require repair/review.

## Step-by-step source investigation

1. Open `Currency Detection using OpenCV in ML/detect.py` and inspect `max_val`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `Currency Detection using OpenCV in ML/detect.py` (not executed during package generation):

```python
max_kp = kp2

	print(i, ' ', training_set[i], ' ', len(good))

if max_val != 8:
	print(training_set[max_pt])
	print('good matches ', max_val)

	train_img = cv2.imread(training_set[max_pt])
	img3 = cv2.drawMatchesKnn(test_img, kp1, train_img, max_kp, good, 4)
	
	note = str(training_set[max_pt])[6:-4]
	print('\nDetected denomination: Rs. ', note)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For winner voting and filename labels, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for winner voting and filename labels, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for winner voting and filename labels. In this repository, the claim must be grounded in the documented behavior and source paths: Currency Detection using OpenCV in ML/detect.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
