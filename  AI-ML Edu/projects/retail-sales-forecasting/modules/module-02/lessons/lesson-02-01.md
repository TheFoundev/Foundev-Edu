# ETL and SQL Aggregation: Understand database loading, group/sum/mean, and query scripts

**Lesson ID:** `lesson-02-01`  
**Module:** ETL and SQL Aggregation  
**Source focus:** `sql/retail_analysis.sql` → `SELECT`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DemandSight: Retail Sales Analytics. By the end, you can describe database loading, group/sum/mean, and query scripts, trace the etl and sql aggregation implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about database loading, group/sum/mean, and query scripts. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

No ML model exists in this project. The core processing is deterministic aggregation:
groupBy + sum/mean over filtered rows, monthly bucketing by calendar month, and a sales-weighted
discount mean (`Σ(discount·sales)/Σ(sales)`). Margin % is `profit/sales`. Sub-category profitability
is a signed sum of profit used for diverging bars.

Connect this explanation to `sql/retail_analysis.sql` and the source focus `SELECT`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No forecasting model exists: the implementation aggregates transaction data. The ETL requires MySQL and pymysql is omitted from requirements. Seasonal prediction is an extension, not shipped behavior.

## Step-by-step source investigation

1. Open `sql/retail_analysis.sql` and inspect `SELECT`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `sql/retail_analysis.sql` (not executed during package generation):

```sql
-- SALES ANALYSIS QUERIES

-- Top 10 Cities by Total Sales
SELECT City, ROUND(SUM(Sales), 2) AS Total_Sales
FROM sales_data
GROUP BY City
ORDER BY Total_Sales DESC
LIMIT 10;

-- Monthly Sales Trend (Year-Wise)
SELECT 
  `Order Year`, 
  `Order Month`,
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For etl and sql aggregation, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-01.md`](../exercises/exercise-02-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand database loading, group/sum/mean, and query scripts, identify its source location, and state a limitation. The key project-specific fact is: Understand database loading, group/sum/mean, and query scripts. In this repository, the claim must be grounded in the documented behavior and source paths: sql/retail_analysis.sql; run_all_queries.py; app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
