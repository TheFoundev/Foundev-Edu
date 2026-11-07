# Features and Intermediate Representation: Validate outputs and identify limitations for features and intermediate representation

**Lesson ID:** `lesson-03-03`  
**Module:** Features and Intermediate Representation  
**Source focus:** `src/data.py` → `features`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Weed Species Detection. By the end, you can describe Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn., trace the features and intermediate representation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `features` in `src/data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Leaves are simple geometric shapes, not field photographs.

## Step-by-step source investigation

1. Open `src/data.py` and inspect `features`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/data.py` (not executed during package generation):

```python
def features(image):
    yy, xx = np.where(image > 70)
    if len(xx) == 0:
        return [0.0] * 7
    width = float(xx.max() - xx.min() + 1)
    height = float(yy.max() - yy.min() + 1)
    area = float(len(xx))
    return [
        area / image.size,
        width / image.shape[1],
        height / image.shape[0],
        width / max(1.0, height),
        float(image[yy, xx].mean()) / 255.0,
        float(np.std(image[yy, xx])) / 255.0,
        float(np.mean(np.abs(np.diff(image[yy, xx])))) / 255.0,
    ]
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
