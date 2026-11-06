# Read ratios and sharpe ratio in the source

**Lesson ID:** `stock-portfolio-analytics-module-03-lesson-2`

## Purpose and learning objectives

Study the implementation in [lib/ratios/ratios.js] and [lib/ratios/sharpe-ratio.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include sharpeRatioStatistics_; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `lib/ratios/ratios.js`, `lib/ratios/sharpe-ratio.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `lib/ratios/ratios.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- `function sharpeRatioStatistics_(portfolioEquityCurve, benchmarkEquityCurve) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function differentialReturns_(portfolioEquityCurve, benchmarkEquityCurve) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### lib/ratios/ratios.js

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

### lib/ratios/sharpe-ratio.js

```text
/**
 * @file Functions related to Sharpe ratio computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */

/* Start Wrapper private methods - Unit tests usage only */
self.sharpeRatioStatistics_ = function(portfolioEquityCurve, benchmarkEquityCurve) { return sharpeRatioStatistics_(portfolioEquityCurve, benchmarkEquityCurve); }
self.differentialReturns_ = function(portfolioEquityCurve, benchmarkEquityCurve) { return differentialReturns_(portfolioEquityCurve, benchmarkEquityCurve); }
/* End Wrapper private methods - Unit tests usage only */


/**
* @function sharpeRatio
*
* @summary Compute the Sharpe ratio of a portfolio v.s. a benchmark.
*
* @description This function returns the Sharpe ratio of a portfolio v.s. a benchmark, both provided as
* equity curves.
*
* The Sharpe ratio is defined as the arithmetic mean of the differential arithmetic returns 
* (arithmetic returns of portfolio minus the arithmetic returns of the benchmark), divided by the sample standard deviation 
* of these differential returns, c.f. the reference.
*
* @see <a href="http://www.iijournals.com/doi/abs/10.3905/jpm.1994.409501?journalCode=jpm">The Sharpe Ratio, William F. Sharpe, The Journal of Portfolio Management, Fall 1994, Vol. 21, No. 1: pp.49-58</a>
* 
* @param {Array.<number>} portfolioEquityCurve the portfolio equity curve, an array of real numbers.
* @param {Array.<number>} equityCurveBenchmark the benchmark equity curve, an array of real numbers of the same length as portfolioEquityCurve.
* @return {number} the Sharpe ratio of the portfolio v.s. the benchmark.
*
* @example
* sharpeRatio([100, 110, 105, 107.5, 115], [100, 100, 100, 100, 100]);
* // ~0.585
*/
self.sharpeRatio = function(portfolioEquityCurve, benchmarkEquityCurve) {
	// Compute the Sharpe ratio statistics
	var srs = sharpeRatioStatistics_(portfolioEquityCurve, benchmarkEquityCurve);
	var sr = srs[0];

	// Return the Sharpe ratio
	return sr;
}  


/**
* @function sharpeRatioStatistics_
*
* @summary Internal function intended to compute the Sharpe ratio, the Sharpe ratio variance
* and the Sharpe ratio asymptotic bias.
*
* @description This internal function returns the Sharpe ratio of a portfolio v.s. a benchmark, both provided as
* equity curves, as well as its variance and its asymptotic bias.
* 
* The Sharpe ratio is defined as the arithmetic mean of the differential arithmetic returns 
* (arithmetic returns of the portfolio minus the arithmetic returns of the benchmark), divided by the sample standard deviation 
* of these differential returns, c.f. the first reference.
*
* The Sharpe ratio asymptotic bias is computed using a factor dependant on the kurtosis of the differential returns
* of the portfolio v.s. the benchmark, c.f. the second reference.
*
* The Sharpe ratio variance is approximated through its asymptotic closed form formula, dependant on the skewness
* and on the kurtosis of these differential returns, c.f. the second reference.
*
* @see <a href="http://www.iijournals.com/doi/abs/10.3905/jpm.1994.409501?journalCode=jpm">The Sharpe Ratio, William F. Sharpe, The Journal of Portfolio Management, Fall 1994, Vol. 21, No. 1: pp.49-58</a>
* @see <a href="http://link.springer.com/article/10.1057/palgrave.jam.2250084">Comparing Sharpe ratios: So where are the p-values, J.D. Opdyke, Journal of Asset Management (2007) 8, 308–336</a>
* 
* @param {Array.<number>} portfolioEquityCurve the portfolio equity curve, an array of real numbers.
* @param {Array.<number>} benchmarkEquityCurve the benchmark equity curve, an array of real numbers of the same length as portfolioEquityCurve.
* @return {Array.<number>} the Sharpe ratio of the portfolio v.s. the benchmark, the variance of the Sharpe ratio and the
* asymptotic bias of the Sharpe ratio.
*
* @example
* sharpeRatioStatistics_([100, 110, 105, 107.5, 115], [100, 100, 100, 100, 100]);
* // [0.5851289093221407, 0.5228801702220195, 1.1019640163238367]
*/
function sharpeRatioStatistics_(portfolioEquityCurve, benchmarkEquity
```

The excerpt comes from this project’s source tree and may omit context. It is not evidence that the source was executed. Never treat a listed function name alone as proof that a user-facing path reaches it.

## Expected behavior and known limits

Only behavior visible in the cited implementation or assertions can be explained as implemented. External calls, deployment settings, successful installation, performance, and test outcomes remain unverified here.

## Practical exercise

Use the module exercise to create a call/data/configuration trace for these exact files. Include a source location for every claim.

## Common mistakes and debugging

- Reading only function names: follow bodies, callers, and return paths.
- Assuming imports prove an integration ran: inspect the call site and configuration.
- Assuming tests pass because they exist: record execution separately.
- If the path is unclear, search all references to the symbol and trace from the actual entry point.

## Best practices and security

Use synthetic fixtures and isolated environments. Redact credentials and personal data. Review validation at input boundaries, dependency declarations, and error handling before suggesting a change.

## Summary

This lesson ties its explanation to `lib/ratios/ratios.js`, `lib/ratios/sharpe-ratio.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
