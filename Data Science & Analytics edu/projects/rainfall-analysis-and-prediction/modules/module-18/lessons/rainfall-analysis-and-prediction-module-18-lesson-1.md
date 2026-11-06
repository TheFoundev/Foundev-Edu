# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `rainfall-analysis-and-prediction-module-18-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.rst with implementation anchors docs/source/conf.py, rrmpg/__init__.py, rrmpg/models/__init__.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.rst`, `docs/source/conf.py`, `rrmpg/__init__.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.rst` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `docs/source/conf.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `docs/source/conf.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- The excerpt from `rrmpg/__init__.py` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### README.rst

```text
Introduction
############

This repository is a work in progress repository.

Official documentation can be found here: `http://rrmpg.readthedocs.io <http://rrmpg.readthedocs.io>`_

Read the :ref:`Idea section <idea>` for further information about the background and aim of this project.

.. _idea:

Idea
----
One of the fundamental parts of hydrology is rainfall-runoff-modelling. The task here is to model the response of a catchment to meteorological input data and to forecast the river discharge. There are different approaches to tackle the problem, namely: conceptual models, physical-based models and data-driven models.

Although this is taught at university, often hands-on experience is missing or is done on using very simple modelling approaches. One of the main reasons I see is, that most (at least the complex ones) hydrological models are implemented in Fortran but very few students of the field of hydrology know Fortran, when they first get in touch with RR-Models. So all they can probably do is simply apply a model to their data and play manually with parameter tuning, but not explore the model and see the effect of code changes.

This might be different if there would exist well performing implementations of hydrological models in a more simplistic and readable language, such as Python.
What was hindering this step was always the speed of Python and the nature of RR-Models - they mostly have to be implemented using loops over all timesteps. And well, big surprise: Pure Python and for-loops is not the best combination in terms of performance.

This could be changed e.g. by using `Cython <http://cython.org/>`_ for the hydrological model, but this again might hinder the code understanding, since Cython adds non-pythonic complexity to the code, which might be hard for beginners to understand and therefore play/experiment with the code.

Another option could be `PyPy <http://pypy.org/>`_. The problem I see with PyPy is, that the user would be forced to install a different Python interpreter, while most I know of are quite comfortable using e.g. `Anaconda <https://www.continuum.io/anaconda-overview>`_.

`Numba <http://numba.pydata.org/>`_ is another way to speed up array-oriented and math-heavy Python code but without changing the language/interpreter and just by few code adaptions. Using numba, the code stays easily readable and therefore better understandable for novices. I won't spend much time now on explaining how numba works, but I'll definitely add further information in the future.
First performance comparisons between Fortran implementations and numba optimized Python code have shown, that the speed is roughly the same (Fortran is about ~1-2 times faster, using the GNU Fortran compiler).

**Summary**: The idea of this code repository is to provide fast (roughly the speed of Fortan) implementations of hydrological models in Python to make it easier to play and experiment with rainfall-runoff models.


You want to contribute?
-----------------------

At the moment I'm looking for a selection of hydrological models I'll implement in Python. If you want to see any (your?) model in this project, feel free to contact me.
There is also a `How to contribute section <http://rrmpg.readthedocs.io/en/latest/contribution.html>`_ at the official documentation, were you can read more on the various ways you can contribute to this repository.

Contributors
------------
I'll add later a better looking section to the official documentation. For now I list everybody, who contributed to this repository here:

- `Ondřej Čertík <https://github.com/certik>`_ with pull request `#3 <https://github.com/kratzert/RRMPG/pull/3>`_: Optimized Fortran code and compilation procedure for fair speed comparision.
- `Daniel Klotz <https://github.com/danklotz>`_ with pull request `#4 <https://github.com/kratzert/RRMPG/pull/4>`_ , `#5 <https://github.com/kratzert/RRMPG/pull/4>`_ and `#9 <https://github.com/kratzert/RRMPG/pull/9>`_: All spell checking.
- 
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

### rrmpg/__init__.py

```text
# This file is part of RRMPG.
#
# RRMPG is free software with the aim to provide a playground for experiments
# with hydrological rainfall-runoff-models while achieving competitive
# performance results.
#
# You should have received a copy of the MIT License along with RRMPG. If not,
# see <https://opensource.org/licenses/MIT>

__author__ = "Frederik Kratzert"
__version__ = "0.1"
__reversion__ = "0.1.1"

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

This lesson ties its explanation to `README.rst`, `docs/source/conf.py`, `rrmpg/__init__.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
