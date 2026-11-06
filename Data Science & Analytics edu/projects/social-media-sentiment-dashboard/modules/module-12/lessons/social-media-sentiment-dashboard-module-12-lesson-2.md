# Read test code and evidence boundaries in the source

**Lesson ID:** `social-media-sentiment-dashboard-module-12-lesson-2`

## Purpose and learning objectives

Read test implementations tests/test_analytics.py, tests/test_fetchers.py. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `tests/test_analytics.py`, `tests/test_fetchers.py`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- In `tests/test_analytics.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_analytics.py`, `from datetime import datetime` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_analytics.py`, `from src.models.social_post import SocialPost` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_analytics.py`, `from analytics.sentiment_analysis import SentimentAnalyzer, sentiment_distribution` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_analytics.py`, `from analytics.trend_analysis import compute_trending_topics` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestAnalytics(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def setUp(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_sentiment_analysis(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_trend_analysis(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_metrics_computation(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_sentiment_distribution(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `tests/test_fetchers.py`, `import unittest` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_fetchers.py`, `from src.fetchers.twitter_fetcher import TwitterFetcher` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_fetchers.py`, `from src.fetchers.facebook_fetcher import FacebookFetcher` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_fetchers.py`, `from src.fetchers.instagram_fetcher import InstagramFetcher` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `tests/test_fetchers.py`, `from src.fetchers.discord_fetcher import DiscordFetcher` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class TestFetchers(unittest.TestCase):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def setUp(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_twitter_fetcher(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_facebook_fetcher(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_instagram_fetcher(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def test_discord_fetcher(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### tests/test_analytics.py

```text
import unittest
from datetime import datetime
from src.models.social_post import SocialPost
from analytics.sentiment_analysis import SentimentAnalyzer, sentiment_distribution
from analytics.trend_analysis import compute_trending_topics
from analytics.metrics import compute_metrics_for_platform

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Create a set of synthetic social posts
        self.posts = []
        for i in range(10):
            content = ("This is a test post with hashtag #test and positive sentiment" 
                       if i % 2 == 0 else "Negative sentiment post #fail")
            post = SocialPost(
                platform="TestPlatform",
                post_id=f"test_{i}",
                content=content,
                timestamp=datetime.now(),
                likes=10,
                retweets=2,
                comments=1
            )
            self.posts.append(post)

    def test_sentiment_analysis(self):
        analyzer = SentimentAnalyzer()
        score = analyzer.analyze(self.posts[0].content)
        self.assertIsInstance(score, float)

    def test_trend_analysis(self):
        trending = compute_trending_topics(self.posts, top_n=3)
        self.assertIsInstance(trending, list)
        self.assertTrue(len(trending) <= 3)

    def test_metrics_computation(self):
        metrics = compute_metrics_for_platform(self.posts)
        self.assertIn("total_posts", metrics)
        self.assertIn("avg_sentiment", metrics)
        self.assertIn("trending", metrics)
        self.assertIn("sentiment_distribution", metrics)

    def test_sentiment_distribution(self):
        # First, analyze sentiment for each post.
        analyzer = SentimentAnalyzer()
        for post in self.posts:
            post.sentiment = analyzer.analyze(post.content)
        dist = sentiment_distribution(self.posts)
        self.assertIn("negative", dist)
        self.assertIn("neutral", dist)
        self.assertIn("positive", dist)

if __name__ == '__main__':
    unittest.main()
```

### tests/test_fetchers.py

```text
import unittest
from src.fetchers.twitter_fetcher import TwitterFetcher
from src.fetchers.facebook_fetcher import FacebookFetcher
from src.fetchers.instagram_fetcher import InstagramFetcher
from src.fetchers.discord_fetcher import DiscordFetcher
from src.fetchers.medium_fetcher import MediumFetcher
from src.fetchers.reddit_fetcher import RedditFetcher
from src.fetchers.youtube_fetcher import YouTubeFetcher
from src.fetchers.tiktok_fetcher import TikTokFetcher

class TestFetchers(unittest.TestCase):
    def setUp(self):
        # Minimal (synthetic) config for fetchers
        self.config = {}

    def test_twitter_fetcher(self):
        fetcher = TwitterFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_facebook_fetcher(self):
        fetcher = FacebookFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_instagram_fetcher(self):
        fetcher = InstagramFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_discord_fetcher(self):
        fetcher = DiscordFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_medium_fetcher(self):
        fetcher = MediumFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_reddit_fetcher(self):
        fetcher = RedditFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_youtube_fetcher(self):
        fetcher = YouTubeFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

    def test_tiktok_fetcher(self):
        fetcher = TikTokFetcher(self.config)
        data = fetcher.get_data()
        self.assertTrue(len(data) > 0)

if __name__ == '__main__':
    unittest.main()
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

This lesson ties its explanation to `tests/test_analytics.py`, `tests/test_fetchers.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### src/main.py

### src/main.py

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

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
