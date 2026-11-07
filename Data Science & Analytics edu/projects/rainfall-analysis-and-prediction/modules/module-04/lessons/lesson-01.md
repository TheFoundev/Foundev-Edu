# Hysteresis Variants and State: Begin with the concept

**Lesson ID:** `rainfall-analysis-and-prediction-module-04-lesson-01`  
**Module ID:** `rainfall-analysis-and-prediction-module-04`  
**Source focus:** `rrmpg/models/cemaneigehystgr4j_model.py` → `run_cemaneigehystgr4j`

## Purpose and learning objectives

Explain hysteresis variants and state in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Cemaneigehystgr4j Model and Cemaneigehystgr4j, Cemaneigehystgr4jice Model and Cemaneigehystgr4jice.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/models/cemaneigehystgr4j_model.py` and locate `run_cemaneigehystgr4j`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/models/cemaneigehystgr4j_model.py`, `rrmpg/models/cemaneigehystgr4j.py`, `rrmpg/models/cemaneigehystgr4jice_model.py`, `rrmpg/models/cemaneigehystgr4jice.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `rrmpg/models/cemaneigehystgr4j_model.py`. source tree absent; excerpt retained from earlier package

### rrmpg/models/cemaneigehystgr4j_model.py

The excerpt below is the selected implementation focus.
### rrmpg/models/cemaneigehystgr4j.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneigehystgr4jice_model.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneigehystgr4jice.py

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

from numba import njit

from .cemaneigehyst_model import run_cemaneigehyst
from .gr4j_model import run_gr4j

@njit
def run_cemaneigehystgr4j(prec, mean_temp, etp, frac_solid_prec, snow_pack_init, 
                      thermal_state_init, sca_init, s_init, r_init, params):
    """Implementation of the Cemaneige Hysteresis + GR4J coupled hydrological model.
    
    This function should be called via the .simulate() function of the 
    CemaneigeHystGR4J class and not directly. It is kept in a separate file for 
    less confusion if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publication [1], [2] and 
    [3].
    
    Args:
        prec: Numpy [t,n] array, which contains the precipitation for each 
            elevation layer n.
        mean_temp: Numpy [t,n] array, which contains the mean temperature for
            each elevation layer n.
        etp: Numpy [t] array, which contains the potential evapotranspiration.
        frac_solid_prec: Numpy [t,n] array, which contains the fraction of 
            solid precipitation for each elevation layer n.
        snow_pack_init: Scalar for the initial state of the snow pack.
        thermal_state_init: Scalar for the initial state of the thermal state.
        sca_init: Scalar for the initial snow-covered area fraction.
        s_init: Scalar for the initial production storage as a fraction of x1.
        r_init: Scalar for the initial routing storage as a fraction of x3.
        params: Numpy array of custom dtype, which contains the model parameter.
        
    Returns:
        qsim: Numpy [t] array, which contains the liquid water outflow for
            each timestep.
        G: Numpy [t] array, which contains the state of the snow pack for 
            each timestep.
        eTG: Numpy [t] arr
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-04.md`](../exercises/exercise-04.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `run_cemaneigehystgr4j` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `run_cemaneigehystgr4j` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
