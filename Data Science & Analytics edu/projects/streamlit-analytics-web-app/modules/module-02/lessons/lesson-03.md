# Server and Pipeline: Test the boundary

**Lesson ID:** `streamlit-analytics-web-app-module-02-lesson-03`  
**Module ID:** `streamlit-analytics-web-app-module-02`  
**Source focus:** `web/server.py` → `summary`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Server and Pipeline.

## Beginner explanation

In plain language, server and pipeline is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `web/server.py` and locate `summary`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `web/server.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `web/server.py` at lines 43–63. Source code was not executed during refinement.

### web/server.py

The excerpt below is the selected implementation focus.
### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
try:  # the domain logic of the project
    from web.api_impl import handle, summary
except Exception:  # pragma: no cover - the project has no domain module yet
    def summary() -> dict:
        return {"stats": {"status": "running"}, "series": [], "lists": {}}

    def handle(method, path, payload, user):
        return 404, {"error": "not found"}

#: The Streamlit page of the project. It is a product of its own and it runs
#: in its own process, so the site sends the visitor there.
STREAMLIT_URL = os.environ.get("STREAMLIT_URL", "http://127.0.0.1:9013/app")

DB_PATH = HERE / "app.db"
SECRET_PATH = HERE / ".session-secret"
SESSION_COOKIE = "foundev_session"
SESSION_TTL = 8 * 3600
DEMO_USER = "demo"
DEMO_PASSWORD = "demo123"

SECRET = b""
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-02.md`](../exercises/exercise-02.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `summary` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `summary` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
