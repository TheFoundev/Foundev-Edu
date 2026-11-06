# A beginner's model of hbvedu model and hbvedu

**Lesson ID:** `rainfall-analysis-and-prediction-module-10-lesson-1`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/hbvedu_model.py] and [rrmpg/models/hbvedu.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_hbvedu, and, HBVEdu, __init__, simulate; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `rrmpg/models/hbvedu_model.py`, `rrmpg/models/hbvedu.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `rrmpg/models/hbvedu_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/hbvedu_model.py`, `from numba import njit` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_hbvedu(temp, prec, month, PE_m, T_m, snow_init, soil_init, s1_init,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class and not directly. It is kept in a separate file for less confusion` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/hbvedu.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/hbvedu.py`, `from scipy import optimize` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/hbvedu.py`, `from ..utils.array_checks import check_for_negatives, validate_array_input` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/hbvedu.py`, `from ..utils.metrics import calc_mse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/hbvedu.py`, `from .basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class HBVEdu(BaseModel):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def simulate(self,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def fit(self,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/hbvedu_model.py

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
def run_hbvedu(temp, prec, month, PE_m, T_m, snow_init, soil_init, s1_init, 
               s2_init, params):
    """Implementation of the HBV educational model.
    
    This function should be called via the .simulate() function of the HBVEdu
    class and not directly. It is kept in a separate file for less confusion
    if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publication [1].
    
    Args:
        temp: Numpy [t] array, which contains the daily mean temperature.
        prec: Numpy [t] array, which contains the daily precipitation.
        month: Numpy [t] array, containing integers that hold the number of the
            month of the current timestep (from 0 to 11 because of Pythons 
            zero indexing).
        PE_m: Numpy array of length 12, containing the long-term monthly 
            potential evapotranspiration.
        T_m: Numpy array of length 12, containing the long-term monthly 
            temperature.
        snow_init: Scalar for the initial state of the snow storage.
        soil_init: Scalar for the initial state of the soil storage.
        s1_init: Scalar for the initial state of the s1 storage.
        s2_init: Scalar for the initial state of the s2 storage.
        params: Numpy array of custom dtype, which contains the model parameter.
    
    Returns:
        qsim: Numpy [t] array with the simulated streamflow.
        snow: Numpy [t] with the state of the snow storage of each timestep.
        soil: Numpy [t] with the state of the soil storage of each timestep.
        s1: Numpy [t] with the state of the s1-storage of each timestep.
        s2: Numpy [t] with the state of the s2-storage of each timestep.
    
    [1] Aghakouchak, Amir, and Emad Habib. "Application of a conceptual 
    hydrologic model in teaching hydrologic processes." International Journal 
    of Engineering Education 26.4 (S1) (2010).
    
    """
    # Number of simulation timesteps
    num_timesteps = len(prec)
    
    # Unpack the model parameters
    T_t = params['T_t']
    DD = params['DD']
    FC = params['FC']
    Beta = params['Beta']
    C = params['C']
    PWP = params['PWP']
    K_0 = params['K_0']
    K_1 = params['K_1']
    K_2 = params['K_2']
    K_p = params['K_p']
    L = params['L']
    
    # initialize empty arrays for all reservoirs and outflow
    snow = np.zeros(num_timesteps, np.float64)
    soil = np.zeros(num_timesteps, np.float64)
    s1 = np.zeros(num_timesteps, np.float64)
    s2 = np.zeros(num_timesteps, np.float64)
    qsim = np.zeros(num_timesteps, np.float64)

    # set initial values
    snow[0] = snow_init
    soil[0] = soil_init
    s1[0] = s1_init
    s2[0] = s2_init

    # Start the model simulation as loop over all timesteps
    for t in range(1, num_timesteps):

        # Check if temperature is below threshold
        if temp[t] < T_t:
            # accumulate snow
            snow[t] = snow[t-1] + prec[t]
            # no liquid water
            liquid_water = 0
        else:
            # melt snow
            snow[t] = max(0, snow[t-1] - DD * (temp[t] - T_t))
            # add melted snow to available liquid water
            liquid_water = prec[t] + min(snow[t-1], DD * (temp[t] - T_t))

        # calculate the effective precipitation
        prec_eff = liquid_water * (soil[t-1] / FC) ** Beta

```

### rrmpg/models/hbvedu.py

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
"""Interface to the educational version of the HBV model."""

import numpy as np
from scipy import optimize

from ..utils.array_checks import check_for_negatives, validate_array_input
from ..utils.metrics import calc_mse
from .basemodel import BaseModel
from .hbvedu_model import run_hbvedu


class HBVEdu(BaseModel):
    """Interface to the educational version of the HBV model.
    
    This class builds an interface to the HBV educational model as presented in
    [1]. This model should only be used with daily data.

    If no model parameters are passed upon initialization, generates random
    parameter set.

    Args:
        params: (optional) Dictonary containing all model parameters as a
            seperate key/value pairs.

    Raises:
        ValueError: If a dictionary of model parameters is passed but one of
            the parameters is missing.
            
    [1] Aghakouchak, Amir, and Emad Habib. "Application of a conceptual 
    hydrologic model in teaching hydrologic processes." International Journal 
    of Engineering Education 26.4 (S1) (2010).

    """

    # List of model parameters
    _param_list = ['T_t', 'DD', 'FC', 'Beta', 'C', 'PWP', 'K_0', 'K_1', 'K_2', 'K_p', 'L']

    # Dictionary with default parameter bounds
    _default_bounds = {
        'T_t': (-1, 1),
        'DD': (3, 7),
        'FC': (100, 200),
        'Beta': (1, 7),
        'C': (0.01, 0.07),
        'PWP': (90, 180),
        'K_0': (0.05, 0.2),
        'K_1': (0.01, 0.1),
        'K_2': (0.01, 0.05),
        'K_p': (0.01, 0.05),
        'L': (2, 5)
    }

    # Custom numpy datatype needed for numba input
    _dtype = np.dtype([('T_t', np.float64), ('DD', np.float64), ('FC', np.float64),
                       ('Beta', np.float64), ('C', np.float64), ('PWP', np.float64),
                       ('K_0', np.float64), ('K_1', np.float64), ('K_2', np.float64),
                       ('K_p', np.float64), ('L', np.float64)])

    def __init__(self, params=None):
        """Initialize a HBVEdu model object.

        Args:
            params: (optional) Dictonary containing all model parameters as a
                seperate key/value pairs.

        Raises:
            ValueError: If a dictionary of model parameters is passed but one of
                the parameters is missing.

        """
        super().__init__(params=params)

    def simulate(self,
                 temp,
                 prec,
                 month,
                 PE_m,
                 T_m,
                 snow_init=0,
                 soil_init=0,
                 s1_init=0,
                 s2_init=0,
                 return_storage=False,
                 params=None):
        """Simulate rainfall-runoff process for given input.

        This function bundles the model parameters and validates the
        meteorological inputs, then calls the optimized model routine.
        The meteorological inputs can be either list, numpy array or pandas 
        Series.

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

This lesson ties its explanation to `rrmpg/models/hbvedu_model.py`, `rrmpg/models/hbvedu.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
