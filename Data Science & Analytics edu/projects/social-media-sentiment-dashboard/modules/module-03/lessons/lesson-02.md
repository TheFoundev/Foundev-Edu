# Dashboard Configuration and Data Manager: Trace the code

**Lesson ID:** `social-media-sentiment-dashboard-module-03-lesson-02`  
**Module ID:** `social-media-sentiment-dashboard-module-03`  
**Source focus:** `src/config.py` → `load_config`

## Purpose and learning objectives

Trace `load_config` in `src/config.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Config and Dashboard, Data Manager and undefined undefined Init undefined undefined.

## Beginner explanation

A social analytics pipeline collects posts, organizes them, scores text, then summarizes trends. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/config.py` and locate `load_config`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/config.py`, `src/dashboard.py`, `src/data_manager.py`, `src/fetchers/__init__.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `src/config.py`. source tree absent; excerpt retained from earlier package

### src/config.py

The excerpt below is the selected implementation focus.
### src/dashboard.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/data_manager.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/fetchers/__init__.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import json
import os

def load_config(config_path: str = None) -> dict:
    """
    Load social accounts configuration from a JSON file.
    """
    if not config_path:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, "..", "config", "social_accounts.json")
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `load_config` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `load_config` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
