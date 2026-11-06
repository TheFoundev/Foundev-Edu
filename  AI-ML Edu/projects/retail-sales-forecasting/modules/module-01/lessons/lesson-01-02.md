# Transaction Data and Business Questions: Inspect the project implementation of transaction data and business questions

**Lesson ID:** `lesson-01-02`  
**Module:** Transaction Data and Business Questions  
**Source focus:** `index.html` → `loadData`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DemandSight: Retail Sales Analytics. By the end, you can describe orders, products, region, sales, profit, trace the transaction data and business questions implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about orders, products, region, sales, profit. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `loadData` in `js/app.js`. Use the excerpt below to trace the actual inputs, transformation, and output for orders, products, region, sales, profit. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No forecasting model exists: the implementation aggregates transaction data. The ETL requires MySQL and pymysql is omitted from requirements. Seasonal prediction is an extension, not shipped behavior.

## Step-by-step source investigation

1. Open `js/app.js` and inspect `loadData`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `js/app.js` (not executed during package generation):

```javascript
async function loadData() {
  retryBtn.style.display = 'none';
  hint.style.display = 'none';
  try {
    loadMsg.textContent = 'Fetching dataset/Superstore.csv…';
    const res = await fetch(DATA_URL);
    if (!res.ok) throw new Error('HTTP ' + res.status);
    const text = await res.text();
    const grid = parseCsv(text);
    if (grid.length < 2) throw new Error('Empty dataset');
    const headers = grid[0].map(h => h.trim());
    rows = [];
    for (let i = 1; i < grid.length; i++) {
      if (grid[i].length < headers.length) continue;
      const o = {};
      for (let j = 0; j < headers.length; j++) o[headers[j]] = grid[i][j];
      const d = parseDate(o['Order Date']);
      if (!d) continue;
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For transaction data and business questions, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-02.md`](../exercises/exercise-01-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of transaction data and business questions, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `loadData` in `js/app.js`. Use the excerpt below to trace the actual inputs, transformation, and output for orders, products, region, sales, profit. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
