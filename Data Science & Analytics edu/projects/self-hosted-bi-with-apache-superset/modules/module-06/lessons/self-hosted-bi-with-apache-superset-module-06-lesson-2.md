# Read declared dependencies and runtime configuration in the source

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-06-lesson-2`

## Purpose and learning objectives

Inspect the actual manifests .github/workflows/ci.yml, requirements.txt. Separate declared packages/settings from imports, installed state, secrets, and runtime success.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.github/workflows/ci.yml`, `requirements.txt`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.github/workflows/ci.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `requirements.txt` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .github/workflows/ci.yml

```text
name: CI

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install the dependencies
        run: pip install -r requirements.txt
      - name: Lint the source
        run: python -m compileall -q src main.py
      - name: Run the tests
        run: pytest -q

```

### requirements.txt

```text
numpy>=1.26
pandas>=2.0
matplotlib>=3.8
flask>=3.0
pytest>=8.0

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

This lesson ties its explanation to `.github/workflows/ci.yml`, `requirements.txt`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### app.py

### app.py

```text
"""A read-only BI page over the saved query output.

The dashboard of the project is still here, at `/demo`. The home page of the
site of the project, its console and the JSON API live in `web/` and are
served by this same application.
"""
import json
from pathlib import Path

from flask import (Flask, jsonify, render_template_string, send_file,
                   send_from_directory)

from src.pipeline import QUERIES, run

app = Flask(__name__)
run(quick=True, base_dir="artifacts")

WEB = Path(__file__).resolve().parent / "web"

PAGE = """
<!doctype html>
<title>Mini BI</title>
<style>
 body { font-family: system-ui, sans-serif; max-width: 980px; margin: 36px auto; color: #1f2937; }
 table { border-collapse: collapse; width: 100%; margin: 8px 0 22px; }
 th, td { text-align: left; padding: 6px 8px; border-bottom: 1px solid #e5e7eb; }
 img { max-width: 100%; border: 1px solid #e5e7eb; }
</style>
<h1>Mini BI dashboard</h1>
<p>Saved SQL queries over a local warehouse. Synthetic data only.</p>
<img src="/chart" alt="Monthly revenue">
<h2>Monthly revenue</h2>
{{ monthly|safe }}
<h2>Top products</h2>
{{ products|safe }}
<h2>Region share</h2>
{{ regions|safe }}
<h2>Repeat purchase rate</h2>
<p>{{ repeat }}% of paying customers ordered more than once.</p>
"""


def to_table(rows):
    if not rows:
        return "<p>No rows.</p>"
    headers = "".join(f"<th>{key}</th>" for key in rows[0])
    body = "".join(
        "<tr>" + "".join(f"<td>{value}</td>" for value in row.values()) + "</tr>"
        for row in rows
    )
    return f"<table><tr>{headers}</tr>{body}</table>"


@app.route("/demo")
def index():
    dashboard = json.loads(Path("artifacts/dashboard.json").read_text())
    repeat = dashboard["repeat_rate"][0]["repeat_rate"]
    return render_template_string(
        PAGE,
        monthly=to_table(dashboard["monthly_revenue"]),
        products=to_table(dashboard["top_products"]),
        regions=to_table(dashboard["region_share"]),
        repeat=repeat,
    )


@app.route("/chart")
def chart():
    return send_file(Path("artifacts/monthly_revenue.png"), mimetype="image/png")


# ------------------------------------------------------------------ #
# The web layer of the project                                        #
# ------------------------------------------------------------------ #

@app.route("/")
def site_index():
    """The home page of the site of the project."""
    return send_from_directory(WEB, "index.html")


@app.route("/console.html")
def site_console():
    """The console of the site of the project."""
    return send_from_directory(WEB, "console.html")


@app.route("/assets/<path:name>")
def site_assets(name):
    """The theme and the runtime of the site of the project."""
    return send_from_directory(WEB / "assets", name)


def _dashboard() -> dict:
    """The answers of the saved queries of the last run."""
    return json.loads(Path("artifacts/dashboard.json").read_text())


@app.route("/api/summary")
def api_summary():
```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
