# Architecture and source map

## Repository evidence

- `.github/workflows/test.yml`
- `README.rst`
- `docs/source/conf.py`
- `docs/source/readme.rst`
- `environment.yml`
- `readthedocs.yml`
- `requirements.txt`
- `rrmpg/__init__.py`
- `rrmpg/data/__init__.py`
- `rrmpg/data/camelsloader.py`
- `rrmpg/models/__init__.py`
- `rrmpg/models/abcmodel.py`
- `rrmpg/models/abcmodel_model.py`
- `rrmpg/models/basemodel.py`
- `rrmpg/models/cemaneige.py`
- `rrmpg/models/cemaneige_model.py`
- `rrmpg/models/cemaneige_utils.py`
- `rrmpg/models/cemaneigegr4j.py`
- `rrmpg/models/cemaneigegr4j_model.py`
- `rrmpg/models/cemaneigegr4jice.py`
- `rrmpg/models/cemaneigegr4jice_model.py`
- `rrmpg/models/cemaneigehyst_model.py`
- `rrmpg/models/cemaneigehystgr4j.py`
- `rrmpg/models/cemaneigehystgr4j_model.py`
- `rrmpg/models/cemaneigehystgr4jice.py`
- `rrmpg/models/cemaneigehystgr4jice_model.py`
- `rrmpg/models/gr4j.py`
- `rrmpg/models/gr4j_model.py`
- `rrmpg/models/hbvedu.py`
- `rrmpg/models/hbvedu_model.py`
- `rrmpg/models/icemelt_model.py`
- `rrmpg/tools/__init__.py`
- `rrmpg/tools/monte_carlo.py`
- `rrmpg/utils/__init__.py`
- `rrmpg/utils/array_checks.py`
- `rrmpg/utils/metrics.py`
- `rrmpg/utils/plot_utils.py`
- `rtd_environment.yml`
- `setup.py`
- `test/test_models.py`
- `test/test_tools.py`
- `test/test_utils.py`

## Reading path

Start with the README, then identify entry points and trace calls into reusable modules. Inspect inputs and outputs at each boundary, then compare tests and configuration. Filenames suggest roles but do not prove execution order.

## Documentation versus implementation

README excerpt for comparison (truncated to 8,000 characters):

> 

Treat these statements as claims. Confirm each against implementation. This package does not assert that every README feature exists, any test passes, or external integrations are live.
