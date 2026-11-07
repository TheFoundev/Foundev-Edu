# Metrics and Plotting: Test the boundary

**Lesson ID:** `rainfall-analysis-and-prediction-module-08-lesson-03`  
**Module ID:** `rainfall-analysis-and-prediction-module-08`  
**Source focus:** `rrmpg/utils/metrics.py` → `calc_nse`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Metrics and Plot Utils.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/utils/metrics.py` and locate `calc_nse`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/utils/metrics.py`, `rrmpg/utils/plot_utils.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `rrmpg/utils/metrics.py`. source tree absent; excerpt retained from earlier package

### rrmpg/utils/metrics.py

The excerpt below is the selected implementation focus.
### rrmpg/utils/plot_utils.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
# -*- coding: utf-8 -*-a 
# This file is part of RRMPG.
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>

"""
Implementation of evaluation metrics for e.g. hydrological model simulations.

Implemented functions:
    calc_nse: Calculate the Nash-Sutcliffe model efficiency coefficient.
    calc_rmse: Calculate the root mean squared error.
    calc_mse: Calculate the mean squared error.
    calc_kge: Calculate the Kling-Gupta-Efficiency.
    calc_alpha_nse: Calculate the alpha decomposition of the NSE.
    calc_beta_nse: Calculate the beta decomposition of the NSE.
    calc_r: Calculate the pearson r coefficient.

"""
import numpy as np
from scipy.stats.stats import pearsonr

from .array_checks import validate_array_input

def calc_nse(obs, sim):
    """Calculate the Nash-Sutcliffe model efficiency coefficient.

    Original Publication:
    Nash, J. Eamonn, and Jonh V. Sutcliffe. "River flow forecasting through
    conceptual models part I—A discussion of principles." Journal of
    hydrology 10.3 (1970): 282-290.
    
    

    Args:
        obs: Array of the observed values
        sim: Array of the simulated values

    Returns:
        The NSE value for the simulation, compared to the observation.

    Raises:
        ValueError: If the arrays are not of equal size or have non-numeric
            values.
        TypeError: If the arrays is not a supported datatype.
        RuntimeError: If all values in qobs are equal. The NSE is not defined
            for this cases.

    """
    # Validation check on the input arrays
    obs = validate_array_input(obs, np.float64, 'obs')
    sim = validate_array_input(sim, np.float64, 'sim')
    
    if len(obs) != len(sim):
        raise ValueError("Arrays must have the same size.")
    
    # denominator of the fraction term
    denominator = np.sum((obs-np.mean(obs))**2)
    
    # this would lead to a division by zero error and nse is defined as -inf
    if denominator == 0:
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-08.md`](../exercises/exercise-08.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `calc_nse` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `calc_nse` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
