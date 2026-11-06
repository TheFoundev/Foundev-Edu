# Stock Portfolio Analytics

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

| [French version](readme.fr.md)

# PortfolioAnalytics v0.0.4 ([Changelog](changelog.md))

[![Travis Build Status](https://travis-ci.org/lequant40/portfolio_analytics_js.svg?style=flat)](https://travis-ci.org/lequant40/portfolio_analytics_js)

In order to track my personal stock market investments performances, as well as to analyse trading strategies on my blog [Le Quant 40](http://www.lequant40.com/), I wanted to use portfolio performances measures computed in JavaScript.

Why in JavaScript ? Because I am a fan of [Google Sheets](https://www.google.com/sheets/about/), which is easily extensible thanks to [Google Apps Script](https://developers.google.com/apps-script/), a JavaScript-based language.

After several fruitless hours of Googling (incomplete codes, incorrect codes, undocumented codes...), I decided to create my own JavaScript library of such portfolio performances measures, hoping that it could be useful to other people...


## Features

- Compatible with Google Sheets
- Compatible with any browser supporting ECMAScript 5 (i.e., front-end development)
- Compatible with [Node.js](https://nodejs.org/) (i.e., back-end development)
- (Performances) Automatically uses JavaScript Typed Arrays
- (Accuracy) Internally uses accurate numerical algorithms (e.g., corrected two pass algorithms for mean, variance, skewness and kurtosis, accurate algorithm for error function...)
- Code continuously tested and integrated by [Travis CI](https://travis-ci.org/)
- Code heavily documented using [JSDoc](http://usejsdoc.org/)

## Usage

### Usage in Google Sheets

If you would like t

## Actual features and limits

README feature statements (verify each against code before relying on it):
- Compatible with Google Sheets
- Compatible with any browser supporting ECMAScript 5 (i.e., front-end development)
- Compatible with [Node.js](https://nodejs.org/) (i.e., back-end development)
- (Performances) Automatically uses JavaScript Typed Arrays
- (Accuracy) Internally uses accurate numerical algorithms (e.g., corrected two pass algorithms for mean, variance, skewness and kurtosis, accurate algorithm for error function...)
- Code continuously tested and integrated by [Travis CI](https://travis-ci.org/)
- Code heavily documented using [JSDoc](http://usejsdoc.org/)
- (Recommended) [Import the external Google Apps Script library](https://developers.google.com/apps-script/guide_libraries) with Script ID 1NXwj16pdgcJT-XG5LiWRJyRW604Dj26U4lqgGsJJfOKLum4y9grakXPI into your spreadsheet script
- Import the JavaScript files from the [dist/gs directory](https://github.com/lequant40/portfolio_analytics_js/tree/master/dist/gs) into your spreadsheet script
- Using a wrapper function in your spreadsheet script, directly accessible from your spreadsheet, to which you can provide a standard data range (A1:A99...), e.g.:
- Using pure Google Apps Script functions - typically the getRange(...) familly of functions -, optimized for speed, e.g.:
- The following command generates the files to be used inside a browser or with Node.js in the `dist` directory:

The implementation inventory includes 33 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `package.json`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.travis.yml`
- `Gruntfile.js`
- `README.md`
- `lib/drawdowns/drawdowns.js`
- `lib/footer.js`
- `lib/header.js`
- `lib/ratios/ratios.js`
- `lib/ratios/sharpe-ratio.js`
- `lib/returns/returns.js`
- `lib/stats/distributions.js`
- `lib/stats/moments.js`
- `package.json`
- `readme.fr.md`
- `test/drawdowns/tests_dev.js`
- `test/drawdowns/tests_dist.js`
- `test/ratios/test_sharpe-ratios_dev.js`
- `test/ratios/tests_dist.js`
- `test/ratios/tests_sharpe-ratios_dist.js`
- `test/returns/tests_dist.js`
- `test/stats/tests_distributions_dev.js`
- `test/stats/tests_moments_dev.js`

## Testing

Test-related paths found: test/drawdowns/index_dev.html, test/drawdowns/index_dist.html, test/drawdowns/tests_dev.js, test/drawdowns/tests_dist.js, test/ratios/index_dev.html, test/ratios/index_dist.html, test/ratios/test_sharpe-ratios_dev.js, test/ratios/tests_dist.js, test/ratios/tests_sharpe-ratios_dist.js, test/returns/index_dev.html, test/returns/index_dist.html, test/returns/tests_dist.js, test/stats/index_dev.html, test/stats/tests_distributions_dev.js, test/stats/tests_moments_dev.js. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
