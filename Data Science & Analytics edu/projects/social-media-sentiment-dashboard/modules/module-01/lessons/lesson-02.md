# Application Entry and Account Model: Trace the code

**Lesson ID:** `social-media-sentiment-dashboard-module-01-lesson-02`  
**Module ID:** `social-media-sentiment-dashboard-module-01`  
**Source focus:** `src/main.py` → `setup_logging`

## Purpose and learning objectives

Trace `setup_logging` in `src/main.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Main and Account, Social Post and Conftest.

## Beginner explanation

A social analytics pipeline collects posts, organizes them, scores text, then summarizes trends. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/main.py` and locate `setup_logging`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/main.py`, `src/models/account.py`, `src/models/social_post.py`, `conftest.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `src/main.py`. source tree absent; excerpt retained from earlier package

### src/main.py

The excerpt below is the selected implementation focus.
### src/models/account.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/models/social_post.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### conftest.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import logging
from config import load_config
from scheduler import start_scheduler
from dashboard import create_dashboard_app

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    setup_logging()
    logging.info("Starting social-metrics-dashboard Application")
    
    config = load_config()
    logging.info("Configuration loaded successfully")
    
    # Start scheduler to periodically fetch data and save to disk
    start_scheduler(config)
    
    # Create and run dashboard app
    app = create_dashboard_app(config)
    logging.info("Dashboard app created, starting server")
    app.run_server(debug=True)

if __name__ == '__main__':
    main()
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-01.md`](../exercises/exercise-01.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `setup_logging` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `setup_logging` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
