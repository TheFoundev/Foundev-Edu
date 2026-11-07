# Moments: Trace the code

**Lesson ID:** `stock-portfolio-analytics-module-05-lesson-02`  
**Module ID:** `stock-portfolio-analytics-module-05`  
**Source focus:** `lib/stats/moments.js` → `hpm_`

## Purpose and learning objectives

Trace `hpm_` in `lib/stats/moments.js` and explain its inputs, behavior, and output.

## Prerequisites

Complete the earlier lesson in this module first. This module covers: Moments.

## Beginner explanation

In plain language, moments is one stage in turning source data into a result. This is a mental model, not a claim that every named source component uses a production-grade implementation.

## Step-by-step source reading

1. Open `lib/stats/moments.js` and locate `hpm_`.
2. Identify its input and returned, stored, displayed, or emitted output.
3. Follow one caller/test into a related source path: `lib/stats/moments.js`.
4. Compare that path with the source README, test fixtures, and documented limitations.

## Source evidence

The selected source finding is: source declarations; imports and callers; inputs and outputs

**Excerpt:** `lib/stats/moments.js`. source tree absent; excerpt retained from earlier package

### lib/stats/moments.js

The excerpt below is the selected implementation focus.

```text
/**
 * @file Functions related to moments computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */

/* Start Wrapper private methods - Unit tests usage only */
self.hpm_ = function(x, n, t) { return hpm_(x, n, t); }
self.lpm_ = function(x, n, t) { return lpm_(x, n, t); }
self.mean_ = function(x) { return mean_(x); }
self.variance_ = function(x) { return variance_(x); }
self.covariance_ = function(x,y) { return covariance_(x,y); }
self.stddev_ = function(x) { return stddev_(x); }
self.sampleStddev_ = function(x) { return sampleStddev_(x); }
self.sampleVariance_ = function(x) { return sampleVariance_(x); }
self.sampleCovariance_ = function(x,y) { return sampleCovariance_(x,y); }
self.skewness_ = function(x) { return skewness_(x); }
self.sampleSkewness_ = function(x) { return sampleSkewness_(x); }
self.kurtosis_ = function(x) { return kurtosis_(x); }
self.sampleKurtosis_ = function(x) { return sampleKurtosis_(x); }
self.sampleMoments_ = function(x) { return sampleMoments_(x); }
/* End Wrapper private methods - Unit tests usage only */
 
 
/**
* @function hpm_
*
* @summary Compute the higher partial moment of a serie of values.
*
* @description This function returns the n-th order higher partial moment of a serie of values [x_1,...,x_p] with respect to a threshold t, 
* which is defined as the arithmetic mean of the p values max(0, x_1-t)^n,...,max(0, x_p-t)^n.
*  
* @see <a href="https://en.wikipedia.org/wiki/Moment_(mathematics)">https://en.wikipedia.org/wiki/Moment_(mathematics)</a>
* 
* @param {Array.<number>} x an array of real numbers.
* @param {number} n the order of the higher partial moment, a positive integer.
* @param {number} t the threshold of the higher partial moment, a real number
* @return {number} the n-th order higher partial moment of the values of the array x with respect to the threshold t.
*
* @example
* hpm_([0.1,-0.2,-0.3], 2, 0.0); 
* // 0.0167
*/
function hpm_(x, n, t) {
	// Code below is adapted from a mean computation, c.f. mean_ function
	// Initialisations
	var nn = x.length;

	// First pass of the mean computation
	var tmpMean = 0.0;
	var sum = 0.0;
	for (var i=0; i<nn; ++i) {
		sum += Math.pow(Math.max(0, x[i]-t), n);
	}
```

Trace branches and transformations. Do not infer runtime success from a declaration alone.

## Expected behavior and limits

source declarations; imports and callers; inputs and outputs The repository’s README notes and tests are part of the scope; no application execution is claimed by this package.

## Practical exercise

Complete [`exercise-05.md`](../exercises/exercise-05.md). Cite the focus symbol and source path, record an expected result, and describe one edge case.

## Common mistakes and debugging

- Confusing the repository’s title or project brief with the implementation that is present.
- Treating a test definition as evidence that the test passed.
- Ignoring sample-data, small-dataset, synthetic-input, or runtime limitations.
- Follow the focus symbol through its caller before drawing conclusions.

## Best practices and security

Use non-sensitive test data, protect credentials, document split and metric assumptions, and do not present synthetic results as production performance. For hiring, public policy, finance, health, or personal data, require qualified human review.

## Summary

You moved from a plain-language model to `hpm_` in the source and identified one verification boundary.

## Knowledge checks

1. What input does this stage receive?
2. What does `hpm_` change, return, or measure?
3. What limitation would you report before using the result outside this sample?

## References

- [Package README](../../../README.md)
- Source project files listed in module.json (relative to the Data Science & Analytics source tree).
