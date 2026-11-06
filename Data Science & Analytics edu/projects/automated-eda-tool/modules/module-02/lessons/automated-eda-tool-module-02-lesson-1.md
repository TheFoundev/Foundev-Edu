# A beginner's model of pca transformer and pipeline

**Lesson ID:** `automated-eda-tool-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [autoeda/pca_transformer.py] and [autoeda/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include apply_pca, run_outlier_pipeline, run_pca_pipeline; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `autoeda/pca_transformer.py`, `autoeda/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `autoeda/pca_transformer.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pca_transformer.py`, `from sklearn.decomposition import PCA` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pca_transformer.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def apply_pca(df, n_components=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `autoeda/pipeline.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pipeline.py`, `from autoeda import outliers` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pipeline.py`, `from autoeda.pca_transformer import apply_pca  # Import here to avoid circular dependency` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_outlier_pipeline(scaled_csv_path, output_dir):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def run_pca_pipeline(input_csv_path, output_dir, n_components=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/pca_transformer.py

```text
import pandas as pd
from sklearn.decomposition import PCA
import os


def apply_pca(df, n_components=None):
    """
    Applies Principal Component Analysis (PCA) to the given DataFrame.

    Args:   df: Input DataFrame with numeric features.
            n_components: Number of principal components to keep.
                If None, all components are retained.

    Returns:
        tuple[pd.dataFrame, dict[str, Any]]:
            - Transformed dataFrame with principal components
            - Metadata containing explained variance and column mappings
    """

    numeric_df = df.select_dtypes(include=["float64", "int64"])
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(numeric_df)

    col_names = [f"PC{i + 1}" for i in range(components.shape[1])]
    pca_df = pd.DataFrame(components, columns=col_names, index=df.index)

    metadata = {
        "explained_variance_ratio": pca.explained_variance_ratio_.tolist(),
        "n_components": components.shape[1],
        "original_columns": numeric_df.columns.tolist(),
        "pca_columns": col_names
    }

    return pca_df, metadata


if __name__ == "__main__":
    INPUT_FILE = "./backend/output/autoEDA_outliers_removed.csv"
    OUTPUT_FILE = "./backend/output/pca_transformed.csv"
    OUTPUT_LOG_FILE = "./backend/output/pca_transformed_log.csv"

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    transformed_df, meta = apply_pca(df)

    transformed_df.to_csv(OUTPUT_FILE, index=False)
    pd.DataFrame([meta]).to_csv(OUTPUT_LOG_FILE, index=False)

    print("PCA transformation completed.")
    print("Explained Variance Ratio:", meta["explained_variance_ratio"])
    print("Output saved to:", OUTPUT_FILE)

```

### autoeda/pipeline.py

```text
"""
pipeline.py: Outlier Processing Pipeline for AutoEDA

This module provides a high-level function to orchestrate outlier detection, flagging, capping, and removal using the logic from outliers.py. It is designed for integration with CLI, backend, or notebook workflows.
"""

import os
import pandas as pd


def run_outlier_pipeline(scaled_csv_path, output_dir):
    """
    Run the full outlier processing pipeline on a scaled dataset.

    Parameters
    ----------
    scaled_csv_path : str
        Path to the scaled CSV file (input dataset).
    output_dir : str
        Directory to store all output files (flagged, capped, removed datasets, and reports).

    Returns
    -------
    dict
        Dictionary containing:
            - 'flagged_csv': Path to flagged dataset
            - 'capped_csv': Path to capped dataset
            - 'removed_csv': Path to dataset with outliers removed
            - 'summary_report_json': Path to outlier summary report (JSON)
            - 'summary_report_csv': Path to outlier summary report (CSV)
            - 'outlier_stats': Outlier statistics/metadata (dict)

    Raises
    ------
    FileNotFoundError: If the input file does not exist.
    ValueError: If the input file is malformed or cannot be loaded.

    Example
    -------
    >>> result = run_outlier_pipeline('output-files/autoEDA_scaled_output.csv', 'output-files/outlier_results')
    >>> print(result['flagged_csv'])
    """
    if not os.path.isfile(scaled_csv_path):
        raise FileNotFoundError(f"Input file not found: {scaled_csv_path}")

    os.makedirs(output_dir, exist_ok=True)

    try:
        df = pd.read_csv(scaled_csv_path)
    except Exception as e:
        raise ValueError(f"Failed to load input CSV: {e}")

    # Call the main orchestration function from the refactored outliers.py
    # outliers.process_outliers now handles saving files and returns paths and summary.
    # Import here to avoid circular dependency if outliers.py also imports pipeline.
    from autoeda import outliers
    outlier_processing_results = outliers.process_outliers(df, output_dir)

    # The process_outliers function already saves the files.
    # We just need to return the paths and summary provided by it.
    # The keys in outlier_processing_results['paths'] are:
    # 'flagged_csv', 'capped_csv', 'removed_csv', 'report_json', 'summary_csv'
    # The key in outlier_processing_results['summary'] is the summary dict itself.

    return {
        'flagged_csv': outlier_processing_results['paths']['flagged_csv'],
        'capped_csv': outlier_processing_results['paths']['capped_csv'],
        'removed_csv': outlier_processing_results['paths']['removed_csv'],
        'summary_report_json': outlier_processing_results['paths']['report_json'],
        'summary_report_csv': outlier_processing_results['paths']['summary_csv'],
        'outlier_stats': outlier_processing_results.get('summary', {})
    }


def run_pca_pipeline(input_csv_path, output_dir, n_components=None):
    """
    Run the PCA transformation pipeline.

    Parameters
    ----------
    input_csv_path : str
        Path to the input CSV file.
    output_dir : str
        Directory to store all output files.
    n_components : int, optional
        Number of principal components to keep. If None, all components are retained.

    Returns
    -------
    dict
        Dictionary containing:
            - 'pca_transformed_csv': Path to the transformed dataset.
            - 'pca_summary': Path to the PCA summary report (JSON).

    Raises
    ------
    FileNotFoundError: If the input file does not exist.
    ValueError: If the input file is malformed or cannot be loaded.
    """
    if not os.path.isfile(input_csv_path):
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

This lesson ties its explanation to `autoeda/pca_transformer.py`, `autoeda/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
