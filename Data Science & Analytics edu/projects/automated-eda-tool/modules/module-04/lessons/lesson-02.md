# Summary Statistics and Cleaning Runner: Trace the code

**Lesson ID:** `automated-eda-tool-module-04-lesson-02`  
**Module ID:** `automated-eda-tool-module-04`  
**Source focus:** `autoeda/summary_stats.py` → `load_and_clean_data`

## Purpose and learning objectives

Trace `load_and_clean_data` in `autoeda/summary_stats.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Summary Stats and Database, Runner and Eslint.config.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `autoeda/summary_stats.py` and locate `load_and_clean_data`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `autoeda/summary_stats.py`, `backend/config/database.js`, `backend/services/runner.py`, `frontend/eslint.config.js`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `autoeda/summary_stats.py`. source tree absent; excerpt retained from earlier package

### autoeda/summary_stats.py

The excerpt below is the selected implementation focus.
### backend/config/database.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### backend/services/runner.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### frontend/eslint.config.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import pandas as pd
import numpy as np
import os
import json


def load_and_clean_data(file_path, encoding):
    """
    Loads a csv file into a pandas DataFrame, removes duplicate rows, fills missing values in numeric columns with the mean, fills missing values in categorical columns with the mode, and strips whitespace from string columns.
    Args:
        file_path: Path to the CSV file.
        encoding: Encoding to use for reading the file.
    Returns:
        pandas.DataFrame: Cleaned DataFrame.
    """
    try:
        df = pd.read_csv(file_path, encoding=encoding)
    except Exception as e:
        raise ValueError(f"could not load file: {e}")

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fill missing values in numeric columns with (mean)
    for col in df.select_dtypes(include='number'):
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing values in categorical columns (mode)
    for col in df.select_dtypes(include='object'):
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].mode()[0])

    # Strip leading/trailing whitespace from string columns
    for col in df.select_dtypes(include='object'):
        df[col] = df[col].str.strip()

    return df


def split_numerical_categorical(df):
    """
    Splits a DataFrame's columns into numerical and categorical columns.
    Numerical columns are those with numeric data types, (here)excluding columns with 10 or fewer unique integer values, which are treated as encoded categorical columns.
    Args:
        df: Input DataFrame.
    Returns:
        Tuple: A tuple containing the numerical columns DataFrame and the categorical columns DataFrame.
    """
    # Get all columns with numeric data types
    numeric_cols = df.select_dtypes(include='number').columns

    numerical_cols = []
    encoded_categorical_cols = []

    # Heuristic: If the column has 10 or fewer unique integer values, treat as
    # categorical
    for col in numeric_cols:
        unique_vals = df[col].dropna().unique()
        if len(unique_vals) <= 10 and all(float(val).is_integer()
                                          for val in unique_vals):
            encoded
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-04.md`](../exercises/exercise-04.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `load_and_clean_data` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `load_and_clean_data` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
