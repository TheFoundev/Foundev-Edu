# Scaling, Null Handling, and Outliers: Begin with the concept

**Lesson ID:** `automated-eda-tool-module-03-lesson-01`  
**Module ID:** `automated-eda-tool-module-03`  
**Source focus:** `autoeda/feat_scaling.py` → `process_scaling`

## Purpose and learning objectives

Explain scaling, null handling, and outliers in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Feat Scaling and Notebook Data Optimization, Null Handler and Outliers.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `autoeda/feat_scaling.py` and locate `process_scaling`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `autoeda/feat_scaling.py`, `autoeda/notebook_data_optimization.py`, `autoeda/null_handler.py`, `autoeda/outliers.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `autoeda/feat_scaling.py`. source tree absent; excerpt retained from earlier package

### autoeda/feat_scaling.py

The excerpt below is the selected implementation focus.
### autoeda/notebook_data_optimization.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### autoeda/null_handler.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### autoeda/outliers.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from scipy.stats import skew
import json
import os
from pathlib import Path


def process_scaling(
        df: pd.DataFrame,
        output_dir: str = "../backend/output") -> None:
    """
    Processes scaling for numeric columns in the DataFrame, selects best scaler per column based on skewness,
    applies the scaling, and saves the scaled data and a report to backend/output.

    Args:
        df: Input DataFrame with data to scale.
        output_dir: Output directory path (default: ./backend/output).
    """
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Identify numeric columns
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

    # Filter columns: non-binary (nunique > 2) and not too many missing (<50%)
    filtered_cols = [
        col for col in numeric_cols
        if df[col].nunique() > 2 and df[col].isnull().mean() < 0.5
    ]

    # Initialize structures
    scaled_df = pd.DataFrame(index=df.index)
    scaler_report = {}

    # Process each column
    for col in filtered_cols:
        col_data = df[col]
        notna_mask = col_data.notna()

        scalers = {
            'StandardScaler': StandardScaler(),
            'MinMaxScaler': MinMaxScaler(),
            'RobustScaler': RobustScaler()
        }

        best_scaler_name = None
        best_skewness = float('inf')
        best_scaled_data = None

        # Evaluate each scaler
        for name, scaler in scalers.items():
            try:
                # Handle non-NaN values
                non_missing = col_data[notna_mask].values.reshape(-1, 1)
                scaled_vals = scaler.fit_transform(non_missing)
                col_skew = abs(skew(scaled_vals.flatten()))

                # Update best scaler if skewness is lower
                if col_skew < best_skewness:
                    best_skewness = col_skew
                    best_scaler_name = name
                    best_scaled_data = scaled_vals.flatten()

            except Exception as e:
                print(
            
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `process_scaling` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `process_scaling` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
