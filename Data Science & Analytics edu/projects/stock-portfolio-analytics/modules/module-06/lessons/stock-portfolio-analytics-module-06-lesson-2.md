# Read test code and evidence boundaries in the source

**Lesson ID:** `stock-portfolio-analytics-module-06-lesson-2`

## Purpose and learning objectives

Read test implementations test/drawdowns/tests_dev.js, test/drawdowns/tests_dist.js, test/ratios/test_sharpe-ratios_dev.js, test/ratios/tests_dist.js. Identify the behavior each assertion encodes, connect it to implementation, and distinguish a test file from an executed passing result.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `test/drawdowns/tests_dev.js`, `test/drawdowns/tests_dist.js`, `test/ratios/test_sharpe-ratios_dev.js`, `test/ratios/tests_dist.js`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `test/drawdowns/tests_dev.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `test/drawdowns/tests_dist.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `test/ratios/test_sharpe-ratios_dev.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `test/ratios/tests_dist.js` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### test/drawdowns/tests_dev.js

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
  assert.deepEqual(PortfolioAnalytics.maxDrawdown_(this.complexEquityCurve, 7, this.complexEquityCurve.length-1), 
                                                   [0.3076923076923077, 9, 12], 
                                                   'Complex max drawdown #3');
});

```

### test/drawdowns/tests_dist.js

```text
// ------------------------------------------------------------
QUnit.module('Drawdowns module', {
  before: function() {
    // Coming from "Ambiguity in Calculating and Interpreting Maximum Drawdown, Research Note, Andreas Steiner Consulting GmbH, December 2010"
	this.complexEquityCurve = [60, 40, 80, 140, 100, 90, 110, 70, 100, 130, 110, 120, 90, 150, 120, 130];
	
	// Coming from "Practical Portfolio Performance Measurement and Attribution, 2nd Edition, Carl R. Bacon."
	this.BaconEquityCurve = [100, 100.3, 102.9078, 104.0397858, 102.9993879, 104.5443788, 107.1579882, 108.872516, 116.1669746, 114.540637, 119.1222625, 118.5266511, 
           128.1273099, 133.2524023, 128.3220634, 120.4944175, 122.5428226, 116.5382243, 113.9743834, 121.9525902, 129.0258404, 120.6391608, 123.5345007, 122.9168282, 121.8105767];
    
  }
});



QUnit.test('Max drawdown computation', function(assert) {    
  assert.equal(PortfolioAnalytics.maxDrawdown([100]), 0, 'No max drawdown #1');
  assert.equal(PortfolioAnalytics.maxDrawdown([100, 110]), 0, 'No max drawdown #2');

  assert.equal(PortfolioAnalytics.maxDrawdown([100, 90]), 0.1, 'Simple max drawdown #1');
  assert.equal(PortfolioAnalytics.maxDrawdown([100, 90, 80]), 0.2, 'Simple max drawdown #2');
  
  assert.equal(PortfolioAnalytics.maxDrawdown(this.complexEquityCurve), 
                                              0.5, 
                                              'Complex max drawdown #1');
  assert.equal(PortfolioAnalytics.maxDrawdown(this.BaconEquityCurve), 
                                              0.14467295573852484, 
                                              'Complex max drawdown #2');
});



QUnit.test('Drawdown function computation', function(assert) {
  assert.deepEqual(PortfolioAnalytics.drawdownFunction([100]), 
                                                       [0], 
                                                       'Simple drawdown function #1');
  assert.deepEqual(PortfolioAnalytics.drawdownFunction([100, 90, 90, 80, 100]), 
                                                       [0, 0.1, 0.1, 0.2, 0], 
                                                       'Simple drawdown function #2');

  assert.deepEqual(PortfolioAnalytics.drawdownFunction(new Float64Array([100, 90, 90, 80, 100])), 
                                                       new Float64Array([0, 0.1, 0.1, 0.2, 0]), 
                                                       'Simple drawdown function with typed array');
													   
  assert.deepEqual(PortfolioAnalytics.drawdownFunction(this.complexEquityCurve, 0, this.complexEquityCurve.length-1), 
                                                       	[0,
                                                         0.3333333333333333,
                                                         0,
                                                         0,
                                                         0.2857142857142857,
                                                         0.35714285714285715,
                                                         0.21428571428571427,
                                                         0.5,
                                                         0.2857142857142857,
                                                         0.07142857142857142,
                                                         0.21428571428571427,
                                                         0.14285714285714285,
                                                         0.35714285714285715,
                                                         0,
                                                         0.2,
                                                         0.13333333333333333
                                                        ], 
                                                       'Complex drawdown function #1');
  assert.deepEqual(PortfolioAnalytics.drawdownFunction(this.BaconEquityCurve, 0, thi
```

### test/ratios/test_sharpe-ratios_dev.js

```text
// ------------------------------------------------------------
QUnit.module('Sharpe ratio internal module', {
  before: function() {
	  // Taken from "Practical Portfolio Performance Measurement and Attribution, 2nd Edition, Carl R. Bacon."
	  var baconPortfolioReturns = [0.003, 0.026, 0.011, -0.01, 0.015, 0.025, 0.016, 0.067, -0.014, 0.04, -0.005, 0.081, 0.04, -0.037, -0.061, 0.017, -0.049, -0.022, 0.07, 0.058, -0.065, 0.024, -0.005, -0.009];
	  var baconBenchmarkReturns = [0.002, 0.025, 0.018, -0.011, 0.014, 0.018, 0.014, 0.065, -0.015, 0.042, -0.006, 0.083, 0.039, -0.038, -0.062, 0.015, -0.048, 0.021, 0.06, 0.056, -0.067, 0.019, -0.003, 0];

	  // Build the equity curves corresponding to the returns
	  this.baconPortfolio = new Array(baconPortfolioReturns.length + 1);
	  this.baconBenchmark = new Array(baconBenchmarkReturns.length + 1);
	  this.zeroRiskFree = new Array(baconBenchmarkReturns.length + 1);
	  this.baconPortfolio[0] = 100;
	  this.baconBenchmark[0] = 100;
	  this.zeroRiskFree[0] = 100;
	  for (var i=0; i<baconPortfolioReturns.length; ++i) {
		this.baconPortfolio[i+1] = this.baconPortfolio[i] * (1 + baconPortfolioReturns[i]);
		this.baconBenchmark[i+1] = this.baconBenchmark[i] * (1 + baconBenchmarkReturns[i]);
		this.zeroRiskFree[i+1] = this.zeroRiskFree[i];
	  }
  }
});


QUnit.test('Differential returns computation internal function', function(assert) {
  // Test Bacon portolios
    // Compute the differential returns
  var diffReturns = PortfolioAnalytics.differentialReturns_(this.baconPortfolio, this.baconBenchmark);
  
    // Bacon differential portfolio returns, as defined in "Practical Portfolio Performance Measurement and Attribution, 2nd Edition, Carl R. Bacon."
  var baconDifferentialReturns = [0.001, 0.001, -0.007, 0.001, 0.001, 0.007, 0.002, 0.002, 0.001, -0.002, 0.001, -0.002, 0.001, 0.001, 0.001, 0.002, -0.001, -0.043, 0.01, 0.002, 0.002, 0.005, -0.002, -0.009];

	// The computed differential returns must math those of Bacon  
  for (var i=0; i<baconDifferentialReturns.length; ++i) {
    assert.ok(Math.abs(diffReturns[i] - baconDifferentialReturns[i]) <= 1e-14, 'Bacon differential returns #' + i);
  }
});


QUnit.test('Sharpe ratio statistics internal function', function(assert) {
  // Test internal consistency of the sharpeRatioStatistics_ function
    // Portfolio #1
  var srs = PortfolioAnalytics.sharpeRatioStatistics_(this.baconPortfolio, this.zeroRiskFree);
  assert.equal(srs[0], PortfolioAnalytics.sharpeRatio(this.baconPortfolio, this.zeroRiskFree), 'Sharpe ratio #1');
  assert.equal(srs[0]/Math.sqrt(srs[1]), PortfolioAnalytics.doubleSharpeRatio(this.baconPortfolio, this.zeroRiskFree), 'Double Sharpe ratio #1');
  assert.equal(srs[0]/srs[2], PortfolioAnalytics.biasAdjustedSharpeRatio(this.baconPortfolio, this.zeroRiskFree), 'Bias adjusted Sharpe ratio #1');
  
    // Portfolio #2
  var srs = PortfolioAnalytics.sharpeRatioStatistics_(this.baconBenchmark, this.zeroRiskFree);
  assert.equal(srs[0], PortfolioAnalytics.sharpeRatio(this.baconBenchmark, this.zeroRiskFree), 'Sharpe ratio #2');
  assert.equal(srs[0]/Math.sqrt(srs[1]), PortfolioAnalytics.doubleSharpeRatio(this.baconBenchmark, this.zeroRiskFree), 'Double Sharpe ratio #2');
  assert.equal(srs[0]/srs[2], PortfolioAnalytics.biasAdjustedSharpeRatio(this.baconBenchmark, this.zeroRiskFree), 'Bias adjusted Sharpe ratio #2');

    // Portfolio #3
  var srs = PortfolioAnalytics.sharpeRatioStatistics_(this.baconPortfolio, this.baconBenchmark);
  assert.equal(srs[0], PortfolioAnalytics.sharpeRatio(this.baconPortfolio, this.baconBenchmark), 'Sharpe ratio #3');
  assert.equal(srs[0]/Math.sqrt(srs[1]), PortfolioAnalytics.doubleSharpeRatio(this.baconPortfolio, this.baconBenchmark), 'Double Sharpe ratio #3');
  assert.equal(srs[0]/srs[2], PortfolioAnalytics.biasAdjustedSharpeRatio(this.baconPortfolio, this.baconBenchmark), 'Bias adjusted Sharpe ratio #3');
});
```

### test/ratios/tests_dist.js

```text
// ------------------------------------------------------------
QUnit.module('Ratios module', {
});

QUnit.test('Gain to pain ratio computation', function(assert) {    
  assert.deepEqual(PortfolioAnalytics.gainToPainRatio([100]), NaN, 'Gain to pain ratio #1');
  assert.equal(PortfolioAnalytics.gainToPainRatio([100, 100, 109.5, 108.405, 109.48905, 108.3941595, 107.8521887]), 3.1999999961252454, 'Gain to pain ratio #2');
  assert.deepEqual(PortfolioAnalytics.gainToPainRatio([100, 110]), NaN, 'Gain to pain ratio #3'); 
});
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

This lesson ties its explanation to `test/drawdowns/tests_dev.js`, `test/drawdowns/tests_dist.js`, `test/ratios/test_sharpe-ratios_dev.js`, `test/ratios/tests_dist.js`. A sound account distinguishes source evidence from inferred behavior.

## Knowledge checks

1. Which visible declaration or configuration element is central to this module?
2. What caller, test, or downstream use would strengthen your explanation?
3. Which conclusion would require execution rather than source inspection?

## References

See [references.json](../../../references.json) and [architecture.md](../../../architecture.md).


### Gruntfile.js

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

This excerpt links the test or configuration evidence to its implementation. Read surrounding declarations and callers in the source repository.
