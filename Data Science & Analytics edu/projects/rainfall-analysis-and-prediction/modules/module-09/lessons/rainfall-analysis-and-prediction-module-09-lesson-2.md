# Read gr4j model and gr4j in the source

**Lesson ID:** `rainfall-analysis-and-prediction-module-09-lesson-2`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/gr4j_model.py] and [rrmpg/models/gr4j.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_gr4j, and, GR4J, __init__, simulate; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `rrmpg/models/gr4j_model.py`, `rrmpg/models/gr4j.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `rrmpg/models/gr4j_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/gr4j_model.py`, `from numba import njit` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_gr4j(prec, etp, s_init, r_init, params):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class and not directly. It is kept in a separate file for less confusion` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _s_curve1(t, x4):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _s_curve2(t, x4):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/gr4j.py`, `import numbers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/gr4j.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/gr4j.py`, `from scipy import optimize` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/gr4j.py`, `from .basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/gr4j.py`, `from .gr4j_model import run_gr4j` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class GR4J(BaseModel):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def simulate(self, prec, etp, s_init=0., r_init=0., return_storage=False,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def fit(self, qobs, prec, etp, s_init=0., r_init=0.):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/gr4j_model.py

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
    prec = np.concatenate((np.zeros(1), prec))
    etp = np.concatenate((np.zeros(1), etp))
    
    # set initial values
    s_store[0] = s_init * x1
    r_store[0] = r_init * x3
    
    # calculate number of unit hydrograph ordinates
    num_uh1 = int(np.ceil(x4))
    num_uh2 = int(np.ceil(2*x4 + 1))
    
    # calculate the ordinates of both unit-hydrographs (eq. 16 & 17)
    uh1_ordinates = np.zeros(num_uh1, np.float64)
    uh2_ordinates = np.zeros(num_uh2, np.float64)
    
    for j in range(1, num_uh1 + 1):
        uh1_ordinates[j - 1] = _s_curve1(j, x4) - _s_curve1(j - 1, x4)
        
    for j in range(1, num_uh2 + 1):
        uh2_ordinates[j - 1] = _s_curve2(j, x4) - _s_curve2(j - 1, x4)
    
    # arrys to store the rain distributed through the unit hydrographs
    uh1 = np.zeros(num_uh1, np.float64)
    uh2 = np.zeros(num_uh2, np.float64)
    
    # Start the model simulation loop
    for t in range(1, num_timesteps+1):
        
        # Calculate netto precipitation and evaporation
        if prec[t] >= etp[t]:
            p_n = prec[t] - etp[t]
            pe_n = 0
        
            # calculate fraction of netto precipitation that fills
            #  production store (eq. 3)
            p_s = ((x1 * (1 - (s_store[t-1] / x1)**2) * np.tanh(p_n/x1)) /
                   (1 + s_store[t-1] / x1 * np.tanh(p_n / x1)))
            
            # no evaporation from production store
            e_s = 0   
        
```

### rrmpg/models/gr4j.py

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
"""Interface to the GR4J hydrological model."""

import numbers

import numpy as np

from scipy import optimize

from .basemodel import BaseModel
from .gr4j_model import run_gr4j
from ..utils.array_checks import validate_array_input, check_for_negatives
from ..utils.metrics import calc_mse


class GR4J(BaseModel):
    """Interface to the GR4J hydrological model.
    
    This class builds an interface to the GR4J model, as presented in [1]. 
    This model should only be used with daily data.
    
    If no model parameters are passed upon initialization, generates random
    parameter set.
    
    [1] Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement 
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
    _param_list = ['x1', 'x2', 'x3', 'x4']
    
    # Dictonary with the default parameter bounds
    _default_bounds = {'x1': (100, 1200),
                       'x2': (-5, 3),
                       'x3': (20, 300),
                       'x4': (1.1, 2.9)}
    
    # Custom numpy datatype needed for the numba function
    _dtype = np.dtype([('x1', np.float64),
                       ('x2', np.float64),
                       ('x3', np.float64),
                       ('x4', np.float64)])
    
    def __init__(self, params=None):
        """Initialize a GR4J model object.
        
        Args:
            params: (optional) Dictionary containing all model parameters as a
                separate key/value pairs.
                
        Raises:
            ValueError: If a dictionary of model parameters is passed but one of
                of the parameters is missing.
                    
        """
        super().__init__(params=params)
        
    def simulate(self, prec, etp, s_init=0., r_init=0., return_storage=False,
                 params=None):
        """Simulate rainfall-runoff process for given input.
        
        This function bundles the model parameters and validates the 
        meteorological inputs, then calls the optimized model routine.
        The meteorological inputs can be either list, numpy arrays or pandas
        Series.
        
        Args: 
            prec: Array of daily precipitation sum [mm]
            etp: Array of mean potential evapotranspiration [mm]
            s_init: (optional) Initial value of the production storage as 
                fraction of x1. 
            r_init: (optional) Initial value of the routing storage as fraction
                of x3.
            return_stprage: (optional) Boolean, indicating if the model 
                storages should also be returned.
            params: (optional) Numpy array of parameter sets, that will be 
                evaluated a once in parallel. Must be of the models own custom
                data type. If nothing is passed, the parameters, stored in the 
                model object, will be used.            
                
        Returns:
            An array with the simulated streamflow and optional one array for 
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `rrmpg/models/gr4j_model.py`, `rrmpg/models/gr4j.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
