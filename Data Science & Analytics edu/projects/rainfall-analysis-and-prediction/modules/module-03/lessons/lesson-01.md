# CemaNeige-GR4J Coupling and Ice Variants: Begin with the concept

**Lesson ID:** `rainfall-analysis-and-prediction-module-03-lesson-01`  
**Module ID:** `rainfall-analysis-and-prediction-module-03`  
**Source focus:** `rrmpg/models/cemaneigegr4j.py` → `CemaneigeGR4J`

## Purpose and learning objectives

Explain cemaneige-gr4j coupling and ice variants in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Cemaneigegr4j and Cemaneigegr4jice Model, Cemaneigegr4jice and Cemaneigehyst Model.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `rrmpg/models/cemaneigegr4j.py` and locate `CemaneigeGR4J`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `rrmpg/models/cemaneigegr4j.py`, `rrmpg/models/cemaneigegr4jice_model.py`, `rrmpg/models/cemaneigegr4jice.py`, `rrmpg/models/cemaneigehyst_model.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `rrmpg/models/cemaneigegr4j.py`. source tree absent; excerpt retained from earlier package

### rrmpg/models/cemaneigegr4j.py

The excerpt below is the selected implementation focus.
### rrmpg/models/cemaneigegr4jice_model.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneigegr4jice.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/cemaneigehyst_model.py

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

"""Interface to the Cemaneige + GR4J coupled hydrological model."""

import numbers

import numpy as np

from scipy import optimize

from .basemodel import BaseModel
from .cemaneigegr4j_model import run_cemaneigegr4j
from .cemaneige_utils import (extrapolate_precipitation,
                              extrapolate_temperature,
                              calculate_solid_fraction)
from ..utils.array_checks import validate_array_input, check_for_negatives
from ..utils.metrics import calc_mse

class CemaneigeGR4J(BaseModel):
    """Interface to the Cemaneige + GR4J coupled hydrological model.
    
    This class builds an interface to the coupled model, consisting of the
    Cemaneige snow routine [1] and the GR4J model [2]. This model should only 
    be used with daily data.
    
    If no model parameters are passed upon initialization, generates random
    parameter set.
    
    [1] Valéry, A. "Modélisation précipitations – débit sous influence nivale.
    Élaboration d’un module neige et évaluation sur 380 bassins versants".
    PhD thesis, Cemagref (Antony), AgroParisTech (Paris), 405 pp. (2010)
    
    [2] Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement 
    of a parsimonious model for streamflow simulation." Journal of hydrology 
    279.1 (2003): 275-289.
    
    Args:
        params: (optional) Dictionary containing all model parameters as a
            separate key/value pairs.
            
    Raises:
        ValueError: If a dictionary of model parameters is passed but one of
            the parameters is missing.
            
    """
    
    # List of model parameters
    _param_list = ['CTG', 'Kf', 'x1', 'x2', 'x3', 'x4']
    
    # Dictonary with the default parameter bounds
    _default_bounds = {'CTG': (0, 1),
                       'Kf': (0, 10),
                       'x1
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `CemaneigeGR4J` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `CemaneigeGR4J` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
