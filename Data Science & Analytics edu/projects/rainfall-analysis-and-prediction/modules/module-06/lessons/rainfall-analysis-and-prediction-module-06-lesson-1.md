# A beginner's model of cemaneigegr4jice and cemaneigehyst model

**Lesson ID:** `rainfall-analysis-and-prediction-module-06-lesson-1`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/cemaneigegr4jice.py] and [rrmpg/models/cemaneigehyst_model.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include CemaneigeGR4JIce, __init__, simulate, run_cemaneigehyst; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `rrmpg/models/cemaneigegr4jice.py`, `rrmpg/models/cemaneigehyst_model.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `rrmpg/models/cemaneigegr4jice.py`, `import numbers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigegr4jice.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigegr4jice.py`, `from scipy import optimize` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigegr4jice.py`, `from .basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigegr4jice.py`, `from .cemaneigegr4jice_model import run_cemaneigegr4jice` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class CemaneigeGR4JIce(BaseModel):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def simulate(self, prec, mean_temp, min_temp, max_temp, etp, frac_ice,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/cemaneigehyst_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehyst_model.py`, `from numba import njit, prange` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_cemaneigehyst(prec, mean_temp, frac_solid_prec, snow_pack_init,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/cemaneigegr4jice.py

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

"""Interface to the IceMelt + Cemaneige + GR4J coupled hydrological model."""

import numbers

import numpy as np

from scipy import optimize

from .basemodel import BaseModel
from .cemaneigegr4jice_model import run_cemaneigegr4jice
from .cemaneige_utils import (extrapolate_precipitation,
                              extrapolate_temperature,
                              calculate_solid_fraction)
from ..utils.array_checks import validate_array_input, check_for_negatives
from ..utils.metrics import calc_mse

class CemaneigeGR4JIce(BaseModel):
    """Interface to the IceMelt + Cemaneige + GR4J coupled hydrological model.
    
    This class builds an interface to the coupled model, consisting of the IceMelt model [1],
    the Cemaneige snow routine [2] and the GR4J model [3]. This model should only 
    be used with daily data.
    
    If no model parameters are passed upon initialization, generates random
    parameter set.
    
    [1] Nepal, S., Chen, J., Penton, D. J., Neumann, L. E., Zheng, H., & Wahid, S. (2017). 
    Spatial GR4J conceptualization of the Tamor glaciated alpine catchment in Eastern Nepal: 
    evaluation of GR4JSG against streamflow and MODIS snow extent. Hydrol. Process., 31, 51–68.
    doi: 10.1002/hyp.10962.

    [2] Valéry, A. "Modélisation précipitations – débit sous influence nivale.
    Élaboration d’un module neige et évaluation sur 380 bassins versants".
    PhD thesis, Cemagref (Antony), AgroParisTech (Paris), 405 pp. (2010)
    
    [3] Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement 
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
    _param_list = ['CTG', 'Kf', 'x1', 'x2', 'x3', 'x4', 'DDF']
    
    # Dictonary with the default parameter bounds
    _default_bounds = {'CTG': (0, 1),
                       'Kf': (1, 15),
                       'x1': (100, 1200),
                       'x2': (-5, 3),
                       'x3': (20, 300),
                       'x4': (1.1, 2.9),
                       'DDF': (1, 30)}
    
    # Custom numpy datatype needed for the numba function
    _dtype = np.dtype([('CTG', np.float64),
                       ('Kf', np.float64),
                       ('x1', np.float64),
                       ('x2', np.float64),
                       ('x3', np.float64),
                       ('x4', np.float64),
                       ('DDF', np.float64)])
    
    def __init__(self, params=None):
        """Initialize a IceMelt + Cemaneige + GR4J coupled hydrological model object.
        
        Args:
            params: (optional) Dictionary containing all model parameters as a
                separate key/value pairs.
                
        Raises:
            ValueError: If a dictionary of model parameters is passed but one
                of the parameters is missing.
                    
        """
        super().__init__(params=params)
        
    def simulate(self, prec, mean_temp, min_temp, max_temp, etp, frac_ice,
                 met_station_height, snow_pack_init=0, thermal_state_init=0, 
                 s_init=0, r_init=0, altitudes=[], return_storages=False, 
                 params=None):
        """Simulate the IceMelt + Cemaneige + GR4J coupled hydrological model.
        
```

### rrmpg/models/cemaneigehyst_model.py

```text
import numpy as np
from numba import njit, prange

@njit
def run_cemaneigehyst(prec, mean_temp, frac_solid_prec, snow_pack_init,
                  thermal_state_init, sca_init, params):
    """Implementation of the Cemaneige snow routine with modified linear hysteresis.
    
    This function should be called via the .simulate() function of the 
    Cemaneige class and not directly. It is kept in a separate file for less 
    confusion if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publications [1] [2].
    
    Args:
        prec: Numpy [t,n] array, which contains the precipitation for each 
            elevation layer n.
        mean_temp: Numpy [t,n] array, which contains the mean temperature for
            each elevation layer n.
        frac_solid_prec: Numpy [t,n] array, which contains the fraction of 
            solid precipitation for each elevation layer n.
        snow_pack_init: Scalar for the initial state of the snow pack.
        thermal_state_init: Scalar for the initial state of the thermal state.
        params: Numpy array of custom dtype, which contains the model parameters.
        sca_init: Scalar for the initial state of the snow-covered area.
        params: Numpy array of custom dtype, which contains the model parameters.
        
    Returns:
        outflow: Numpy [t] array, which contains the liquid water outflow for
            each timestep.
        G: Numpy [t,n] array, which contains the state of the snow pack for 
            each timestep.
        eTG: Numpy [t,n] array, which contains the thermal state of the snow
            pack for each timestep.
        sca: Numpy [t,n] array, which contains the snow-covered area fraction for each timestep
            and elevation layer.
        rain: Numpy [t,n] array, which contains the liquid precipitation (rainfall)
            for each timestep and elevation layer.
            
    [1] Valéry, A. "Modélisation précipitations – débit sous influence nivale.
    Élaboration d’un module neige et évaluation sur 380 bassins versants".
    PhD thesis, Cemagref (Antony), AgroParisTech (Paris), 405 pp. (2010)

    [2] Riboust, P., Thirel, G., Le Moine, N., Ribstein, P. "Revisiting a simple degree-day model for
    integrating satellite data: implementation of SWE-SCA hystereses". Jounral of Hydrology and Hydromenchanics,
    vol. 67, pp. 70-81, (2019)
    
    """
    # Number of simulation timesteps
    num_timesteps = len(prec)
    
    # Number of elevation layers
    num_layers = prec.shape[1]
    
    # Unpack model parameters
    CTG = params['CTG']
    Kf = params['Kf']
    Thacc = params['Thacc']
    Rsp = params['Rsp']
    
    # Snow pack of each layer ## current SWE at each timestep
    G = np.zeros((num_timesteps, num_layers), np.float64)
    
    # Thermal state of each layer
    eTG = np.zeros((num_timesteps, num_layers), np.float64)
    
    # Outflow as sum of liquid precipitation and melt of each layer
    liquid_water = np.zeros((num_timesteps, num_layers), np.float64)
    
    # Snow-covered area of each layer
    sca = np.zeros((num_timesteps, num_layers), np.float64)

    # rainfall of each layer
    rain = np.zeros((num_timesteps, num_layers), np.float64)
    
    # Total outflow which is the mean of liquid water of each layer
    outflow = np.zeros(num_timesteps, np.float64)
    
    #  Track maximum SWE before melting to determine Thmax
    swe_max = np.zeros(num_layers, np.float64)
    Thmax = np.zeros(num_layers, np.float64)
    
    # Calculate Cemaneige routine for each elevation zone independently
    for l in prange(num_layers):
        
        # Split input precipitation into solid and liquid precipitation
        snow = prec[:, l] * frac_solid_prec[:, l]
        rain[:, l] = prec[:, l] - snow

        # Calc mean annual solid precipitation for each elevation zone
        Psolannual = 365.25 * np.mean(snow)

        for t in range(num_timesteps):
          
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

This lesson ties its explanation to `rrmpg/models/cemaneigegr4jice.py`, `rrmpg/models/cemaneigehyst_model.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
