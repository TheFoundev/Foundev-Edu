# CemaNeige Snow and Temperature Components: Trace the code

**Lesson ID:** `rainfall-analysis-and-prediction-module-02-lesson-02`  
**Module ID:** `rainfall-analysis-and-prediction-module-02`  
**Source focus:** `rrmpg/models/cemaneige_model.py` → `run_cemaneige`

## Purpose and learning objectives

Trace `run_cemaneige` in `rrmpg/models/cemaneige_model.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Cemaneige Model and Cemaneige Utils, Cemaneige and Cemaneigegr4j Model.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/models/cemaneige_model.py` and locate `run_cemaneige`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/models/cemaneige_model.py`, `rrmpg/models/cemaneige_utils.py`, `rrmpg/models/cemaneige.py`, `rrmpg/models/cemaneigegr4j_model.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `rrmpg/models/cemaneige_model.py`. source tree absent; excerpt retained from earlier package

### rrmpg/models/cemaneige_model.py

The excerpt below is the selected implementation focus.
### rrmpg/models/cemaneige_utils.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneige.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneigegr4j_model.py

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
def run_cemaneige(prec, mean_temp, frac_solid_prec, snow_pack_init,
                  thermal_state_init, params):
    """Implementation of the Cemaneige snow routine.
    
    This function should be called via the .simulate() function of the 
    Cemaneige class and not directly. It is kept in a separate file for less 
    confusion if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publication [1].
    
    Args:
        prec: Numpy [t,n] array, which contains the precipitation for each 
            elevation layer n.
        mean_temp: Numpy [t,n] array, which contains the mean temperature for
            each elevation layer n.
        frac_solid_prec: Numpy [t,n] array, which contains the fraction of 
            solid precipitation for each elevation layer n.
        snow_pack_init: Scalar for the initial state of the snow pack.
        thermal_state_init: Scalar for the initial state of the thermal state.
        params: Numpy array of custom dtype, which contains the model parameter.
        
    Returns:
        outflow: Numpy [t] array, which contains the liquid water outflow for
            each timestep.
        G: Numpy [t] array, which contains the state of the snow pack for 
            each timestep.
        eTG: Numpy [t] array, which contains the thermal state of the snow
            pack for each timestep.
            
    [1] Valéry, A. "Modélisation précipitations – débit sous influence nivale.
    Élaboration d’un module neige et évaluation sur 380 bassins versants".
    PhD thesis, Cemagref (Antony), AgroParisTech (Paris), 405 pp. (2010)
        
    """
    # Number of simulation timesteps
    num_timesteps = len(prec)
    
    # Number of elevation layers
    num_laye
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-02.md`](../exercises/exercise-02.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `run_cemaneige` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `run_cemaneige` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
