# A beginner's model of abcmodel and basemodel

**Lesson ID:** `rainfall-analysis-and-prediction-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/abcmodel.py] and [rrmpg/models/basemodel.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include ABCModel, __init__, get_random_params, simulate, BaseModel, __init__, get_random_params, get_params, set_params; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `rrmpg/models/abcmodel.py`, `rrmpg/models/basemodel.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `rrmpg/models/abcmodel.py`, `import numbers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/abcmodel.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/abcmodel.py`, `from scipy import optimize` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/abcmodel.py`, `from .basemodel import BaseModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/abcmodel.py`, `from .abcmodel_model import run_abcmodel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class ABCModel(BaseModel):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_random_params(self, num=1):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def simulate(self, prec, initial_state=0, return_storage=False,` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def fit(self, qobs, prec, initial_state=0):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def _loss(X, *args):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/models/basemodel.py`, `import numbers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/basemodel.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/basemodel.py`, `from numpy.random import uniform` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class BaseModel(object):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, params=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_random_params(self, num=1):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_params(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def set_params(self, params):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_parameter_names(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/abcmodel.py

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

"""Interface to the the ABC-Model."""

import numbers

import numpy as np

from scipy import optimize

from .basemodel import BaseModel
from .abcmodel_model import run_abcmodel
from ..utils.metrics import calc_mse
from ..utils.array_checks import check_for_negatives, validate_array_input


class ABCModel(BaseModel):
    """Interface to the the ABC-Model.

    This model implements the classical ABC-Model. It was developed for
    educational purpose and represents a simple linear model.

    Original Publication:
        Myron B. Fiering "Streamflow synthesis" Cambridge, Harvard University
        Press, 1967. 139 P. (1967).

    If no model parameters are passed upon initialization, generates random
    parameter set.

    Args:
        params: (optional) Dictonary containing all model parameters as a
            seperate key/value pairs.

    """

    # List of model parameters
    _param_list = ['a', 'b', 'c']

    # Dictionary with default parameter bounds
    _default_bounds = {'a': (0, 1),
                       'b': (0, 1),
                       'c': (0, 1)}

    # Custom numpy datatype needed for numba input
    _dtype = np.dtype([('a', np.float64),
                       ('b', np.float64),
                       ('c', np.float64)])

    def __init__(self, params=None):
        """Initialize an ABC-Model.

        If no parameters are passed as input arguments, random values are
        sampled that satisfy the parameter constraints of the ABC-Model.

        Args:
            params: (optional) Dictonary containing all model parameters as a
                seperate key/value pairs.

        """
        super().__init__(params=params)
        
    def get_random_params(self, num=1):
        """Generate random sets of model parameters for the ABC-model.

        The ABC-model has specific parameter constraints, therefore we will 
        overwrite the function of the BaseModel, to generated random model
        parameters, that satisfy the ABC-Model constraints.

        Args:
            num: (optional) Integer, specifying the number of parameter sets,
                that will be generated. Default is 1.
                
        Returns:
            A dict containing one key/value pair for each model parameter.

        """
        params = np.zeros(num, dtype=self._dtype)
        
        # sample parameter 'a' between the bounds [0,1]
        params['a'][:] = np.random.uniform(low=self._default_bounds['a'][0],
                                           high=self._default_bounds['a'][1],
                                           size=num)
                # parameter 'c' must be between [0,1] and has no further constraints
        params['c'][:] = np.random.uniform(low=self._default_bounds['c'][0],
                                           high=self._default_bounds['c'][1],
                                           size=num)
        
        # Parameter b is constraint by its corresponding a parameter.
        for i in range(num):
            # sample parameter 'b' between lower bound 0 and upper bnd (1 - a)
            params['b'][i] = np.random.uniform(low=self._default_bounds['b'][0],
                                               high=(1-params['a'][i]),
```

### rrmpg/models/basemodel.py

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

"""Parent class for all models implemented in rrmpg.models."""

import numbers

import numpy as np

from numpy.random import uniform


class BaseModel(object):
    """Basic model class for all rainfall-runoff model.

    This class builds the core skelleton for all rainfall-runoff models
    within this project. Every other model will inherit from this class and
    therefore only have to implement the model specific methods.
    """

    # List of strings containing all model parameters
    _param_list = []

    # Dict containing the default parameter bounds
    _default_bounds = {}

    # Custom numpy datatype needed for numba input
    _dtype = np.dtype([])

    def __init__(self, params=None):
        """Initialize a new hydrological model.

        This is the base class for all hydrological models. In common for all
        models is, then upon initialization you can either pass concrete model
        parameters or if you don't, random parameters within the default bounds
        will be generated.

        Args:
            params: (optional) Dictonary containing all model parameters as a
                seperate key/value pairs.

        Raises:
            AttributeError: If a model parameter is missing in the passed 
                dictonary.

        """
        # Check if params are passed
        if params:
            # Check if a value for each parameter is passed
            missings = [p for p in self._param_list if p not in params.keys()]
            if len(missings) > 0:
                raise AttributeError("Missing the following model parameters: "
                                     "{}".format(missings))
        else:
            # Generate random model parameters
            params = self.get_random_params()

        # Parse model parameters as class attributes
        self.set_params(params)

    def get_random_params(self, num=1):
        """Generate random sets of model parameters in the default bounds.

        Samples num values for each model parameter from a uniform distribution
        between the default bounds.
        
        Args:
            num: (optional) Integer, specifying the number of parameter sets,
                that will be generated. Default is 1.
        
        Returns:
            A numpy array of the models custom data type, containing the at
            random generated parameters.

        """
        params = np.zeros(num, dtype=self._dtype)
        # sample one value for each parameter
        for param in self._param_list:
            values = uniform(low=self._default_bounds[param][0],
                             high=self._default_bounds[param][1],
                             size=num)
            params[param] = values

        return params

    def get_params(self):
        """Return a dict with all model parameters and their current value."""
        params = {}
        for param in self._param_list:
            params[param] = getattr(self, param)
        return params

    def set_params(self, params):
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

This lesson ties its explanation to `rrmpg/models/abcmodel.py`, `rrmpg/models/basemodel.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
