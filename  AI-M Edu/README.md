# AI & Machine Learning Learning Content Library

This portable library contains source-aligned learning packages for the 20 projects in the supplied AI/ML source folder. Each package has project documentation, prerequisites, setup and architecture guides, glossary, references, progressively structured lessons, practical exercises, student assessments, separate answer keys, final project requirements, and a mentor guide.

## Layout

- `projects/<slug>/` — one standalone package per source project.
- `schemas/` — shared JSON schemas for project metadata, modules, and assessments.
- `tools/build_ai_ml_packages.py` — reproducible content-generation script and curated curriculum/source maps.
- `tools/validate_content.py` — structural validator; it cannot certify factual correctness.
- `reports/` — per-package structural results and human-review notes.
- `dist/` — ZIP archives suitable for later upload.

`reports/module-source-audit.md` lists every module, its source paths, and the implementation symbol or code focus used in the lessons. Each module is taught from basic terms toward that cited code.

Every module contains exactly ten MCQs (three basic, five intermediate, two advanced), four options each, and a separate answer key. Module counts vary from six to eight to fit project complexity. Source packages and application code are not copied into these educational packages.

## Rebuild and validate

The build script reads the source directory configured at its top. Run:

```bash
python tools/build_ai_ml_packages.py
python tools/validate_content.py
```

Validation checks files, IDs, counts, answer-key shape, manifest inventory, and existence of cited source paths. It does not establish that an explanation or answer is technically correct. Read `reports/validation-report.md` and the individual project `architecture.md` / `final-project/solution-guide.md` before upload.

## Portability and safety

The package folders and ZIPs are standalone learning materials and do not connect to Foundev or modify its application. Some projects require external data, model weights, APIs, databases, cameras, or local model runtimes not included here. Sensitive domains require consent, privacy controls, and meaningful human review; no learning demo should be treated as an automated decision system.
