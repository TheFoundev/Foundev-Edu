# A beginner's model of sentiment analysis and trend analysis

**Lesson ID:** `social-media-sentiment-dashboard-module-04-lesson-1`

## Purpose and learning objectives

Study the implementation in [src/analytics/sentiment_analysis.py] and [src/analytics/trend_analysis.py]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include SentimentAnalyzer, __init__, analyze, analyze_posts_sentiment, sentiment_distribution, extract_hashtags, compute_trending_topics; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `src/analytics/sentiment_analysis.py`, `src/analytics/trend_analysis.py`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- In `src/analytics/sentiment_analysis.py`, `import nltk` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/sentiment_analysis.py`, `from nltk.sentiment import SentimentIntensityAnalyzer` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/sentiment_analysis.py`, `from models.social_post import SocialPost` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/sentiment_analysis.py`, `from utils import setup_logger` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `class SentimentAnalyzer:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def __init__(self):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def analyze(self, text: str) -> float:` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def analyze_posts_sentiment(posts):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def sentiment_distribution(posts):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- In `src/analytics/trend_analysis.py`, `import re` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/trend_analysis.py`, `from collections import Counter` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/trend_analysis.py`, `from models.social_post import SocialPost` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- In `src/analytics/trend_analysis.py`, `from utils import setup_logger` brings a module or package name into this file; follow later references before claiming it is used on a running path.
- `def extract_hashtags(text):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `def compute_trending_topics(posts, top_n=5):` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### src/analytics/sentiment_analysis.py

```text
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from models.social_post import SocialPost
from utils import setup_logger

# Ensure that VADER lexicon is available.
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.logger = setup_logger(self.__class__.__name__)

    def analyze(self, text: str) -> float:
        """
        Analyze the sentiment of the given text and return the compound score.
        """
        self.logger.info("Analyzing sentiment for text.")
        scores = self.analyzer.polarity_scores(text)
        return scores['compound']

def analyze_posts_sentiment(posts):
    """
    Apply sentiment analysis to a list of SocialPost objects.
    """
    analyzer = SentimentAnalyzer()
    for post in posts:
        post.sentiment = analyzer.analyze(post.content)
    return posts

def sentiment_distribution(posts):
    """
    Compute sentiment distribution over a list of posts.
    Returns a dictionary with counts for negative, neutral and positive sentiments.
    """
    distribution = {"negative": 0, "neutral": 0, "positive": 0}
    for post in posts:
        score = post.sentiment
        if score < -0.05:
            distribution["negative"] += 1
        elif score > 0.05:
            distribution["positive"] += 1
        else:
            distribution["neutral"] += 1
    return distribution
```

### src/analytics/trend_analysis.py

```text
import re
from collections import Counter
from models.social_post import SocialPost
from utils import setup_logger

def extract_hashtags(text):
    """
    Extract all hashtags from the provided text.
    """
    return re.findall(r"#(\w+)", text)

def compute_trending_topics(posts, top_n=5):
    """
    Compute the top N trending topics based on hashtags found in the posts.
    """
    logger = setup_logger("TrendAnalysis")
    logger.info("Computing trending topics from posts.")
    hashtags = []
    for post in posts:
        hashtags.extend(extract_hashtags(post.content))
    counter = Counter(hashtags)
    trending = counter.most_common(top_n)
    logger.info(f"Trending topics computed: {trending}")
    return trending
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

This lesson ties its explanation to `src/analytics/sentiment_analysis.py`, `src/analytics/trend_analysis.py`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
