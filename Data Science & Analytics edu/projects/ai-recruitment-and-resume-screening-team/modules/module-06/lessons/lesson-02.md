# Code review and safe change 6: Trace the code

**Lesson ID:** `ai-recruitment-and-resume-screening-team-module-06-lesson-02`  
**Module ID:** `ai-recruitment-and-resume-screening-team-module-06`  
**Source focus:** `src/model.py` → `rank_candidates`

## Purpose and learning objectives

Trace `rank_candidates` in `src/model.py` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Code review and safe change 6.

## Beginner explanation

In plain language, code review and safe change 6 is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `src/model.py` and locate `rank_candidates`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `app.py`, `main.py`, `src/data.py`, `src/model.py`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: call graph; failure cases; safe extension

**Excerpt:** `src/model.py` at lines 144–164. Source code was not executed during refinement.

### app.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### main.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/data.py

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### src/model.py

The excerpt below is the selected implementation focus.

```py
}


def rank_candidates(model, data):
    """The candidates of the test set, the best first."""
    rows = [resume_features(resume) for resume in data["test"]]
    matrix = _matrix(rows, model["vectorizer"])
    scores = model["classifier"].predict_proba(matrix)[:, 1]
    order = np.argsort(scores)[::-1]
    return [(data["test"][int(index)], float(scores[index])) for index in order]


def demo(data):
    model, metrics = train(data, quick=True)
    ranked = rank_candidates(model, data)
    print("Ranked candidates:")
    for resume, score in ranked[:4]:
        print(f"  {resume['name']:14s} score={score:.2f} skills={','.join(resume['skills'][:4])}")
    print(f"Shortlist precision: {metrics['precision']:.2f}, recall: {metrics['recall']:.2f}")

    print("\nQuestions for the interview of the first candidate:")
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

call graph; failure cases; safe extension The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-06.md`](../exercises/exercise-06.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `rank_candidates` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `rank_candidates` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
