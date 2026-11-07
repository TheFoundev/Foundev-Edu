# Reddit and TikTok Fetchers: Begin with the concept

**Lesson ID:** `social-media-sentiment-dashboard-module-06-lesson-01`  
**Module ID:** `social-media-sentiment-dashboard-module-06`  
**Source focus:** `src/scheduler.py` → `fetch_all_data`

## Purpose and learning objectives

Explain reddit and tiktok fetchers in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Scheduler and Utils.

## Beginner explanation

A social analytics pipeline collects posts, organizes them, scores text, then summarizes trends. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/scheduler.py` and locate `fetch_all_data`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/scheduler.py`, `src/utils.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `src/scheduler.py`. source tree absent; excerpt retained from earlier package

### src/scheduler.py

The excerpt below is the selected implementation focus.
### src/utils.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from fetchers import twitter_fetcher, facebook_fetcher, instagram_fetcher, discord_fetcher, medium_fetcher, reddit_fetcher, youtube_fetcher, tiktok_fetcher
from analytics import metrics
from data_manager import save_data
import datetime

def fetch_all_data(config):
    logging.info("Starting data fetch cycle")
    
    # Instantiate each fetcher with its configuration details.
    twitter_data = twitter_fetcher.TwitterFetcher(config.get("twitter", {})).get_data()
    facebook_data = facebook_fetcher.FacebookFetcher(config.get("facebook", {})).get_data()
    instagram_data = instagram_fetcher.InstagramFetcher(config.get("instagram", {})).get_data()
    discord_data = discord_fetcher.DiscordFetcher(config.get("discord", {})).get_data()
    medium_data = medium_fetcher.MediumFetcher(config.get("medium", {})).get_data()
    reddit_data = reddit_fetcher.RedditFetcher(config.get("reddit", {})).get_data()
    youtube_data = youtube_fetcher.YouTubeFetcher(config.get("youtube", {})).get_data()
    tiktok_data = tiktok_fetcher.TikTokFetcher(config.get("tiktok", {})).get_data()
    
    all_data = {
        "twitter": twitter_data,
        "facebook": facebook_data,
        "instagram": instagram_data,
        "discord": discord_data,
        "medium": medium_data,
        "reddit": reddit_data,
        "youtube": youtube_data,
        "tiktok": tiktok_data
    }
    
    # Save each platform's data to disk
    for platform, posts in all_data.items():
        save_data(platform, posts)
    
    # Process and compute overall metrics
    computed_metrics = metrics.compute_overall_metrics(all_data)
    logging.info("Data fetch cycle completed at {}. Computed Metrics: {}"
                 .format(datetime.datetime.now(), computed_metrics))

def start_scheduler(config):
    scheduler = BackgroundScheduler()
    # Schedule the fetch_all_data job to run every 5 minutes
    scheduler.add_job(fetch_all_data, 'interval', minutes=5, args=[config])
    scheduler.start()
    logging.info("Scheduler started with a 5-minute interval")
```

First read the signature/declared data shape; then follow the code and caller.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-06.md`](../exercises/exercise-06.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `fetch_all_data` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `fetch_all_data` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
