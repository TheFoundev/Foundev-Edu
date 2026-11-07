# Discord and Facebook Fetchers: Trace the code

**Lesson ID:** `social-media-sentiment-dashboard-module-04-lesson-02`  
**Module ID:** `social-media-sentiment-dashboard-module-04`  
**Source focus:** `src/fetchers/discord_fetcher.py` → `DiscordFetcher`

## Purpose and learning objectives

Trace `DiscordFetcher` in `src/fetchers/discord_fetcher.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Discord Fetcher and Facebook Fetcher, Instagram Fetcher and Medium Fetcher.

## Beginner explanation

A social analytics pipeline collects posts, organizes them, scores text, then summarizes trends. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/fetchers/discord_fetcher.py` and locate `DiscordFetcher`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `src/fetchers/discord_fetcher.py`, `src/fetchers/facebook_fetcher.py`, `src/fetchers/instagram_fetcher.py`, `src/fetchers/medium_fetcher.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs; source declarations

**Excerpt:** `src/fetchers/discord_fetcher.py`. source tree absent; excerpt retained from earlier package

### src/fetchers/discord_fetcher.py

The excerpt below is the selected implementation focus.
### src/fetchers/facebook_fetcher.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/fetchers/instagram_fetcher.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/fetchers/medium_fetcher.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class DiscordFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Discord API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 6 Discord messages.
        for i in range(6):
            post = SocialPost(
                platform="Discord",
                post_id=f"dc_{i}",
                content=f"Simulated Discord message number {i} with #discord{i} mention.",
                timestamp=datetime.now(),
                likes=random.randint(5, 200),
                retweets=0,
                comments=random.randint(0, 30)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Discord messages")
        return posts
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs; source declarations The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-04.md`](../exercises/exercise-04.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `DiscordFetcher` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `DiscordFetcher` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
