# Source and validation report: Automated Eda Tool

## Inspection scope

Inventory covered 138 files excluding caches and vendor directories. Read README text and bounded excerpts from source, tests, dependency/configuration and deployment files.

Stack signals: Python, Dash, JavaScript/Node.js, Docker.

## Source-specific findings

- README claims were retained as claims; code/configuration remains authoritative.
- Examined source paths: none.
- Test paths: autoeda/test_notebook_data_optimization.py, autoeda/test_null_handler.py, backend/output/standalone_outlier_tests/autoEDA_outlier_report.json, backend/output/standalone_outlier_tests/autoEDA_outlier_summary.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_capped.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_flagged.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_removed.csv, backend/services/run_data_optimization_test.py, unit_tests/.gitignore, unit_tests/__init__.py, unit_tests/outlier_test.py, unit_tests/test_data_optimizer.py, unit_tests/test_encoding_categorical.py, unit_tests/test_feat_scaling.py, unit_tests/test_feature_selector.py, unit_tests/test_pca_transformer.py. Presence does not mean tests passed.
- Dependency/configuration paths: .github/workflows/ci.yml, backend/.env.sample, backend/DOCKERFILE, backend/docker-compose.yml, backend/requirements.txt, docker-compose.yml, frontend/DOCKERFILE, frontend/package.json, package.json.

## Passed checks

- Package structure and required file presence.
- JSON parse, identifiers/references, assessment shape, answer-key mapping and manifest counts/list.
- ZIP integrity checked after packaging.

## Warnings and human/runtime review

- README contains limitation/qualification language; reconcile every feature claim against implementation.
- Human reviewer should compare README feature claims to complete source and inspect security/dependency posture.
- Runtime reviewer should install in an isolated environment, run documented tests and verify external services only where authorized.
- Applications were not executed or deployed; structural validation cannot establish educational accuracy or prove applications, APIs, data sources or infrastructure work.

## Code-anchored curriculum

Modules: 21; lessons: 42; questions: 210. Each module names source paths in source_files, includes bounded excerpts, and explains visible imports/declarations before tracing behavior. Module count follows substantive implementation files with tests, configuration, and documentation topics included.

### Module sources

- automated-eda-tool-module-01: backend/app.py, autoeda/feature_selector.py
- automated-eda-tool-module-02: autoeda/pca_transformer.py, autoeda/pipeline.py
- automated-eda-tool-module-03: autoeda/data_optimizer.py, autoeda/encoding_categorical.py
- automated-eda-tool-module-04: autoeda/feat_scaling.py, autoeda/notebook_data_optimization.py
- automated-eda-tool-module-05: autoeda/null_handler.py, autoeda/outliers.py
- automated-eda-tool-module-06: autoeda/summary_stats.py, backend/config/database.js
- automated-eda-tool-module-07: backend/services/runner.py, frontend/eslint.config.js
- automated-eda-tool-module-08: frontend/src/App.jsx, frontend/src/components/About.jsx
- automated-eda-tool-module-09: frontend/src/components/Auth.jsx, frontend/src/components/Contact.jsx
- automated-eda-tool-module-10: frontend/src/components/Dashboard.jsx, frontend/src/components/FileUpload.jsx
- automated-eda-tool-module-11: frontend/src/components/Footer.jsx, frontend/src/components/Home.jsx
- automated-eda-tool-module-12: frontend/src/components/HowItWorks.jsx, frontend/src/components/Navbar.jsx
- automated-eda-tool-module-13: frontend/src/components/scrollCard.jsx, frontend/src/components/theme-provider.jsx
- automated-eda-tool-module-14: frontend/src/components/ui/button.jsx, frontend/src/components/ui/card.jsx
- automated-eda-tool-module-15: frontend/src/components/ui/input.jsx, frontend/src/components/userProfile.jsx
- automated-eda-tool-module-16: frontend/src/lib/utils.js, frontend/src/main.jsx
- automated-eda-tool-module-17: frontend/tailwind.config.js, frontend/vite.config.js
- automated-eda-tool-module-18: run_cleaning.py
- automated-eda-tool-module-19: autoeda/test_notebook_data_optimization.py, autoeda/test_null_handler.py, backend/services/run_data_optimization_test.py, unit_tests/test_data_optimizer.py
- automated-eda-tool-module-20: .github/workflows/ci.yml, backend/DOCKERFILE, backend/docker-compose.yml, backend/requirements.txt
- automated-eda-tool-module-21: README.md, autoeda/data_optimizer.py, autoeda/encoding_categorical.py

Runtime status: no source application or test suite was executed or deployed. Structural validation cannot prove educational accuracy or runtime behavior. Human review should check source-specific feature claims, provider setup, dependency security, privacy, and operational safety.

## Module relevance audit

21 modules were checked. Each names an implementation source file and each lesson contains an excerpt for every declared anchor. Lessons follow the beginner explanation → source-reading steps → source evidence sequence. This structural review confirms source linkage and sequence, not the accuracy of every explanation.
