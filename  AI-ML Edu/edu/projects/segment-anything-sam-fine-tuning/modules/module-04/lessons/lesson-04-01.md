# Image Encoding and Prompt Types: Understand An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment.

**Lesson ID:** `lesson-04-01`  
**Module:** Image Encoding and Prompt Types  
**Source focus:** `src/model.py` → `encode_image`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Segment Anything (SAM) Fine-tuning. By the end, you can describe An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment., trace the image encoding and prompt types implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `encode_image` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Only one bright shape per image is supported.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `encode_image`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def encode_image(image, threshold=110):
    """Turn an image into an embedding.

    The embedding holds the probability that a pixel belongs to a foreground
    object, the bright pixels of the image, and the size of the image, so the
    decoder can work on the embedding and not on the image again.
    """
    values = np.asarray(image, dtype=float)
    bright = values > threshold
    probability = np.clip((values - threshold) / max(1.0, 255.0 - threshold), 0.0, 1.0)
    labels, count = ndimage.label(bright)
    return {
        "probability": probability,
        "bright": bright,
        "labels": labels,
        "count": count,
        "shape": values.shape,
        "threshold": threshold,
    }
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For image encoding and prompt types, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-01.md`](../exercises/exercise-04-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand an image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment., identify its source location, and state a limitation. The key project-specific fact is: Understand An image encoder creates a compact representation; a point, box, or mask prompt tells a decoder which object to segment.. In this repository, the claim must be grounded in the documented behavior and source paths: src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
