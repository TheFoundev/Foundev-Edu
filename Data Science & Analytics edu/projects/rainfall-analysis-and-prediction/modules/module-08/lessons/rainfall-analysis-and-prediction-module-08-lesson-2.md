# Read cemaneigehystgr4jice model and cemaneigehystgr4jice in the source

**Lesson ID:** `rainfall-analysis-and-prediction-module-08-lesson-2`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/cemaneigehystgr4jice_model.py] and [rrmpg/models/cemaneigehystgr4jice.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_cemaneigehystgr4jice, CemaneigeHystGR4JIce, __init__; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `rrmpg/models/cemaneigehystgr4jice_model.py`, `rrmpg/models/cemaneigehystgr4jice.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `rrmpg/models/cemaneigehystgr4jice_model.py`, `from numba import njit` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice_model.py`, `from .cemaneigehyst_model import run_cemaneigehyst` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice_model.py`, `from .gr4j_model import run_gr4j` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice_model.py`, `from .icemelt_model import run_icemelt` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_cemaneigehystgr4jice(prec, mean_temp, etp, frac_ice, frac_solid_prec, snow_pack_init,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/cemaneigehystgr4jice.py`, `import numbers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice.py`, `from scipy import optimize` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/cemaneigehystgr4jice.py`, `from .basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class CemaneigeHystGR4JIce(BaseModel):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def simulate(self, prec, mean_temp, min_temp, max_temp, etp, frac_ice,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/cemaneigehystgr4jice_model.py

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
# Updated by Mat


from numba import njit
import numpy as np

from .cemaneigehyst_model import run_cemaneigehyst
from .gr4j_model import run_gr4j
from .icemelt_model import run_icemelt


@njit
def run_cemaneigehystgr4jice(prec, mean_temp, etp, frac_ice, frac_solid_prec, snow_pack_init, 
                      thermal_state_init, sca_init, s_init, r_init, params):
    """Implementation of the IceMelt + Cemaneige Hysteresis + GR4J coupled hydrological model.
    
    This function should be called via the .simulate() function of the 
    CemaneigeHystGR4JIce class and not directly. It is kept in a separate file for 
    less confusion if anyone wants to inspect the actual model routine.
    
    The naming of the variables is kept as in the original publication [1], [2], [3] and [4].
    
    Args:
        prec: Numpy [t,n] array, which contains the precipitation for each 
            elevation layer n.
        mean_temp: Numpy [t,n] array, which contains the mean temperature for
            each elevation layer n.
        etp: Numpy [t] array, which contains the potential evapotranspiration.
        frac_ice: Numpy [n] array, which contains the fraction of ice for 
            each elevation layer n.
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
        eTG: Numpy [t] array, which contains the thermal state of the snow
            pack for each timestep.
        s_store: Numpy [t] array, which contains the state of the production 
            storage for each timestep.
        r_store: Numpy [t] array, which contains the state of the routing 
            storage for each timestep.
        sca: Numpy [t,n] array, which contains the snow-covered area fraction 
            for each timestep and elevation layer.
        icemelt: Numpy [t] array, which contains the ice melt contribution for 
            each timestep.
        snowmelt: Numpy [t,n] array, which contains the snowmelt for each 
            timestep and elevation layer.
        rain: Numpy [t,n] array, which contains the liquid precipitation 
            (rainfall) for each timestep and elevation layer.
        

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

    [4] Riboust, 
```

### rrmpg/models/cemaneigehystgr4jice.py

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

"""Interface to the IceMelt + Cemaneige Hysteresis + GR4J coupled hydrological model."""

import numbers
import numpy as np
import pandas as pd
from scipy import optimize

from .basemodel import BaseModel
from .cemaneigehystgr4jice_model import run_cemaneigehystgr4jice
from .cemaneige_utils import (extrapolate_precipitation,
                              extrapolate_temperature,
                              calculate_solid_fraction)
from ..utils.array_checks import validate_array_input, check_for_negatives
from ..utils.metrics import calc_mse, calc_kge

class CemaneigeHystGR4JIce(BaseModel):
    """Interface to the IceMelt + Cemaneige Hysteresis + GR4J coupled hydrological model.
    
    This class builds an interface to the coupled model, consisting of the IceMelt model [1], the
    Cemaneige snow routine with hysteresis [2][3] and the GR4J model [4]. This model should only 
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

    [3] Riboust, P., Thirel, G., Le Moine, N., Ribstein, P. "Revisiting a simple degree-day model for
    integrating satellite data: implementation of SWE-SCA hystereses". Jounral of Hydrology and Hydromenchanics,
    vol. 67, pp. 70-81, (2019)
    
    [4] Perrin, Charles, Claude Michel, and Vazken Andréassian. "Improvement 
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
    _param_list = ['CTG', 'Kf', 'Thacc', 'Rsp', 'x1', 'x2', 'x3', 'x4', 'DDF']
    
    # Dictonary with the default parameter bounds
    _default_bounds = {'CTG': (0, 1),
                       'Kf': (0, 10),
                       'Thacc': (0, 1000), 
                       'Rsp': (0, 1), 
                       'x1': (10, 1200),
                       'x2': (-5, 3),
                       'x3': (20, 5000),
                       'x4': (1.1, 10),
                       'DDF': (0, 30)}
    
    # Custom numpy datatype needed for the numba function
    _dtype = np.dtype([('CTG', np.float64),
                       ('Kf', np.float64),
                       ('Thacc', np.float64),
                       ('Rsp', np.float64),
                       ('x1', np.float64),
                       ('x2', np.float64),
                       ('x3', np.float64),
                       ('x4', np.float64),
                       ('DDF', np.float64)])
    
    def __init__(self, params=None):
        """Initialize a IceMelt + Cemaneige Hysteresis + GR4J coupled hydrological model object.
        
        Args:
            params: (optional) Dictionary containing all model parameters as a
                separate key/value pairs.
                
        Raises:
            ValueError: If a dictionary of model paramete
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

This lesson ties its explanation to `rrmpg/models/cemaneigehystgr4jice_model.py`, `rrmpg/models/cemaneigehystgr4jice.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
