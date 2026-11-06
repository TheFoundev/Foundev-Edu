# Read test code and evidence boundaries in the source

**Lesson ID:** `automated-eda-tool-module-19-lesson-2`

## Purpose and learning objectives

Read test implementations autoeda/test_notebook_data_optimization.py, autoeda/test_null_handler.py, backend/services/run_data_optimization_test.py, unit_tests/test_data_optimizer.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `autoeda/test_notebook_data_optimization.py`, `autoeda/test_null_handler.py`, `backend/services/run_data_optimization_test.py`, `unit_tests/test_data_optimizer.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `autoeda/test_notebook_data_optimization.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_notebook_data_optimization.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_notebook_data_optimization.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_notebook_data_optimization.py`, `from notebook_data_optimization import optimize_data` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestDataOptimization(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_optimize_data(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_optimize_data_empty_df(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_optimize_data_all_numeric(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_optimize_data_with_non_convertible_date(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/test_null_handler.py`, `import pytest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_null_handler.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_null_handler.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_null_handler.py`, `import tempfile` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/test_null_handler.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def empty_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def no_nulls_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def numeric_nulls_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def categorical_nulls_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def all_null_column_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def mixed_nulls_df():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `backend/services/run_data_optimization_test.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/services/run_data_optimization_test.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/services/run_data_optimization_test.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/services/run_data_optimization_test.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `backend/services/run_data_optimization_test.py`, `from autoeda.notebook_data_optimization import optimize_data` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def setup_logging(log_file_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def main():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `unit_tests/test_data_optimizer.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `unit_tests/test_data_optimizer.py`, `import pytest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `unit_tests/test_data_optimizer.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `unit_tests/test_data_optimizer.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `unit_tests/test_data_optimizer.py`, `from pandas.api.types import is_datetime64_any_dtype` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_categorical_conversion():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_numerical_conversion():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_optimize_csv(mock_read_csv, mock_to_csv, mock_optimize_dtypes):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/test_notebook_data_optimization.py

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
        pd.testing.assert_series_equal(
            df_optimized['int_values'],
            df['int_values_copy'].astype(
                df_optimized['int_values'].dtype),
            check_dtype=True,
            check_names=False)

    def test_optimize_data_empty_df(self):
        df = pd.DataFrame()
        df_optimized = optimize_data(df.copy())
        self.assertTrue(df_optimized.empty)

    def test_optimize_data_all_numeric(self):
        df = pd.DataFrame({
            'A': np.array([1, 2, 3], dtype='int64'),
            'B': np.array([1.0, 2.0, 3.0], dtype='float64')
        })
        df_optimized = optimize_data(df.copy())
        self.assertTrue(str(df_optimized['A'].dtype).startswith('int'))
        self.assertTrue(str(df_optimized['B'].dtype).startswith('float32'))

    def test_optimize_data_with_non_convertible_date(self):
        df = pd.DataFrame({
            'date_col_valid': ['2023-01-01', '2023-01-02'],
            'date_col_invalid': ['2023-01-01', 'not_a_date']
        })
        df_optimized = optimize_data(df.copy())
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(
            df_optimized['date_col_valid']))
        self.assertEqual(df_optimized['date_col_invalid'].dtype.name, 'object')


if __name__ == '__main__':
    unittest.main()

```

### autoeda/test_null_handler.py

```text
import pytest
import pandas as pd
import numpy as np
import tempfile
import os
from pandas import testing as tm
from autoeda import null_handler 
# Assuming autoeda is in PYTHONPATH or installed
# If autoeda is a local directory and not installed, Python might not find it
# without adjusting sys.path. For now, let's assume it's discoverable.

# Specifically import all functions to be tested
from autoeda.null_handler import (
    drop_nulls,
    replace_with_fixed,
    replace_with_mean,
    replace_with_median,
    replace_with_mode,
    forward_fill,
    backward_fill,
    evaluate_methods,
    process_csv
)

# region Fixtures
@pytest.fixture
def empty_df():
    """DataFrame that is completely empty."""
    return pd.DataFrame()

@pytest.fixture
def no_nulls_df():
    """DataFrame with no null values."""
    data = {'col_a': [1, 2, 3], 'col_b': ['x', 'y', 'z'], 'col_c': [4.0, 5.1, 6.2]}
    return pd.DataFrame(data)

@pytest.fixture
def numeric_nulls_df():
    """DataFrame with nulls only in numeric columns."""
    data = {'num_col1': [1.0, np.nan, 3.0, np.nan],
            'num_col2': [np.nan, 2.2, 3.3, 4.4],
            'cat_col1': ['a', 'b', 'c', 'd']}
    return pd.DataFrame(data)

@pytest.fixture
def categorical_nulls_df():
    """DataFrame with nulls only in categorical columns."""
    data = {'num_col1': [1.0, 2.0, 3.0, 4.0],
            'cat_col1': ['a', np.nan, 'c', np.nan],
            'cat_col2': [np.nan, 'x', 'y', 'z']}
    return pd.DataFrame(data)

@pytest.fixture
def all_null_column_df():
    """DataFrame with at least one column containing all nulls."""
    data = {'num_col_all_null': [np.nan, np.nan, np.nan],
            'cat_col_all_null': [np.nan, np.nan, np.nan],
            'mixed_col': [1, np.nan, 'a']}
    return pd.DataFrame(data)

@pytest.fixture
def mixed_nulls_df():
    """DataFrame with a mix of numeric and categorical columns, and nulls in various places."""
    data = {'A_num': [1.0, np.nan, 3.0, 4.0, 5.0],
            'B_cat': ['apple', 'banana', np.nan, 'cherry', 'banana'],
            'C_num_with_nan': [10.0, 20.0, np.nan, np.nan, 50.0],
            'D_cat_with_nan': [None, 'dog', 'cat', None, 'dog'],
            'E_all_nan_numeric': [np.nan, np.nan, np.nan, np.nan, np.nan],
            'F_all_nan_cat': [np.nan, np.nan, np.nan, np.nan, np.nan]}
    return pd.DataFrame(data)

@pytest.fixture
def all_nan_object_col_df():
    """DataFrame with a single column of object dtype that is all NaN."""
    return pd.DataFrame({'obj_all_nan': pd.Series([np.nan, np.nan, np.nan], dtype=object)})

# endregion Fixtures

# region Tests for drop_nulls
def test_drop_nulls_with_numeric_nulls(numeric_nulls_df):
    """Test drop_nulls with nulls in numeric columns."""
    original_shape = numeric_nulls_df.shape
    cleaned_df = drop_nulls(numeric_nulls_df.copy())
    assert cleaned_df.isnull().sum().sum() == 0
    assert cleaned_df.shape[0] < original_shape[0] # Rows should be dropped
    assert cleaned_df.shape[1] == original_shape[1] # Columns should remain the same

def test_drop_nulls_with_categorical_nulls(categorical_nulls_df):
    """Test drop_nulls with nulls in categorical columns."""
    original_shape = categorical_nulls_df.shape
    cleaned_df = drop_nulls(categorical_nulls_df.copy())
    assert cleaned_df.isnull().sum().sum() == 0
    assert cleaned_df.shape[0] < original_shape[0]
    assert cleaned_df.shape[1] == original_shape[1]

def test_drop_nulls_with_all_null_column(all_null_column_df):
    """Test drop_nulls with a column that is entirely null.
    Pandas dropna by default drops rows if ANY value in the row is NaN.
    If a column is all NaN, and other columns have data, rows might not be dropped
    unless all columns for a row are NaN, or if how='all' is used.
```

### backend/services/run_data_optimization_test.py

```text
import pandas as pd
import logging
import os
import sys

# Add the autoeda directory to the Python path
# This is needed to import the optimize_data function
# Assuming the script is in backend/services and autoeda is at the root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from autoeda.notebook_data_optimization import optimize_data

def setup_logging(log_file_path):
    """Configures logging to file and console."""
    log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove any existing handlers to avoid duplication
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Add file handler
    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    # Log confirmation of file handler setup
    # This initial log might go to console if stream handler is added first or if not configured yet for file
    # For it to reliably go to file, it needs to be after addHandler, but let's see
    # We will get a specific logger for this initial message.
    init_logger = logging.getLogger("init_setup")
    init_logger.info(f"FileHandler configured for {log_file_path}. Stream: {file_handler.stream}")


    # Add stream handler (for console)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_formatter)
    root_logger.addHandler(stream_handler)

    return file_handler # Return file_handler to be closed later

def main():
    # Define file paths
    input_csv_path = os.path.join(project_root, 'backend', 'output', 'sample_input_for_optimization.csv')
    output_csv_path = os.path.join(project_root, 'backend', 'output', 'optimized_sample_output.csv')
    log_file_path = os.path.join(project_root, 'backend', 'output', 'data_optimization_run.txt')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)

    # Setup logging for this script and get the file handler
    file_handler_to_close = setup_logging(log_file_path)
    
    logger = logging.getLogger(__name__) # Get a logger for the current module

    logger.info(f"Script started. Input CSV: {input_csv_path}, Output CSV: {output_csv_path}, Log File: {log_file_path}")

    # Check if input CSV exists
    if not os.path.exists(input_csv_path):
        logger.error(f"Input CSV file not found at {input_csv_path}")
        return

    try:
        # Load the sample CSV
        logger.info(f"Loading data from {input_csv_path}")
        df = pd.read_csv(input_csv_path)
        logger.info("Data loaded successfully.")
        logger.info(f"Original memory usage: {df.memory_usage(deep=True).sum()} bytes")
        logger.info("Original dtypes:\n%s", df.dtypes)

        # Call the optimize_data function
        logger.info("Optimizing data...")
        df_optimized = optimize_data(df.copy()) # Use .copy() if optimize_data modifies inplace
        logger.info("Data optimization complete.")
        logger.info(f"Optimized memory usage: {df_optimized.memory_usage(deep=True).sum()} bytes")
        logger.info("Optimized dtypes:\n%s", df_optimized.dtypes)


        # Save the optimized DataFrame
        logger.info(f"Saving optimized data to {output_csv_path}")
        df_optimized.to_csv(output_csv_path, index=False)
        logger.info("Optimized data saved successfully.")

    except FileNotFoundError:
        logger.error(f"Error: The file {input_csv_path} was not found.")
    except pd.errors.EmptyDataError:
        logger.error(f"Error: The file {input_csv_path} is empty.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

    logger.info("Script finished.")

    if file_handler_to_close:
        logger.info(f"Closing log fi
```

### unit_tests/test_data_optimizer.py

```text
import pandas as pd
import pytest
import sys
import os
from pandas.api.types import is_datetime64_any_dtype

from unittest.mock import patch, MagicMock
from autoeda.data_optimizer import optimize_csv



sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from autoeda.data_optimizer import optimize_dtypes
from autoeda.data_optimizer import optimize_csv


def test_categorical_conversion():

    df = pd.DataFrame({
        "small_category": [f'item_{i % 49}' for i in range(100)],  
        "large_category": [f'item_{i % 52}' for i in range(100)],  
        'numeric': list(range(100))  
    })
    optimized_df = optimize_dtypes(df)
    assert optimized_df['small_category'].dtype.name == 'category', "small_category should be converted to category"
    assert optimized_df['large_category'].dtype.name != 'category', "large_category should not be converted"
    assert optimized_df['numeric'].dtype.kind in ['i', 'f'], "numeric column should remain numeric"


def test_numerical_conversion():
    int_data=[3,45,32,2233,739281802301]
    float_data=[4.7,8.8,3,72.89213,9823.09329]
    date_data = ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']
    bad_date_data= ['not-a-date', '2023-02-30', '13-2023-01', 'someday', '']
    df=pd.DataFrame({
         'float_col': float_data,
        'int_col': int_data,
        'created_date': date_data,
        'bad_timestamp': bad_date_data
    })

    df_optimized=optimize_dtypes(df)
    assert df_optimized['float_col'].dtype.name in ['float32', 'float16']
    assert df_optimized['int_col'].dtype.name in ['int32','int16']
    assert is_datetime64_any_dtype(df_optimized['created_date']), "created_date should be datetime"
    assert not pd.api.types.is_datetime64_any_dtype(df_optimized['bad_timestamp']), "bad_timestamp should not be converted"

@patch("autoeda.data_optimizer.optimize_dtypes")
@patch("pandas.DataFrame.to_csv")
@patch("pandas.read_csv")
def test_optimize_csv(mock_read_csv, mock_to_csv, mock_optimize_dtypes):

    input_path = "dummy_input.csv"
    output_path = "dummy_output.csv"

    
    dummy_df = pd.DataFrame({
        'col1': ['A', 'B', 'A'],
        'col2': [1.0, 2.0, 3.0],
        'date_col': ['2023-01-01', '2023-01-02', '2023-01-03']
    })

    
    mock_read_csv.return_value = dummy_df
    mock_optimize_dtypes.return_value = dummy_df  

    
    optimize_csv(input_path, output_path)

    
    mock_read_csv.assert_called_once_with(input_path)
    mock_optimize_dtypes.assert_called_once_with(dummy_df)
    mock_to_csv.assert_called_once_with(output_path, index=False)







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

This lesson ties its explanation to `autoeda/test_notebook_data_optimization.py`, `autoeda/test_null_handler.py`, `backend/services/run_data_optimization_test.py`, `unit_tests/test_data_optimizer.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### autoeda/notebook_data_optimization.py

### autoeda/notebook_data_optimization.py

```text
import pandas as pd
import numpy as np
import logging

# Get a logger for this module
logger = logging.getLogger(__name__)


def optimize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimizes the data types of a pandas DataFrame to reduce memory usage.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with optimized data types.
    """
    logger.info("Starting data type optimization.")
    processed_date_cols = set()

    # Convert date-like columns first
    for col in df.columns:
        if any(x in col.lower() for x in ['date', 'time', 'timestamp']):
            if df[col].dtype == 'object':  # Only attempt conversion if it's an object type
                # Mark as processed for date conversion attempt
                processed_date_cols.add(col)
                try:
                    logger.info(
                        f"Attempting to convert column '{col}' to datetime objects.")
                    df[col] = pd.to_datetime(df[col])
                    logger.info(
                        f"Successfully converted column '{col}' to datetime.")
                except Exception as e:
                    logger.warning(
                        f"Could not convert column '{col}' to datetime: {e}. It will remain an object type.")
                    # If conversion fails, it remains object.
                    pass

    # Convert object columns with low cardinality to category
    # Exclude columns that were identified as date-like but failed conversion,
    # they should remain object.
    for col in df.select_dtypes(include='object'):
        if col not in processed_date_cols or pd.api.types.is_datetime64_any_dtype(
                df[col]):
            # If it's not a processed date col OR it was successfully converted to datetime (which means it's not object anymore)
            # This check might be redundant for the second part if
            # select_dtypes(include='object') is efficient
            if df[col].nunique() < 50:
                # Additional check: ensure it's not a date-like column that
                # failed conversion
                is_failed_date_col = any(
                    x in col.lower() for x in [
                        'date',
                        'time',
                        'timestamp']) and col in processed_date_cols and not pd.api.types.is_datetime64_any_dtype(
                    df[col])
                if not is_failed_date_col:
                    logger.info(f"Converting column '{col}' to category type.")
                    df[col] = df[col].astype('category')
                else:
                    logger.info(
                        f"Skipping category conversion for failed date column '{col}'.")

    # Downcast numeric columns
    for col in df.select_dtypes(include=['float']):
        logger.info(f"Downcasting float column '{col}'.")
        df[col] = pd.to_numeric(df[col], downcast='float')
    for col in df.select_dtypes(include=['int']):
        logger.info(f"Downcasting integer column '{col}'.")
        df[col] = pd.to_numeric(df[col], downcast='integer')

    logger.info("Data type optimization complete.")
    return df

```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
