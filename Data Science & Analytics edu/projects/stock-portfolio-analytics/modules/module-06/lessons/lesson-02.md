# Test code and evidence boundaries: Trace the code

**Lesson ID:** `stock-portfolio-analytics-module-06-lesson-02`  
**Module ID:** `stock-portfolio-analytics-module-06`  
**Source focus:** `test/drawdowns/tests_dev.js` → `tests_dev`

## Purpose and learning objectives

Trace `tests_dev` in `test/drawdowns/tests_dev.js` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Test code and evidence boundaries.

## Beginner explanation

In plain language, test code and evidence boundaries is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `test/drawdowns/tests_dev.js` and locate `tests_dev`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `test/drawdowns/tests_dev.js`, `test/drawdowns/tests_dist.js`, `test/ratios/test_sharpe-ratios_dev.js`, `test/ratios/tests_dist.js`, `Gruntfile.js`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: test assertions; fixtures; limits of test evidence

**Excerpt:** `test/drawdowns/tests_dev.js`. source tree absent; excerpt retained from earlier package

### test/drawdowns/tests_dev.js

The excerpt below is the selected implementation focus.
### test/drawdowns/tests_dist.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### test/ratios/test_sharpe-ratios_dev.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### test/ratios/tests_dist.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.
### Gruntfile.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
// ------------------------------------------------------------
QUnit.module('Drawdowns internal module', {
  before: function() {
    // Coming from "Ambiguity in Calculating and Interpreting Maximum Drawdown, Research Note, Andreas Steiner Consulting GmbH, December 2010"
	this.complexEquityCurve = [60, 40, 80, 140, 100, 90, 110, 70, 100, 130, 110, 120, 90, 150, 120, 130];
  }
});


QUnit.test('Max drawdown internal computation', function(assert) {    
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_([100], 0, 0), 
                                                   [0, 0, 0], 
                                                   'No max drawdown #1');
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_([100, 110], 0, 1), 
                                                   [0, 0, 0], 
                                                   'No max drawdown #1');
                                                    
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_([100, 90], 0, 1), 
                                                   [0.1, 0, 1], 
                                                   'Simple max drawdown #1');
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_([100, 90, 80], 0, 2), 
                                                   [0.2, 0, 2], 
                                                   'Simple max drawdown #2');

 assert.deepEqual(PortfolioAnalytics.maxDrawdown_([100, 150, 75, 150, 75], 0, 4), 
                                                   [0.5, 1, 2], 
                                                   'Ties in max drawdown');  
												   
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_(this.complexEquityCurve, 0, this.complexEquityCurve.length-1), 
                                                   [0.5, 3, 7], 
                                                   'Complex max drawdown #1');
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_(this.complexEquityCurve, 0, 2), 
                                                   [0.33333333333333333, 0, 1], 
                                                   'Complex max drawdown #2');
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_(this.complexEquityCurve, 7, this.complexEquityCurve
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

test assertions; fixtures; limits of test evidence The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

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

You moved from a plain-language model to `tests_dev` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `tests_dev` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
