# Capstone and Deployment Boundaries: Understand static console versus backend, config, and production gaps

**Lesson ID:** `lesson-08-01`  
**Module:** Capstone and Deployment Boundaries  
**Source focus:** `config/settings.py` → `Settings`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe static console versus backend, config, and production gaps, trace the capstone and deployment boundaries implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about static console versus backend, config, and production gaps. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `Settings` in `config/settings.py`. Use the excerpt below to trace the actual inputs, transformation, and output for static console versus backend, config, and production gaps. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `config/settings.py` and inspect `Settings`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `config/settings.py` (not executed during package generation):

```python
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8-sig",   # handles BOM produced by Windows editors
        extra="ignore",
    )

    # --- API ---
    openrouter_api_key: str = ""
    openrouter_site_url: str = "http://localhost:8501"
    openrouter_app_name: str = "College FAQ Chatbot"

    # --- Branding (make the app your own) ---
    institution_name: str = "Your College"
    app_title: str = "College FAQ Chatbot"
    app_icon: str = "🎓"
    knowledge_base_label: str = "knowledge_base.docx"

    # --- Models ---
    llm_model: str = "openai/gpt-4o-mini"
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For capstone and deployment boundaries, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-08-01.md`](../exercises/exercise-08-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand static console versus backend, config, and production gaps, identify its source location, and state a limitation. The key project-specific fact is: Understand static console versus backend, config, and production gaps. In this repository, the claim must be grounded in the documented behavior and source paths: config/settings.py; WORKFLOW.md.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
