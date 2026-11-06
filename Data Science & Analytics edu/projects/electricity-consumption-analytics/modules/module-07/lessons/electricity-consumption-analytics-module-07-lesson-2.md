# Read documented goals mapped to implementation in the source

**Lesson ID:** `electricity-consumption-analytics-module-07-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors setup.py, smap/__init__.py, smap/constants.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `setup.py`, `smap/__init__.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `setup.py`, `from setuptools import setup, find_packages` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `smap/__init__.py`, `from .module import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.md

```text

# SMAP: Smart Meter Analytics Python 

SMAP (Smart Meter Analytics Python) is a Python library for smart meter analysis of consumption and temperature time-series data. It's designed as a Python implementation of the R package [SmartMeterAnalytics](https://cran.r-project.org/web/packages/SmartMeterAnalytics/index.html), providing similar functionality for Python users. SMAP is built using Polars, a dataframe library, optimized for high speed performance on scale. 

## Features

Derived from extensive research and machine learning analysis, SMAP uses smart meter and weather data to derive 77 features, enabling recognition of various household characteristics with high accuracy. These features facilitate detailed analyses of energy consumption behavior and extracting explanatory features of user behavior from the complex high-resolution time-series data. Current implementation aggregates smart meter data with 15 min / 30 min / 1 hr granularity into a curated set of engineered features characterizing various properties of smart meter consumption. A list of implemented features is provided below, and includes features describing statistical properties (mean, variance, quartiles, etc.), peak behavior, temporal behavior, correlation with temperature and various ratios (e.g., weekday/weekend). Correlation with other weather features (wind speed, humidity, etc.) is due to be added in later versions.

| Feature Function       | Description                                                      |
|------------------------|------------------------------------------------------------------|
| `c_week`               | Computes the average consumption for each week.                  |
| `s_max`                | Finds the maximum consumption for each week.                     |
| `s_min`                | Finds the minimum consumption for each week.                     |
| `c_morning`            | Calculates average consumption in the morning (6:00–9:59) weekly.|
| `c_noon`               | Calculates average consumption at noon (10:00–13:59) weekly.     |
| `c_afternoon`          | Calculates average consumption in the afternoon (14:00–17:59) weekly.|
| `c_evening`            | Calculates average consumption in the evening (18:00–21:59) weekly.|
| `c_night`              | Calculates average consumption at night (1:00–5:59) weekly.      |
| `c_weekday`            | Computes average consumption on weekdays (Monday–Friday).        |
| `c_var_weekday`        | Computes variance of consumption on weekdays (Monday–Friday).    |
| `s_wd_min`             | Finds the minimum consumption on weekdays per week.              |
| `s_wd_max`             | Finds the maximum consumption on weekdays per week.              |
| `c_wd_morning`         | Calculates average weekday morning consumption.                  |
| `c_wd_noon`            | Calculates average weekday noon consumption.                     |
| `c_wd_afternoon`       | Calculates average weekday afternoon consumption.                |
| `c_wd_evening`         | Calculates average weekday evening consumption.                  |
| `c_wd_night`           | Calculates average weekday night consumption.                    |
| `c_weekend`            | Calculates average consumption on weekends (Saturday–Sunday).    |
| `c_var_weekend`        | Computes variance of weekend consumption.                        |
| `s_we_min`             | Finds the minimum weekend consumption per week.                  |
| `s_we_max`             | Finds the maximum weekend consumption per week.                  |
| `c_we_morning`         | Calculates average weekend morning consumption.                  |
| `c_we_noon`            | Calculates average weekend noon consumption.                     |
| `c_we_afternoon`       | Calculates average weekend afternoon consumption.                |
| `c_we_evening`         | Calculates average weekend evening consumption.                  |
| `c_we_night`           | Calculates a
```

### setup.py

```text
from setuptools import setup, find_packages

setup(
    name='SMAP',  # Replace with the name of your library
    version='0.1.1',  # Replace with your library's version
    author='Evgenii Genov',  # Replace with your name
    author_email='eugengenov@gmail.com',  # Replace with your email address
    description='This libary is a recreation of an R package for smart meter alanlysis of consumption and temperature time-series. ',  # Replace with a brief description of your library
    long_description=open('README.md').read(),  # Long description read from the the readme file
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/SMAP',  # Replace with the link to your github or project website
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'polars>=0.20.31'  # Replace with the version of Polars you are using or compatible with

    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Change as appropriate
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',  # Replace with the Python version requirements
    keywords='meter analytics polars',  # Replace with keywords relevant to your library
)

```

### smap/__init__.py

```text
# smap/__init__.py
from .module import (
    c_week,
    s_max,
    s_min,
    c_morning,
    c_noon,
    c_afternoon,
    c_evening,
    c_night,
    c_weekday,
    c_var_weekday,
    s_wd_min,
    s_wd_max,
    c_wd_morning,
    c_wd_noon,
    c_wd_afternoon,
    c_wd_evening,
    c_wd_night,
    c_weekend,
    c_var_weekend,
    s_we_min,
    s_we_max,
    c_we_morning,
    c_we_noon,
    c_we_afternoon,
    c_we_evening,
    c_we_night,
    c_week_no_min,
    s_max_no_min,
    c_evening_no_min,
    c_morning_no_min,
    c_noon_no_min,
    c_night_no_min,
    r_mean_max,
    r_min_mean,
    r_night_mean,
    r_morning_noon,
    r_evening_noon,
    r_mean_max_no_min,
    r_evening_noon_no_min,
    r_morning_noon_no_min,
    r_day_night_no_min,
    r_var_wd_we,
    r_min_wd_we,
    r_max_wd_we,
    r_evening_wd_we,
    r_night_wd_we,
    r_noon_wd_we,
    r_morning_wd_we,
    r_afternoon_wd_we,
    r_we_night_day,
    r_we_morning_noon,
    r_we_evening_noon,
    r_wd_night_day,
    r_wd_morning_noon,
    r_wd_evening_noon,
    s_sm_variety,
    s_bg_variety,
    s_day_diff,
    s_variance,
    s_var_wd,
    s_var_we,
    s_diff,
    s_cor,
    s_num_peaks,
    s_q1,
    s_q2,
    s_q3,
    c_max_avg,
    c_min_avg,
    s_number_zeros,
    s_cor_wd,
    s_cor_we,
    s_cor_wd_we,
    s_number_small_peaks,
    s_number_big_peaks,
    w_temp_cor_overall,
    #w_temp_cor_daily,
    w_temp_cor_night,
    w_temp_cor_daytime,
    w_temp_cor_evening,
    w_temp_cor_minima,
    w_temp_cor_maxima,
    w_temp_cor_maxmin,
    w_temp_cor_weekday_weekend,
    t_above_1kw,
    t_above_2kw,
    t_above_mean,
    t_daily_max,
    t_daily_min,
    ts_stl_varRem,
    ts_acf_mean3h,
    ts_acf_mean3h_weekday,
    t_wide_peaks,
    t_width_peaks
)

__all__ = [
    "c_week",
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

This lesson ties its explanation to `README.md`, `setup.py`, `smap/__init__.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
