# A beginner's model of data optimizer and encoding categorical

**Lesson ID:** `automated-eda-tool-module-03-lesson-1`

## Purpose and learning objectives

Study the implementation in [autoeda/data_optimizer.py] and [autoeda/encoding_categorical.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include optimize_dtypes, optimize_csv, label_encode, one_hot_encode; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `autoeda/data_optimizer.py`, `autoeda/encoding_categorical.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `autoeda/data_optimizer.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/data_optimizer.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/data_optimizer.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/data_optimizer.py`, `from pandas.api.types import is_string_dtype` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def optimize_csv(input_path: str, output_path: str) -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/encoding_categorical.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/encoding_categorical.py`, `from sklearn.preprocessing import LabelEncoder` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/encoding_categorical.py`, `from pandas.api.types import is_string_dtype` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/encoding_categorical.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/encoding_categorical.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def label_encode(df, columns):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def one_hot_encode(df, columns):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/data_optimizer.py

```text
import pandas as pd
import logging
import os
from pandas.api.types import is_string_dtype

# Configure logging to file: optimized_log.txt
# This will create optimized_log.txt if it doesn't exist, or append to it.
logging.basicConfig(filename='optimized_log.txt',
                    filemode='a',  # Append to the log file
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    force=True)  # force=True is important if re-running in same session


def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Optimizes the data types of a Pandas DataFrame.

    Args:
        df: The input DataFrame.

    Returns:
        A new DataFrame with optimized data types.
    """
    df_optimized = df.copy()
    logging.info("Starting data type optimization.")

    for col in df_optimized.columns:
        col_dtype = df_optimized[col].dtype
        original_memory = df_optimized[col].memory_usage(deep=True)

        try:
            # Determine if this looks like a date/time column
            is_date_col = any(keyword in col.lower()
                              for keyword in ['date', 'time', 'timestamp'])

            # Step 1: Try datetime conversion first for date-like string columns
            if is_date_col and is_string_dtype(col_dtype):
                try:
                    df_optimized[col] = pd.to_datetime(
                        df_optimized[col], errors='raise')
                    logging.info(f"Column '{col}': Converted to datetime.")
                except Exception as e_dt:
                    logging.warning(
                        f"Column '{col}': Could not convert to datetime. Error: {e_dt}")

            # Re-fetch dtype after potential datetime conversion
            col_dtype = df_optimized[col].dtype

            # Skip categorical/numeric optimization for datetime columns
            if pd.api.types.is_datetime64_any_dtype(col_dtype):
                optimized_memory = df_optimized[col].memory_usage(deep=True)
                if original_memory != optimized_memory:
                    logging.info(
                        f"Column '{col}': Memory usage changed from {original_memory} to {optimized_memory} bytes.")
                continue

            # Step 2: Categorical Conversion (for remaining string columns)
            if is_string_dtype(col_dtype):
                num_unique_values = df_optimized[col].nunique()
                if num_unique_values < 50:
                    df_optimized[col] = df_optimized[col].astype('category')
                    logging.info(
                        f"Column '{col}': Converted to category. Unique values: {num_unique_values}.")

            # Step 3: Numeric Downcasting (Floats)
            elif col_dtype == 'float64':
                df_optimized[col] = df_optimized[col].astype('float32')
                logging.info(
                    f"Column '{col}': Downcast to float32.")

            # Step 4: Numeric Downcasting (Integers)
            elif col_dtype == 'int64':
                df_optimized[col] = df_optimized[col].astype('int32')
                logging.info(
                    f"Column '{col}': Downcast to int32 or smaller (e.g., int16, int8).")
        except Exception as e:
            logging.error(
                f"Column '{col}': Error during optimization. Original dtype: {col_dtype}. Error: {e}")
            continue  # Continue to the next column

        optimized_memory = df_optimized[col].memory_usage(deep=True)
        if original_memory != optimized_memory:  # Log only if memory changed
            logging.info(
                f"Column '{col}': Memory usage changed from {original_memory} to {optimized_memory} bytes.")

    logging.info("Data type optimization finished.")
    return df_optimized


def optimize_csv(input_path: str, output_path: str) -> None:
    """
    Reads a CSV, optimizes its data types, and saves it to a new CSV.

    Args:
        input_pat
```

### autoeda/encoding_categorical.py

```text
"""
Module for encoding categorical features.
Provides functions for label encoding and one-hot encoding.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from pandas.api.types import is_string_dtype
import logging
import os

# Set up logging to file in backend/output
OUTPUT_DIR = "backend/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
LOG_FILE = os.path.join(OUTPUT_DIR, "encoding_log.txt")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def label_encode(df, columns):
    """
    Applies Label Encoding to the specified columns in the dataframe.
    """
    df = df.copy()
    le = LabelEncoder()
    for col in columns:
        if is_string_dtype(df[col].dtype):
            df[col] = le.fit_transform(df[col].astype(str))
            logging.info(f"Label encoding applied on column: {col}")
        else:
            logging.warning(f"Skipped column (non-object dtype): {col}")
    return df

def one_hot_encode(df, columns):
    """
    Applies One-Hot Encoding to the specified columns in the dataframe.
    """
    df = df.copy()
    df = pd.get_dummies(df, columns=columns)
    logging.info(f"One-hot encoding applied on columns: {columns}")
    return df

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

This lesson ties its explanation to `autoeda/data_optimizer.py`, `autoeda/encoding_categorical.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
