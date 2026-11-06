# Music Recommendation Rules: Inspect the project implementation of music recommendation rules

**Lesson ID:** `lesson-04-02`  
**Module:** Music Recommendation Rules  
**Source focus:** `backend/app.py` → `get_music_by_emotion`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by MoodTunes: Emotion Detection and Music Recommendation. By the end, you can describe deterministic mapping from labels to tracks, trace the music recommendation rules implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about deterministic mapping from labels to tracks. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### The recommendation algorithm (not machine learning)

`get_music_by_emotion()` is a deterministic, non-learning pipeline:

1. **Query construction** — for `language == "Any"` (or blank) it uses the curated
   `EMOTION_QUERIES` table (`happy → "happy upbeat pop"`, `sad → "sad emotional"`,
   `angry → "heavy aggressive"`, `neutral → "chill relaxing acoustic"`, `surprise → "feel
   good party"`, `fear → "calming peaceful"`, `disgust → "moody atmospheric"`). For a
   specific region it switches to deliberately simple keywords
   (`happy → "happy"`, `neutral → "relaxing"`, `disgust → "lofi"`) and composes
   `"{language} {keyword} songs"`. The code comment explains why: richer English genre
   words make the search engine prioritise English results and ignore the requested
   language.
2. **Cache lookup** — `GET yt_cache:{emotion}:{language_lower_underscored}` from Redis.
   A hit returns the stored JSON verbatim and skips the network entirely.
3. **Search** — `DDGS().videos(f"site:youtube.com {query}", max_results=limit)` (default
   `limit=5`).
4. **Extraction** — for each result, th

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `backend/app.py` and the source focus `get_music_by_emotion`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The expected face weights are absent and training provenance is unavailable. Facial/text emotion labels are uncertain and sensitive; no mood inference should be treated as fact.

## Step-by-step source investigation

1. Open `backend/app.py` and inspect `get_music_by_emotion`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `backend/app.py` (not executed during package generation):

```python
def get_music_by_emotion(emotion: str, limit: int = 5, language: str = "Any"):
    """Search YouTube for songs matching the detected emotion, customized by language."""
    
    # If a specific local region/language is selected, we MUST use very simple keywords.
    # Otherwise, YouTube's NLP engine will prioritize English genres (e.g. "pop", "acoustic") and ignore the language.
    if language and language.strip() and language.lower() != "any":
        simplified_keywords = {
            "happy":    "happy",
            "sad":      "sad",
            "angry":    "angry",
            "neutral":  "relaxing",
            "surprise": "party",
            "fear":     "calming",
            "disgust":  "lofi",
        }
        keyword = simplified_keywords.get(emotion, emotion)
        query = f"{language} {keyword} songs"
    else:
        # Default global English-focused queries
        query = EMOTION_QUERIES.get(emotion, "top music")
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For music recommendation rules, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-02.md`](../exercises/exercise-04-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of music recommendation rules, identify its source location, and state a limitation. The key project-specific fact is: ### The recommendation algorithm (not machine learning)

`get_music_by_emotion()` is a deterministic, non-learning pipeline:

1. **Query construction** — for `language == "Any"` (or blank) it uses the curated
   `EMOTION_QUERIES` table (`happy → "happy upbeat pop"`, `sad → "sad emotional"`,
   `angry → "heavy aggressive"`, `neutral → "chill relaxing acoustic"`, `surprise → "feel
   good party"`, `fear → "calming peaceful"`, `disgust → "moody atmospheric"`). For a
   specific region it switches to deliberately simple keywords
   (`happy → "happy"`, `neutral → "relaxing"`, `disgust → "lofi"`) and composes
   `"{language} {keyword} songs"`. The code comment explains why: richer English genre
   words make the search engine prioritise English results and ignore the requested
   language.
2. **Cache lookup** — `GET yt_cache:{emotion}:{language_lower_underscored}` from Redis.
   A hit returns the stored JSON verbatim and skips the network entirely.
3. **Search** — `DDGS().videos(f"site:youtube.com {query}", max_results=limit)` (default
   `limit=5`).
4. **Extraction** — for each result, th

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `backend/app.py` and the source focus `get_music_by_emotion`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
