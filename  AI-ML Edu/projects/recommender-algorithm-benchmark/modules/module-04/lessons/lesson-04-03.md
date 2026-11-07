# Ranking Metrics and Catalogue Coverage: Validate outputs and identify limitations for ranking metrics and catalogue coverage

**Lesson ID:** `lesson-04-03`  
**Module:** Ranking Metrics and Catalogue Coverage  
**Source focus:** `src/model.py` → `evaluate`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Recommender Algorithm Benchmark. By the end, you can describe Precision asks how many recommended items are relevant; recall asks how many relevant items were recovered; coverage measures catalogue breadth., trace the ranking metrics and catalogue coverage implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Precision asks how many recommended items are relevant; recall asks how many relevant items were recovered; coverage measures catalogue breadth.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `evaluate` in `src/model.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Precision asks how many recommended items are relevant; recall asks how many relevant items were recovered; coverage measures catalogue breadth.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The dataset is small and synthetic.

## Step-by-step source investigation

1. Open `src/model.py` and inspect `evaluate`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/model.py` (not executed during package generation):

```python
def evaluate(model, data, k=5):
    """The metrics of every recommender.

    The precision is the share of the recommendations that were relevant, so
    the denominator is the number of recommendations that were made and not
    the number of users times k. The recall is the share of the relevant items
    that were found, and the coverage is the share of the catalogue that was
    recommended at all.
    """
    relevant = data["test"][data["test"]["rating"] >= 4]
    results = {}
    for name, scores in model["scores"].items():
        hits = 0
        total = 0
        found = 0
        covered = set()
        for user, group in relevant.groupby("user_id"):
            user = int(user)
            if user >= data["n_users"]:
                continue
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For ranking metrics and catalogue coverage, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for ranking metrics and catalogue coverage, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for ranking metrics and catalogue coverage. In this repository, the claim must be grounded in the documented behavior and source paths: src/model.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
