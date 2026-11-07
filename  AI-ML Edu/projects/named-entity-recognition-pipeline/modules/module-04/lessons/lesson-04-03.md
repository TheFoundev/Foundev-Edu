# BIO Tags, Token Features, and Entity Spans: Validate outputs and identify limitations for bio tags, token features, and entity spans

**Lesson ID:** `lesson-04-03`  
**Module:** BIO Tags, Token Features, and Entity Spans  
**Source focus:** `src/model.py` → `spans`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Named Entity Recognition Pipeline. By the end, you can describe A BIO tag marks a token as beginning, inside, or outside an entity; adjacent tags are combined into a span., trace the bio tags, token features, and entity spans implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about A BIO tag marks a token as beginning, inside, or outside an entity; adjacent tags are combined into a span.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `spans` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A BIO tag marks a token as beginning, inside, or outside an entity; adjacent tags are combined into a span.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Sentences are generated from templates and fixed name lists.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `spans`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def spans(tokens, labels):
    """The entities of a labelled sentence.

    The labels may be plain ("PER") or in the BIO form ("B-PER", "I-PER"). A
    token that is marked as a continuation belongs to the entity before it,
    so "Ada Lovelace" is one entity and not two.
    """
    result = []
    current = None
    for token, label in zip(tokens, labels):
        if label == "O":
            if current:
                result.append(current)
                current = None
            continue

        # The BIO prefix says whether the entity starts or continues.
        prefix = ""
        kind = label
        if len(label) > 2 and label[1] == "-" and label[0] in ("B", "I", "S", "E"):
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For bio tags, token features, and entity spans, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for bio tags, token features, and entity spans, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for bio tags, token features, and entity spans. In this repository, the claim must be grounded in the documented behavior and source paths: src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
