# Read test code and evidence boundaries in the source

**Lesson ID:** `data-quality-gates-with-great-expectations-module-03-lesson-2`

## Purpose and learning objectives

Read test implementations tests/test_pipeline.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `tests/test_pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pandas as pd` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_check_that_is_not_written_is_an_error():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_missing_value_is_found():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_duplicated_value_is_found():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_value_outside_the_range_is_found():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_a_value_outside_the_set_is_found():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_pipeline.py

```text
"""Tests for the quality checks."""
import json

import pandas as pd

from src.pipeline import (
    AGE_RANGE,
    VALID_STATUSES,
    Between,
    Check,
    InSet,
    Matches,
    NotNull,
    Unique,
    default_checks,
    make_customers,
    run,
    run_checks,
    demo,
)


def test_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


# ---------------------------------------------------------------------------
# The checks
# ---------------------------------------------------------------------------

def test_a_check_that_is_not_written_is_an_error():
    check = Check("empty", "critical")
    try:
        check.evaluate(pd.DataFrame({"a": [1]}))
    except NotImplementedError:
        return
    raise AssertionError("a check without an implementation should raise")


def test_a_missing_value_is_found():
    frame = pd.DataFrame({"customer_id": [1, None, 3]})
    failed = NotNull("customer_id").evaluate(frame)
    assert len(failed) == 1
    assert "reason" in failed.columns


def test_a_duplicated_value_is_found():
    frame = pd.DataFrame({"customer_id": [1, 1, 2]})
    assert len(Unique("customer_id").evaluate(frame)) == 2


def test_a_value_outside_the_range_is_found():
    frame = pd.DataFrame({"age": [20, 13, 100]})
    failed = Between("age", AGE_RANGE[0], AGE_RANGE[1]).evaluate(frame)
    assert len(failed) == 2


def test_a_value_outside_the_set_is_found():
    frame = pd.DataFrame({"status": ["active", "unknown"]})
    failed = InSet("status", VALID_STATUSES).evaluate(frame)
    assert len(failed) == 1
    assert failed.iloc[0]["reason"]


def test_a_value_that_does_not_match_the_pattern_is_found():
    import re

    frame = pd.DataFrame({"email": ["a@b.test", "broken", None]})
    failed = Matches("email", re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")).evaluate(frame)
    assert len(failed) == 2


def test_a_column_that_is_not_there_is_not_a_failure():
    frame = pd.DataFrame({"other": [1, 2]})
    assert len(NotNull("missing").evaluate(frame)) == 0


# ---------------------------------------------------------------------------
# The report
# ---------------------------------------------------------------------------

def test_the_report_names_the_rows_that_failed(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    report = json.loads((tmp_path / "quality_report.json").read_text())

    assert report["failed_rows"]
    for row in report["failed_rows"]:
        assert row["checks"]
        assert "customer_id" in row


def test_the_report_holds_the_examples_of_a_check(tmp_path):
    run(quick=True, base_dir=str(tmp_path))
    report = json.loads((tmp_path / "quality_report.json").read_text())
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

This lesson ties its explanation to `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### src/pipeline.py

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

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
