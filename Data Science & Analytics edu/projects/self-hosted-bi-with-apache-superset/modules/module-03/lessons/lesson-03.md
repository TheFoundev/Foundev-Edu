# Region Share and Repeat Rate: Test the boundary

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-03-lesson-03`  
**Module ID:** `self-hosted-bi-with-apache-superset-module-03`  
**Source focus:** `sql/repeat_rate.sql` → `Repeat`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Region Share and Repeat Rate.

## Beginner explanation

In plain language, region share and repeat rate is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `sql/repeat_rate.sql` and locate `Repeat`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `sql/region_share.sql`, `sql/repeat_rate.sql`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `sql/repeat_rate.sql` at lines 1–8. Source code was not executed during refinement.

### sql/region_share.sql

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### sql/repeat_rate.sql

The excerpt below is the selected implementation focus.

```sql
SELECT
    ROUND(100.0 * SUM(CASE WHEN orders > 1 THEN 1 ELSE 0 END) / COUNT(*), 1) AS repeat_rate
FROM (
    SELECT customer_id, COUNT(*) AS orders
    FROM orders
    WHERE status = 'paid'
    GROUP BY customer_id
)
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-03.md`](../exercises/exercise-03.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `Repeat` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `Repeat` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
