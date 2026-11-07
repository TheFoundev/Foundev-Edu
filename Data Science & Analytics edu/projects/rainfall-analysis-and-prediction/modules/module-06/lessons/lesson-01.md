# Ice Melt and Model Initialization: Begin with the concept

**Lesson ID:** `rainfall-analysis-and-prediction-module-06-lesson-01`  
**Module ID:** `rainfall-analysis-and-prediction-module-06`  
**Source focus:** `rrmpg/models/icemelt_model.py` → `run_icemelt`

## Purpose and learning objectives

Explain ice melt and model initialization in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Icemelt Model and Conf, undefined undefined Init undefined undefined and undefined undefined Init undefined undefined.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/models/icemelt_model.py` and locate `run_icemelt`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/models/icemelt_model.py`, `docs/source/conf.py`, `rrmpg/__init__.py`, `rrmpg/tools/__init__.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `rrmpg/models/icemelt_model.py`. source tree absent; excerpt retained from earlier package

### rrmpg/models/icemelt_model.py

The excerpt below is the selected implementation focus.
### docs/source/conf.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/__init__.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/tools/__init__.py

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

import numpy as np

from numba import njit, prange

@njit    
def run_icemelt(temp, snow, params):
    """Implementation of a degree-day Ice Melt Model (modified after Nepal et al. 2017).
    
    This model simulates ice melt based on a simple degree-day approach.
    
    Args:
        temp: Numpy [t, n] array containing mean temperature for each time step and layer.
        snow: Numpy [t, n] array containing snowpack storage at each time step and layer.
        params: Numpy structured array containing model parameters:
            - 'DDF': Degree-day factor (mm/°C/day).
        
    Returns:
        liquid_water: Numpy [t, n] array containing the liquid water produced from melt
                      for each timestep and layer.
    
    References:
    [1] Nepal, S., Chen, J., Penton, D. J., Neumann, L. E., Zheng, H., & Wahid, S. (2017). 
        Spatial GR4J conceptualization of the Tamor glaciated alpine catchment in Eastern Nepal: 
        evaluation of GR4JSG against streamflow and MODIS snow extent. Hydrol. Process., 31, 51–68.
        doi: 10.1002/hyp.10962.
    """

    # Number of simulation timesteps
    num_timesteps = len(temp)

    # Unpack model parameters
    ddf = params['DDF']
    
    # tbase not calibrated
    tbase = 0

    # Number of elevation layers
    num_layers = temp.shape[1]

    # outflow as sum of liquid precipitation and melt of each layer
    liquid_water = np.zeros((num_timesteps, num_layers), dtype=np.float64)

    # Calculate routine for each elevation zone independently
    for l in prange(num_layers):
        for t in range(num_timesteps):
            # Calculate actual ice melt
            melt = ddf * (temp[t, l]-tbase)
            if melt < 0:
                melt = 0
            if snow[t, l] > 1:
                liquid_water[t, l] = 0
            else:
                l
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-06.md`](../exercises/exercise-06.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `run_icemelt` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `run_icemelt` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
