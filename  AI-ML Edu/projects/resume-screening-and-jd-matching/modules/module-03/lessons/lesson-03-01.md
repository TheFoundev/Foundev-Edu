# Cosine Matching and Ranking: Understand similarity scores and candidate ordering

**Lesson ID:** `lesson-03-01`  
**Module:** Cosine Matching and Ranking  
**Source focus:** `src/matcher.py` → `rank_candidates`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TalentMatch Lens: Resume and Job Description Matching. By the end, you can describe similarity scores and candidate ordering, trace the cosine matching and ranking implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about similarity scores and candidate ordering. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `rank_candidates` in `src/matcher.py`. Use the excerpt below to trace the actual inputs, transformation, and output for similarity scores and candidate ordering. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.

## Step-by-step source investigation

1. Open `src/matcher.py` and inspect `rank_candidates`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/matcher.py` (not executed during package generation):

```python
def rank_candidates(
    jd_embedding: np.ndarray,
    resume_embeddings: np.ndarray,
    resume_names: list[str],
) -> list[dict]:
    """
    Scores each resume against the job description and returns them
    sorted from best match to worst match.

    Args:
        jd_embedding: Embedding vector for the job description, shape (1, dim).
        resume_embeddings: Embedding matrix for all resumes, shape (n, dim).
        resume_names: Filenames/identifiers corresponding to each resume row.

    Returns:
        List of dicts sorted by descending score:
        [{"name": str, "score": float}, ...]
    """
    # cosine_similarity expects 2D arrays; jd_embedding is already (1, dim)
    similarities = cosine_similarity(jd_embedding, resume_embeddings)[0]
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For cosine matching and ranking, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand similarity scores and candidate ordering, identify its source location, and state a limitation. The key project-specific fact is: Understand similarity scores and candidate ordering. In this repository, the claim must be grounded in the documented behavior and source paths: src/matcher.py; src/embedder.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
