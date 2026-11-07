# Code review and safe change 5: Begin with the concept

**Lesson ID:** `crime-data-hotspot-analysis-module-05-lesson-01`  
**Module ID:** `crime-data-hotspot-analysis-module-05`  
**Source focus:** `EDA.py` → `load_preprocessed_data`

## Purpose and learning objectives

Explain code review and safe change 5 in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Code review and safe change 5.

## Beginner explanation

In plain language, code review and safe change 5 is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `EDA.py` and locate `load_preprocessed_data`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `EDA.py`, `app.py`, `clustering_analysis.py`, `dimensionality_reduction.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: call graph; failure cases; safe extension

**Excerpt:** `EDA.py`. source tree absent; excerpt retained from earlier package

### EDA.py

The excerpt below is the selected implementation focus.
### app.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### clustering_analysis.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### dimensionality_reduction.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_preprocessed_data():
    """Load preprocessed data"""
    return pd.read_csv('chicago_crimes_preprocessed.csv')

def perform_eda(df):
    """
    Comprehensive exploratory data analysis
    """
    print("="*50)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*50)
    
    # Basic statistics
    print("\n1. DATASET OVERVIEW")
    print(f"Total Records: {len(df)}")
    print(f"Date Range: {df['Date'].min()} to {df['Date'].max()}")
    print(f"\nColumns: {df.columns.tolist()}")
    
    # Crime type distribution
    print("\n2. CRIME TYPE DISTRIBUTION")
    crime_counts = df['Primary Type'].value_counts()
    print(crime_counts.head(10))
    
    # Arrest rate
    arrest_rate = (df['Arrest'].sum() / len(df)) * 100
    print(f"\n3. ARREST RATE: {arrest_rate:.2f}%")
    
    # Domestic violence rate
    domestic_rate = (df['Domestic'].sum() / len(df)) * 100
    print(f"4. DOMESTIC VIOLENCE RATE: {domestic_rate:.2f}%")
    
    # Temporal patterns
    print("\n5. TEMPORAL PATTERNS")
    print(f"Crimes by Hour:\n{df['Hour'].value_counts().sort_index().head(10)}")
    print(f"\nCrimes by Day:\n{df['Day_of_Week'].value_counts()}")
    print(f"\nCrimes by Month:\n{df['Month'].value_counts().sort_index()}")
    
    return df

def create_eda_visualizations(df):
    """
    Create EDA visualizations
    """
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    
    # 1. Top 10 Crime Types
    crime_counts = df['Primary Type'].value_counts().head(10)
    axes[0, 0].barh(crime_counts.index, crime_counts.values, color='steelblue')
    axes[0, 0].set_xlabel('Number of Crimes')
    axes[0, 0].set_title('Top 10 Crime Types')
    axes[0, 0].invert_yaxis()
    
    # 2. Crimes by Hour
    hourly_crimes = df['Hour'].value_counts().sort_index()
    axes[0, 1].plot(hourly_crimes.index, hourly_crimes.values, marker='o', color='crimson')
    axes[0, 1].set_xlabel('Hour of Day')
    axes[0, 1].set_ylabel('Number of Crimes')
    axes[0, 1].set_title('Crimes by Hour of Day')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Crimes by Day of Week
    day_order = ['Monday', 'Tuesda
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

call graph; failure cases; safe extension The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-05.md`](../exercises/exercise-05.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `load_preprocessed_data` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `load_preprocessed_data` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
