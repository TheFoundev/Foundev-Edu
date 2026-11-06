# Source and validation report: Streamlit Analytics Web App

## Inspection scope

Inventory covered 19 files excluding caches and vendor directories. Read README text and bounded excerpts from source, tests, dependency/configuration and deployment files.

Stack signals: Python, JavaScript/Node.js.

## Source-specific findings

- README claims were retained as claims; code/configuration remains authoritative.
- Examined source paths: none.
- Test paths: tests/test_pipeline.py. Presence does not mean tests passed.
- Dependency/configuration paths: requirements.txt.

## Passed checks

- Package structure and required file presence.
- JSON parse, identifiers/references, assessment shape, answer-key mapping and manifest counts/list.
- ZIP integrity checked after packaging.

## Warnings and human/runtime review

- No Dockerfile path identified in inspected inventory.
- No docker-compose path identified in inspected inventory.
- No .env path identified in inspected inventory.
- No SECURITY path identified in inspected inventory.
- README contains limitation/qualification language; reconcile every feature claim against implementation.
- Human reviewer should compare README feature claims to complete source and inspect security/dependency posture.
- Runtime reviewer should install in an isolated environment, run documented tests and verify external services only where authorized.
- Applications were not executed or deployed; structural validation cannot establish educational accuracy or prove applications, APIs, data sources or infrastructure work.

## Code-anchored curriculum

Modules: 6; lessons: 12; questions: 60. Each module names source paths in source_files, includes bounded excerpts, and explains visible imports/declarations before tracing behavior. Module count follows substantive implementation files with tests, configuration, and documentation topics included.

### Module sources

- streamlit-analytics-web-app-module-01: app.py, main.py
- streamlit-analytics-web-app-module-02: web/server.py, src/pipeline.py
- streamlit-analytics-web-app-module-03: web/api_impl.py
- streamlit-analytics-web-app-module-04: tests/test_pipeline.py
- streamlit-analytics-web-app-module-05: requirements.txt
- streamlit-analytics-web-app-module-06: README.md, app.py, main.py

Runtime status: no source application or test suite was executed or deployed. Structural validation cannot prove educational accuracy or runtime behavior. Human review should check source-specific feature claims, provider setup, dependency security, privacy, and operational safety.

### Documentation discrepancy

The source README calls the app "without Streamlit" while describing a Streamlit page and listing Streamlit in its stack and dependencies. Review this contradiction against the application code.

## Module relevance audit

6 modules were checked. Each names an implementation source file and each lesson contains an excerpt for every declared anchor. Lessons follow the beginner explanation → source-reading steps → source evidence sequence. This structural review confirms source linkage and sequence, not the accuracy of every explanation.
