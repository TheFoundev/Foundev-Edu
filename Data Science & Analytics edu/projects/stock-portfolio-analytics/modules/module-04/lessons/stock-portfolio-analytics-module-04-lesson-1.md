# A beginner's model of returns and distributions

**Lesson ID:** `stock-portfolio-analytics-module-04-lesson-1`

## Purpose and learning objectives

Study the implementation in [lib/returns/returns.js] and [lib/stats/distributions.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include treatAsUTC, norminv_; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `lib/returns/returns.js`, `lib/stats/distributions.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- `function treatAsUTC(date) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function norminv_(p, extendedPrecision) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function normcdf_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function erf_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function erfc_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function calerf_(x, j) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### lib/returns/returns.js

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
* @param {Array.<number>} portfolioEquityCurve the portfolio equity curve, an array of real numbers.
* @param {Array.<date>} valuationDates the portfolio valuation dates, an array of Dates of same length as portfolioEquityCurve.
* @return {number} the compound annual growth rate of the portfolio, expressed as a percentage.
*
* @example
* cagr([1, 1.1, 1.2], [new Date("2015-12-31"), new Date("2016-12-31"), new Date("2017-12-31")]);
* // 0.095, i.e. 9.5% cagr over two years, from 31/12/2015 to 31/12/2017
*/
self.cagr = function(portfolioEquityCurve, valuationDates) {
	// Extract the initial and the final equity curve values and valuation dates
	var initialValue = portfolioEquityCurve[0];
	var initialValuationDate = valuationDates[0];
	var finalValue = portfolioEquityCurve[portfolioEquityCurve.length-1];
	var finalValuationDate = valuationDates[valuationDates.length-1];

	// Compute the number of invested calendar days and then years
	// The computation of the number of calendar days is following the algorithm
	// of Michael Liu - http://stackoverflow.com/questions/542938/how-do-i-get-the-number-of-days-between-two-dates-in-javascript
	function treatAsUTC(date) {
		var result = new Date(date);
		result.setMinutes(result.getMinutes() - result.getTimezoneOffset());
		return result;
	}
	var millisecondsPerDay = 24 * 60 * 60 * 1000;
	var nbInvestedDays = (treatAsUTC(finalValuationDate) - treatAsUTC(initialValuationDate)) / millisecondsPerDay;
	var nbInvestedYears = nbInvestedDays/365.25;

	// Compute the CAGR
	var valCagr = Math.pow(finalValue/initialValue, 1/nbInvestedYears) - 1;

	// Return the computed value
	return valCagr;
}


/**
* @function arithmeticReturns
*
* @summary Compute the period-to-period arithmetic returns of a portfolio.
*
* @description This function return
```

### lib/stats/distributions.js

```text
/**
 * @file Functions related to distributions computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */

 
/* Start Wrapper private methods - Unit tests usage only */
self.norminv_ = function(p, extendedPrecision) { return norminv_(p, extendedPrecision); }
self.normcdf_ = function(x) { return normcdf_(x); }
self.erf_ = function(x) { return erf_(x); }
self.erfc_ = function(x) { return erfc_(x); }
/* End Wrapper private methods - Unit tests usage only */


/**
* @function norminv_
*
* @summary Compute the inverse of the standard normal cumulative distribution function.
*
* @description This function returns an approximation of the inverse standard normal cumulative distribution function, i.e.
* given p in [0,1] it returns an approximation to the x value satisfying p = Pr{Z <= x} where Z is a
* random variable following a standard normal distribution law.
*
* x is also called a z-score.
*
* The algorithm uses the fact that if F^-1(p) is the inverse normal cumulative distribution function, then G^-1(p) = F^-1(p+1/2) is an odd function.
* The algorithm uses two separate rational minimax approximations: one rational approximation is used for the central region and another one is used for the tails.
* The algorithm has a relative error whose absolute value is less than 1.15e-9, but if needed, the approximation of the inverse normal cumulative distribution function can be refined better precision using Halley's method.
*
* @author Peter John Acklam <jacklam@math.uio.no>
*
* @see <a href="http://home.online.no/%7Epjacklam/notes/invnorm">http://home.online.no/%7Epjacklam/notes/invnorm</a>
* @see <a href="https://web.archive.org/web/20151030215612/http://home.online.no/%7Epjacklam/notes/invnorm/">https://web.archive.org/web/20151030215612/http://home.online.no/%7Epjacklam/notes/invnorm/</a>
* 
* @param {number} p a probability value, real number belonging to interval [0,1].
* @param {boolean} extendedPrecision an optional boolean, either false for a standard approximation (default) or true for a refined approximation.
* @return {number} an approximation to the x value satisfying p = Pr{Z <= x} where Z is a random variable following a standard normal distribution law.
*
* @example
* norminv_(0.5);
* // 0
*/
function norminv_(p, extendedPrecision) {
	// By default, standard precision is required
	if (extendedPrecision === undefined) {
		extendedPrecision = false;
	}

	// Coefficients in rational approximations.
	var a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00];
	var b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01, -1.328068155288572e+01];
	var c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00];
	var d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00];

	// Define break-points.
	var p_low = 0.02425;
	var p_high = 1 - p_low;

	// Regions definition.
	var x = NaN;
	if (p == 0.0) {
		x = Number.NEGATIVE_INFINITY;
	}
	else if (p == 1.0) {
		x = Number.POSITIVE_INFINITY;
	}
	else if (p < p_low) {
		// Rational approximation for lower region.
		var q = Math.sqrt(-2*Math.log(p));
		x =  (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) /
		((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);
	}
	else if (p > p_high) {
		// Rational approximation for upper region.
		var q  = Math.sqrt(-2*Math.log(1-p));
		x = -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) /
		((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1);
	}
	else if (p_low <= p && p <= p_high) {
		// Rational approximation for central region.
		var q = p - 0.5;
		var r = q*q;
		x = (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q /
		(((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1);
	}

	// Improve the precision, if required.
	if (extendedPrecision === true) {
		var e = 0.5 * erfc_(-x/1.4142135623730951) - p; // C
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

This lesson ties its explanation to `lib/returns/returns.js`, `lib/stats/distributions.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
