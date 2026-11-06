# Source and validation report: Stock Portfolio Analytics

## Inspection scope

Inventory covered 33 files excluding caches and vendor directories. Read README text and bounded excerpts from source, tests, dependency/configuration and deployment files.

Stack signals: JavaScript/Node.js.

## Source-specific findings

- README claims were retained as claims; code/configuration remains authoritative.
- Examined source paths: none.
- Test paths: test/drawdowns/index_dev.html, test/drawdowns/index_dist.html, test/drawdowns/tests_dev.js, test/drawdowns/tests_dist.js, test/ratios/index_dev.html, test/ratios/index_dist.html, test/ratios/test_sharpe-ratios_dev.js, test/ratios/tests_dist.js, test/ratios/tests_sharpe-ratios_dist.js, test/returns/index_dev.html, test/returns/index_dist.html, test/returns/tests_dist.js, test/stats/index_dev.html, test/stats/tests_distributions_dev.js, test/stats/tests_moments_dev.js. Presence does not mean tests passed.
- Dependency/configuration paths: .travis.yml, package.json.

## Passed checks

- Package structure and required file presence.
- JSON parse, identifiers/references, assessment shape, answer-key mapping and manifest counts/list.
- ZIP integrity checked after packaging.

## Warnings and human/runtime review

- No Dockerfile path identified in inspected inventory.
- No docker-compose path identified in inspected inventory.
- No .env path identified in inspected inventory.
- No SECURITY path identified in inspected inventory.
- Data may be sensitive or consequential; verify provenance, privacy, bias, and permitted use with a human reviewer.
- Human reviewer should compare README feature claims to complete source and inspect security/dependency posture.
- Runtime reviewer should install in an isolated environment, run documented tests and verify external services only where authorized.
- Applications were not executed or deployed; structural validation cannot establish educational accuracy or prove applications, APIs, data sources or infrastructure work.

## Code-anchored curriculum

Modules: 8; lessons: 16; questions: 80. Each module names source paths in source_files, includes bounded excerpts, and explains visible imports/declarations before tracing behavior. Module count follows substantive implementation files with tests, configuration, and documentation topics included.

### Module sources

- stock-portfolio-analytics-module-01: Gruntfile.js, lib/drawdowns/drawdowns.js
- stock-portfolio-analytics-module-02: lib/footer.js, lib/header.js
- stock-portfolio-analytics-module-03: lib/ratios/ratios.js, lib/ratios/sharpe-ratio.js
- stock-portfolio-analytics-module-04: lib/returns/returns.js, lib/stats/distributions.js
- stock-portfolio-analytics-module-05: lib/stats/moments.js
- stock-portfolio-analytics-module-06: test/drawdowns/tests_dev.js, test/drawdowns/tests_dist.js, test/ratios/test_sharpe-ratios_dev.js, test/ratios/tests_dist.js
- stock-portfolio-analytics-module-07: .travis.yml, package.json
- stock-portfolio-analytics-module-08: README.md, Gruntfile.js, lib/drawdowns/drawdowns.js

Runtime status: no source application or test suite was executed or deployed. Structural validation cannot prove educational accuracy or runtime behavior. Human review should check source-specific feature claims, provider setup, dependency security, privacy, and operational safety.

## Module relevance audit

8 modules were checked. Each names an implementation source file and each lesson contains an excerpt for every declared anchor. Lessons follow the beginner explanation → source-reading steps → source evidence sequence. This structural review confirms source linkage and sequence, not the accuracy of every explanation.
