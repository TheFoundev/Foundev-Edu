# Monte Carlo and Array Utilities: Test the boundary

**Lesson ID:** `rainfall-analysis-and-prediction-module-07-lesson-03`  
**Module ID:** `rainfall-analysis-and-prediction-module-07`  
**Source focus:** `rrmpg/tools/monte_carlo.py` → `monte_carlo`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Monte Carlo and Array Checks.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/tools/monte_carlo.py` and locate `monte_carlo`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/tools/monte_carlo.py`, `rrmpg/utils/array_checks.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `rrmpg/tools/monte_carlo.py`. source tree absent; excerpt retained from earlier package

### rrmpg/tools/monte_carlo.py

The excerpt below is the selected implementation focus.
### rrmpg/utils/array_checks.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
# -*- coding: utf-8 -*-
# This file is part of RRMPG.
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>
"""Implementation of Monte_Carlo-Simulation for rrmpg.models."""

import numpy as np

from ..models.basemodel import BaseModel
from ..utils.metrics import calc_mse
from ..utils.array_checks import validate_array_input


def monte_carlo(model, num, qobs=None, **kwargs):
    """Perform Monte-Carlo-Simulation.

    This function performs a Monte-Carlo-Simulation for any given hydrological
    model of this repository.

    Args:
        model: Any instance of a hydrological model of this repository.
        num: Number of simulations.
        qobs: (optional) Array of observed streamflow.
        **kwargs: Keyword arguments, matching the inputs the model needs to
            perform a simulation (e.g. qobs, precipitation, temperature etc.).
            See help(model.simulate) for model input requirements.

    Returns:
        A dictonary containing the following two keys ['params', 'qsim']. The 
        key 'params' contains a numpy array with the model parameter of each 
        simulation. 'qsim' is a 2D numpy array with the simulated streamflow 
        for each simulation. If an array of observed streamflow is provided,
        one additional key is returned in the dictonary, being 'mse'. This key
        contains an array of the mean-squared-error for each simulation.

    Raises:
        ValueError: If any input contains invalid values.
        TypeError: If any of the inputs has a wrong datatype.

    """
    # Make sure the model contains to this repository.
    if not issubclass(model.__class__, BaseModel):
        msg = ["The model must be one of the models implemented in the ",
               "rrmpg.models module."]
        raise TypeError("".join(msg))

    # Check if n is an integer.
    if not isinstance(num, int) or num < 1:
        raise TypeError("'n' must be a positive integer greate than zero.")

 
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-07.md`](../exercises/exercise-07.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `monte_carlo` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `monte_carlo` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
