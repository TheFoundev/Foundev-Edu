# Mentor solution guide — ExamForge: Syllabus-Based Question Generation

## Review approach

A strong submission follows the actual repository path rather than recreating features based on the catalogue title. Check `architecture.md`, all module source-file citations, and the source `PROJECT_OVERVIEW.md`/`WORKFLOW.md`.

## Expected solution characteristics
- Correctly identifies the algorithm/model and whether it is trained, pretrained, rule-based, retrieval-based, or only a heuristic.
- Names required artifacts and reports absent assets honestly.
- Keeps preprocessing consistent between training and inference.
- Selects metrics and split strategy appropriate to class balance, chronology, geography, or group structure.
- Includes understandable failure behavior and domain-specific ethical safeguards.

## Project-specific review notes

- The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

Do not award correctness for fabricated benchmark scores or claims that this package's examples ran. Review source evidence, tests, and limitations before accepting the demo.
