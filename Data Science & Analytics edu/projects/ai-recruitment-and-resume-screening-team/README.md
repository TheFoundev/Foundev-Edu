# Ai Recruitment And Resume Screening Team

This package was generated from the repository inventory and inspected source excerpts. Source code/configuration is authoritative where documentation differs. Structural content validation does not validate educational accuracy or prove the application works.

## Purpose and use cases

# AI Recruitment and Resume Screening Team

Rank resumes against a job description with skills and a small classifier.

> Automate a hiring pipeline with collaborating agents that parse resumes, match skills to job descriptions, shortlist candidates and draft interview questions.

## Overview

An original, self-contained implementation of the **AI Recruitment and Resume Screening Team** concept, built for the Foundev portfolio. It focuses on the core workflow described in the project brief and keeps the architecture small enough to read end to end.

## Features

- A resume parser that reads the facts (the years, the degree, the number of
  the projects and the skills) out of the text of the resume
- A logistic regression over the text, with the candidates stored in SQLite
- The interview questions drafted from the resume: a question for every skill
  it mentions, a question for every skill of the job it does not mention, and
  a few general ones
- A read-only dashboard over the candidates

## Stack

`Python; CrewAI; Streamlit; SQLite`

The CSV stack is CrewAI + Streamlit + SQLite. CrewAI and Streamlit are not installed, so the pipeline uses a small classifier and Flask with a SQLite table.

## Run

```bash
pip install -r requirements.txt
python main.py train
python app.py
python main.py demo
pytest -q
```

## Structure

```text
ai-recruitment-and-resume-screening-team/
├── main.py                 train / demo CLI
├── src/data.py             dataset builder
├── src/model.py            model and evaluation
├── tests/test_pipeline.py  smoke test
├── requirements.txt
├── app.py

## Actual features and limits

README feature statements (verify each against code before relying on it):
- A resume parser that reads the facts (the years, the degree, the number of
- A logistic regression over the text, with the candidates stored in SQLite
- The interview questions drafted from the resume: a question for every skill
- A read-only dashboard over the candidates
- Resumes are synthetic; no real applicant data is used.
- The label is generated from a simple skills/experience policy, so the model learns that policy.
- There is no PDF parsing, bias audit or human-in-the-loop review.

The implementation inventory includes 15 files (excluding caches and vendor/dependency directories). Generated content is a learning guide, not an application feature. External services, data sources, and runtime behavior are not presumed available.

## Requirements and setup

Inspect `requirements.txt`. Follow [setup-guide.md](setup-guide.md). No setup or application execution was performed while producing this package.

## Architecture and important components

See [architecture.md](architecture.md). Source evidence examined:
- `README.md`
- `app.py`
- `main.py`
- `requirements.txt`
- `src/__init__.py`
- `src/data.py`
- `src/model.py`
- `tests/test_pipeline.py`
- `web/assets/app.js`

## Testing

Test-related paths found: tests/test_pipeline.py. Presence of tests is not evidence they passed; none were run.

## Security

Review secrets, input validation, data privacy, package versions, and deployment defaults before real use. Do not commit credentials or expose local databases/data. See SECURITY or deployment files if present; human review is required.

## Troubleshooting

Check the documented interpreter/runtime version, install from the project dependency manifest in an isolated environment, inspect required environment variables and data paths, then use the project tests as written. Resolve mismatches against source rather than inventing setup values.

## Expected learning outcome

You should be able to explain the repository's evidenced data/code flow, distinguish implementation from claims, and propose a testable safe extension.

## Further learning

Read the original repository README and official references in references.json.
