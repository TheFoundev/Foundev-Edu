# Calendar Buckets and Weighted Metrics: Inspect the project implementation of calendar buckets and weighted metrics

**Lesson ID:** `lesson-03-02`  
**Module:** Calendar Buckets and Weighted Metrics  
**Source focus:** `index.html` → `wDisc`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by DemandSight: Retail Sales Analytics. By the end, you can describe monthly buckets, margin, and sales-weighted discount, trace the calendar buckets and weighted metrics implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about monthly buckets, margin, and sales-weighted discount. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `wDisc` in `js/app.js`. Use the excerpt below to trace the actual inputs, transformation, and output for monthly buckets, margin, and sales-weighted discount. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: No forecasting model exists: the implementation aggregates transaction data. The ETL requires MySQL and pymysql is omitted from requirements. Seasonal prediction is an extension, not shipped behavior.

## Step-by-step source investigation

1. Open `js/app.js` and inspect `wDisc`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `js/app.js` (not executed during package generation):

```javascript
const wDisc = filtered.reduce((s, r) => s + r._discount * r._sales, 0) / discountBase;
  document.getElementById('kpiSales').textContent = fmtMoney(sales);
  document.getElementById('kpiProfit').textContent = fmtMoney(profit);
  document.getElementById('kpiMargin').textContent = sales ? fmtPct(profit / sales) : '—';
  document.getElementById('kpiOrders').textContent = orders.toLocaleString();
  document.getElementById('kpiDiscount').textContent = fmtPct(wDisc);
  document.getElementById('kpiSalesSub').textContent = filtered.length.toLocaleString() + ' line items';
  document.getElementById('kpiProfitSub').textContent = profit >= 0 ? 'Net positive in filter' : 'Net negative in filter';
  document.getElementById('kpiOrdersSub').textContent = 'Unique Order IDs';
  renderSparkline('sparkSales', monthlySeries(filtered, '_sales').map(s => s.value), '#6ee7b7');
  renderSparkline('sparkProfit', monthlySeries(filtered, '_profit').map(s => s.value), '#93c5fd');
}

function renderSparkline(id, values, color) {
  const canvas = document.getElementById(id);
  const ctx = canvas.getContext('2d');
  const w = canvas.width = canvas.offsetWidth * 2;
  const h = canvas.height = 80;
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For calendar buckets and weighted metrics, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-02.md`](../exercises/exercise-03-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of calendar buckets and weighted metrics, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `wDisc` in `js/app.js`. Use the excerpt below to trace the actual inputs, transformation, and output for monthly buckets, margin, and sales-weighted discount. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
