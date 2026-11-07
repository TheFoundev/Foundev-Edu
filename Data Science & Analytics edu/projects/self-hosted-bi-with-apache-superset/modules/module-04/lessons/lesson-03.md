# Top Products: Test the boundary

**Lesson ID:** `self-hosted-bi-with-apache-superset-module-04-lesson-03`  
**Module ID:** `self-hosted-bi-with-apache-superset-module-04`  
**Source focus:** `sql/top_products.sql` → `its`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Top Products.

## Beginner explanation

In plain language, top products is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `sql/top_products.sql` and locate `its`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `sql/top_products.sql`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `sql/top_products.sql` at lines 1–9. Source code was not executed during refinement.

### sql/top_products.sql

The excerpt below is the selected implementation focus.

```sql
SELECT
    product,
    SUM(quantity) AS units,
    ROUND(SUM(quantity * unit_price), 2) AS revenue
FROM orders
WHERE status = 'paid'
GROUP BY product
ORDER BY revenue DESC
LIMIT 5
```

Use the test or boundary to separate checked behavior from real-world performance, deployment, or provider claims.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-04.md`](../exercises/exercise-04.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `its` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `its` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
