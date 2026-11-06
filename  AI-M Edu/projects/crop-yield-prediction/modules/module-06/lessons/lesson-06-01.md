# Evaluation, Uncertainty, and Reproducibility: Understand spatial leakage, calibration, missing dependencies, and limits

**Lesson ID:** `lesson-06-01`  
**Module:** Evaluation, Uncertainty, and Reproducibility  
**Source focus:** `cyp/models/base.py` → `analyze_results`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by YieldSight: County-Level Crop Yield Prediction. By the end, you can describe spatial leakage, calibration, missing dependencies, and limits, trace the evaluation, uncertainty, and reproducibility implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about spatial leakage, calibration, missing dependencies, and limits. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `analyze_results` in `cyp/models/base.py`. Use the excerpt below to trace the actual inputs, transformation, and output for spatial leakage, calibration, missing dependencies, and limits. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.

## Step-by-step source investigation

1. Open `cyp/models/base.py` and inspect `analyze_results`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `cyp/models/base.py` (not executed during package generation):

```python
def analyze_results(true, pred, pred_gp):
        """Calculate ME and RMSE"""
        rmse = np.sqrt(np.mean((true - pred) ** 2))
        me = np.mean(true - pred)

        print(f"Without GP: RMSE: {rmse}, ME: {me}")

        if pred_gp is not None:
            rmse_gp = np.sqrt(np.mean((true - pred_gp) ** 2))
            me_gp = np.mean(true - pred_gp)
            print(f"With GP: RMSE: {rmse_gp}, ME: {me_gp}")
            return rmse, me, rmse_gp, me_gp
        return rmse, me
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, uncertainty, and reproducibility, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-01.md`](../exercises/exercise-06-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand spatial leakage, calibration, missing dependencies, and limits, identify its source location, and state a limitation. The key project-specific fact is: Understand spatial leakage, calibration, missing dependencies, and limits. In this repository, the claim must be grounded in the documented behavior and source paths: cyp/models/base.py; cyp/analysis/counties_plot.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
