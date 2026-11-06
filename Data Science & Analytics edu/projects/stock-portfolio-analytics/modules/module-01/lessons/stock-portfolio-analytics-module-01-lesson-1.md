# A beginner's model of gruntfile and drawdowns

**Lesson ID:** `stock-portfolio-analytics-module-01-lesson-1`

## Purpose and learning objectives

Study the implementation in [Gruntfile.js] and [lib/drawdowns/drawdowns.js]. Trace its declarations and dependencies into a caller or test. Prominent declared symbols visible in the inspected excerpt include maxDrawdown_; confirm their complete definitions and callers in the file.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Begin with the role of the source files in this module: `Gruntfile.js`, `lib/drawdowns/drawdowns.js`. The code excerpt below is the evidence to study. Read imports first, then find declarations, then follow one call or data value into its next use.

## What the excerpt shows

- The excerpt from `Gruntfile.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- `function maxDrawdown_(equityCurve, idxStart, idxEnd) {` introduces a callable or type. The body and call sites determine its actual behavior; the declaration name alone does not.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### Gruntfile.js

```text
module.exports = function(grunt) {
  var path = require('path');

  // Load plugins
  grunt.loadNpmTasks('grunt-contrib-qunit');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-strip-code');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-replace');

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
	
	strip_code: {
      portfolio_analytics_gs: {
		options: {
			blocks: [
			{ start_block: "/* Start Not to be used as is in Google Sheets */",
			  end_block: "/* End Not to be used as is in Google Sheets */"
			}
			]
		},
        files: [
		  { src: ['dist/portfolio_analytics.dist.js'], dest: 'dist/gs/portfolio_analytics.gs'}
		]
      },
      portfolio_analytics_dist: {
		options: {
			blocks: [
			{ start_block: "/* Start Wrapper private methods - Unit tests usage only */",
			  end_block: "/* End Wrapper private methods - Unit tests usage only */"
			}
			]
		},
        files: [
		  { src: ['dist/portfolio_analytics.dist.js'], dest: 'dist/portfolio_analytics.dist.js'}
		]
      },
    },

    replace: {
      portfolio_analytics_gs: {
        options: {
		  preserveOrder: true,
          patterns: [
            {
              match: /self\.(\w+)\s=\sfunction/g,
              replacement: 'function $1'
            },
            {
              match: /self\./g,
              replacement: ''
            }			
          ]
        },
        files: [
          { src: ['dist/gs/portfolio_analytics.gs'], dest: 'dist/gs/portfolio_analytics.gs'}
        ]
      }
    },
	
	concat: {
	  portfolio_analytics_dev: {
	    src: ['lib/header.js', 'lib/*/*.js', 'lib/footer.js'],
	    dest: 'dist/portfolio_analytics.dev.js',
	  },
	  portfolio_analytics_dist: {
	    src: ['lib/header.js', 'lib/*/*.js', 'lib/footer.js'],
	    dest: 'dist/portfolio_analytics.dist.js',
	  },
	},
  
    uglify: {
	  options: {
	    banner: '/*! <%= pkg.name %> - v<%= pkg.version %> (<%= pkg.date %>), <%= pkg.author %> */'
      },
      portfolio_analytics_dev: {
        files: {
          'dist/portfolio_analytics.dev.min.js': ['dist/portfolio_analytics.dev.js']
        }
      },
      portfolio_analytics_dist: {
        files: {
          'dist/portfolio_analytics.dist.min.js': ['dist/portfolio_analytics.dist.js']
        }
      }	  
    },
	
	qunit: { 
      dev: ['test/*/*_dev.html'],
	  dist: ['test/*/*_dist.html']
    }

  });


  //
  grunt.registerTask('test', 'Tests the app.', function() {
	// Build the app in dev mode, and run all dev unit tests, 
	// which are a superset of dist unit tests
```

### lib/drawdowns/drawdowns.js

```text
/**
 * @file Functions related to drawdowns computation.
 * @author Roman Rubsamen <roman.rubsamen@gmail.com>
 */


/* Start Wrapper private methods - Unit tests usage only */
self.maxDrawdown_ = function(equityCurve, idxStart, idxEnd) { return maxDrawdown_(equityCurve, idxStart, idxEnd); }
/* End Wrapper private methods - Unit tests usage only */
 
  
/**
* @function maxDrawdown
*
* @description Compute the maximum drawdown associated to a portfolio equity curve.
*
* @see <a href="https://en.wikipedia.org/wiki/Drawdown_(economics)">https://en.wikipedia.org/wiki/Drawdown_(economics)</a>
* 
* @param {Array.<number>} equityCurve the portfolio equity curve.
* @return {number} the maximum drawdown.
*
* @example
* maxDrawdown([1, 2, 1]); 
* // 0.5, i.e. 50% drawdown
*
* @example
* maxDrawdown([1, 2, 3]);
* // 0.0, i.e. no drawdown
*
* @example
* maxDrawdown([]);
* // 0.0, i.e. no drawdown
*/
self.maxDrawdown = function(equityCurve) {
	// Compute the maximum drawdown and its associated duration
	var maxDd_ = maxDrawdown_(equityCurve, 0, equityCurve.length-1);

	// Return the maximum drawdown
	if (maxDd_[0] == -Infinity) {
		return 0.0;
	}
	else {
		return maxDd_[0];
	}
}
  
  
/**
* @function maxDrawdown_
*
* @description Compute the maximum drawdown associated to a portfolio equity curve,
* as well as the indexes of the start/end of the maximum drawdown phase.
*
* In case there are several identical maximum drawdowns, the indexes returned
* correspond to the start/end of the first encountered maximum drawdown phase.
*
* @see <a href="https://en.wikipedia.org/wiki/Drawdown_(economics)">https://en.wikipedia.org/wiki/Drawdown_(economics)</a>
* 
* @param {Array.<number>} equityCurve the portfolio equity curve.
* @param {number} idxStart the equityCurve array index from which to compute the maximum drawdown.
* @param {number} idxEnd the equityCurve index until which to compute the maximum drawdown.
* @return {Array.<number>} in this order, the maximum drawdown and
* the indexes of the start/end of the maximum drawdown phase.
*
* @example
* maxDrawdown_([1, 2, 1], 0, 2); 
* // [0.5, 1.0, 2.0], i.e. 50% drawdown, starting at index 1 and ending at index 2
*
* @example
* maxDrawdown_([1, 2, 3], 0, 2); 
* // [0.0, -1.0, -1.0], i.e. no drawdown computed, hence no start/end indexes
*
* @example
* maxDrawdown_([1, 2, 3], 0, -1); 
* // [-Infinity, -1.0, -1.0], i.e. failure in the drawdown computation, hence no start/end indexes
*/
function maxDrawdown_(equityCurve, idxStart, idxEnd) {
	// Initialisations
	var highWaterMark = -Infinity;
	var maxDd = -Infinity;
	var idxHighWaterMark = -1;
	var idxStartMaxDd = -1;
	var idxEndMaxDd = -1;

	// Loop over all the values to compute the maximum drawdown
	for (var i=idxStart; i<idxEnd+1; ++i) {     
		if (equityCurve[i] > highWaterMark) {
			highWaterMark = equityCurve[i];
			idxHighWaterMark = i;
		}

		var dd = (highWaterMark - equityCurve[i]) / highWaterMark;

		if (dd > maxDd) {
			maxDd = dd;
			idxStartMaxDd = idxHighWaterMark;
			idxEndMaxDd = i;
		}
	}

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

This lesson ties its explanation to `Gruntfile.js`, `lib/drawdowns/drawdowns.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).
