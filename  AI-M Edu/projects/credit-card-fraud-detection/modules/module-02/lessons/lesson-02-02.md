# Dataset and Leakage Controls: Inspect the project implementation of dataset and leakage controls

**Lesson ID:** `lesson-02-02`  
**Module:** Dataset and Leakage Controls  
**Source focus:** `src/train.py` → `split_dataset`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by FraudGuard: Credit Card Fraud Detection. By the end, you can describe feature split, scaling, and held-out evaluation, trace the dataset and leakage controls implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about feature split, scaling, and held-out evaluation. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `split_dataset` in `src/train.py`. Use the excerpt below to trace the actual inputs, transformation, and output for feature split, scaling, and held-out evaluation. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A real score depends on a separately supplied model/data artifact; class imbalance means accuracy alone is misleading. Validate privacy and threshold choices before real decisions.

## Step-by-step source investigation

1. Open `src/train.py` and inspect `split_dataset`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/train.py` (not executed during package generation):

```python
def split_dataset():
    """ Read and split dataset into train and test subsets """
    df = pd.read_csv(DATASET_FILENAME, header=0)
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values
    return train_test_split(X, y, test_size=0.2, random_state=42)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For dataset and leakage controls, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-02.md`](../exercises/exercise-02-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of dataset and leakage controls, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `split_dataset` in `src/train.py`. Use the excerpt below to trace the actual inputs, transformation, and output for feature split, scaling, and held-out evaluation. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
