# Online Updates, Thresholds, and Detection Delay: Inspect the project implementation of online updates, thresholds, and detection delay

**Lesson ID:** `lesson-04-02`  
**Module:** Online Updates, Thresholds, and Detection Delay  
**Source focus:** `src/model.py` → `simulate`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Streaming Anomaly Detection. By the end, you can describe An online detector updates its baseline as each value arrives and flags values far from that baseline., trace the online updates, thresholds, and detection delay implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about An online detector updates its baseline as each value arrives and flags values far from that baseline.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `simulate` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for An online detector updates its baseline as each value arrives and flags values far from that baseline.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The stream is generated, not read from NAB.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `simulate`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def simulate(values, alpha=0.08, threshold=3.2, warmup=20):
    mean = float(values[0])
    variance = 1.0
    scores = np.zeros(len(values))
    flags = np.zeros(len(values), dtype=int)

    for index, value in enumerate(values):
        difference = value - mean
        mean += alpha * difference
        variance = (1 - alpha) * (variance + alpha * difference ** 2)
        scores[index] = abs(difference) / (np.sqrt(variance) + 1e-6)
        if index >= warmup and scores[index] > threshold:
            flags[index] = 1
    return scores, flags
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For online updates, thresholds, and detection delay, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-02.md`](../exercises/exercise-04-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of online updates, thresholds, and detection delay, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `simulate` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for An online detector updates its baseline as each value arrives and flags values far from that baseline.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
