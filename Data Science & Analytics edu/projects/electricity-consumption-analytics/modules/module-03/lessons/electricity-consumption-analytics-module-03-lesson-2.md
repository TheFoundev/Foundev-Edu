# Read helpers and module in the source

**Lesson ID:** `electricity-consumption-analytics-module-03-lesson-2`

## Purpose and learning objectives

Study the implementation in [smap/helpers.py] and [smap/module.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include calc_features_consumption, c_week, s_max, s_min, c_morning, c_noon; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `smap/helpers.py`, `smap/module.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `smap/helpers.py`, `import polars as pl` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/helpers.py`, `from smap import *` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def calc_features_consumption(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `smap/module.py`, `import polars as pl` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/module.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/module.py`, `from typing import List` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/module.py`, `import statsmodels.api as sm` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/module.py`, `from statsmodels.nonparametric.smoothers_lowess import lowess` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def c_week(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def s_max(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def s_min(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def c_morning(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def c_noon(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def c_afternoon(df):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### smap/helpers.py

```text
import polars as pl
from smap import * 

def calc_features_consumption(df):
    # Add year and week columns
    df = df.with_columns([
        pl.col('dt').dt.year().alias("year"),
        pl.col('dt').dt.week().alias("week")
    ])

    # Calculate basic weekly consumption statistics
    avg_weekly = c_week(df)  # Calculate average consumption per week
    max_weekly = s_max(df)   # Calculate maximum consumption per week
    min_weekly = s_min(df)   # Calculate minimum consumption per week

    # Calculate ratios and other derived features for further analysis
    ratio_mean_max = r_mean_max(df)
    ratio_min_mean = r_min_mean(df)
    ratio_night_mean = r_night_mean(df)
    ratio_morning_noon = r_morning_noon(df)
    ratio_evening_noon = r_evening_noon(df)
    ratio_mean_max_no_min = r_mean_max_no_min(df)
    ratio_evening_noon_no_min = r_evening_noon_no_min(df)
    ratio_morning_noon_no_min = r_morning_noon_no_min(df)
    ratio_day_night_no_min = r_day_night_no_min(df)
    ratio_var_wd_we = r_var_wd_we(df)
    ratio_min_wd_we = r_min_wd_we(df)
    ratio_max_wd_we = r_max_wd_we(df)
    ratio_evening_wd_we = r_evening_wd_we(df)
    ratio_night_wd_we = r_night_wd_we(df)
    ratio_noon_wd_we = r_noon_wd_we(df)
    ratio_morning_wd_we = r_morning_wd_we(df)
    ratio_afternoon_wd_we = r_afternoon_wd_we(df)
    ratio_we_night_day = r_we_night_day(df)
    ratio_we_morning_noon = r_we_morning_noon(df)
    ratio_we_evening_noon = r_we_evening_noon(df)
    ratio_wd_night_day = r_wd_night_day(df)
    ratio_wd_morning_noon = r_wd_morning_noon(df)
    ratio_wd_evening_noon = r_wd_evening_noon(df)

    max_weekend = s_we_max(df)
    min_weekend = s_we_min(df)
    max_weekday = s_wd_max(df)
    min_weekday = s_wd_min(df)

    correlation_we = s_cor_we(df)
    correlation_wd = s_cor_wd(df)
    correlation_wd_we = s_cor_wd_we(df)

    sm_variety = s_sm_variety(df)
    bg_variety = s_bg_variety(df)
    day_difference = s_day_diff(df)
    variance_we = s_var_we(df)
    variance_wd = s_var_wd(df)
    difference = s_diff(df)
    num_peaks = s_num_peaks(df)
    quartile_1 = s_q1(df)
    quartile_2 = s_q2(df)
    quartile_3 = s_q3(df)

    max_avg = c_max_avg(df)
    min_avg = c_min_avg(df)
    num_zeros = s_number_zeros(df)
    num_small_peaks = s_number_small_peaks(df)
    num_big_peaks = s_number_big_peaks(df)

    morning_avg = c_morning(df)
    noon_avg = c_noon(df)
    afternoon_avg = c_afternoon(df)
    evening_avg = c_evening(df)
    night_avg = c_night(df)
    weekday_avg = c_weekday(df)
    weekend_avg = c_weekend(df)
    var_weekday = c_var_weekday(df)
    morning_wd = c_wd_morning(df)
    noon_wd = c_wd_noon(df)
    afternoon_wd = c_wd_afternoon(df)
    evening_wd = c_wd_evening(df)
    night_wd = c_wd_night(df)
    var_weekend = c_var_weekend(df)
    morning_we = c_we_morning(df)
    noon_we = c_we_noon(df)
    afternoon_we = c_we_afternoon(df)
    evening_we = c_we_evening(df)
    night_we = c_we_night(df)
    week_no_min = c_week_no_min(df)

    time_above_1kw = t_above_1kw(df)
    time_above_2kw = t_above_2kw(df)
    time_above_mean = t_above_mean(df)
    daily_max_time = t_daily_max(df)
    daily_min_time = t_daily_min(df)

    # Variance and correlation calculations
    variance = s_variance(df)
    correlation = s_cor(df)

    # Temporal features like the first time daily consumption exceeds 1 kW
    first_time_above_1kw = t_above_1kw(df)

```

### smap/module.py

```text
import polars as pl
import numpy as np
from typing import List
import statsmodels.api as sm
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import acf
from datetime import timedelta
from .utilities import calculate_lags_for_3h
from .decorators import replace_na_with_defaults_decorator
from .constants import rep_zero, rep_min1


# function inputs a time-series in polars, outputs average consumption for each weak 
def c_week(df):
    """
    Takes a DataFrame with a datetime column 'dt' and a consumption column 'cons',
    and returns a DataFrame with average weekly consumption.

    :param df: Polars DataFrame with 'dt' and 'cons' columns
    :return: Polars DataFrame with weekly average consumption
    """
    # Add columns for the year and week
    df = df.with_columns([
        pl.col('dt').dt.year().alias("year"),
        pl.col('dt').dt.week().alias("week")
    ])
    # Group by year and week and calculate the average consumption
    weekly_avg = df.group_by(["year", "week"]).agg(
        pl.col('cons').mean().alias('average_cons')
    )
    return weekly_avg


# function inputs a time-series in polars, outputs maximum consumption for each weak 
def s_max(df):
    """
    Takes a DataFrame with a datetime column 'dt' and a consumption column 'cons',
    and returns a DataFrame with maximum weekly consumption.

    :param df: Polars DataFrame with 'dt' and 'cons' columns
    :return: Polars DataFrame with weekly maximum consumption
    """
    # Add columns for the year and week
    df = df.with_columns([
        pl.col('dt').dt.year().alias("year"),
        pl.col('dt').dt.week().alias("week")
    ])
    # Group by year and week and calculate the maximum consumption
    weekly_max = df.group_by(["year", "week"]).agg(
        pl.col('cons').max().alias('max_cons')
    )
    return weekly_max


# function inputs a time-series in polars, outputs minimum consumption for each weak
def s_min(df):
    """
    Takes a DataFrame with a datetime column 'dt' and a consumption column 'cons',
    and returns a DataFrame with minimum weekly consumption.

    :param df: Polars DataFrame with 'dt' and 'cons' columns
    :return: Polars DataFrame with weekly minimum consumption
    """
    # Add columns for the year and week
    df = df.with_columns([
        pl.col('dt').dt.year().alias("year"),
        pl.col('dt').dt.week().alias("week")
    ])
    # Group by year and week and calculate the minimum consumption
    weekly_min = df.group_by(["year", "week"]).agg(
        pl.col('cons').min().alias('min_cons')
    )
    return weekly_min


# function inputs a time-series in polars, outputs average cons in the morning (6:00–9:59) for each weak
def c_morning(df):
    """
    Takes a DataFrame with a datetime column 'dt' and a consumption column 'cons',
    and returns a DataFrame with average morning consumption.

    :param df: Polars DataFrame with 'dt' and 'cons' columns
    :return: Polars DataFrame with morning average consumption
    """
    # Add columns for the year, week, and hour
    df = df.with_columns([
        pl.col('dt').dt.year().alias("year"),
        pl.col('dt').dt.week().alias("week"),
        pl.col('dt').dt.hour().alias("hour")
    ])
    # Filter for morning hours
    df = df.filter(pl.col('hour').is_in([6, 7, 8, 9]))
    # Group by year and week and calculate the average consumption
    morning_avg = df.group_by(["year", "week"]).agg(
        pl.col('cons').mean().alias('average_cons_morning')
    )
    return morning_avg


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

This lesson ties its explanation to `smap/helpers.py`, `smap/module.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
