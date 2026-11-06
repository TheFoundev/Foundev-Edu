# A beginner's model of documented goals mapped to implementation

**Lesson ID:** `data-quality-gates-with-great-expectations-module-05-lesson-1`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors main.py, src/pipeline.py, web/api_impl.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `README.md`, `main.py`, `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class Check:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, name, severity, description=""):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def evaluate(self, frame):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class ColumnPresent(Check):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, column, severity="critical"):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def evaluate(self, frame):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# Data Quality Gates with Great Expectations

Data quality gates over a messy customer export.

> Add an automated data-quality layer that profiles datasets, defines expectation suites and blocks bad loads with generated data docs.

## Overview

An original, self-contained implementation of the **Data Quality Gates with Great Expectations** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- Every check is written down once: it says what it looks at and how severe
  it is, and both the number of the failures and the cleaning of the table
  come from it
- The report names the rows that failed and the checks they failed, and it
  holds an example of every failure
- The critical failures and the warnings are counted apart, and only the rows
  of a critical check are thrown away

## Stack

`Python; NumPy; Pandas`
The CSV stack is Python + NumPy + Pandas. Great Expectations is not available, so the quality checks are plain pandas functions and the report is JSON.

## Run

```bash
pip install -r requirements.txt
python main.py run
python main.py demo
pytest -q
```

## Structure

```text
data-quality-gates-with-great-expectations/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
```

## Testing

```bash
```bash
pytest -q
```

13 tests: every check on its own, the report that names the rows, the
severities that are counted apart, the cleaned table and the agreement
between the report and the cleaning.
```

## Notes and limitations

- The checks are hand-written functions instead of an expectation suite.
- The pipeline does not run inside Airflow.
- The report is JSON; there is no data docs site.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Run quality gates on a synthetic customer export.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Run quality gates on a synthetic customer export.')
        print("Run `python main.py run` to execute the pipeline.")
        return

    if args.command == "demo":
        demo(base_dir=args.base_dir)
        return

    summary = run(quick=args.quick, base_dir=args.base_dir)
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()

```

### src/pipeline.py

```text
"""Quality checks plus a cleaned customer table.

Every check is written down once: the check says what it looks at and how
severe it is, and both the number of the failures and the cleaning of the
table come from it, so the report and the output can never disagree.
"""
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

REQUIRED_COLUMNS = ["customer_id", "email", "age", "status", "country"]

#: The statuses a customer may have.
VALID_STATUSES = ["active", "paused", "cancelled"]

#: The age a customer has to be in.
AGE_RANGE = (18, 90)

#: The countries the customers come from.
VALID_COUNTRIES = ["CA", "US", "UK", "DE"]

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class Check:
    """One quality check.

    The check knows what it looks at and how bad it is when it fails, so the
    number of the failures and the rows that are thrown away are both worked
    out from it.
    """

    def __init__(self, name, severity, description=""):
        self.name = name
        self.severity = severity
        self.description = description

    def evaluate(self, frame):
        """The rows that fail the check, with the reason."""
        raise NotImplementedError


class ColumnPresent(Check):
    """The column has to be there."""

    def __init__(self, column, severity="critical"):
        super().__init__(f"{column}_present", severity, f"the column {column} has to be there")
        self.column = column

    def evaluate(self, frame):
        if self.column in frame.columns:
            return frame.iloc[0:0].assign(reason="")
        return frame.iloc[0:0].assign(reason=f"the column {self.column} is missing")


class NotNull(Check):
    """The value may not be missing."""

    def __init__(self, column, severity="critical"):
        super().__init__(f"{column}_not_null", severity, f"the column {column} may not be empty")
        self.column = column

    def evaluate(self, frame):
        if self.column not in frame.columns:
            return frame.iloc[0:0].assign(reason="")
        failed = frame[frame[self.column].isna()].copy()
        failed["reason"] = f"{self.column} is empty"
        return failed


class Unique(Check):
    """The value may only be there once."""

    def __init__(self, column, severity="critical"):
        super().__init__(f"{column}_unique", severity, f"the column {column} may only be there once")
        self.column = column

    def evaluate(self, frame):
        if self.column not in frame.columns:
            return frame.iloc[0:0].assign(reason="")
        duplicated = frame[frame.duplicated(subset=[self.column], keep=False)].copy()
        duplicated["reason"] = f"{self.column} is there more than once"
        return duplicated


class Matches(Check):
    """The value has to match a pattern."""

    def __init__(self, column, pattern, severity="critical"):
        super().__init__(f"{column}_format", severity, f"the column {column} has to match {pattern.pattern}")
        self.column = column
        self.pattern = pattern

    def evaluate(self, frame):
        if self.column not in frame.columns:
            return frame.iloc[0:0].assign(reason="")
        values = frame[self.column].fillna("").astype(str)
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

This lesson ties its explanation to `README.md`, `main.py`, `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
