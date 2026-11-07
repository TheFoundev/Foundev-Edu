# Tests and Evidence Boundaries: Trace the code

**Lesson ID:** `automated-eda-tool-module-09-lesson-02`  
**Module ID:** `automated-eda-tool-module-09`  
**Source focus:** `autoeda/test_notebook_data_optimization.py` → `TestDataOptimization`

## Purpose and learning objectives

Trace `TestDataOptimization` in `autoeda/test_notebook_data_optimization.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Test code and evidence boundaries.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `autoeda/test_notebook_data_optimization.py` and locate `TestDataOptimization`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `autoeda/test_notebook_data_optimization.py`, `autoeda/test_null_handler.py`, `backend/services/run_data_optimization_test.py`, `unit_tests/test_data_optimizer.py`, `autoeda/notebook_data_optimization.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `autoeda/test_notebook_data_optimization.py`. source tree absent; excerpt retained from earlier package

### autoeda/test_notebook_data_optimization.py

The excerpt below is the selected implementation focus.
### autoeda/test_null_handler.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### backend/services/run_data_optimization_test.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### unit_tests/test_data_optimizer.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### autoeda/notebook_data_optimization.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import unittest
import pandas as pd
import numpy as np
from notebook_data_optimization import optimize_data


class TestDataOptimization(unittest.TestCase):

    def test_optimize_data(self):
        # Create a sample DataFrame
        df = pd.DataFrame({
            'id': range(1, 101),
            'category_low_cardinality': ['A', 'B'] * 50,
            'category_high_cardinality': [f'item_{i}' for i in range(100)],
            'float_values': np.random.rand(100) * 100,
            'int_values': np.random.randint(0, 1000, 100),
            'date_strings': pd.date_range('2024-01-01', periods=100, freq='D').astype(str)
        })
        df['float_values_copy'] = df['float_values'].copy()
        df['int_values_copy'] = df['int_values'].copy()

        # Apply optimization
        # Use a copy to avoid modifying original df for assertions
        df_optimized = optimize_data(df.copy())

        # Assertions
        # Check category conversion
        self.assertEqual(
            df_optimized['category_low_cardinality'].dtype.name, 'category')
        # Should remain object
        self.assertEqual(
            df_optimized['category_high_cardinality'].dtype.name, 'object')

        # Check numeric downcasting
        self.assertTrue(str(df_optimized['float_values'].dtype).startswith(
            'float32'))  # or float16 depending on data
        # e.g. int8, int16, int32
        self.assertTrue(
            str(df_optimized['int_values'].dtype).startswith('int'))

        # Check date conversion
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(
            df_optimized['date_strings']))

        # Check that values are not altered significantly for numeric types (simple check)
        # Compare values of float_values and float_values_copy
        np.testing.assert_allclose(df_optimized['float_values'].to_numpy(
        ), df_optimized['float_values_copy'].to_numpy(), rtol=1e-5)
        self.assertEqual(df_optimized['float_values'].dtype, np.float32)
        self.assertEqual(df_optimized['float_values_copy'].dtype, np.float32)

        # Ensure original int values are preserved by comparing with original
        # df values cast to the new dtype
   
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

test assertions; fixtures; limits of test evidence The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-09.md`](../exercises/exercise-09.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `TestDataOptimization` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `TestDataOptimization` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
