# Inference, Demo, and User Interface: Understand Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.

**Lesson ID:** `lesson-06-01`  
**Module:** Inference, Demo, and User Interface  
**Source focus:** `web/api_impl.py` → `summary`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Movie Recommender with ALS. By the end, you can describe Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result., trace the inference, demo, and user interface implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `summary` in `web/api_impl.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: Ratings are simulated from genre preferences plus noise.

## Step-by-step source investigation

1. Open `web/api_impl.py` and inspect `summary`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with the source `README.md` and nearby implementation; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `web/api_impl.py` (not executed during package generation):

```python
def summary():
    data, model, metrics = _state()
    movies = data["movies"]
    recommendations = _recommendations(data, model, 0)

    # The mean of the training ratings per genre, straight from the data.
    merged = data["train"].merge(movies, left_on="item_id", right_on="item_id")
    per_genre = merged.groupby("genre")["rating"].agg(["count", "mean"]).reset_index()
    per_genre = per_genre.sort_values("count", ascending=False)

    return {
        "stats": {
            "movies": int(data["n_items"]),
            "users": int(data["n_users"]),
            "ratings": int(len(data["train"]) + len(data["test"])),
            "precision_at_5": metrics["precision_at_5"],
        },
        "series": [
            {"label": row["title"], "value": row["predicted"]}
            for row in recommendations
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For inference, demo, and user interface, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-01.md`](../exercises/exercise-06-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result., identify its source location, and state a limitation. The key project-specific fact is: Understand Inference means applying the trained or configured method to a new input; a user interface is only the path that sends that input and displays the result.. In this repository, the claim must be grounded in the documented behavior and source paths: web/api_impl.py; main.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository `README.md` and cited code files (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
