# Features and Intermediate Representation: Understand Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.

**Lesson ID:** `lesson-03-01`  
**Module:** Features and Intermediate Representation  
**Source focus:** `src/data.py` → `make_stream`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Streaming Anomaly Detection. By the end, you can describe Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn., trace the features and intermediate representation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `make_stream` in `src/data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The stream is generated, not read from NAB.

## Step-by-step source investigation

1. Open `src/data.py` and inspect `make_stream`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/data.py` (not executed during package generation):

```python
def make_stream(count=600, seed=42):
    rng = np.random.default_rng(seed)
    index = np.arange(count)
    base = 50 + 0.02 * index + 3 * np.sin(index / 20)
    values = base + rng.normal(0, 1.2, count)
    labels = np.zeros(count, dtype=int)
    for center in (90, 180, 300, 410, 520):
        width = int(rng.integers(3, 7))
        amplitude = float(rng.choice([-1, 1]) * rng.uniform(8, 15))
        values[center:center + width] += amplitude
        labels[center:center + width] = 1
    return {"values": values, "labels": labels, "timestamps": index}
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For features and intermediate representation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn., identify its source location, and state a limitation. The key project-specific fact is: Understand Features are the measurements or encoded representations the algorithm can use; their shape determines what the model can learn.. In this repository, the claim must be grounded in the documented behavior and source paths: src/data.py; src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
