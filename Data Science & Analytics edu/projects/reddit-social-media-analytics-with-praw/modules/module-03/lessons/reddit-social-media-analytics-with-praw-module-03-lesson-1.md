# A beginner's model of test code and evidence boundaries

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-03-lesson-1`

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

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
