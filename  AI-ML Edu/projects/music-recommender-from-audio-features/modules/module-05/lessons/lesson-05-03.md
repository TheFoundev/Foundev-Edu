# Testing and Explanation: Validate outputs and identify limitations for testing and explanation

**Lesson ID:** `lesson-05-03`  
**Module:** Testing and Explanation  
**Source focus:** `tests/test_clean_dataset.py` → `recommended_songs`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Groove Observatory: Audio Feature Music Recommendation. By the end, you can describe artist selection, cleaning, visualization, and Audio DNA, trace the testing and explanation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about artist selection, cleaning, visualization, and Audio DNA. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 6. The "Audio DNA" explanation

`showComparison()` does not call a separate explainability library — it simply re-uses the same normalised matrix to draw the seed's and the match's value for each of the ten features as paired bars. The explanation is therefore *exact* rather than approximate: it shows the numbers that produced the cosine, and lets the user see which dimensions are shared and which are not. The trade-off is that cosine itself does not decompose into per-feature contributions, so the panel shows the profile, not the per-feature contribution to the score.

Connect this explanation to `tests/test_cosine_similarity.py` and the source focus `recommended_songs`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: This is deterministic cosine-neighbor ranking over a local 2,261-row, ten-feature catalogue, not a learned recommender. Catalog coverage and popularity bias limit results.

## Step-by-step source investigation

1. Open `tests/test_cosine_similarity.py` and inspect `recommended_songs`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `tests/test_cosine_similarity.py` (not executed during package generation):

```python
recommended_songs = df.sort_values(by='similarity', ascending=False)[['title', 'artist', 'similarity']]

# Print recommended songs
print("Recommended Songs:")
print(recommended_songs.head())
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For testing and explanation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-03.md`](../exercises/exercise-05-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for testing and explanation, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for testing and explanation. In this repository, the claim must be grounded in the documented behavior and source paths: tests/test_clean_dataset.py; tests/test_cosine_similarity.py; tests/test_artist_selection.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
