# Read moments in the source

**Lesson ID:** `stock-portfolio-analytics-module-05-lesson-2`

## Purpose and learning objectives

Study the implementation in [lib/stats/moments.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include hpm_, lpm_; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `lib/stats/moments.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- `function hpm_(x, n, t) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function lpm_(x, n, t) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function mean_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function variance_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function sampleVariance_(x) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.
- `function covariance_(x, y) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### lib/stats/moments.js

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
	tmpMean = sum/nn;

	// Second pass of the mean computation
	var sum2 = 0.0;
	for (var i=0; i<nn; ++i) {
		sum2 += (Math.pow(Math.max(0, x[i]-t), n) - tmpMean);
	}

	// Corrected computed mean
	return (sum + sum2)/nn;
}


/**
* @function lpm_
*
* @summary Compute the lower partial moment of a serie of values.
*
* @description This function returns the n-th order lower partial moment of a serie of values [x_1,...,x_p] with respect to a threshold t, 
* which is defined as the arithmetic mean of the p values max(0, t-x_1)^n,...,max(0, t-x_p)^n.
*  
* @see <a href="https://en.wikipedia.org/wiki/Moment_(mathematics)">https://en.wikipedia.org/wiki/Moment_(mathematics)</a>
* 
* @param {Array.<number>} x an array of real numbers.
* @param {number} n the order of the lower partial moment, a positive integer.
* @param {number} t the threshold of the lower partial moment, a real number.
* @return {number} the n-th order lower partial moment of the values of the array x with respect to the threshold t.
*
* @example
* lpm_([0.1,0.2,-0.3], 2, 0.0); 
* // 0.03
*/
function lpm_(x, n, t) {
	// Code below is adapted from a mean computation, c.f. mean_ function
	// Initialisations
	var nn = x.length;

	// First pass of the mean computation
	var tmpMean = 0.0;
	var sum = 0.0;
	for (var i=0; i<nn; ++i) {
		sum += Math.pow(Math.max(0, t-x[i]), n);
	}
	tmpMean = sum/nn;

	// Second pass of the mean computation
	var sum2 = 0.0;
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

This lesson ties its explanation to `lib/stats/moments.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
