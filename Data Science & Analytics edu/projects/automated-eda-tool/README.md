# Automated Eda Tool

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./frontend/src/components/Autd.svg" />
  <source media="(prefers-color-scheme: light)" srcset="./frontend/src/components/Aut.svg" />
  <img src="path/to/light-logo.png" alt="Project Logo" width="250" />
</picture>

</div>

---

# ⚡ AutoEDA - Automated Data Preprocessing Toolkit

![GitHub repo size](https://img.shields.io/github/repo-size/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit?color=brightgreen)
![GitHub contributors](https://img.shields.io/github/contributors/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
![GitHub last commit](https://img.shields.io/github/last-commit/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
![Issues](https://img.shields.io/github/issues/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
![License](https://img.shields.io/github/license/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit)
![GitHub Stars](https://img.shields.io/github/stars/Nidhi-Satyapriya/AutoEDA-Automated-Data-Preprocessing-Toolkit?style=flat-square)

> ⚡ Automate tedious data cleaning — focus more on insights, not pipelines.

---

## 📌 Table of Contents

* [🔍 Overview](#-overview)
* [✨ Key Features](#-key-features)
* [🧱 Project Architecture](#-project-architecture)
* [📦 Requirements](#-requirements)
* [🚀 Getting Started](#-getting-started)
* [🤝 How to Contribute](#-how-to-contribute)
* [🛡 License](#-license)
* [📬 Contact](#-contact)

## 🔍 Overview

AutoEDA is a lightweight yet powerful toolkit that streamlines da

## Actual features and limits

README feature statements (verify each against code before relying on it):
- [🔍 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🧱 Project Architecture](#-project-architecture)
- [📦 Requirements](#-requirements)
- [🚀 Getting Started](#-getting-started)
- [🤝 How to Contribute](#-how-to-contribute)
- [🛡 License](#-license)
- [📬 Contact](#-contact)
- ✅ Seamless CSV upload & schema validation
- ✅ Null value imputation & type inference
- ✅ Smart duplicate detection & cleanup
- ✅ Feature extraction and transformation

The implementation inventory includes 138 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `backend/requirements.txt, frontend/package.json, package.json`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `.github/workflows/ci.yml`
- `README.md`
- `autoeda/__init__.py`
- `autoeda/data_optimizer.py`
- `autoeda/encoding_categorical.py`
- `autoeda/feat_scaling.py`
- `autoeda/feature_selector.py`
- `autoeda/notebook_data_optimization.py`
- `autoeda/null_handler.py`
- `autoeda/outliers.py`
- `autoeda/pca_transformer.py`
- `autoeda/pipeline.py`
- `autoeda/summary_stats.py`
- `autoeda/test_notebook_data_optimization.py`
- `autoeda/test_null_handler.py`
- `backend/DOCKERFILE`
- `backend/README.md`
- `backend/app.py`
- `backend/config/database.js`
- `backend/docker-compose.yml`
- `backend/requirements.txt`
- `backend/router/file_router.py`
- `backend/services/run_data_optimization_test.py`
- `backend/services/runner.py`
- `docker-compose.yml`
- `frontend/DOCKERFILE`
- `frontend/README.md`
- `frontend/eslint.config.js`
- `frontend/package.json`
- `frontend/postcss.config.js`
- `frontend/src/App.jsx`
- `frontend/src/components/About.jsx`
- `frontend/src/components/Auth.jsx`
- `frontend/src/components/Contact.jsx`
- `frontend/src/components/Dashboard.jsx`
- `frontend/src/components/FileUpload.jsx`
- `frontend/src/components/Footer.jsx`
- `frontend/src/components/Home.jsx`
- `frontend/src/components/HowItWorks.jsx`
- `frontend/src/components/Navbar.jsx`
- `frontend/src/components/scrollCard.jsx`
- `frontend/src/components/theme-provider.jsx`
- `frontend/src/components/ui/button.jsx`
- `frontend/src/components/ui/card.jsx`
- `frontend/src/components/ui/input.jsx`
- `frontend/src/components/userProfile.jsx`
- `frontend/src/lib/utils.js`
- `frontend/src/main.jsx`
- `frontend/tailwind.config.js`
- `frontend/vite.config.js`
- `package.json`
- `run_cleaning.py`
- `unit_tests/__init__.py`
- `unit_tests/outlier_test.py`
- `unit_tests/test_data_optimizer.py`
- `unit_tests/test_encoding_categorical.py`
- `unit_tests/test_feat_scaling.py`
- `unit_tests/test_feature_selector.py`
- `unit_tests/test_pca_transformer.py`

## Testing

Test-related paths found: autoeda/test_notebook_data_optimization.py, autoeda/test_null_handler.py, backend/output/standalone_outlier_tests/autoEDA_outlier_report.json, backend/output/standalone_outlier_tests/autoEDA_outlier_summary.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_capped.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_flagged.csv, backend/output/standalone_outlier_tests/autoEDA_outliers_removed.csv, backend/services/run_data_optimization_test.py, unit_tests/.gitignore, unit_tests/__init__.py, unit_tests/outlier_test.py, unit_tests/test_data_optimizer.py, unit_tests/test_encoding_categorical.py, unit_tests/test_feat_scaling.py, unit_tests/test_feature_selector.py, unit_tests/test_pca_transformer.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
