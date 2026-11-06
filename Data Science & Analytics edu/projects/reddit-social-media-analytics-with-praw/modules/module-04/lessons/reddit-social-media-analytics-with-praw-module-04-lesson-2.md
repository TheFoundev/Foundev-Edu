# Read declared dependencies and runtime configuration in the source

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-04-lesson-2`

## Purpose and learning objectives

Inspect the actual manifests requirements.txt. Separate declared packages/settings from imports, installed state, secrets, and runtime success.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `requirements.txt`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

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
pandas>=2.0
matplotlib>=3.8
flask>=3.0
praw>=7.7
vaderSentiment>=3.3
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
"""The dashboard of the subreddit analytics and the site of the project.

The posts and the comments are synthetic, so the analytics run without a
Reddit account. The site of the project lives in `web/`, and `/api/summary`
answers with the numbers of the database the pipeline wrote.
"""
import os
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, render_template_string, send_file, send_from_directory

from src.pipeline import run

app = Flask(__name__)
run(quick=True, base_dir="artifacts")

#: The site of the project.
WEB = Path(__file__).resolve().parent / "web"

#: The database the pipeline writes.
DB_PATH = Path("artifacts/analytics.db")

PAGE = """
<!doctype html>
<title>Subreddit analytics</title>
<link rel="stylesheet" href="/assets/theme.css">
<style>
 body { font-family: system-ui, sans-serif; max-width: 820px; margin: 36px auto; color: #1f2937; }
 table { border-collapse: collapse; width: 100%; margin: 16px 0; }
 th, td { text-align: left; padding: 7px 9px; border-bottom: 1px solid #e5e7eb; }
 img { max-width: 100%; border: 1px solid #e5e7eb; }
</style>
<h1>Subreddit analytics</h1>
<p>Posts and comments are synthetic; there is no Reddit API call.</p>
<h2>Activity</h2>
<img src="/chart" alt="Posting activity by hour">
<h2>Top subreddits</h2>
<table>
<tr><th>Subreddit</th><th>Posts</th><th>Score</th><th>Comments</th></tr>
{% for row in rows %}
<tr><td>{{ row[0] }}</td><td>{{ row[1] }}</td><td>{{ row[2] }}</td><td>{{ row[3] }}</td></tr>
{% endfor %}
</table>
<h2>Top posts</h2>
<ul>
{% for row in posts %}
<li><strong>{{ row[0] }}</strong> — score {{ row[1] }}, {{ row[2] }} comments</li>
{% endfor %}
</ul>
<p><a href="/console.html">Open the console</a></p>
"""


def _query(sql: str, parameters: tuple = ()) -> list[tuple]:
    """The rows of a query of the analytics database."""
    if not DB_PATH.exists():
        return []
    connection = sqlite3.connect(DB_PATH)
    try:
        return connection.execute(sql, parameters).fetchall()
    finally:
        connection.close()


def summary_payload():
    """The state of the analytics: the database the pipeline wrote.

    The engagement of a post is its score plus twice its number of
    comments, the same way the pipeline weighs it.
    """
    subreddits = _query(
        "SELECT subreddit, COUNT(*), SUM(score), SUM(comments), "
        "SUM(score + 2 * comments) FROM posts GROUP BY subreddit "
        "ORDER BY SUM(score + 2 * comments) DESC"
    )
    posts = _query("SELECT title, subreddit, score, comments, sentiment_label FROM posts "
                   "ORDER BY score DESC LIMIT 8")
    authors = _query("SELECT author, COUNT(*), SUM(score + 2 * comments) FROM posts "
                     "GROUP BY author ORDER BY SUM(score + 2 * comments) DESC LIMIT 8")
    hours = _query("SELECT hour, COUNT(*), SUM(score + 2 * comments) FROM posts "
                   "GROUP BY hour ORDER BY hour")
    comment_row = _query("SELECT COUNT(*), AVG(sentiment) FROM comments")
    comments = comment_row[0] if comment_row else (0, 0.0)
    runs = _query("SELECT run_at, source, COUNT(*) FROM posts GROUP BY run_at, source "
                  "ORDER BY run_at DESC LIMIT 8")
    total_posts = _query("SELECT COUNT(*) FROM posts")[0][0]
    sentiment = _query("SELECT sentiment_label, COUNT(*) FROM posts GROUP BY sentiment_label")

    return {
        "stats": {
            "posts": int(total_posts),
            "comments": int(comments[0]),
            "subreddits": len(subreddits),
            "positive_share": round(
                float(sum(count for label, count in sentiment if label == "positive"))
                / max(1, total_posts), 4),
        },
        "series": [{"label": f"{int(hour):02d}:00", "value": int(count)} for hour, count, _ in hours],
        "lists": {
```

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
