# A beginner's model of cemaneige model and cemaneige utils

**Lesson ID:** `rainfall-analysis-and-prediction-module-03-lesson-1`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/cemaneige_model.py] and [rrmpg/models/cemaneige_utils.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_cemaneige, calculate_solid_fraction, extrapolate_precipitation; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `rrmpg/models/cemaneige_model.py`, `rrmpg/models/cemaneige_utils.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `rrmpg/models/cemaneige_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneige_model.py`, `from numba import njit, prange` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_cemaneige(prec, mean_temp, frac_solid_prec, snow_pack_init,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/cemaneige_utils.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneige_utils.py`, `from numba import njit, prange` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def calculate_solid_fraction(prec, altitudes, mean_temp, min_temp, max_temp):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extrapolate_precipitation(prec, altitudes, met_station_height):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def extrapolate_temperature(min_temp, mean_temp, max_temp, altitudes,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/cemaneige_model.py

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
    num_layers = prec.shape[1]
    
    # Unpack model parameters
    CTG = params['CTG']
    Kf = params['Kf']
    
    # snow pack of each layer
    G = np.zeros((num_timesteps, num_layers), np.float64)
    
    # thermal state of each layer
    eTG = np.zeros((num_timesteps, num_layers), np.float64)
    
    # outflow as sum of liquid precipitation and melt of each layer
    liquid_water = np.zeros((num_timesteps, num_layers), np.float64)
    
    # total outflow which is the mean of liquid water of each layer
    outflow = np.zeros(num_timesteps, np.float64)
    
    # Calculate Cemaneige routine for each elevation zone indipentendly
    for l in prange(num_layers):
        
        # Split input precipitation into solid and liquid precipitation
        snow = prec[:, l] * frac_solid_prec[:, l]
        rain = prec[:, l] - snow
        
        # calc the snow cover threshold from mean anual solid precipitation
        G_tresh = 0.9 * 365.25 * np.mean(snow)
        
        for t in range(num_timesteps):
            
            # Accumulate solid precipitation to snow pack
            if t == 0:
                G[t, l] = snow_pack_init
            else: 
                G[t, l] = G[t-1, l] + snow[t]
            
            # Calculate snow pack thermal state before melt eTG ( eTG <= 0 )
            if t == 0:
                eTG[t, l] = thermal_state_init
            else:
                eTG[t, l] = CTG * eTG[t-1, l] + (1 - CTG) * mean_temp[t, l]
            if eTG[t, l] > 0:
                eTG[t, l] = 0
            
            # Calculate potential melt 
            if eTG[t, l] == 0 and mean_temp[t, l] > 0:
                pot_melt = Kf * mean_temp[t, l]
```

### rrmpg/models/cemaneige_utils.py

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

@njit(parallel=True)
def calculate_solid_fraction(prec, altitudes, mean_temp, min_temp, max_temp):
    """Function to calculate the fraction of solid precipitation.
    
    This function is taken from the airGR R-package [1]. It calculates the
    fraction of solid precipitation as a function of the altitude and the daily
    min-/mean-/max-temperature. The elevation threshold of 1500 m, which is 
    used to apply different functions depending on the height can be found in
    [2].
    
    Args:
        prec: Numpy [t,n] array, which contains the precipitation for each 
            elevation layer n.
        altitudes: Numpy [n] array, with the median elevation of each 
            elevation layer.
        mean_temp: Numpy [t,n] array, which contains the daily mean temperature 
            for each elevation layer n.
        min_temp: Numpy [t,n] array, which contains the daily min temperature
            for each elevation layer n.
        max_temp: Numpy [t,n] array, which contains the daily max temperature
            for each elevation layer n.
        
    
    Returns:
        frac_solid_prec: Numpy [t,n] array, which contains the fraction of 
            solid precipitation for each elevation layer n.
    
    [1] https://odelaigue.github.io/airGR/
    [2] Audrey Valery, Vazken Andreassian, Charles Perrin. "'As simple as 
    possible but not simpler': What is useful in a temperature-based snow-
    accounting routine? Part 2 - Sensitivity analysis of the Cemaneige snow
    accounting routine in 380 Catchments." Journal of Hydrology 517 (2014) 
    1176-1187.
    """
    # elevation threshold, since calculation depends on altitude
    z_thresh = 1500
    
    # Number of elevation layer
    num_layers = len(altitudes)

    # Number of timesteps
    num_timesteps = prec.shape[0]
    
    # array for solid fraction of precipitation for each zone and timestep
    solid_fraction = np.zeros((num_timesteps, num_layers), dtype=np.float64)
    
    for l in prange(num_layers):
        
        # apply different calculation depending of altitude of elevation zone
        if altitudes[l] < z_thresh:
        
            for t in prange(num_timesteps):
                
                # if max daily temp under 0, everything is solid
                if max_temp[t, l] <= 0:
                    solid_fraction[t, l] = 1
                
                # if min daily temp is above 0 everything is liquid    
                elif min_temp[t, l] >= 0:              
                    solid_fraction[t, l] = 0
                
                # calculate fraction between 0-1    
                else:
                    solid_fraction[t, l] = 1 - (max_temp[t, l] / 
                                               (max_temp[t, l] - 
                                                min_temp[t, l]))
                    
        else:
            
            for t in prange(num_timesteps):
                
                # if mean temp greater than +3 everything is liquid
                if mean_temp[t, l] >= 3:
                    solid_fraction[t, l] = 0
                    
                # if mean temp smaller than 0 everything is solid
                elif mean_temp[t, l] <= 0:
                    solid_fraction[t, l] = 1
                    
                # calculate fraction between 0-1
                else:
                    solid_fraction[t, l] = 1 - (mean_temp[t, l] + 1) / 4
            
    return solid_fraction
   
@njit(parallel=True)    
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

This lesson ties its explanation to `rrmpg/models/cemaneige_model.py`, `rrmpg/models/cemaneige_utils.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
