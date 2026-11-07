# GR4J and HBV Runoff Models: Trace the code

**Lesson ID:** `rainfall-analysis-and-prediction-module-05-lesson-02`  
**Module ID:** `rainfall-analysis-and-prediction-module-05`  
**Source focus:** `rrmpg/models/gr4j_model.py` → `run_gr4j`

## Purpose and learning objectives

Trace `run_gr4j` in `rrmpg/models/gr4j_model.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Gr4j Model and Gr4j, Hbvedu Model and Hbvedu.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/models/gr4j_model.py` and locate `run_gr4j`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/models/gr4j_model.py`, `rrmpg/models/gr4j.py`, `rrmpg/models/hbvedu_model.py`, `rrmpg/models/hbvedu.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `rrmpg/models/gr4j_model.py`. source tree absent; excerpt retained from earlier package

### rrmpg/models/gr4j_model.py

The excerpt below is the selected implementation focus.
### rrmpg/models/gr4j.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/hbvedu_model.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/hbvedu.py

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

from numba import njit

@njit
def run_gr4j(prec, etp, s_init, r_init, params):
    """Implementation of the GR4J model.
    
    This function should be called via the .simulate() function of the GR4J
    class and not directly. It is kept in a separate file for less confusion
    if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publication [1].
    
    Args:
        prec: Numpy [t] array, which contains the precipitation input.
        etp: Numpty [t] array, which contains the evapotranspiration input.
        s_init: Scalar for the initial state of the s-storage.
        r_init: Scalar for the initial state of the r-storage.
        params: Numpy array of custom dtype, which contains the model parameter.
        
    Returns:
        qsim: Numpy [t] array with the simulated streamflow.
        s_store: Numpy [t] array with the state of the s-storage of each
            timestep.
        r_store: Numpy [t] array with the state of the r-storage of each
            timestep.
            
    [1] Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement 
    of a parsimonious model for streamflow simulation." Journal of hydrology 
    279.1 (2003): 275-289.
        
    """
    # Number of simulation timesteps
    num_timesteps = len(prec)
    
    # Unpack the model parameters
    x1 = params['x1']
    x2 = params['x2']
    x3 = params['x3']
    x4 = params['x4']
    
    # initialize empty arrays for discharge and all storages
    s_store = np.zeros(num_timesteps+1, np.float64)
    r_store = np.zeros(num_timesteps+1, np.float64)
    qsim = np.zeros(num_timesteps+1, np.float64)
    
    # for clean array indexing, add 0 element at the 0th index of prec and 
    # etp so we start simulating at the index 1
    prec = np
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-05.md`](../exercises/exercise-05.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `run_gr4j` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `run_gr4j` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
