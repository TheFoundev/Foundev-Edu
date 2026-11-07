# Dependencies and Runtime Configuration: Begin with the concept

**Lesson ID:** `automated-eda-tool-module-10-lesson-01`  
**Module ID:** `automated-eda-tool-module-10`  
**Source focus:** `.github/workflows/ci.yml` → `ci`

## Purpose and learning objectives

Explain dependencies and runtime configuration in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Declared dependencies and runtime configuration.

## Beginner explanation

An EDA tool is a workbench that helps inspect and prepare a table before analysis. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `.github/workflows/ci.yml` and locate `ci`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `.github/workflows/ci.yml`, `backend/DOCKERFILE`, `backend/docker-compose.yml`, `backend/requirements.txt`, `backend/app.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: declared dependencies; configuration keys; safe setup

**Excerpt:** `.github/workflows/ci.yml`. source tree absent; excerpt retained from earlier package

### .github/workflows/ci.yml

The excerpt below is the selected implementation focus.
### backend/DOCKERFILE

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### backend/docker-compose.yml

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### backend/requirements.txt

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### backend/app.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
name: CI - Python Lint and React Build

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8

    - name: Run flake8
      run: |
        flake8 autoeda --ignore=E501

    - name: Set up Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'

    - name: Install npm dependencies
      run: npm install
      working-directory: frontend  

    - name: Run React build
      run: npm run build
      working-directory: frontend
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

declared dependencies; configuration keys; safe setup The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-10.md`](../exercises/exercise-10.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `ci` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `ci` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
