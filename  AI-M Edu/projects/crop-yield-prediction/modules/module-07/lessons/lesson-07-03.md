# Visualization and Interpretation: Validate outputs and identify limitations for visualization and interpretation

**Lesson ID:** `lesson-07-03`  
**Module:** Visualization and Interpretation  
**Source focus:** `cyp/analysis/counties_plot.py` → `plot_county_errors`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by YieldSight: County-Level Crop Yield Prediction. By the end, you can describe county plots, error maps, and uncertainty-aware reading, trace the visualization and interpretation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about county plots, error maps, and uncertainty-aware reading. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `plot_county_errors` in `cyp/analysis/counties_plot.py`. Use the excerpt below to trace the actual inputs, transformation, and output for county plots, error maps, and uncertainty-aware reading. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The workflow needs Earth Engine exports and large raster data not included in the package. Optional error-map dependencies are missing from the declared environment; results require spatially honest evaluation.

## Step-by-step source investigation

1. Open `cyp/analysis/counties_plot.py` and inspect `plot_county_errors`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `cyp/analysis/counties_plot.py` (not executed during package generation):

```python
def plot_county_errors(model, svg_file=Path("data/counties.svg"), save_colorbar=True):
    """
    For the most part, reformatting of
    https://github.com/JiaxuanYou/crop_yield_prediction/blob/master/6%20result_analysis/yield_map.py

    Generates an svg of the counties, coloured by their prediction error.

    Parameters
    ----------
    model: pathlib Path
        Path to the model being plotted.
    svg_file: pathlib Path, default=Path('data/counties.svg')
        Path to the counties svg file used as a base
    save_colorbar: boolean, default=True
        Whether to save a colorbar too.
    """

    model_sd = torch.load(model, map_location="cpu")

    model_dir = model.parents[0]
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For visualization and interpretation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-07-03.md`](../exercises/exercise-07-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for visualization and interpretation, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for visualization and interpretation. In this repository, the claim must be grounded in the documented behavior and source paths: cyp/analysis/counties_plot.py; index.html.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
