# Read code review and safe change 6 in the source

**Lesson ID:** `data-quality-gates-with-great-expectations-module-06-lesson-2`

## Purpose and learning objectives

Use main.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

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
- In `web/api_impl.py`, `from __future__ import annotations` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `web/api_impl.py`, `from src.pipeline import run  # noqa: E402` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def state() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def checks() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def failures() -> list:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary() -> dict:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def handle(method, path, payload, user):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### web/api_impl.py

```text
"""The API of the project: the checks of the gate and the rows they rejected.

The numbers come from a real run of the gate: the checks are run over the
messy customer export, the report is written and the rows of the critical
checks are thrown away, so the report and the cleaned table always agree.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.pipeline import run  # noqa: E402

#: Where the gate writes the raw table, the clean one and the report.
BASE_DIR = ROOT / "artifacts"
REPORT = BASE_DIR / "quality_report.json"

#: The summary of the last run, kept for the life of the process.
_STATE: dict = {}


def state() -> dict:
    """Run the gate and keep the report of the run."""
    if "run" not in _STATE:
        result = run(quick=False, base_dir=str(BASE_DIR))
        report = json.loads(REPORT.read_text(encoding="utf-8"))
        _STATE["run"] = result
        _STATE["report"] = report
    return _STATE


def checks() -> list:
    """Every check of the gate with its severity and its failures."""
    return [
        {
            "check": check["name"],
            "severity": check["severity"],
            "failures": check["failures"],
            "state": "ok" if check["passed"] else "failed",
        }
        for check in state()["report"]["checks"]
    ]


def failures() -> list:
    """The rows that failed a check, with the checks they failed."""
    return [
        {
            "customer": row["customer_id"],
            "checks": ", ".join(row["checks"]),
        }
        for row in state()["report"]["failed_rows"]
    ]


def summary() -> dict:
    """The state of the last gate: the rows, the clean rows and the failures."""
    current = state()
    result = current["run"]
    all_checks = current["report"]["checks"]
    return {
        "stats": {
            "rows": result["rows"],
            "clean_rows": result["clean_rows"],
            "critical_failures": result["critical_failures"],
            "warning_failures": result["warning_failures"],
        },
        "series": [
            {"label": check["name"], "value": check["failures"]} for check in all_checks
        ],
        "lists": {
            "checks": checks(),
            "failures": failures(),
        },
    }


def handle(method, path, payload, user):
    """The read and the write endpoints of the project."""
    if method == "GET" and path == "/api/checks":
        return 200, {"checks": checks()}
    if method == "GET" and path == "/api/failures":
        return 200, {"failures": failures()}
    if method == "POST" and path == "/api/run":
        _STATE.pop("run", None)
        _STATE.pop("report", None)
        state()
        return 200, summary()["stats"]
    return 404, {"error": "not found"}

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

This lesson ties its explanation to `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, `web/api_impl.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
