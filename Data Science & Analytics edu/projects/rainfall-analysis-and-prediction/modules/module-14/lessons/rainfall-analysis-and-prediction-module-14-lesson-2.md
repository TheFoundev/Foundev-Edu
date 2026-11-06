# Read metrics and plot utils in the source

**Lesson ID:** `rainfall-analysis-and-prediction-module-14-lesson-2`

## Purpose and learning objectives

Study the implementation in [rrmpg/utils/metrics.py] and [rrmpg/utils/plot_utils.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include calc_nse, calc_rmse, calc_mse, plot_qsim_range; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `rrmpg/utils/metrics.py`, `rrmpg/utils/plot_utils.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `rrmpg/utils/metrics.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/metrics.py`, `from scipy.stats.stats import pearsonr` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/metrics.py`, `from .array_checks import validate_array_input` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def calc_nse(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def calc_rmse(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def calc_mse(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def calc_kge(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def calc_alpha_nse(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def calc_beta_nse(obs, sim):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `rrmpg/utils/plot_utils.py`, `import matplotlib.pyplot as plt` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/plot_utils.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/utils/plot_utils.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def plot_qsim_range(qsim, x_vals=None, qobs=None):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/utils/metrics.py

```text
# -*- coding: utf-8 -*-a 
# This file is part of RRMPG.
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>

"""
Implementation of evaluation metrics for e.g. hydrological model simulations.

Implemented functions:
    calc_nse: Calculate the Nash-Sutcliffe model efficiency coefficient.
    calc_rmse: Calculate the root mean squared error.
    calc_mse: Calculate the mean squared error.
    calc_kge: Calculate the Kling-Gupta-Efficiency.
    calc_alpha_nse: Calculate the alpha decomposition of the NSE.
    calc_beta_nse: Calculate the beta decomposition of the NSE.
    calc_r: Calculate the pearson r coefficient.

"""
import numpy as np
from scipy.stats.stats import pearsonr

from .array_checks import validate_array_input

def calc_nse(obs, sim):
    """Calculate the Nash-Sutcliffe model efficiency coefficient.

    Original Publication:
    Nash, J. Eamonn, and Jonh V. Sutcliffe. "River flow forecasting through
    conceptual models part I—A discussion of principles." Journal of
    hydrology 10.3 (1970): 282-290.
    
    

    Args:
        obs: Array of the observed values
        sim: Array of the simulated values

    Returns:
        The NSE value for the simulation, compared to the observation.

    Raises:
        ValueError: If the arrays are not of equal size or have non-numeric
            values.
        TypeError: If the arrays is not a supported datatype.
        RuntimeError: If all values in qobs are equal. The NSE is not defined
            for this cases.

    """
    # Validation check on the input arrays
    obs = validate_array_input(obs, np.float64, 'obs')
    sim = validate_array_input(sim, np.float64, 'sim')
    
    if len(obs) != len(sim):
        raise ValueError("Arrays must have the same size.")
    
    # denominator of the fraction term
    denominator = np.sum((obs-np.mean(obs))**2)
    
    # this would lead to a division by zero error and nse is defined as -inf
    if denominator == 0:
        msg = ["The Nash-Sutcliffe-Efficiency coefficient is not defined ",
               "for the case, that all values in the observations are equal.",
               " Maybe you should use the Mean-Squared-Error instead."]
        raise RuntimeError("".join(msg))
    
    # numerator of the fraction term
    numerator = np.sum((sim-obs)**2)

    # calculate the NSE
    nse_val = 1 - numerator/denominator
    
    return nse_val



def calc_rmse(obs, sim):
    """Calculate the root mean squared error.

    Args:
        obs: Array of the observed values
        sim: Array of the simulated values

    Returns:
        The RMSE value for the simulation, compared to the observation.

    Raises:
        ValueError: If the arrays are not of equal size or have non-numeric
            values.
        TypeError: If the arrays is not a supported datatype.

    """
    # Validation check on the input arrays
    obs = validate_array_input(obs, np.float64, 'obs')
    sim = validate_array_input(sim, np.float64, 'sim')
    
```

### rrmpg/utils/plot_utils.py

```text
# -*- coding: utf-8 -*-
# This file is part of RRMPG.
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>
"""
This module implements some utility functions for plotting.

Implemented functions:
    plot_qsim_range: Plot the range of multiple simulations and their mean.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_qsim_range(qsim, x_vals=None, qobs=None):
    """Plot the range of multiple simulations and their mean.

    This function plots the quantiles of multiple simulations as a filled area
    and the mean as a line. The (0.05, 0.95) and the (0.25, 0.75) quantile
    are plotted as different colored areas and the mean as a solid line. If
    observations are also passed, they are plotted as well as a solid line.

    Args:
        qsim: 2D array of simulations. Shape must be (num_timesteps, num_sims)
        x_vals: (optional) 1D array, that will be used as x-axes values.
            (e.g. date)
        qobs: (optional) 1D arary of oversations.

    Returns:
        A handle to the matplotlib figure.

    Raises:
        ValueError: For incorrect inputs.

    """
    # Validate inputs
    if not isinstance(qsim, np.ndarray) or (len(qsim.shape) != 2):
        raise ValueError("'qsim' must be a two dimensional numpy.ndarray.")

    if x_vals is not None:
        if not isinstance(x_vals, (list, np.ndarray, pd.Series, pd.Index)):
            msg = ["'x_vals' must be either a list, numpy.ndarray or ",
                   "pandas.Series."]
            raise ValueError("".join(msg))

    if qobs is not None:
        if isinstance(qobs, (list, np.ndarray, pd.Series)):
            try:
                qobs = np.array(qobs, dtype=np.float64)
            except:
                raise ValueError("All elements in 'qobs' must be numerical.")
        else:
            msg = ["'qobs' must be either a list, numpy.ndarray or ",
                   "pandas.Series."]
            raise ValueError("".join(msg))
        if len(qobs.shape) != 1:
            raise ValueError("'qobs' must be one dimensional.")

    # Calculate quantiles
    q05 = np.percentile(qsim, 5, axis=1)
    q25 = np.percentile(qsim, 25, axis=1)
    q75 = np.percentile(qsim, 75, axis=1)
    q95 = np.percentile(qsim, 95, axis=1)

    # If an array for the x values exist.
    if x_vals is None:
        x_vals = np.arange(qsim.shape[0])

    # Create plot
    fig, ax = plt.subplots(1)

    ax.plot(x_vals, np.mean(qsim, axis=1), color='red', label="Qsim mean",
            lw=0.5)
    if qobs is not None:
        ax.plot(x_vals, qobs, color='blue', label="Qobs", lw=0.5)

    ax.fill_between(x_vals, q05, q95, color=(1, 0, 0, 0.3),
                    label="5%/95% quantile")
    ax.fill_between(x_vals, q25, q75, color=(1, 0, 0, 0.1),
                    label="25%/75% quantile")
    plt.legend()
    plt.show()

    return fig, ax

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

This lesson ties its explanation to `rrmpg/utils/metrics.py`, `rrmpg/utils/plot_utils.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
