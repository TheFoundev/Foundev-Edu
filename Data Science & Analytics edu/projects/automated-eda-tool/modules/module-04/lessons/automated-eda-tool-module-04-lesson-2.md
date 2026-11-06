# Read feat scaling and notebook data optimization in the source

**Lesson ID:** `automated-eda-tool-module-04-lesson-2`

## Purpose and learning objectives

Study the implementation in [autoeda/feat_scaling.py] and [autoeda/notebook_data_optimization.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include process_scaling, optimize_data; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `autoeda/feat_scaling.py`, `autoeda/notebook_data_optimization.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `autoeda/feat_scaling.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feat_scaling.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feat_scaling.py`, `from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feat_scaling.py`, `from scipy.stats import skew` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/feat_scaling.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def process_scaling(` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/notebook_data_optimization.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/notebook_data_optimization.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/notebook_data_optimization.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def optimize_data(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/feat_scaling.py

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
                    f"⚠️ Skipped scaler '{name}' for column '{col}': {str(e)}")
                continue

        # Reconstruct full column with NaNs preserved
        full_col = pd.Series(np.nan, index=col_data.index)
        full_col[notna_mask] = best_scaled_data

        scaled_df[col] = full_col
        scaler_report[col] = best_scaler_name

    # Save scaled data to backend/output
    scaled_path = os.path.join(output_dir, "autoEDA_scaled_output.csv")
    scaled_df.to_csv(scaled_path, index=False)

    # Save scaler report to backend/output
    report_path = os.path.join(output_dir, "scaling_report.json")
    with open(report_path, 'w') as f:
        json.dump(scaler_report, f, indent=4)

    print(f"✅ Scaled data saved to: {scaled_path}")
    print(f"📋 Scaler report saved to: {report_path}")


if __name__ == "__main__":
    # Load your file
    df = pd.read_csv("laptopData.csv")

    process_scaling(df)

```

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

This lesson ties its explanation to `autoeda/feat_scaling.py`, `autoeda/notebook_data_optimization.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
