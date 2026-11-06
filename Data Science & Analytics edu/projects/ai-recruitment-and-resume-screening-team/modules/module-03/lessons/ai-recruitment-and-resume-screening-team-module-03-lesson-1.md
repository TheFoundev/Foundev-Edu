# A beginner's model of test code and evidence boundaries

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-03-lesson-1`

## Purpose and learning objectives

Read test implementations tests/test_pipeline.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `tests/test_pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `tests/test_pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `import pytest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.data import load_data, make_resume, parse_resume` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.model import draft_interview_questions, rank_candidates, train, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from app import app as flask_app` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_pipeline_runs(capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_seed_is_usable():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_parser_reads_the_facts_of_a_resume():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_parser_of_a_text_without_a_fact_gives_zero():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_label_is_not_a_function_of_the_skills():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_metrics_are_reported(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

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
"""Tests for the screening pipeline, the parser and the questions."""
import sqlite3

import pytest

from src.data import load_data, make_resume, parse_resume
from src.model import draft_interview_questions, rank_candidates, train, demo
from app import app as flask_app


def test_pipeline_runs(capsys):
    data = load_data(seed=1, quick=True)
    assert data is not None

    model, metrics = train(data, quick=True)
    assert model is not None
    assert isinstance(metrics, dict) and metrics

    for value in metrics.values():
        if isinstance(value, bool):
            continue
        assert value is None or isinstance(value, (int, float, str))

    demo(data)
    assert capsys.readouterr().out.strip()


def test_seed_is_usable():
    first = load_data(seed=3, quick=True)
    second = load_data(seed=3, quick=True)
    assert first.keys() == second.keys()


# ---------------------------------------------------------------------------
# The parser
# ---------------------------------------------------------------------------

def test_the_parser_reads_the_facts_of_a_resume():
    resume = make_resume(0, seed=1)
    parsed = parse_resume(resume["text"])

    assert parsed["years"] == resume["years"]
    assert parsed["projects"] == resume["projects"]
    assert parsed["education"] == resume["education"]
    # The parser can only find the skills the text mentions.
    assert set(parsed["skills"]).issubset(set(resume["skills"]))


def test_the_parser_of_a_text_without_a_fact_gives_zero():
    parsed = parse_resume("A short note about nothing in particular.")
    assert parsed["years"] == 0
    assert parsed["projects"] == 0
    assert parsed["skills"] == []


# ---------------------------------------------------------------------------
# The label
# ---------------------------------------------------------------------------

def test_the_label_is_not_a_function_of_the_skills():
    """The label may not be computed from the skills the model reads.

    The same skills with a different work history can give a different label,
    so the skills alone do not decide it.
    """
    from src.data import make_resume as build

    same_skills = ["python", "sql", "testing"]
    labels = {
        build(index, seed=3, skills=same_skills)["label"]
        for index in range(40)
    }
    assert len(labels) == 2, f"the same skills can give both labels, got {labels}"


# ---------------------------------------------------------------------------
# The training
# ---------------------------------------------------------------------------

def test_the_metrics_are_reported(tmp_path):
    data = load_data(seed=5, quick=True)
    _, metrics = train(data, quick=True, db_path=str(tmp_path / "candidates.db"))

    assert 0 <= metrics["precision"] <= 1
    assert 0 <= metrics["recall"] <= 1
    assert metrics["candidates"] == len(data["test"])
    assert metrics["shortlisted"] == int(metrics["shortlisted"])


def test_the_candidates_are_stored(tmp_path):
    data = load_data(seed=5, quick=True)
    path = tmp_path / "candidates.db"
    train(data, quick=True, db_path=str(path))

    connection = sqlite3.connect(path)
    rows = connection.execute("SELECT name, years, skills, score, shortlisted FROM candidates").fetchall()
    connection.close()

    assert len(rows) == len(data["test"])
    assert all(0 <= row[3] <= 1 for row in rows)
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


### app.py

### app.py

```text
"""The web layer of the project: the site, the console and the API.

Three things live here:

    /             the home page of the site
    /console.html the console, with the candidates and the metrics of the run
    /candidates   the dashboard of the project, with the table of the
                  candidates (this is the page the project had)

The API behind the console is /api/summary, /api/candidates and
/api/questions, and /api/train fits the classifier again.
"""
import os
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, render_template_string, request, send_from_directory

from src.data import load_data
from src.model import draft_interview_questions, rank_candidates, train

#: The directory of the site and the database of the candidates.
ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
DB_PATH = ROOT / "artifacts" / "candidates.db"

app = Flask(__name__)

DATA = load_data(seed=3, quick=False)
MODEL, METRICS = train(DATA, quick=False, db_path=str(DB_PATH))

PAGE = """
<!doctype html>
<title>Resume screening</title>
<style>
 body { font-family: system-ui, sans-serif; max-width: 720px; margin: 40px auto; }
 table { border-collapse: collapse; width: 100%; }
 th, td { text-align: left; padding: 8px; border-bottom: 1px solid #e5e7eb; }
 .yes { color: #15803d; font-weight: 600; }
</style>
<h1>Resume screening</h1>
<p>{{ job }}</p>
<table>
<tr><th>Candidate</th><th>Years</th><th>Score</th><th>Shortlist</th></tr>
{% for row in rows %}
<tr>
  <td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ '%.2f'|format(row[3]) }}</td>
  <td class="{{ 'yes' if row[4] else '' }}">{{ 'yes' if row[4] else 'no' }}</td>
</tr>
{% endfor %}
</table>
<p>Metrics: precision {{ '%.2f'|format(metrics.precision) }}, recall {{ '%.2f'|format(metrics.recall) }}.</p>

<h2>Questions for the interview</h2>
{% for question in questions %}
<p>- {{ question }}</p>
{% endfor %}
"""


def candidates():
    """The candidates of the database, the best score first."""
    connection = sqlite3.connect(DB_PATH)
    rows = connection.execute(
        "SELECT name, years, skills, score, shortlisted FROM candidates ORDER BY score DESC"
    ).fetchall()
    connection.close()
    return rows


def interview_questions():
    """The questions of the interview, drafted from the best candidate."""
    ranked = rank_candidates(MODEL, DATA)
    if not ranked:
        return []
    return draft_interview_questions(ranked[0][0], DATA["job_description"])


def summary_payload():
    """The answer of /api/summary: the numbers of the run."""
    rows = candidates()
    questions = interview_questions()
    return {
        "stats": {
            "candidates": len(rows),
            "shortlisted": sum(1 for row in rows if row[4]),
            "precision": METRICS["precision"],
            "recall": METRICS["recall"],
        },
        "series": [
            {"label": row[0], "value": round(row[3], 4)} for row in rows
        ],
        "lists": {
            "candidates": [
                {
                    "name": row[0],
                    "years": row[1],
                    "score": round(row[3], 4),
                    "shortlisted": "yes" if row[4] else "no",
                }
```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
