# Read documented goals mapped to implementation in the source

**Lesson ID:** `social-media-sentiment-dashboard-module-14-lesson-2`

## Purpose and learning objectives

Compare the source documentation in README.md with implementation anchors conftest.py, src/analytics/__init__.py, src/analytics/metrics.py. Trace one feature claim to its code path and record any mismatch or evidence gap.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `README.md`, `conftest.py`, `src/analytics/__init__.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `README.md` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- In `conftest.py`, `import sys` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `conftest.py`, `import os` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/__init__.py`, `from .sentiment_analysis import SentimentAnalyzer, analyze_posts_sentiment, sentiment_distribution` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/__init__.py`, `from .trend_analysis import compute_trending_topics` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/__init__.py`, `from .metrics import compute_metrics_for_platform, compute_overall_metrics` brings a module or package name into this file; follow later references before claiming it is used on a running path.

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
A demonstration-grade solution: full-stack data analytics platform leveraging REST API integrations, sentiment and trend analysis and real-time interactive dashboards built with Python, Flask and Dash, aggregating social media data from Twitter, Facebook, Instagram, Discord, Medium, Reddit, YouTube and TikTok for marketing insights.

The project was developed as part of my freelance project, which was published with the client's permission. In this release, all sensitive data has been replaced with synthetic examples to ensure the privacy of the freelance client and their customers.

Some features:
- **Multi-platform data aggregation**  
Integrates data fetching from multiple social media platforms using simulated API calls.
- **Advanced analytics**  
Performs sentiment analysis using NLTK's VADER, computes trending topics from hashtags and calculates key performance metrics.
- **Real-time dashboard**  
Interactive dashboard displaying real-time metrics and visualizations using Plotly Dash.
- **Scheduling & automation**  
Uses APScheduler to automatically refresh and update data.
- **Data management**  
Saves and reloads historical data records.
- **Modular & tested**  
Well-structured codebase with dedicated modules for fetchers, analytics, models and utility functions along with unit tests.

## Technologies
- Python 3.x, Flask, Dash, APScheduler
- Pandas, NumPy for data processing
- Requests for simulated API calls
- NLTK for sentiment analysis
- Standard Python logging, unittest for tests

## Structure
```
.
├── README.md
├── .gitignore
├── requirements.txt
├── config/
│   └── social_accounts.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── scheduler.py
│   ├── utils.py
│   ├── dashboard.py
│   ├── data_manager.py
│   ├── fetchers/
│   │   ├── __init__.py
│   │   ├── twitter_fetcher.py
│   │   ├── facebook_fetcher.py
│   │   ├── instagram_fetcher.py
│   │   ├── discord_fetcher.py
│   │   ├── medium_fetcher.py
│   │   ├── reddit_fetcher.py
│   │   ├── youtube_fetcher.py
│   │   └── tiktok_fetcher.py
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── sentiment_analysis.py
│   │   ├── trend_analysis.py
│   │   └── metrics.py
│   └── models/
│       ├── __init__.py
│       ├── social_post.py
│       └── account.py
└── tests/
    ├── test_fetchers.py
    └── test_analytics.py
```

## How to run
1. Clone the repository
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Update `config/social_accounts.json` with your social media account details.
4. Start the app:
   ```
   python src/main.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:8050` to view the dashboard.

## Testing
Run tests using:
```
pytest tests/
```

## To do
TBA

## Contributions
are welcome

## License
Apache 2.0

```

### conftest.py

```text
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

```

### src/analytics/__init__.py

```text
from .sentiment_analysis import SentimentAnalyzer, analyze_posts_sentiment, sentiment_distribution
from .trend_analysis import compute_trending_topics
from .metrics import compute_metrics_for_platform, compute_overall_metrics
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

This lesson ties its explanation to `README.md`, `conftest.py`, `src/analytics/__init__.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
