# Features and Intermediate Representation: Validate outputs and identify limitations for features and intermediate representation

**Lesson ID:** `lesson-03-03`  
**Module:** Features and Intermediate Representation  
**Source focus:** `src/data.py` → `draw_face`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Facial Attribute Analysis Kiosk. By the end, you can describe Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn., trace the features and intermediate representation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `draw_face` in `src/data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The faces are drawn with rectangles and ellipses; there are no photos or real people.

## Step-by-step source investigation

1. Open `src/data.py` and inspect `draw_face`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/data.py` (not executed during package generation):

```python
def draw_face(seed=0, size=32):
    rng = np.random.default_rng(seed)
    image = rng.normal(0.86, 0.03, (size, size))
    has_glasses = bool(rng.random() < 0.5)
    smiling = bool(rng.random() < 0.5)

    yy, xx = np.mgrid[0:size, 0:size]
    face = ((xx - size / 2) ** 2 / (size * 0.32) ** 2 + (yy - size / 2) ** 2 / (size * 0.40) ** 2) <= 1
    image[face] = 0.72 + rng.normal(0, 0.02, face.sum())

    for eye_x in (int(size * 0.36), int(size * 0.64)):
        eye = (xx - eye_x) ** 2 + (yy - int(size * 0.44)) ** 2 <= 2.2 ** 2
        image[eye] = 0.18

    if has_glasses:
        for eye_x in (int(size * 0.36), int(size * 0.64)):
            ring = np.abs(np.sqrt((xx - eye_x) ** 2 + (yy - int(size * 0.44)) ** 2) - 5) < 1.1
            image[ring] = 0.1
        bridge = (np.abs(yy - int(size * 0.44)) < 1) & (xx > int(size * 0.36)) & (xx < int(size * 0.64))
        image[bridge] = 0.1
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For features and intermediate representation, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for features and intermediate representation, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for features and intermediate representation. In this repository, the claim must be grounded in the documented behavior and source paths: src/data.py; src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
