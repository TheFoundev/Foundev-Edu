# A beginner's model of pipeline

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-02-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/pipeline.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include RedditSource, fetch, SyntheticRedditSource, __init__, fetch, PrawRedditSource, __init__, fetch; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/pipeline.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

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

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

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

This lesson ties its explanation to `src/pipeline.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
