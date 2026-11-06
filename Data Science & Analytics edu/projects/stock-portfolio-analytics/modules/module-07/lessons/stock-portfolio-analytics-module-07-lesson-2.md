# Read declared dependencies and runtime configuration in the source

**Lesson ID:** `stock-portfolio-analytics-module-07-lesson-2`

## Purpose and learning objectives

Inspect the actual manifests .travis.yml, package.json. Separate declared packages/settings from imports, installed state, secrets, and runtime success.

By the end, you can explain the role of the listed source files, locate a declaration or configuration value, trace how it is used, and state what the excerpt does not prove.

## Prerequisites

Read [prerequisites.md](../../../prerequisites.md). For lesson 2, complete lesson 1 first.

## Beginner explanation

A source file is one working part of a larger program. Its imports show what it relies on; its declarations show the operations or settings it makes available; its callers show whether and how that part is used. Read these relationships as a path through the project.

## From mental model to implementation

Now trace the same source at implementation level. For each declaration in `.travis.yml`, `package.json`, record its inputs, branches, calls, and returned or written value. Confirm whether a test or caller exercises that path.

## What the excerpt shows

- The excerpt from `.travis.yml` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.
- The excerpt from `package.json` has no recognized import or function declaration. Read its actual statements from top to bottom and use the adjacent module/file context to establish its role.

These observations describe visible imports and declarations. Check function bodies and callers before inferring exact data transformations or runtime use.

## Step-by-step source reading

1. Open the complete file shown below; the excerpt is truncated for portability.
2. Mark imports, top-level declarations, and any configuration or data boundaries.
3. For a function or class, write down parameters and visible return/output operations. For configuration or documentation, identify the exact key or claim and where source consumes or implements it.
4. Search the repository for callers, imports, or tests referencing the declaration.
5. Compare documentation and implementation, recording confirmed facts separately from unknown runtime behavior.

## Source evidence

### .travis.yml

```text
language: node_js
node_js:
  - "node"
install: npm install
after_script: grunt deliver
```

### package.json

```text
{
  "name": "portfolio-analytics",
  "version": "0.0.4",
  "date": "2017-05-25",
  "author": "Roman Rubsamen <roman.rubsamen@gmail.com>",
  "contributors": [],
  "description": "A JavaScript library to track and measure stock market portfolios performances.",
  "license": "MIT",
  "directories": {
    "lib": "lib",
    "test": "tests"
  },
  "keywords": [
    "quantitative finance",
    "google sheets",
    "portfolio"
  ],
  "repository": {
    "type": "git",
    "url": "https://github.com/lequant40/portfolio_analytics_js.git"
  },
  "devDependencies": {
    "grunt": "^1.0.0",
    "grunt-contrib-concat": "^1.0.1",
    "grunt-contrib-qunit": "^1.2.0",
    "grunt-contrib-uglify": "^1.0.2",
    "grunt-replace": "^1.0.1",
    "grunt-strip-code": "^1.0.4"
  },
  "bugs": {
    "url": "https://github.com/lequant40/portfolio_analytics_js/issues"
  },
  "main": "dist/portfolio_analytics.dist.min.js",
  "scripts": {
    "test": "grunt test"
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

This lesson ties its explanation to `.travis.yml`, `package.json`. A sound account distinguishes source evidence from inferred behavior.

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
