# Source and validation report: Rainfall Analysis And Prediction

## Inspection scope

Inventory covered 78 files excluding caches and vendor directories. Read README text and bounded excerpts from source, tests, dependency/configuration and deployment files.

Stack signals: Python, JavaScript/Node.js.

## Source-specific findings

- README claims were retained as claims; code/configuration remains authoritative.
- Examined source paths: none.
- Test paths: .github/workflows/test.yml, test/data/cemaneige_validation_data.csv, test/data/cemaneigegr4j_validation_data.csv, test/data/cemaneigehystgr4j_validation_data.csv, test/data/cemaneigehystgr4jice_validation_data.csv, test/data/gr4j_example_data.csv, test/data/hbv_daily_inputs.txt, test/data/hbv_monthly_inputs.txt, test/data/hbv_qsim.csv, test/test_models.py, test/test_tools.py, test/test_utils.py. Presence does not mean tests passed.
- Dependency/configuration paths: .github/workflows/test.yml, environment.yml, readthedocs.yml, requirements.txt, rtd_environment.yml, setup.py.

## Passed checks

- Package structure and required file presence.
- JSON parse, identifiers/references, assessment shape, answer-key mapping and manifest counts/list.
- ZIP integrity checked after packaging.

## Warnings and human/runtime review

- No Dockerfile path identified in inspected inventory.
- No docker-compose path identified in inspected inventory.
- No SECURITY path identified in inspected inventory.
- Human reviewer should compare README feature claims to complete source and inspect security/dependency posture.
- Runtime reviewer should install in an isolated environment, run documented tests and verify external services only where authorized.
- Applications were not executed or deployed; structural validation cannot establish educational accuracy or prove applications, APIs, data sources or infrastructure work.

## Code-anchored curriculum

Modules: 18; lessons: 36; questions: 180. Each module names source paths in source_files, includes bounded excerpts, and explains visible imports/declarations before tracing behavior. Module count follows substantive implementation files with tests, configuration, and documentation topics included.

### Module sources

- rainfall-analysis-and-prediction-module-01: rrmpg/models/__init__.py, rrmpg/models/abcmodel_model.py
- rainfall-analysis-and-prediction-module-02: rrmpg/models/abcmodel.py, rrmpg/models/basemodel.py
- rainfall-analysis-and-prediction-module-03: rrmpg/models/cemaneige_model.py, rrmpg/models/cemaneige_utils.py
- rainfall-analysis-and-prediction-module-04: rrmpg/models/cemaneige.py, rrmpg/models/cemaneigegr4j_model.py
- rainfall-analysis-and-prediction-module-05: rrmpg/models/cemaneigegr4j.py, rrmpg/models/cemaneigegr4jice_model.py
- rainfall-analysis-and-prediction-module-06: rrmpg/models/cemaneigegr4jice.py, rrmpg/models/cemaneigehyst_model.py
- rainfall-analysis-and-prediction-module-07: rrmpg/models/cemaneigehystgr4j_model.py, rrmpg/models/cemaneigehystgr4j.py
- rainfall-analysis-and-prediction-module-08: rrmpg/models/cemaneigehystgr4jice_model.py, rrmpg/models/cemaneigehystgr4jice.py
- rainfall-analysis-and-prediction-module-09: rrmpg/models/gr4j_model.py, rrmpg/models/gr4j.py
- rainfall-analysis-and-prediction-module-10: rrmpg/models/hbvedu_model.py, rrmpg/models/hbvedu.py
- rainfall-analysis-and-prediction-module-11: rrmpg/models/icemelt_model.py, docs/source/conf.py
- rainfall-analysis-and-prediction-module-12: rrmpg/__init__.py, rrmpg/tools/__init__.py
- rainfall-analysis-and-prediction-module-13: rrmpg/tools/monte_carlo.py, rrmpg/utils/array_checks.py
- rainfall-analysis-and-prediction-module-14: rrmpg/utils/metrics.py, rrmpg/utils/plot_utils.py
- rainfall-analysis-and-prediction-module-15: setup.py
- rainfall-analysis-and-prediction-module-16: test/test_models.py, test/test_tools.py, test/test_utils.py
- rainfall-analysis-and-prediction-module-17: .github/workflows/test.yml, environment.yml, readthedocs.yml, requirements.txt
- rainfall-analysis-and-prediction-module-18: README.rst, docs/source/conf.py, rrmpg/__init__.py

Runtime status: no source application or test suite was executed or deployed. Structural validation cannot prove educational accuracy or runtime behavior. Human review should check source-specific feature claims, provider setup, dependency security, privacy, and operational safety.

## Module relevance audit

18 modules were checked. Each names an implementation source file and each lesson contains an excerpt for every declared anchor. Lessons follow the beginner explanation → source-reading steps → source evidence sequence. This structural review confirms source linkage and sequence, not the accuracy of every explanation.
