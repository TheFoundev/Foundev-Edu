# Evaluation, Fairness, and Human Oversight: Understand proxy bias, missing context, privacy, and non-decision use

**Lesson ID:** `lesson-06-01`  
**Module:** Evaluation, Fairness, and Human Oversight  
**Source focus:** `PROJECT_OVERVIEW.md` → `generate_explanation`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TalentMatch Lens: Resume and Job Description Matching. By the end, you can describe proxy bias, missing context, privacy, and non-decision use, trace the evaluation, fairness, and human oversight implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about proxy bias, missing context, privacy, and non-decision use. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `generate_explanation` in `src/explainer.py`. Use the excerpt below to trace the actual inputs, transformation, and output for proxy bias, missing context, privacy, and non-decision use. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.

## Step-by-step source investigation

1. Open `src/explainer.py` and inspect `generate_explanation`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/explainer.py` (not executed during package generation):

```python
def generate_explanation(jd_skills: set, resume_skills: set, similarity_score: float) -> dict:
    """
    Compares the skill sets of the JD and a resume, and builds a
    structured explanation.

    Args:
        jd_skills: Set of skills extracted from the job description.
        resume_skills: Set of skills extracted from this resume.
        similarity_score: Cosine similarity score (0 to 1) for this resume.

    Returns:
        A dictionary containing:
        - matched_skills: skills present in both JD and resume
        - missing_skills: skills required by JD but absent in resume
        - extra_skills: skills in resume not mentioned in JD (bonus skills)
        - skill_match_percentage: % of JD skills that were matched
        - summary: a plain-English one-line summary
    """
    matched_skills = sorted(jd_skills.intersection(resume_skills))
    missing_skills = sorted(jd_skills.difference(resume_skills))
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, fairness, and human oversight, use the repository's own output format and the available test fixture where possible.

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

You can now understand proxy bias, missing context, privacy, and non-decision use, identify its source location, and state a limitation. The key project-specific fact is: Understand proxy bias, missing context, privacy, and non-decision use. In this repository, the claim must be grounded in the documented behavior and source paths: PROJECT_OVERVIEW.md; src/explainer.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
