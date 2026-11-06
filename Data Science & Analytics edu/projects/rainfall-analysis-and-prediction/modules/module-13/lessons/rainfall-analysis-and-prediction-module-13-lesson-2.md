# Read monte carlo and array checks in the source

**Lesson ID:** `rainfall-analysis-and-prediction-module-13-lesson-2`

## Purpose and learning objectives

Study the implementation in [rrmpg/tools/monte_carlo.py] and [rrmpg/utils/array_checks.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include monte_carlo, check_for_negatives, validate_array_input; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `rrmpg/tools/monte_carlo.py`, `rrmpg/utils/array_checks.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `rrmpg/tools/monte_carlo.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/tools/monte_carlo.py`, `from ..models.basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/tools/monte_carlo.py`, `from ..utils.metrics import calc_mse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/tools/monte_carlo.py`, `from ..utils.array_checks import validate_array_input` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def monte_carlo(model, num, qobs=None, **kwargs):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/utils/array_checks.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/array_checks.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/array_checks.py`, `from numba import njit` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def check_for_negatives(arr):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def validate_array_input(arr, dtype, arr_name):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/tools/monte_carlo.py

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
"""Implementation of Monte_Carlo-Simulation for rrmpg.models."""

import numpy as np

from ..models.basemodel import BaseModel
from ..utils.metrics import calc_mse
from ..utils.array_checks import validate_array_input


def monte_carlo(model, num, qobs=None, **kwargs):
    """Perform Monte-Carlo-Simulation.

    This function performs a Monte-Carlo-Simulation for any given hydrological
    model of this repository.

    Args:
        model: Any instance of a hydrological model of this repository.
        num: Number of simulations.
        qobs: (optional) Array of observed streamflow.
        **kwargs: Keyword arguments, matching the inputs the model needs to
            perform a simulation (e.g. qobs, precipitation, temperature etc.).
            See help(model.simulate) for model input requirements.

    Returns:
        A dictonary containing the following two keys ['params', 'qsim']. The 
        key 'params' contains a numpy array with the model parameter of each 
        simulation. 'qsim' is a 2D numpy array with the simulated streamflow 
        for each simulation. If an array of observed streamflow is provided,
        one additional key is returned in the dictonary, being 'mse'. This key
        contains an array of the mean-squared-error for each simulation.

    Raises:
        ValueError: If any input contains invalid values.
        TypeError: If any of the inputs has a wrong datatype.

    """
    # Make sure the model contains to this repository.
    if not issubclass(model.__class__, BaseModel):
        msg = ["The model must be one of the models implemented in the ",
               "rrmpg.models module."]
        raise TypeError("".join(msg))

    # Check if n is an integer.
    if not isinstance(num, int) or num < 1:
        raise TypeError("'n' must be a positive integer greate than zero.")

    if qobs is not None: 
        # Validation check of qobs
        qobs = validate_array_input(qobs, np.float64, 'qobs')
    
    # Generate sets of random parameters
    params = model.get_random_params(num=num)

    # perform monte carlo simulation by calculating simulation of all param sets
    qsim = model.simulate(params=params, **kwargs)

    if qobs is not None:  
        # calculate nse of each simulation
        mse_values = np.zeros(num, dtype=np.float64)
        
        for n in range(num):
            mse_values[n] = calc_mse(qobs, qsim[:, n])
            
        return {'params': params, 'qsim': qsim, 'mse': mse_values}
    
    else:
        return {'params': params, 'qsim': qsim}

```

### rrmpg/utils/array_checks.py

```text
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>
"""Implementation of various checks that will be performed on inputs."""

import numpy as np
import pandas as pd

from numba import njit

@njit
def check_for_negatives(arr):
    """Check if array contains negative number.
    
    Numba optimized function to check if a numpy array containes a negative
    value. Returns, whenever the first negative function is found.
    
    Args:
        arr: Numpy array
    
    Returns:
        True, if the array contains at least on negative number and False, if
        the array contains no negative number.
    """
    for val in arr:
        if val < 0:
            return True
    return False


def validate_array_input(arr, dtype, arr_name):
    """Check if array has correct type and is numerical.

    This function checks if the input is either a list, numpy.ndarray or
    pandas.Series of numerical values, converts it to a numpy.ndarray and
    throws an error in case of incorrect data.

    Args:
        arr: Array of data
        dtype: One of numpy's dtypes
        arr_name: String specifing the variable name, so that the error
            message can be adapted correctly.

    Returns:
        A as numpy.ndarray converted array of values with a datatype
        specified in the input argument.

    Raises:
        ValueError: In case non-numerical data is passed
        TypeError: If the error is neither a list, a numpy.ndarray nor a 
            pandas.Series

    """
    # Check for correct data type
    if isinstance(arr, (list, np.ndarray, pd.Series)):
        # Try to convert as numpy array
        try:
            arr = np.array(arr, dtype=dtype).flatten()
        except:
            msg = ["The data in the parameter array '{}'".format(arr_name),
                   " must be purely numerical."]
            raise ValueError("".join(msg))
    else:
        msg = ["The array {} must be either a list, ".format(arr_name),
               "numpy.ndarray or pandas.Series"]
        raise TypeError("".join(msg))
    
    # return converted array
    return arr

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

This lesson ties its explanation to `rrmpg/tools/monte_carlo.py`, `rrmpg/utils/array_checks.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
