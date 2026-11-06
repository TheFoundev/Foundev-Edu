# County-Year Prediction Problem: Validate outputs and identify limitations for county-year prediction problem

**Lesson ID:** `lesson-01-03`  
**Module:** County-Year Prediction Problem  
**Source focus:** `run.py` → `train_cnn`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by YieldSight: County-Level Crop Yield Prediction. By the end, you can describe geography, year, targets, and supervised learning, trace the county-year prediction problem implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about geography, year, targets, and supervised learning. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `train_cnn` in `run.py`. Use the excerpt below to trace the actual inputs, transformation, and output for geography, year, targets, and supervised learning. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.

## Step-by-step source investigation

1. Open `run.py` and inspect `train_cnn`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `run.py` (not executed during package generation):

```python
def train_cnn(
        cleaned_data_path=Path("data/img_output"),
        dropout=0.5,
        dense_features=None,
        savedir=Path("data/models"),
        times="all",
        pred_years=None,
        num_runs=2,
        train_steps=25000,
        batch_size=32,
        starter_learning_rate=1e-3,
        weight_decay=1,
        l1_weight=0,
        patience=10,
        use_gp=True,
        sigma=1,
        r_loc=0.5,
        r_year=1.5,
        sigma_e=0.32,
        sigma_b=0.01,
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For county-year prediction problem, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-03.md`](../exercises/exercise-01-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for county-year prediction problem, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for county-year prediction problem. In this repository, the claim must be grounded in the documented behavior and source paths: run.py; cyp/data/feature_engineering.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
