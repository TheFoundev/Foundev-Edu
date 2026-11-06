# A beginner's model of scheduler and utils

**Lesson ID:** `social-media-sentiment-dashboard-module-11-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/scheduler.py] and [src/utils.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include fetch_all_data, start_scheduler, simulate_network_delay, setup_logger, format_timestamp; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/scheduler.py`, `src/utils.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/scheduler.py`, `from apscheduler.schedulers.background import BackgroundScheduler` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/scheduler.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/scheduler.py`, `from fetchers import twitter_fetcher, facebook_fetcher, instagram_fetcher, discord_fetcher, medium_fetcher, reddit_fetcher, youtube_fetcher, tiktok_fetcher` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/scheduler.py`, `from analytics import metrics` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/scheduler.py`, `from data_manager import save_data` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def fetch_all_data(config):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def start_scheduler(config):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/utils.py`, `import time` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/utils.py`, `import random` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/utils.py`, `import logging` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def simulate_network_delay():` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def setup_logger(name):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def format_timestamp(ts):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/scheduler.py

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

### src/utils.py

```text
import time
import random
import logging

def simulate_network_delay():
    """
    Simulate network latency between 0.1 and 0.5 seconds.
    """
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)

def setup_logger(name):
    """
    Create and configure a logger with the given name.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger

def format_timestamp(ts):
    """
    Format a datetime timestamp into a readable string.
    """
    return ts.strftime("%Y-%m-%d %H:%M:%S")
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

This lesson ties its explanation to `src/scheduler.py`, `src/utils.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
