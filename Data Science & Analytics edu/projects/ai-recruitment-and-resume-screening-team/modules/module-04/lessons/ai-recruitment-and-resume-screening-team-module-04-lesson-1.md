# A beginner's model of declared dependencies and runtime configuration

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-04-lesson-1`

## Purpose and learning objectives

Inspect the actual manifests requirements.txt. Separate declared packages/settings from imports, installed state, secrets, and runtime success.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `requirements.txt`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `requirements.txt` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### requirements.txt

```text
numpy>=1.26
scikit-learn>=1.4
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

This lesson ties its explanation to `requirements.txt`. A sound account distinguishes source evidence from inferred behavior.

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
