# Read summary stats and database in the source

**Lesson ID:** `automated-eda-tool-module-06-lesson-2`

## Purpose and learning objectives

Study the implementation in [autoeda/summary_stats.py] and [backend/config/database.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include load_and_clean_data, split_numerical_categorical, numerical_stats, most_frequent_values, categorical_stats, connectDB; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `autoeda/summary_stats.py`, `backend/config/database.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `autoeda/summary_stats.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/summary_stats.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/summary_stats.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `autoeda/summary_stats.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def load_and_clean_data(file_path, encoding):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def split_numerical_categorical(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def numerical_stats(num_df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def most_frequent_values(series):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def categorical_stats(cat_df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def full_stats(numerical_df, categorical_df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `backend/config/database.js`, `require('dotenv').config();` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `async function connectDB() {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### autoeda/summary_stats.py

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
            encoded_categorical_cols.append(col)
        else:
            numerical_cols.append(col)

    df_numerical = df[numerical_cols]
    df_categorical = df.select_dtypes(include='object')
    # Add detected encoded categorical columns to the categorical DataFrame
    df_categorical = pd.concat(
        [df_categorical, df[encoded_categorical_cols]], axis=1)

    return df_numerical, df_categorical

# only to be used on numerical data


def numerical_stats(num_df):
    """
    Calculate basic statistics for each numerical column in the DataFrame.
    Parameters:
        num_df: DataFrame containing numerical columns.
    Returns:
        dict: A dictionary where each key is a column name and the value is another dictionary with mean, median, min, max, std, and missing value count.
    """

    stats = {}
    for col in num_df.columns:
        stats[col] = {
            "mean": num_df[col].mean(),
            "median": num_df[col].median(),
            "min": num_df[col].min(),
            "max": num_df[col].max(),
            "std": num_df[col].std(),
            "missing": num_df[col].isnull().sum()
        }
    return stats

# returns most frequent values


def most_frequent_values(series):
```

### backend/config/database.js

```text
const { MongoClient } = require('mongodb');
require('dotenv').config();

const uri = process.env.MONGODB_URI;

const client = new MongoClient(uri);

async function connectDB() {
  try {
    await client.connect();
    await client.db("admin").command({ ping: 1 });
    console.log("Connected to MongoDB successfully!");
  } catch (err) {
    console.error("Failed to connect to MongoDB:", err);
  }
}

module.exports = connectDB;

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

This lesson ties its explanation to `autoeda/summary_stats.py`, `backend/config/database.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
