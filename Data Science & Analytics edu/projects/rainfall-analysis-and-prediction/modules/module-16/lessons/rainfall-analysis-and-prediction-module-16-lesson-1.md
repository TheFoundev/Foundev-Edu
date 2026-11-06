# A beginner's model of test code and evidence boundaries

**Lesson ID:** `rainfall-analysis-and-prediction-module-16-lesson-1`

## Purpose and learning objectives

Read test implementations test/test_models.py, test/test_tools.py, test/test_utils.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `test/test_models.py`, `test/test_tools.py`, `test/test_utils.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `test/test_models.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_models.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_models.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_models.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_models.py`, `from rrmpg.models import ABCModel, HBVEdu, GR4J, Cemaneige, CemaneigeGR4J, CemaneigeHystGR4J, CemaneigeHystGR4JIce` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestBaseModelFunctions(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def setUp(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_get_parameter_names(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_get_params(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_get_default_bounds(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_get_dtype(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `test/test_tools.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_tools.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_tools.py`, `from rrmpg.models import ABCModel` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_tools.py`, `from rrmpg.tools.monte_carlo import monte_carlo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestMonteCarlo(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def setUp(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_runs_for_correct_number(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `test/test_utils.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_utils.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_utils.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_utils.py`, `from rrmpg.utils.metrics import calc_nse, calc_rmse, calc_mse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `test/test_utils.py`, `from rrmpg.utils.array_checks import check_for_negatives, validate_array_input` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestNSE(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_nse_for_equal_arrays(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_nse_constant_obs(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_nse_simulation_equals_obs_mean(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class TestRMSE(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_rmse_for_equal_arrays(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### test/test_models.py

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

import unittest
import os

import numpy as np
import pandas as pd

from rrmpg.models import ABCModel, HBVEdu, GR4J, Cemaneige, CemaneigeGR4J, CemaneigeHystGR4J, CemaneigeHystGR4JIce
from rrmpg.models.basemodel import BaseModel

class TestBaseModelFunctions(unittest.TestCase):
    """Test all functions implemented in the BaseModel.
    
    These will not be tested for all models, but one as an example for one of 
    the models.
    """
    
    def setUp(self):
        self.model = ABCModel()
        self.param_names = ['a', 'b', 'c']
        self.default_bounds =  {'a': (0, 1),
                                'b': (0, 1),
                                'c': (0, 1)}
        self.dtype = np.dtype([('a', np.float64),
                               ('b', np.float64),
                               ('c', np.float64)])
        unittest.TestCase.setUp(self)
        
    def test_get_parameter_names(self):
        self.assertEqual(self.model.get_parameter_names(), self.param_names)
        
    def test_get_params(self):
        params = self.model.get_params()
        for param in self.param_names:
            msg = "Failed, because '{}' not in '{}'".format(param, params.keys)
            self.assertIn(param, params, msg)
            
    def test_get_default_bounds(self):
        bounds = self.model.get_default_bounds()
        self.assertDictEqual(bounds, self.default_bounds)
        
    def test_get_dtype(self):
        self.assertEqual(self.dtype, self.model.get_dtype())
        
    def test_random_params_in_default_bounds(self):
        params = self.model.get_random_params()
        bnds = self.default_bounds
        
        for p in self.param_names:
            msg = ["Failed for param: '{}', which has a ".format(p),
                   "a value of {}, but lower bounds ".format(params[p][0]),
                   "is {} and upper bound {}.".format(bnds[p][0], bnds[p][1])]
            self.assertTrue(bnds[p][0] <= params[p][0] <= bnds[p][1], 
                            "".join(msg))
    
    def test_get_multiple_random_param_sets(self):
        num = 24
        params = self.model.get_random_params(num=num)
        self.assertEqual(num, params.size)
              
    def test_set_params(self):
        rand_params = self.model.get_random_params()
        # convert rand_params array to dict:
        params = {}
        for p in self.param_names:
            params[p] = rand_params[p][0]
        self.model.set_params(params)
        self.assertDictEqual(params, self.model.get_params()) 
        
        
class TestABCModel(unittest.TestCase):
    """Test ABC-Model specific functions."""
    
    def setUp(self):
        self.model = ABCModel()
        unittest.TestCase.setUp(self)
        
    def test_model_subclass_of_basemodel(self):
        self.assertTrue(issubclass(self.model.__class__, BaseModel))
        
    def test_simulate_zero_rain(self):
        qsim = self.model.simulate(np.zeros(100))
        self.assertEqual(np.sum(qsim), 0)
        
    def test_simulate_negative_rain(self):
        with self.assertRaises(ValueError) as context:
            self.model.simulate([-1,1,1])
        expr = ("In the precipitation array are negative values." in
                str(context.exception)) 
        self.assertTrue(expr)

```

### test/test_tools.py

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

import unittest

import numpy as np

from rrmpg.models import ABCModel
from rrmpg.tools.monte_carlo import monte_carlo

class TestMonteCarlo(unittest.TestCase):
    """Test the monte carlo implementation."""
    
    def setUp(self):
        self.model = ABCModel()
        self.rain = np.random.random(100)
        unittest.TestCase.setUp(self)
        
    def test_runs_for_correct_number(self):
        num = 24
        results = monte_carlo(self.model, num, prec=self.rain)
        self.assertEqual(results['qsim'].shape[1], num)
        
```

### test/test_utils.py

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

import unittest

import numpy as np
import pandas as pd

from rrmpg.utils.metrics import calc_nse, calc_rmse, calc_mse
from rrmpg.utils.array_checks import check_for_negatives, validate_array_input

class TestNSE(unittest.TestCase):
    """Test of the NSE function."""
    
    def test_nse_for_equal_arrays(self):
        self.assertEqual(calc_nse(obs=[1,2,3], sim=[1,2,3]), 1)
        
    def test_nse_constant_obs(self):
        with self.assertRaises(RuntimeError) as context:
            _ = calc_nse(obs=[2,2,2], sim=[1,2,3])
        msg = ["The Nash-Sutcliffe-Efficiency coefficient is not defined ",
               "for the case, that all values in the observations are equal.",
               " Maybe you should use the Mean-Squared-Error instead."]
        expr = ("".join(msg) in str(context.exception)) 
        self.assertTrue(expr)
        
    def test_nse_simulation_equals_obs_mean(self):
        self.assertEqual(calc_nse(obs=[1,2,3], sim=[2,2,2]), 0)
        
        
class TestRMSE(unittest.TestCase):
    """Test of the RMSE function."""
    
    def test_rmse_for_equal_arrays(self):
        self.assertEqual(calc_rmse(obs=[1,2,3], sim=[1,2,3]), 0)
        
    def test_rmse_for_nonequal_arrays(self):
        self.assertEqual(calc_rmse(obs=[1,1,1], sim=[3,3,3]), 2)


class TestMSE(unittest.TestCase):
    """Test of the MSE function."""
    
    def test_mse_for_equal_arrays(self):
        self.assertEqual(calc_mse(obs=[1,2,3], sim=[1,2,3]), 0)
        
    def test_mse_for_nonequal_arrays(self):
        self.assertEqual(calc_mse(obs=[1,1,1], sim=[3,3,3]), 4)        
        

class TestCheckForNegatives(unittest.TestCase):
    """Test the function that checks for negatives."""
    
    def test_func_without_negatives(self):
        arr = np.array([1,2,3,4,5], dtype=np.float64)
        self.assertFalse(check_for_negatives(arr))
        
    def test_func_with_negatives(self):
        arr = np.array([1,2,-3,4,5], dtype=np.float64)
        self.assertTrue(check_for_negatives(arr))     
        
        
class TestValidateArrayInput(unittest.TestCase):
    """Test the array validation function."""
    
    def test_func_with_pandas_series(self):
        vals = [1, 2, 3, 4]
        data = pd.Series(data=vals, dtype=np.float64)
        arr = validate_array_input(data, np.float64, 'arr')
        self.assertSequenceEqual(arr.tolist(), 
                                 np.array(vals, np.float64).tolist())
        
    def test_func_with_list(self):
        vals = [1., 2., 3., 4.]
        arr = validate_array_input(vals, np.float64, 'arr')
        self.assertSequenceEqual(vals, arr.tolist())
        
    def test_func_with_non_numerical_input(self):
        with self.assertRaises(ValueError) as context:
            _ = validate_array_input(['a', 'b', 1], np.float64, 'arr')
        msg = ["The data in the parameter array '{}'".format('arr'),
                " must be purely numerical."]
        self.assertTrue("".join(msg) in str(context.exception))
        
    def test_func_with_incorrect_datatype(self):
        with self.assertRaises(TypeError) as context:
            _ = validate_array_input((1, 2, 3), np.float64, 'arr')
        msg = ["The array {} must be either a list, ".format('arr'),
               "numpy.ndarray or pandas.Series"]
        self.assertTrue("".join(msg) in str(context.exception))     
              
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

This lesson ties its explanation to `test/test_models.py`, `test/test_tools.py`, `test/test_utils.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### rrmpg/models/__init__.py

### rrmpg/models/__init__.py

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

from .abcmodel import ABCModel
from .hbvedu import HBVEdu
from .gr4j import GR4J
from .cemaneige import Cemaneige
from .cemaneigegr4j import CemaneigeGR4J
from .cemaneigehystgr4j import CemaneigeHystGR4J
from .cemaneigegr4jice import CemaneigeGR4JIce
from .cemaneigehystgr4jice import CemaneigeHystGR4JIce

```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
