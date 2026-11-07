# Test code and evidence boundaries: Trace the code

**Lesson ID:** `reddit-social-media-analytics-with-praw-module-03-lesson-02`  
**Module ID:** `reddit-social-media-analytics-with-praw-module-03`  
**Source focus:** `tests/test_pipeline.py` → `test_the_sentiment_understands_a_negation`

## Purpose and learning objectives

Trace `test_the_sentiment_understands_a_negation` in `tests/test_pipeline.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Test code and evidence boundaries.

## Beginner explanation

In plain language, test code and evidence boundaries is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `tests/test_pipeline.py` and locate `test_the_sentiment_understands_a_negation`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `tests/test_pipeline.py`, `src/pipeline.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `tests/test_pipeline.py` at lines 28–48. Source code was not executed during refinement.

### tests/test_pipeline.py

The excerpt below is the selected implementation focus.
### src/pipeline.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```py
assert capsys.readouterr().out.strip()


def test_the_sentiment_understands_a_negation():
    """A negation has to change the sign of the sentiment."""
    assert sentiment("this is great and useful") > 0
    assert sentiment("this is confusing and broken") < 0
    assert sentiment("this is not good at all") < 0
    assert sentiment("") == 0


def test_the_sentiment_has_a_label():
    assert sentiment_label(0.8) == "positive"
    assert sentiment_label(-0.8) == "negative"
    assert sentiment_label(0.0) == "neutral"


def test_the_lexicon_fallback_still_works():
    assert sentiment_from_lexicon("great helpful") == 1.0
    assert sentiment_from_lexicon("confusing broken") == -1.0
    assert sentiment_from_lexicon("hello") == 0.0
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

test assertions; fixtures; limits of test evidence The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `test_the_sentiment_understands_a_negation` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `test_the_sentiment_understands_a_negation` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
