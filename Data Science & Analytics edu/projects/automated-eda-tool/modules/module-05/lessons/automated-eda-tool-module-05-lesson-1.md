# A beginner's model of null handler and outliers

**Lesson ID:** `automated-eda-tool-module-05-lesson-1`

## Purpose and learning objectives

Study the implementation in [autoeda/null_handler.py] and [autoeda/outliers.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include drop_nulls, replace_with_fixed, replace_with_mean, replace_with_median, replace_with_mode, forward_fill, backward_fill, evaluate_methods, process_outliers; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `autoeda/null_handler.py`, `autoeda/outliers.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `autoeda/null_handler.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/null_handler.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/null_handler.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/null_handler.py`, `from typing import Dict, Callable` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/null_handler.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def drop_nulls(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def replace_with_fixed(df: pd.DataFrame, value=0) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def replace_with_mean(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def replace_with_median(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def replace_with_mode(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def forward_fill(df: pd.DataFrame) -> pd.DataFrame:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/outliers.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/outliers.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/outliers.py`, `from scipy.stats import zscore` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/outliers.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/outliers.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def process_outliers(df_input: pd.DataFrame, base_output_dir: str):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/null_handler.py

```text
import pandas as pd
import numpy as np
import os
from typing import Dict, Callable
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# --------------*NULL HANDLING STRATEGIES*------------------


def drop_nulls(df: pd.DataFrame) -> pd.DataFrame:
    return df.dropna()


def replace_with_fixed(df: pd.DataFrame, value=0) -> pd.DataFrame:
    return df.fillna(value)


def replace_with_mean(df: pd.DataFrame) -> pd.DataFrame:
    df_filled = df.copy()
    for col in df_filled.select_dtypes(include=[np.number]):
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())
    return df_filled


def replace_with_median(df: pd.DataFrame) -> pd.DataFrame:
    df_filled = df.copy()
    for col in df_filled.select_dtypes(include=[np.number]):
        df_filled[col] = df_filled[col].fillna(df_filled[col].median())
    return df_filled


def replace_with_mode(df: pd.DataFrame) -> pd.DataFrame:
    df_filled = df.copy()
    for col in df.columns:
        if df[col].isnull().any():
            mode_val = df[col].mode()
            if not mode_val.empty:
                df_filled[col] = df_filled[col].fillna(mode_val.iloc[0])
            elif df[col].dtype in ['object', 'category']:
                df_filled[col] = df_filled[col].fillna("Unknown")
            else:
                df_filled[col] = df_filled[col].fillna(0)
    return df_filled


def forward_fill(df: pd.DataFrame) -> pd.DataFrame:
    return df.ffill()


def backward_fill(df: pd.DataFrame) -> pd.DataFrame:
    return df.bfill()

# ------------------*EVALUATION & STRATEGY SELECTION*----------------------


def evaluate_methods(original_df: pd.DataFrame,
                     cleaned_versions: Dict[str,
                                            pd.DataFrame],
                     log_lines: list) -> str:
    original_nulls = original_df.isnull().sum().sum()
    original_shape = original_df.shape
    best_score = float("-inf")
    best_method = None

    for name, df in cleaned_versions.items():
        remaining_nulls = df.isnull().sum().sum()
        nulls_removed = original_nulls - remaining_nulls
        row_ratio = df.shape[0] / original_shape[0] if original_shape[0] else 0
        col_ratio = df.shape[1] / original_shape[1] if original_shape[1] else 0

        score = ((nulls_removed / original_nulls if original_nulls >
                  0 else 1.0) * 0.5 + row_ratio * 0.25 + col_ratio * 0.25)

        log_lines.append(f"Method tried: {name}")
        log_lines.append(f" - Nulls removed: {nulls_removed}")
        log_lines.append(f" - Remaining nulls: {remaining_nulls}")
        log_lines.append(f" - Shape after cleaning: {df.shape}")
        log_lines.append(f" - Strategy score: {score:.4f}\n")

        if score > best_score:
            best_score = score
            best_method = name

    log_lines.append(f"✅ Best strategy selected: {best_method}\n")
    return best_method

# ------------------------* MAIN ENTRYPOINT *-------------------------------


def process_csv(input_path: str, output_path: str) -> None:
    if not os.path.exists(input_path):
        logging.error(f"Input file not found: {input_path}")
        return

    try:
        df = pd.read_csv(input_path)
    except Exception as e:
        logging.error(f"Failed to read CSV: {e}")
```

### autoeda/outliers.py

```text
import pandas as pd
import numpy as np
from scipy.stats import zscore
import json
import os

def process_outliers(df_input: pd.DataFrame, base_output_dir: str):
    """
    Detects, flags, caps, and removes outliers from a DataFrame.

    Parameters:
    ----------
    df_input : pd.DataFrame
        The input DataFrame with numeric columns for outlier processing.
    base_output_dir : str
        The directory where output files (CSV and JSON reports) will be saved.

    Returns:
    -------
    dict
        A dictionary containing:
        - 'flagged_df': DataFrame with outlier flags.
        - 'capped_df': DataFrame with outliers capped (Winsorized).
        - 'removed_df': DataFrame with outliers removed.
        - 'summary': Dictionary containing the outlier report data.
        - 'paths': Dictionary with paths to the saved files:
            - 'flagged_csv': Path to the flagged outliers CSV.
            - 'capped_csv': Path to the capped outliers CSV.
            - 'removed_csv': Path to the removed outliers CSV.
            - 'report_json': Path to the JSON outlier report.
            - 'summary_csv': Path to the tabular summary CSV.
    """
    os.makedirs(base_output_dir, exist_ok=True)

    # Work on a copy to avoid modifying the original DataFrame
    df = df_input.copy()
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    # Containers for results
    detection_methods = {}
    outliers_detected_count = {}
    rows_with_outliers = set()
    outlier_flags_df = pd.DataFrame(index=df.index)

    # Detect Skewness and apply outlier detection
    for col in numeric_cols:
        # Fill NaNs to avoid zscore errors and issues with quantile
        if df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median()) # Or some other appropriate strategy

        skew_val = df[col].skew()

        if abs(skew_val) < 1.0:
            # Z-score method
            method = "Z-score"
            if df[col].std() == 0: # Avoid division by zero if all values are the same
                z_scores_col = np.zeros_like(df[col], dtype=float)
                outliers = np.zeros_like(df[col], dtype=bool)
                lower_b = df[col].mean() # No real bounds if std is 0
                upper_b = df[col].mean()
            else:
                z_scores_col = zscore(df[col])
                outliers = np.abs(z_scores_col) > 3
                lower_b = df[col].mean() - 3 * df[col].std()
                upper_b = df[col].mean() + 3 * df[col].std()
        else:
            # IQR method
            method = "IQR"
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_b = Q1 - 1.5 * IQR
            upper_b = Q3 + 1.5 * IQR
            outliers = (df[col] < lower_b) | (df[col] > upper_b)

        detection_methods[col] = method
        outliers_detected_count[col] = int(outliers.sum())
        rows_with_outliers.update(df[outliers].index)
        outlier_flags_df[f"{col}_is_outlier"] = outliers.astype(int)

    # Create flagged dataset
    flagged_df = pd.concat([df_input.copy(), outlier_flags_df], axis=1) # Use original df_input for concatenation
    flagged_csv_path = os.path.join(base_output_dir, "autoEDA_outliers_flagged.csv")
    flagged_df.to_csv(flagged_csv_path, index=False)

    # Outlier Capping (Winsorization)
    capped_df = df.copy() # Use the NaN-filled 'df' for capping calculations
    for col in numeric_cols:
        # Re-calculate bounds based on the (potentially NaN-filled and now processed) column
        skew_val = capped_df[col].skew() # Skew might change slightly if NaNs were filled
        if abs(skew_val) < 1.0:
            if capped_df[col].std() == 0:
                lower_b_cap = capped_df[col].mean()
                upper_b_cap = capped_df[col].mean()
            else:
                lower_b_cap = capped_df[col].mean() - 3 * capped_df[col].std()
                upper_b_cap = capped_df[col].mean() 
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

This lesson ties its explanation to `autoeda/null_handler.py`, `autoeda/outliers.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
