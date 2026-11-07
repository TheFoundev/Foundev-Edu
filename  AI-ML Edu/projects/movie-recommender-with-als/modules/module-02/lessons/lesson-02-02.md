# Dataset Generation, Labels, and Splits: Inspect the project implementation of dataset generation, labels, and splits

**Lesson ID:** `lesson-02-02`  
**Module:** Dataset Generation, Labels, and Splits  
**Source focus:** `src/data.py` → `load_data`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Movie Recommender with ALS. By the end, you can describe A dataset is a set of examples and target labels; this repository creates or loads the specific examples named in its README., trace the dataset generation, labels, and splits implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about A dataset is a set of examples and target labels; this repository creates or loads the specific examples named in its README.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `load_data` in `src/data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A dataset is a set of examples and target labels; this repository creates or loads the specific examples named in its README.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Ratings are simulated from genre preferences plus noise.

## Step-by-step source investigation

1. Open `src/data.py` and inspect `load_data`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/data.py` (not executed during package generation):

```python
def load_data(seed=42, quick=False):
    rng = np.random.default_rng(seed)
    n_users = 35 if quick else 70
    n_items = 30
    genres = sorted({genre for _, genre in MOVIES})
    genre_index = {genre: index for index, genre in enumerate(genres)}
    item_genre = np.array([genre_index[genre] for _, genre in MOVIES])
    user_pref = rng.normal(0, 0.7, (n_users, len(genres)))

    rows = []
    for user in range(n_users):
        for item in range(n_items):
            if rng.random() < 0.35:
                score = 3.3 + user_pref[user, item_genre[item]] + rng.normal(0, 0.7)
                rows.append((user, item, float(np.clip(score, 1, 5))))

    ratings = pd.DataFrame(rows, columns=["user_id", "item_id", "rating"])
    ratings = ratings.sample(frac=1, random_state=seed).reset_index(drop=True)
    split = int(len(ratings) * 0.8)
    movies = pd.DataFrame({
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For dataset generation, labels, and splits, use the repository's own output format and the available test fixture where possible.

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

You can now inspect the project implementation of dataset generation, labels, and splits, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `load_data` in `src/data.py`. Use the excerpt below to trace the actual inputs, transformation, and output for A dataset is a set of examples and target labels; this repository creates or loads the specific examples named in its README.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
