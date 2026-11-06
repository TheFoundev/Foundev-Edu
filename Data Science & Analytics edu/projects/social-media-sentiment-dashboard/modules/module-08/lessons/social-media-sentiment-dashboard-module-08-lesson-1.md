# A beginner's model of instagram fetcher and medium fetcher

**Lesson ID:** `social-media-sentiment-dashboard-module-08-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/fetchers/instagram_fetcher.py] and [src/fetchers/medium_fetcher.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include InstagramFetcher, __init__, get_data, MediumFetcher, __init__, get_data; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/fetchers/instagram_fetcher.py`, `src/fetchers/medium_fetcher.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/fetchers/instagram_fetcher.py`, `import random` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/instagram_fetcher.py`, `from datetime import datetime` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/instagram_fetcher.py`, `from models.social_post import SocialPost` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/instagram_fetcher.py`, `from utils import simulate_network_delay, setup_logger` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class InstagramFetcher:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, config):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_data(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/fetchers/medium_fetcher.py`, `import random` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/medium_fetcher.py`, `from datetime import datetime` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/medium_fetcher.py`, `from models.social_post import SocialPost` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/fetchers/medium_fetcher.py`, `from utils import simulate_network_delay, setup_logger` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class MediumFetcher:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self, config):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def get_data(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/fetchers/instagram_fetcher.py

```text
import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class InstagramFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Instagram API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 12 Instagram posts.
        for i in range(12):
            post = SocialPost(
                platform="Instagram",
                post_id=f"ig_{i}",
                content=f"Simulated Instagram post content number {i} featuring #insta{i} and vibrant visuals.",
                timestamp=datetime.now(),
                likes=random.randint(30, 1000),
                retweets=0,
                comments=random.randint(0, 100)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Instagram posts")
        return posts
```

### src/fetchers/medium_fetcher.py

```text
import random
from datetime import datetime
from models.social_post import SocialPost
from utils import simulate_network_delay, setup_logger

class MediumFetcher:
    def __init__(self, config):
        self.config = config
        self.logger = setup_logger(self.__class__.__name__)

    def get_data(self):
        self.logger.info("Fetching data from Medium API simulation")
        simulate_network_delay()
        posts = []
        # Simulate fetching 4 Medium articles.
        for i in range(4):
            post = SocialPost(
                platform="Medium",
                post_id=f"md_{i}",
                content=f"Simulated Medium article content number {i} discussing trends and insights #medium{i}.",
                timestamp=datetime.now(),
                likes=random.randint(50, 300),
                retweets=0,
                comments=random.randint(0, 20)
            )
            posts.append(post)
        self.logger.info(f"Fetched {len(posts)} Medium articles")
        return posts
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

This lesson ties its explanation to `src/fetchers/instagram_fetcher.py`, `src/fetchers/medium_fetcher.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
