# Read code review and safe change 6 in the source

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-06-lesson-2`

## Purpose and learning objectives

Use app.py to identify a bounded change, its callers, and a testable acceptance condition. Do not infer unobserved behavior.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `app.py`, `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `app.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from flask import Flask, jsonify, render_template_string, send_file, send_from_directory` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `app.py`, `from src.pipeline import run` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def _query(sql: str, parameters: tuple = ()) -> list[tuple]:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def summary_payload():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def index():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def demo():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def console():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def login():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `main.py`, `import argparse` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `import json` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `main.py`, `from src.pipeline import run, demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def main() -> None:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/pipeline.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import sqlite3` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from datetime import datetime, timezone` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `from pathlib import Path` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/pipeline.py`, `import numpy as np` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class RedditSource:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def fetch(self, limit=120):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class SyntheticRedditSource(RedditSource):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, seed=42):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def fetch(self, limit=120):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `class PrawRedditSource(RedditSource):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_pipeline.py`, `from src.pipeline import (` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_pipeline.py`, `from src.pipeline import demo` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def test_the_pipeline_runs(tmp_path, capsys):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_sentiment_understands_a_negation():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_sentiment_has_a_label():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_lexicon_fallback_still_works():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_engagement_is_defined():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_the_subreddit_table_has_the_averages(tmp_path):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

### main.py

```text
"""Pipeline entry point. Run `python main.py run` or `python main.py demo`."""
import argparse
import json

from src.pipeline import run, demo


def main() -> None:
    parser = argparse.ArgumentParser(description='Analyse a synthetic Reddit-style dataset.')
    parser.add_argument("command", choices=["run", "demo", "info"])
    parser.add_argument("--quick", action="store_true", help="small local run")
    parser.add_argument("--base-dir", default="artifacts", help="output directory")
    args = parser.parse_args()

    if args.command == "info":
        print('Analyse a synthetic Reddit-style dataset.')
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
"""Collect Reddit posts and comments, then compute the engagement analytics.

The data comes from a `RedditSource`. The project ships with the synthetic
source, so it runs without an account, and `PrawRedditSource` talks to the
real Reddit API when praw and the credentials are there.
"""
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

SUBREDDITS = ["learnpython", "datascience", "webdev", "devops"]
POSITIVE = ["helpful", "great", "clear", "works", "thanks", "nice", "useful", "solved"]
NEGATIVE = ["confusing", "broken", "slow", "error", "stuck", "hate", "wrong", "failed"]

#: How a post is scored. The score of Reddit and the number of comments are
#: not on the same scale, so they are weighted before they are added.
SCORE_WEIGHT = 1.0
COMMENT_WEIGHT = 2.0


# ---------------------------------------------------------------------------
# The sources
# ---------------------------------------------------------------------------


class RedditSource:
    """Where the posts and the comments come from."""

    name = "base"

    def fetch(self, limit=120):
        """Return the posts and the comments as two data frames."""
        raise NotImplementedError


class SyntheticRedditSource(RedditSource):
    """A generator that makes Reddit-style posts and comments."""

    name = "synthetic"

    def __init__(self, seed=42):
        self.seed = seed

    def fetch(self, limit=120):
        rng = np.random.default_rng(self.seed)
        titles = [
            "How do I structure a small project?",
            "My first dashboard finally works",
            "Question about testing database code",
            "A short note on deployment",
            "Why is this query slow?",
            "Sharing a weekend side project",
        ]
        posts = []
        for index in range(limit):
            words = rng.choice(POSITIVE + NEGATIVE, size=5)
            body = " ".join(words) + " " + str(rng.choice(titles))
            posts.append({
                "post_id": index + 1,
                "subreddit": str(rng.choice(SUBREDDITS)),
                "title": str(rng.choice(titles)),
                "body": body,
                "score": int(rng.integers(0, 220)),
                "comments": int(rng.integers(0, 40)),
                "hour": int(rng.integers(0, 24)),
                "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "author": f"user_{index % 17}",
            })
        posts = pd.DataFrame(posts)

        comment_rows = []
        for index in range(limit * 2):
            text = " ".join(rng.choice(POSITIVE + NEGATIVE, size=4))
            comment_rows.append({
                "comment_id": index + 1,
                "post_id": int(rng.integers(1, limit + 1)),
                "body": text,
                "score": int(rng.integers(-2, 40)),
                "author": f"user_{index % 23}",
                "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            })
        return posts, pd.DataFrame(comment_rows)


class PrawRedditSource(RedditSource):
    """The real Reddit API, through praw.

    The credentials come from the environment: REDDIT_CLIENT_ID,
    REDDIT_CLIENT_SECRET and REDDIT_USER_AGENT. Nothing is written to disk.
    """

    name = "praw"

    def __init__(self, subreddits=None, sort="top", time_filter="week"):
        self.subreddits = subreddits or SUBREDDITS
        self.sort = sort
```

### tests/test_pipeline.py

```text
"""Tests for the Reddit analytics."""
from src.pipeline import (
    PrawRedditSource,
    RedditSource,
    SyntheticRedditSource,
    author_analysis,
    by_hour,
    by_subreddit,
    comment_analysis,
    engagement,
    history,
    run,
    sentiment,
    sentiment_from_lexicon,
    sentiment_label,
)


def test_the_pipeline_runs(tmp_path, capsys):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert isinstance(summary, dict)
    assert summary
    assert any(tmp_path.iterdir())

    from src.pipeline import demo

    demo(base_dir=str(tmp_path))
    assert capsys.readouterr().out.strip()


def test_the_sentiment_understands_a_negation():
    """A negation has to change the sign of the sentiment."""
    assert sentiment("this is great and useful") > 0
    assert sentiment("this is confusing and broken") < 0
    assert sentiment("this is not good at all") < 0
    assert sentiment("") == 0


def test_the_sentiment_has_a_label():
    assert sentiment_label(0.8) == "positive"
    assert sentiment_label(-0.8) == "negative"
    assert sentiment_label(0.0) == "neutral"


def test_the_lexicon_fallback_still_works():
    assert sentiment_from_lexicon("great helpful") == 1.0
    assert sentiment_from_lexicon("confusing broken") == -1.0
    assert sentiment_from_lexicon("hello") == 0.0


def test_the_engagement_is_defined():
    """The engagement is the score plus twice the number of comments."""
    assert engagement({"score": 10, "comments": 3}) == 16.0


def test_the_subreddit_table_has_the_averages(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["top_subreddit"]
    assert summary["top_engagement"] > 0
    assert "average_engagement" in summary


def test_the_comments_are_analysed(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["comments"] > 0
    assert summary["comment_positive_share"] >= 0
    assert summary["top_commenters"]


def test_the_authors_are_ranked(tmp_path):
    summary = run(quick=True, base_dir=str(tmp_path))
    assert summary["authors"]
    first = summary["authors"][0]
    assert "author" in first and "posts" in first


def test_the_runs_are_kept(tmp_path):
    """Two runs leave two rows in the history."""
    run(quick=True, base_dir=str(tmp_path))
    run(quick=True, base_dir=str(tmp_path))
    entries = history(base_dir=str(tmp_path))
    assert len(entries) == 2
    assert entries[0]["posts"] > 0


def test_the_history_is_empty_without_a_database(tmp_path):
    assert history(base_dir=str(tmp_path)) == []


def test_the_source_can_be_swapped(tmp_path):
    """A source is an interface, so the pipeline works with any of them."""
    source = SyntheticRedditSource(seed=3)
    posts, comments = source.fetch(10)
    assert len(posts) == 10
    assert len(comments) == 20

    summary = run(quick=True, base_dir=str(tmp_path), source=source)
    assert summary["source"] == "synthetic"


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

This lesson ties its explanation to `app.py`, `main.py`, `src/pipeline.py`, `tests/test_pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
