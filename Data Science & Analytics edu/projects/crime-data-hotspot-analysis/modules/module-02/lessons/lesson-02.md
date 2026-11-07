# Dimensionality Reduction and EDA: Trace the code

**Lesson ID:** `crime-data-hotspot-analysis-module-02-lesson-02`  
**Module ID:** `crime-data-hotspot-analysis-module-02`  
**Source focus:** `dimensionality_reduction.py` → `prepare_features`

## Purpose and learning objectives

Trace `prepare_features` in `dimensionality_reduction.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Dimensionality Reduction and EDA.

## Beginner explanation

In plain language, dimensionality reduction and eda is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `dimensionality_reduction.py` and locate `prepare_features`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `dimensionality_reduction.py`, `EDA.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `dimensionality_reduction.py`. source tree absent; excerpt retained from earlier package

### dimensionality_reduction.py

The excerpt below is the selected implementation focus.
### EDA.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import mlflow

def prepare_features(df):
    """
    Prepare features for dimensionality reduction
    """
    feature_cols = ['Latitude', 'Longitude', 'Hour', 'Month', 'Is_Weekend',
                    'Crime_Severity_Score', 'Crime_Type_Encoded', 
                    'Location_Desc_Encoded']
    
    # Add day of week encoding
    df['Day_of_Week_Encoded'] = pd.factorize(df['Day_of_Week'])[0]
    feature_cols.append('Day_of_Week_Encoded')
    
    X = df[feature_cols].copy()
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, feature_cols

def apply_pca(X_scaled, feature_cols, n_components=3):
    """
    Apply PCA for dimensionality reduction
    """
    print("\n" + "="*50)
    print("PCA - Principal Component Analysis")
    print("="*50)
    
    # Full PCA to see explained variance
    pca_full = PCA()
    pca_full.fit(X_scaled)
    
    # Scree plot
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(range(1, len(pca_full.explained_variance_ratio_) + 1),
             np.cumsum(pca_full.explained_variance_ratio_), marker='o')
    plt.xlabel('Number of Components')
    plt.ylabel('Cumulative Explained Variance')
    plt.title('PCA Explained Variance')
    plt.grid(True)
    plt.axhline(y=0.7, color='r', linestyle='--', label='70% threshold')
    plt.axhline(y=0.8, color='g', linestyle='--', label='80% threshold')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.bar(range(1, min(11, len(pca_full.explained_variance_ratio_) + 1)),
            pca_full.explained_variance_ratio_[:10])
    plt.xlabel('Principal Component')
    plt.ylabel('Explained Variance Ratio')
    plt.title('Individual Component Variance')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pca_variance_analysis.png', dpi=300)
    plt.close()
    
    # Apply PCA with n_components
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
  
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `prepare_features` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `prepare_features` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
