# Feature Cleaning and Scaling: Inspect the project implementation of feature cleaning and scaling

**Lesson ID:** `lesson-02-02`  
**Module:** Feature Cleaning and Scaling  
**Source focus:** `src/main_cosine_similarity.py` → `for feature in acoustic_features`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Groove Observatory: Audio Feature Music Recommendation. By the end, you can describe deduplication, case folding, and min-max normalization, trace the feature cleaning and scaling implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about deduplication, case folding, and min-max normalization. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 2. Why min-max normalisation is mandatory here

Cosine similarity is *not* scale-invariant — only rotation-invariant. If `duration` (measured in milliseconds, range 0–400+) and `valence` (0–100) are used raw, the duration coordinate dominates the dot product by two orders of magnitude and the "similarity" becomes a duration ranking. Min-max scaling `(x - min) / (max - min)` maps every feature to `[0, 1]`, making the ten dimensions commensurable and letting each contribute comparably to the angle.

The trade-off is that min-max is **outlier-sensitive**: one extreme value compresses the rest of the column into a narrow band, so that feature effectively stops discriminating. The repository does not treat or winsorise outliers.

Connect this explanation to `src/main_cosine_similarity.py` and the source focus `for feature in acoustic_features`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: This is deterministic cosine-neighbor ranking over a local 2,261-row, ten-feature catalogue, not a learned recommender. Catalog coverage and popularity bias limit results.

## Step-by-step source investigation

1. Open `src/main_cosine_similarity.py` and inspect `for feature in acoustic_features`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/main_cosine_similarity.py` (not executed during package generation):

```python
# Select Acoustic Features for Cosine Similarity
acoustic_features = ['bpm', 'energy', 'danceability ', 'dB', 'liveness', 'valence', 'duration', 'acousticness', 'speechiness ', 'popularity']

# Normalize Acoustic Features: Have all points between [-1,1]
for feature in acoustic_features:
    df[feature] = (df[feature] - df[feature].min()) / (df[feature].max() - df[feature].min())
    
# Create a vector for the selected song
selected_song_vector = df[(df['artist'] == select_artist) & (df['title'] == select_title)][acoustic_features].values

# Calculate Cosine Similarity
df['similarity'] = cosine_similarity(df[acoustic_features], selected_song_vector)

# Sort by Similarity and Recommend similar songs
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For feature cleaning and scaling, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-02.md`](../exercises/exercise-02-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of feature cleaning and scaling, identify its source location, and state a limitation. The key project-specific fact is: ### 2. Why min-max normalisation is mandatory here

Cosine similarity is *not* scale-invariant — only rotation-invariant. If `duration` (measured in milliseconds, range 0–400+) and `valence` (0–100) are used raw, the duration coordinate dominates the dot product by two orders of magnitude and the "similarity" becomes a duration ranking. Min-max scaling `(x - min) / (max - min)` maps every feature to `[0, 1]`, making the ten dimensions commensurable and letting each contribute comparably to the angle.

The trade-off is that min-max is **outlier-sensitive**: one extreme value compresses the rest of the column into a narrow band, so that feature effectively stops discriminating. The repository does not treat or winsorise outliers.

Connect this explanation to `src/main_cosine_similarity.py` and the source focus `for feature in acoustic_features`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
