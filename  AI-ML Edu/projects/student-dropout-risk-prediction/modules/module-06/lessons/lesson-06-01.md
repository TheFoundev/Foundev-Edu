# Privacy, Fairness, and Supportive Use: Understand student privacy, bias, intervention support, and human review

**Lesson ID:** `lesson-06-01`  
**Module:** Privacy, Fairness, and Supportive Use  
**Source focus:** `db_creation/add_dropout_column.sql` → `dropout`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DEWS: Student Dropout Risk Prediction. By the end, you can describe student privacy, bias, intervention support, and human review, trace the privacy, fairness, and supportive use implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about student privacy, bias, intervention support, and human review. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `dropout` in `db_creation/add_dropout_column.sql`. Use the excerpt below to trace the actual inputs, transformation, and output for student privacy, bias, intervention support, and human review. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The UI is a demo; the historical pipeline scripts are documented as mostly broken/legacy. Labels are an administrative rule. Risk scores must support voluntary services, not punitive decisions.

## Step-by-step source investigation

1. Open `db_creation/add_dropout_column.sql` and inspect `dropout`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `db_creation/add_dropout_column.sql` (not executed during package generation):

```sql
ALTER TABLE cohort1_all
ADD COLUMN dropout int,
ADD COLUMN g6_dropout int,
ADD COLUMN g7_dropout int,
ADD COLUMN g8_dropout int,
ADD COLUMN g9_dropout int,
ADD COLUMN g10_dropout int,
ADD COLUMN g11_dropout int,
ADD COLUMN g12_dropout int;

UPDATE cohort1_all
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For privacy, fairness, and supportive use, use the repository's own output format and the available test fixture where possible.

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

You can now understand student privacy, bias, intervention support, and human review, identify its source location, and state a limitation. The key project-specific fact is: Understand student privacy, bias, intervention support, and human review. In this repository, the claim must be grounded in the documented behavior and source paths: db_creation/add_dropout_column.sql; pipeline/__6_Evaluate.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
