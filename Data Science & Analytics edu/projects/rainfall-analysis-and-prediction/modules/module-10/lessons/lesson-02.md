# Model Test Suite: Trace the code

**Lesson ID:** `rainfall-analysis-and-prediction-module-10-lesson-02`  
**Module ID:** `rainfall-analysis-and-prediction-module-10`  
**Source focus:** `test/test_models.py` → `TestBaseModelFunctions`

## Purpose and learning objectives

Trace `TestBaseModelFunctions` in `test/test_models.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Test code and evidence boundaries.

## Beginner explanation

A rainfall-runoff model is a bucket system: rain enters, stores fill or drain, and the model estimates flow. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `test/test_models.py` and locate `TestBaseModelFunctions`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `test/test_models.py`, `test/test_tools.py`, `test/test_utils.py`, `rrmpg/models/__init__.py`, `rrmpg/__init__.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `test/test_models.py`. source tree absent; excerpt retained from earlier package

### test/test_models.py

The excerpt below is the selected implementation focus.
### test/test_tools.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### test/test_utils.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/__init__.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/__init__.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### rrmpg/models/basemodel.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### README.rst

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
                
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

test assertions; fixtures; limits of test evidence The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-10.md`](../exercises/exercise-10.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `TestBaseModelFunctions` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `TestBaseModelFunctions` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
