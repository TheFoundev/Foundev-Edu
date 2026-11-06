# Read icemelt model and conf in the source

**Lesson ID:** `rainfall-analysis-and-prediction-module-11-lesson-2`

## Purpose and learning objectives

Study the implementation in [rrmpg/models/icemelt_model.py] and [docs/source/conf.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include run_icemelt; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `rrmpg/models/icemelt_model.py`, `docs/source/conf.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `rrmpg/models/icemelt_model.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `rrmpg/models/icemelt_model.py`, `from numba import njit, prange` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def run_icemelt(temp, snow, params):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `docs/source/conf.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `docs/source/conf.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### rrmpg/models/icemelt_model.py

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

import numpy as np

from numba import njit, prange

@njit    
def run_icemelt(temp, snow, params):
    """Implementation of a degree-day Ice Melt Model (modified after Nepal et al. 2017).
    
    This model simulates ice melt based on a simple degree-day approach.
    
    Args:
        temp: Numpy [t, n] array containing mean temperature for each time step and layer.
        snow: Numpy [t, n] array containing snowpack storage at each time step and layer.
        params: Numpy structured array containing model parameters:
            - 'DDF': Degree-day factor (mm/°C/day).
        
    Returns:
        liquid_water: Numpy [t, n] array containing the liquid water produced from melt
                      for each timestep and layer.
    
    References:
    [1] Nepal, S., Chen, J., Penton, D. J., Neumann, L. E., Zheng, H., & Wahid, S. (2017). 
        Spatial GR4J conceptualization of the Tamor glaciated alpine catchment in Eastern Nepal: 
        evaluation of GR4JSG against streamflow and MODIS snow extent. Hydrol. Process., 31, 51–68.
        doi: 10.1002/hyp.10962.
    """

    # Number of simulation timesteps
    num_timesteps = len(temp)

    # Unpack model parameters
    ddf = params['DDF']
    
    # tbase not calibrated
    tbase = 0

    # Number of elevation layers
    num_layers = temp.shape[1]

    # outflow as sum of liquid precipitation and melt of each layer
    liquid_water = np.zeros((num_timesteps, num_layers), dtype=np.float64)

    # Calculate routine for each elevation zone independently
    for l in prange(num_layers):
        for t in range(num_timesteps):
            # Calculate actual ice melt
            melt = ddf * (temp[t, l]-tbase)
            if melt < 0:
                melt = 0
            if snow[t, l] > 1:
                liquid_water[t, l] = 0
            else:
                liquid_water[t, l] = melt
    
    return liquid_water

```

### docs/source/conf.py

```text
# -*- coding: utf-8 -*-
#
# RRMPG documentation build configuration file, created by
# sphinx-quickstart on Sun Aug 20 15:18:16 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting']

napoleon_google_docstring = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'RRMPG'
copyright = u'2017, Frederik Kratzert'
author = u'Frederik Kratzert'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'0.0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme' #'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
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

This lesson ties its explanation to `rrmpg/models/icemelt_model.py`, `docs/source/conf.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
