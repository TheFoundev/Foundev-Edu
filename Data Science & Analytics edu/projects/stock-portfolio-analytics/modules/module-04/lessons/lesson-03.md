# Returns and Distributions: Test the boundary

**Lesson ID:** `stock-portfolio-analytics-module-04-lesson-03`  
**Module ID:** `stock-portfolio-analytics-module-04`  
**Source focus:** `lib/returns/returns.js` → `cumulativeReturn`

## Purpose and learning objectives

Use a test or boundary case to assess what the implementation proves and what remains unverified.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Returns and Distributions.

## Beginner explanation

In plain language, returns and distributions is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `lib/returns/returns.js` and locate `cumulativeReturn`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `lib/returns/returns.js`, `lib/stats/distributions.js`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `lib/returns/returns.js`. source tree absent; excerpt retained from earlier package

### lib/returns/returns.js

The excerpt below is the selected implementation focus.
### lib/stats/distributions.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
/**
 * @file Functions related to returns computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */


/**
* @function cumulativeReturn
*
* @summary Compute the cumulative return of a portfolio.
*
* @description This function returns the cumulative return of a portfolio, provided as an
* equity curve.
*
* The cumulative return of a portfolio is defined as its rate of return over the period
* on which it is provided, c.f. the reference.
*
* @see <a href="https://en.wikipedia.org/wiki/Rate_of_return">https://en.wikipedia.org/wiki/Rate_of_return</a>
* 
* @param {Array.<number>} portfolioEquityCurve the portfolio equity curve, an array of real numbers.
* @return {number} the cumulative return of the portfolio, expressed as a percentage.
*
* @example
* cumulativeReturn([1, 2, 1]); 
* // 0.0, i.e. 0% return over the period
*
* @example
* cumulativeReturn([1, 2, 2]);
* // 1, i.e. 100% return over the period
*/
self.cumulativeReturn = function(portfolioEquityCurve) {
	// Compute the cumulative return
	var cumRet = NaN;
	if (portfolioEquityCurve.length >= 2) { // In order to compute a proper cumulative return, at least 2 periods are required
		cumRet = (portfolioEquityCurve[portfolioEquityCurve.length-1] - portfolioEquityCurve[0])/portfolioEquityCurve[0];
	}

	// Return it
	return cumRet;
}


/**
* @function cagr
*
* @summary Compute the compound annual growth rate of a portfolio.
*
* @description This function returns compound annual growth rate of a portfolio, provided as an
* equity curve together with its associated valuation dates.
*
* The compound annual growth rate of a portfolio is defined as the geometric progression ratio
* that provides a constant rate of return over the period on which the portfolio valuations are provided, c.f. the reference.
*
* The algorithm automatically computes the number of (calendar) days between the first portfolio valuation date
* and the last portfolio valuation date, which is then converted into a number of years for the cagr computation following the
* formula of the reference.
*
* @see <a href="https://en.wikipedia.org/wiki/Compound_annual_growth_rate">https://en.wikipedia.org/wiki/Compound_annual_growth_rate</a>
* 
*
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

You moved from a plain-language model to `cumulativeReturn` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `cumulativeReturn` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
