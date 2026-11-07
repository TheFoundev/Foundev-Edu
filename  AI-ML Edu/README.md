# AI & Machine Learning Learning Content Library

This portable library contains source-aligned learning packages for 56 AI/ML source projects. It combines two batches into one curriculum:

- **Batch 1 — 20 projects:** the original AI/ML library.
- **Batch 2 — 36 projects:** the follow-on library generated from `/home/aziz/foundev/AI-ML`.

Each package has project documentation, prerequisites, setup and architecture guides, glossary, references, progressively structured lessons, practical exercises, student assessments, separate answer keys, final project requirements, and a mentor guide.

## Layout

- `projects/<slug>/` — one standalone package per source project (56 total).
- `schemas/` — shared JSON schemas for project metadata, modules, and assessments.
- `tools/build_ai_ml_packages.py` — reproducible batch-1 content-generation script and curated curriculum/source maps.
- `tools/build_36_ai_ml_packages.py` and `tools/build_36_core.py` — reproducible batch-2 builders.
- `tools/validate_content.py` — batch-1 structural validator; it cannot certify factual correctness.
- `tools/validate_content_36.py` — batch-2 structural validator; it cannot certify factual correctness.
- `reports/` — per-package structural results and human-review notes.
- `dist/` — 56 ZIP archives suitable for later upload.

`reports/module-source-audit.md` lists every module, its source paths, and the implementation symbol or code focus used in the lessons, grouped by batch. Each module is taught from basic terms toward that cited code.

Every module contains exactly ten MCQs (three basic, five intermediate, two advanced), four options each, and a separate answer key. Module counts vary from six to eight to fit project complexity. Source packages and application code are not copied into these educational packages.

## Rebuild and validate

Each build script reads the source directory configured at its top. Run the pair for the batch you are rebuilding:

```bash
# Batch 1 (20-project library)
python tools/build_ai_ml_packages.py
python tools/validate_content.py

# Batch 2 (36-project library)
python tools/build_36_ai_ml_packages.py
python tools/validate_content_36.py
```

Validation checks files, IDs, counts, answer-key shape, manifest inventory, and existence of cited source paths. It does not establish that an explanation or answer is technically correct. Read `reports/validation-report.md`, `reports/source-review.md`, and the individual project `architecture.md` / `final-project/solution-guide.md` before upload. Each validator writes only its own batch summary; the checked-in `reports/validation-summary.json` is the combined summary for all 56 packages.

## Portability and safety

The package folders and ZIPs are standalone learning materials and do not connect to Foundev or modify its application. Some projects require external data, model weights, APIs, databases, cameras, or local model runtimes not included here. Sensitive domains require consent, privacy controls, and meaningful human review; no learning demo should be treated as an automated decision system.
