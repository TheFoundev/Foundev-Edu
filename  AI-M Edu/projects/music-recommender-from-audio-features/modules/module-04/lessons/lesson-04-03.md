# API and Dataset Flow: Validate outputs and identify limitations for api and dataset flow

**Lesson ID:** `lesson-04-03`  
**Module:** API and Dataset Flow  
**Source focus:** `src/api.py` → `recommend`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Groove Observatory: Audio Feature Music Recommendation. By the end, you can describe 2261 rows, ten features, Flask endpoints, and static UI, trace the api and dataset flow implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about 2261 rows, ten features, Flask endpoints, and static UI. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 1. Content-based filtering as geometry

Each track is a point `x ∈ ℝ¹⁰` — one coordinate per acoustic feature. "Sounds like" becomes "is close to". The catalogue of 2,261 points is a cloud; the seed is a query point; the answer is the neighbourhood.

The choice of distance function is the whole design decision, and cosine similarity is chosen for two specific reasons:

- **Magnitude invariance.** Cosine compares *direction*, not length. A track that is uniformly "louder" on every axis (higher bpm *and* higher energy *and* higher valence) keeps the same similarity to the seed regardless of the overall scale. For audio, where absolute levels vary wildly across genres and eras, that is exactly the right behaviour: we want "same shape of track", not "same numeric size".
- **Non-negative, bounded features.** After min-max scaling every coordinate lies in `[0, 1]`, so the vectors live in the non-negative orthant. The angle between two such vectors is bounded and interpretable, and the dot product is never negative.

The formula, as implemented in `js/app.js` and equivalent to `sklearn.

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `src/api.py` and the source focus `recommend`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: This is deterministic cosine-neighbor ranking over a local 2,261-row, ten-feature catalogue, not a learned recommender. Catalog coverage and popularity bias limit results.

## Step-by-step source investigation

1. Open `src/api.py` and inspect `recommend`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/api.py` (not executed during package generation):

```python
def recommend():
    payload = request.get_json(silent=True) or {}
    artist = payload.get("artist")
    title = payload.get("title")
    if not artist or not title:
        return jsonify({"error": "'artist' and 'title' are required"}), 400
    limit = int(payload.get("limit", 10))
    limit = max(1, min(limit, 50))
    exclude_self = bool(payload.get("excludeSelf", True))

    seed = find_seed(str(artist), str(title))
    if seed is None:
        return jsonify({"error": "Song not found for that artist"}), 404

    seed_idx = DATA.index.get_loc(seed.name)
    sims = cosine_similarity(MATRIX[seed_idx:seed_idx + 1], MATRIX)[0]
    order = sims.argsort()[::-1]

    recommendations = []
    for idx in order:
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For api and dataset flow, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-03.md`](../exercises/exercise-04-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for api and dataset flow, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for api and dataset flow. In this repository, the claim must be grounded in the documented behavior and source paths: src/api.py; index.html; js/app.js.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
