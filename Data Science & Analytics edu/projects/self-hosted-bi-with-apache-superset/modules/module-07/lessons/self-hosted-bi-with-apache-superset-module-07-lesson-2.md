# Read documented goals mapped to implementation in the source

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-07-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors app.py, main.py, sql/monthly_revenue.sql. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `app.py`, `main.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `app.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from flask import (Flask, jsonify, render_template_string, send_file,` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from src.pipeline import QUERIES, run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def to_table(rows):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def chart():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_console():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def site_assets(name):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
# Self-Hosted BI with Apache Superset

A small SQL-driven BI warehouse and dashboard.

> Deploy and model a multi-dataset BI portal in Apache Superset with roles, SQL Lab, datasets and embedded dashboards.

## Overview

An original, self-contained implementation of the **Self-Hosted BI with Apache Superset** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- SQLite warehouse with customers and orders
- Monthly revenue, top products, region mix and repeat-rate SQL
- Saved dashboard JSON and a revenue chart
- Read-only Flask BI page

## Stack

`Python; Flask; Matplotlib; NumPy; Pandas`
The CSV stack is Python + Flask + Matplotlib + NumPy + Pandas. Superset is not installed, so the saved queries run against SQLite and a small Flask page renders the results.

## Run

```bash
pip install -r requirements.txt
python main.py run
python app.py
python main.py demo
pytest -q
```

## Structure

```text
self-hosted-bi-with-apache-superset/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── sql/*.sql                 saved BI queries
├── app.py                    Flask BI page
```

## Testing

```bash
pytest -q
```

4 tests (`pytest -q`), up from 2.


## Notes and limitations

- There is no Superset installation, metadata database or chart editor.
- The warehouse is populated with synthetic orders.
- The dashboard layout is hard-coded around four saved queries.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production data platform. It uses local files and SQLite so the pipeline can run on one machine. The notes above list the production pieces that were replaced or skipped.

```

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

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Run saved BI queries and render a small dashboard.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Run saved BI queries and render a small dashboard.')
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

This lesson ties its explanation to `README.md`, `app.py`, `main.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
