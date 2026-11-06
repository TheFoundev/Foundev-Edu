# Architecture and source map

## Repository evidence

- `README.md`
- `setup.py`
- `smap/__init__.py`
- `smap/constants.py`
- `smap/decorators.py`
- `smap/helpers.py`
- `smap/module.py`
- `smap/utilities.py`
- `tests/test_c_noon.py`

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> 
> # SMAP: Smart Meter Analytics Python 
> 
> SMAP (Smart Meter Analytics Python) is a Python library for smart meter analysis of consumption and temperature time-series data. It's designed as a Python implementation of the R package [SmartMeterAnalytics](https://cran.r-project.org/web/packages/SmartMeterAnalytics/index.html), providing similar functionality for Python users. SMAP is built using Polars, a dataframe library, optimized for high speed performance on scale. 
> 
> ## Features
> 
> Derived from extensive research and machine learning analysis, SMAP uses smart meter and weather data to derive 77 features, enabling recognition of various household characteristics with high accuracy. These features facilitate detailed analyses of energy consumption behavior and extracting explanatory features of user behavior from the complex high-resolution time-series data. Current implementation aggregates smart meter data with 15 min / 30 min / 1 hr granularity into a curated set of engineered features characterizing various properties of smart meter consumption. A list of implemented features is provided below, and includes features describing statistical properties (mean, variance, quartiles, etc.), peak behavior, temporal behavior, correlation with temperature and various ratios (e.g., weekday/weekend). Correlation with other weather features (wind speed, humidity, etc.) is due to be added in later versions.
> 
> | Feature Function       | Description                                                      |
> |------------------------|------------------------------------------------------------------|
> | `c_week`               | Computes the average consumption for each week.                  |
> | `s_max`                | Finds the maximum consumption for each week.                     |
> | `s_min`                | Finds the minimum consumption for each week.                     |
> | `c_morning`            | Calculates average consumption in the morning (6:00–9:59) weekly.|
> | `c_noon`               | Calculates average consumption at noon (10:00–13:59) weekly.     |
> | `c_afternoon`          | Calculates average consumption in the afternoon (14:00–17:59) weekly.|
> | `c_evening`            | Calculates average consumption in the evening (18:00–21:59) weekly.|
> | `c_night`              | Calculates average consumption at night (1:00–5:59) weekly.      |
> | `c_weekday`            | Computes average consumption on weekdays (Monday–Friday).        |
> | `c_var_weekday`        | Computes variance of consumption on weekdays (Monday–Friday).    |
> | `s_wd_min`             | Finds the minimum consumption on weekdays per week.              |
> | `s_wd_max`             | Finds the maximum consumption on weekdays per week.              |
> | `c_wd_morning`         | Calculates average weekday morning consumption.                  |
> | `c_wd_noon`            | Calculates average weekday noon consumption.                     |
> | `c_wd_afternoon`       | Calculates average weekday afternoon consumption.                |
> | `c_wd_evening`         | Calculates average weekday evening consumption.                  |
> | `c_wd_night`           | Calculates average weekday night consumption.                    |
> | `c_weekend`            | Calculates average consumption on weekends (Saturday–Sunday).    |
> | `c_var_weekend`        | Computes variance of weekend consumption.                        |
> | `s_we_min`             | Finds the minimum weekend consumption per week.                  |
> | `s_we_max`             | Finds the maximum weekend consumption per week.                  |
> | `c_we_morning`         | Calculates average weekend morning consumption.                  |
> | `c_we_noon`            | Calculates average weekend noon consumption.                     |
> | `c_we_afternoon`       | Calculates average weekend afternoon consumption.                |
> | `c_we_evening`         | Calculates average weekend evening consumption.                  |
> | `c_we_night`           | Calculates average weekend night consumption.                    |
> | `c_week_no_min`        | Computes the difference between average and minimum weekly consumption.|
> | `s_max_no_min`         | Computes the difference between maximum and minimum weekly consumption.|
> | `c_evening_no_min`     | Computes evening consumption minus the minimum weekly consumption.|
> | `c_morning_no_min`     | Computes morning consumption minus the minimum weekly consumption.|
> | `c_noon_no_min`        | Computes noon consumption minus the minimum weekly consumption.  |
> | `c_night_no_min`       | Computes night consumption minus the minimum weekly consumption. |
> | `r_mean_max`           | Ratio between weekly average and maximum consumption.            |
> | `r_min_mean`           | Ratio between minimum and weekly average consumption.            |
> | `r_night_mean`         | Ratio between night and weekly average consumption.              |
> | `r_morning_noon`       | Ratio between morning and noon consumption.                      |
> | `r_evening_noon`       | Ratio between evening and noon consumption.                      |
> | `r_mean_max_no_min`    | Ratio between average minus minimum and maximum minus minimum weekly consumption.|
> | `r_evening_noon_no_min`| Ratio between evening minus minimum and noon minus minimum consumption.|
> | `r_morning_noon_no_min`| Ratio between morning minus minimum and noon minus minimum consumption.|
> | `r_day_night_no_min`   | Ratio between day minus minimum and night minus minimum consumption.|
> | `r_var_wd_we`          | Ratio between variance of weekday and weekend consumption.       |
> | `r_min_wd_we`          | Ratio between minimum weekday and weekend consumption.           |
> | `r_max_wd_we`          | Ratio between maximum weekday and weekend consumption.           |
> | `r_evening_wd_we`      | Ratio between evening weekday and weekend consumption.           |
> | `r_night_wd_we`        | Ratio between night weekday and weekend consumption.             |
> | `r_noon_wd_we`         | Ratio between noon weekday and weekend consumption.              |
> | `r_morning_wd_we`      | Ratio between morning weekday and weekend consumption.           |
> | `r_afternoon_wd_we`    | Ratio between afternoon weekday and weekend consumption.         |
> | `s_sm_variety`     | Calculates the 20%-quintile of absolute differences in consumption (`cons`) per week and year. |
> | `s_bg_variety`     | Calculates the 60%-quintile of absolute differences in consumption (`cons`) per week and year. |
> | `s_day_diff`       | Computes the mean of absolute differences in daily consumption during weekdays, grouped by year and week. |
> | `s_variance`       | Computes the variance of consumption (`cons`) grouped by year and week. |
> | `s_var_wd`         | Computes the variance of weekday consumption grouped by year and week. |
> | `s_var_we`         | Computes the variance of weekend consumption grouped by year and week. |
> | `s_diff`           | Computes the total absolute difference in consumption for each year and week. |
> | `s_cor`            | Computes the correlations between daily consumption patterns across different weekdays within a week. |
> | `s_num_peaks`      | Identifies and counts the number of peaks in consumption data per week. |
> | `s_q1`             | Calculates the first quartile (Q1) of consumption data for each week. |
> | `s_q2`             | Calculates the median (Q2) of consumption data for each week. |
> | `s_q3`             | Calculates the third quartile (Q3) of consumption data for each week. |
> | `c_max_avg`        | Calculates the average of daily maximum consumption values per week. |
> | `c_min_avg`        | Calculates the average of daily minimum consumption values per week. |
> | `s_number_zeros`   | Counts the number of zero consumption readings per week. |
> | `s_cor_wd`         | Computes average correlations between weekdays' consumption. |
> | `s_cor_we`         | Computes correlations between Saturday and Sunday consumption. |
> | `s_cor_wd_we`      | Compute

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
