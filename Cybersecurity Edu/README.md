# Cybersecurity learning packages

Portable, source-grounded educational packages for 22 repositories from C:\Foundev\Projects-main\Projects-main\05-cybersecurity. Each package is independent under projects/{slug}.

## Use

Read a project's README and prerequisites, then study modules in order. Assessments are student-facing; keep answer-key.json instructor-only. Source paths and short excerpts help establish evidence, but inspect the full upstream source to understand context.

## Limitations

No application was executed or deployed during generation. Security tools were not run against any target. Structural validation does not establish educational accuracy, application behavior, provider availability, deployment success, or security. Review reports for source-specific warnings and human/runtime review items.

## Contents

- projects/: 22 portable learning packages.
- schemas/: JSON schema documents.
- tools/validate_content.py: structural validator.
- reports/: project-specific inspection and validation summaries.
- dist/: one ZIP per project, each rooted at its project slug.

Python 3 is required to rerun the validator; Node.js was used to generate these packages.


## Curriculum review

See reports/module-relevance-audit.md for the module-to-code linkage and lesson sequence audit. All source applications remain unexecuted unless a report explicitly says otherwise.
