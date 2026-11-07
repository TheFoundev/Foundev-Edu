# PCA Pipeline and Categorical Encoding: Trace the code

**Lesson ID:** `automated-eda-tool-module-02-lesson-02`  
**Module ID:** `automated-eda-tool-module-02`  
**Source focus:** `autoeda/pca_transformer.py` → `apply_pca`

## Purpose and learning objectives

Trace `apply_pca` in `autoeda/pca_transformer.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Pca Transformer and Pipeline, Data Optimizer and Encoding Categorical.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `autoeda/pca_transformer.py` and locate `apply_pca`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `autoeda/pca_transformer.py`, `autoeda/pipeline.py`, `autoeda/data_optimizer.py`, `autoeda/encoding_categorical.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `autoeda/pca_transformer.py`. source tree absent; excerpt retained from earlier package

### autoeda/pca_transformer.py

The excerpt below is the selected implementation focus.
### autoeda/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### autoeda/data_optimizer.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### autoeda/encoding_categorical.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

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

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-02.md`](../exercises/exercise-02.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `apply_pca` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `apply_pca` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
