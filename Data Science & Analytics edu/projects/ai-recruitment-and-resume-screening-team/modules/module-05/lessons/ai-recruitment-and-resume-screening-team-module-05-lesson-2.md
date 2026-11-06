# Read documented goals mapped to implementation in the source

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-05-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors app.py, main.py, src/data.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `app.py`, `main.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `app.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from flask import Flask, jsonify, render_template_string, request, send_from_directory` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from src.data import load_data` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def candidates():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def interview_questions():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary_payload():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def home():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def console():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import pickle` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.data import load_data` brings a module or package name into this file; follow later references before claiming it is used on a running path.
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
# AI Recruitment and Resume Screening Team

Rank resumes against a job description with skills and a small classifier.

> Automate a hiring pipeline with collaborating agents that parse resumes, match skills to job descriptions, shortlist candidates and draft interview questions.

## Overview

An original, self-contained implementation of the **AI Recruitment and Resume Screening Team** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A resume parser that reads the facts (the years, the degree, the number of
  the projects and the skills) out of the text of the resume
- A logistic regression over the text, with the candidates stored in SQLite
- The interview questions drafted from the resume: a question for every skill
  it mentions, a question for every skill of the job it does not mention, and
  a few general ones
- A read-only dashboard over the candidates

## Stack

`Python; CrewAI; Streamlit; SQLite`

The CSV stack is CrewAI + Streamlit + SQLite. CrewAI and Streamlit are not installed, so the pipeline uses a small classifier and Flask with a SQLite table.

## Run

```bash
pip install -r requirements.txt
python main.py train
python app.py
python main.py demo
pytest -q
```

## Structure

```text
ai-recruitment-and-resume-screening-team/
├── main.py                 train / demo CLI
├── src/data.py             dataset builder
├── src/model.py            model and evaluation
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── app.py                  Flask candidate dashboard
```

## Testing

```bash
pytest -q
```

13 tests: the parser, the label (the same skills can give both labels, so
the label is not a function of the skills), the metrics, the candidates in the
database, the ranking, the questions for the interview and the dashboard.

## Notes and limitations

- Resumes are synthetic; no real applicant data is used.
- The label is generated from a simple skills/experience policy, so the model learns that policy.
- There is no PDF parsing, bias audit or human-in-the-loop review.

## License

Apache-2.0. See `LICENSE`.

## About the scope

This is a third-year student project, not a production system. The code is small enough to read in one sitting and focuses on the core idea from the brief. The notes above list the parts that are simplified or simulated.

```

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

### main.py

```text
"""Command line entry point. Run `python main.py train` or `python main.py demo`."""
import argparse
import json
import pickle
from pathlib import Path

from src.data import load_data
from src.model import train, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Screen synthetic resumes against a job description.')
    parser.add_argument("command", choices=["train", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="use a tiny run for smoke tests")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.command == "info":
        print('Screen synthetic resumes against a job description.')
        print("Run `python main.py train` to fit the model, or `demo` for a sample.")
        return

    data = load_data(seed=args.seed, quick=args.quick)
    if args.command == "demo":
        demo(data)
        return

    model, metrics = train(data, quick=args.quick)
    out = Path("artifacts")
    out.mkdir(exist_ok=True)
    if hasattr(model, "save"):
        try:
            model.save(out / "model.keras")
        except Exception:
            pass
    else:
        try:
            with open(out / "model.pkl", "wb") as handle:
                pickle.dump(model, handle)
        except Exception:
            pass

    print(json.dumps(metrics, indent=2, default=float))
    print("\nSaved model output under artifacts/ (when supported).")


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
