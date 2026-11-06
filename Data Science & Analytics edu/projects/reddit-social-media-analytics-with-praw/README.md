# Reddit Social Media Analytics With Praw

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# Reddit Social Media Analytics with PRAW

Analyse synthetic subreddit posts and comments in SQLite.

> Collect subreddit posts and comments to track sentiment trends, topic bursts and community engagement over time in a live dashboard.

## Overview

An original, self-contained implementation of the **Reddit Social Media Analytics with PRAW** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- The data comes from a `RedditSource`: the synthetic generator that ships with
  the project, or the real Reddit API through praw
- Engagement per subreddit, with the averages, and the most active authors
- A sentiment score for every post and every comment, with VADER, so a
  negation is understood
- The comments are analysed as well: the sentiment, the most active
  commenters and the depth of the threads
- Every run is appended to the database with the time it ran, so the history
  of the runs can be read back
- An activity chart and an engagement chart

## StackStack

`Python; PRAW; SQLite; Streamlit`

The CSV stack is PRAW + SQLite + Streamlit. PRAW needs Reddit API credentials and Streamlit is not installed, so this build uses generated posts, SQLite and Flask.

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
reddit-social-media-analytics-with-praw/
├── main.py                 pipeline CLI
├── src/pipeline.py         data pipeline
├── tests/test_pipeline.py  smoke

## Actual features and limits

README feature statements (verify each against code before relying on it):
- The data comes from a `RedditSource`: the synthetic generator that ships with
- Engagement per subreddit, with the averages, and the most active authors
- A sentiment score for every post and every comment, with VADER, so a
- The comments are analysed as well: the sentiment, the most active
- Every run is appended to the database with the time it ran, so the history
- An activity chart and an engagement chart
- No Reddit API is called; all posts and comments are synthetic.
- Sentiment uses a small positive/negative word list, not a trained model.
- The dashboard is read-only and has no live refresh.

The implementation inventory includes 13 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/pipeline.py`
- `tests/test_pipeline.py`
- `web/assets/app.js`

## Testing

Test-related paths found: tests/test_pipeline.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
