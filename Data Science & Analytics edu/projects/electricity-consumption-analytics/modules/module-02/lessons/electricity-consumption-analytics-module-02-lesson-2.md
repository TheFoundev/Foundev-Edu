# Read constants and decorators in the source

**Lesson ID:** `electricity-consumption-analytics-module-02-lesson-2`

## Purpose and learning objectives

Study the implementation in [smap/constants.py] and [smap/decorators.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include replace_na_with_defaults_decorator, decorator, wrapper; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `smap/constants.py`, `smap/decorators.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `smap/constants.py` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `smap/decorators.py`, `import polars as pl` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def replace_na_with_defaults_decorator(rep_zero: dict, rep_min1: dict):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def decorator(func):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def wrapper(df, replace_NA_with_defaults=False, *args, **kwargs):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### smap/constants.py

```text
rep_zero = {
    'r_mean_max_no_min': ['cons'],
    'r_evening_noon_no_min': ['cons'],
    'r_morning_noon_no_min': ['cons'],
    'r_day_night_no_min': ['cons'],
    'r_var_wd_we': ['cons'],
    'r_mean_max': ['cons'],
    'r_min_mean': ['cons'],
    'r_max_wd_we': ['cons'],
    'ts_acf_mean3h': ['cons'],
    'ts_acf_mean3h_weekday': ['cons'],
    #"t15_value_min_guess": ['cons'],
    's_num_small_peaks': ['cons'],
    's_num_big_peaks': ['cons'],
    's_num_peaks': ['cons'],
    's_cor_wd_we': ['cons'],
    's15_sm_max': ['cons'],
    's_number_zeros': ['cons'],
    'ts_stl_varRem': ['cons'],
    #"t15_percent_above_base": ['cons']
}

rep_min1 = {
    #"t15_above_0.5kw", ['cons'],
    't_above_1kw': ['cons'],
    't_above_2kw': ['cons'],
    't_above_mean': ['cons']
    #"t15_above_base": ['cons'],
    #"t15_value_above_base": ['cons']
}


```

### smap/decorators.py

```text
# smap/decorators.py

import polars as pl

def replace_na_with_defaults_decorator(rep_zero: dict, rep_min1: dict):
    def decorator(func):
        def wrapper(df, replace_NA_with_defaults=False, *args, **kwargs):
            func_name = func.__name__
            
            # If the replace_NA_with_defaults flag is True, handle missing values before applying the function
            if replace_NA_with_defaults:
                # Handle columns in rep_zero
                if func_name in rep_zero:
                    for col in rep_zero[func_name]:
                        if col in df.columns:
                            df = df.with_columns(
                                pl.when(pl.col(col).is_infinite()).then(None).otherwise(pl.col(col)).alias(col)
                            )
                            # Use fill_nan to replace NaN values with 0
                            df = df.with_columns(
                                pl.col(col).fill_nan(0).fill_null(0).alias(col)
                            )
                
                # Handle columns in rep_min1
                if func_name in rep_min1:
                    for col in rep_min1[func_name]:
                        if col in df.columns:
                            df = df.with_columns(
                                pl.when(pl.col(col).is_infinite()).then(None).otherwise(pl.col(col)).alias(col)
                            )
                            # Use fill_nan to replace NaN values with -1
                            df = df.with_columns(
                                pl.col(col).fill_nan(-1).fill_null(-1).alias(col)
                            )
            
            # Apply the original function after handling missing values
            result = func(df, *args, **kwargs)
            
            return result
        
        return wrapper
    return decorator
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

This lesson ties its explanation to `smap/constants.py`, `smap/decorators.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
