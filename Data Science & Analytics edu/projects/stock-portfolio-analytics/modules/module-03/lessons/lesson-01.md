# Ratios and Sharpe Ratio: Begin with the concept

**Lesson ID:** `stock-portfolio-analytics-module-03-lesson-01`  
**Module ID:** `stock-portfolio-analytics-module-03`  
**Source focus:** `lib/ratios/ratios.js` → `gainToPainRatio`

## Purpose and learning objectives

Explain ratios and sharpe ratio in plain language using the project source.

## Prerequisites

Basic Python and source-file navigation. This module covers: Ratios and Sharpe Ratio.

## Beginner explanation

In plain language, ratios and sharpe ratio is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `lib/ratios/ratios.js` and locate `gainToPainRatio`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `lib/ratios/ratios.js`, `lib/ratios/sharpe-ratio.js`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `lib/ratios/ratios.js`. source tree absent; excerpt retained from earlier package

### lib/ratios/ratios.js

The excerpt below is the selected implementation focus.
### lib/ratios/sharpe-ratio.js

This mapped path is part of the module scope; inspect it alongside its callers and tests.

```text
/**
 * @file Functions related to performances ratios computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */


/**
* @function gainToPainRatio
*
* @summary Compute the gain to pain ratio of a portfolio.
*
* @description This function returns the gain to pain ratio of a portfolio, provided as an
* equity curve.
*
* The the gain to pain ratio is defined as the sum of all returns divided by the absolute value of the sum of all losses, c.f. the reference.
*
* From the reference, a gain to pain ratio above 1.0 is very good, and a gain to pain ratio above 1.5 is excellent.
*
* @see <a href="http://onlinelibrary.wiley.com/doi/10.1002/9781119203469.app1/summary">Hedge Fund Market Wizards: How Winning Traders Win, Jack D. Schwager, Wiley, 2012</a>
* 
* @param {Array.<number>} portfolioEquityCurve the portfolio equity curve, an array of real numbers.
* @return {number} the gain to pain ratio of the portfolio.
*
* @example
* gainToPainRatio([1, 2, 1]); 
* // 1.0 
*
* @example
* gainToPainRatio([1, 1.1, 1.4]); 
* // NaN
*/
self.gainToPainRatio = function(portfolioEquityCurve) {
	// Compute the arithmetic returns of the portfolio
	var returns = self.arithmeticReturns(portfolioEquityCurve).slice(1); // First value is NaN

	// If there is no usable returns, exit
	if (returns.length == 0) {
		return NaN;
	}

	// Else, compute the gain to pain ratio as the the sum of the returns divided by
	// the sum of the absolute values of the negative returns, c.f. the reference.
	var numerator = mean_(returns);
	var denominator = lpm_(returns, 1, 0.0);

	// Return the gain to pain ratio
	if (denominator == 0.0) {
		return NaN; // The gain to pain ratio is undefined in case there is no negative returns
	}
	else {
		return numerator/denominator;
	}
}
```

First read the signature/declared data shape; then follow the code and caller.

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

You moved from a plain-language model to `gainToPainRatio` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `gainToPainRatio` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
