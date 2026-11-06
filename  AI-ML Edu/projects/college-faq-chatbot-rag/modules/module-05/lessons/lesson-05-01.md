# Grounded Generation and Streamlit: Understand prompt context, optional rewriting, and chat flow

**Lesson ID:** `lesson-05-01`  
**Module:** Grounded Generation and Streamlit  
**Source focus:** `src/rag_chain.py` → `ask`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe prompt context, optional rewriting, and chat flow, trace the grounded generation and streamlit implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about prompt context, optional rewriting, and chat flow. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 6. Grounded prompting

`build_system_prompt()` instructs the model to answer only from the provided excerpts, to use partial matches rather than refusing unnecessarily, to never use its own knowledge, and to quote the exact refusal sentence when nothing is found. `build_user_prompt()` injects the numbered context blocks and the original question.

Connect this explanation to `src/rag_chain.py` and the source focus `ask`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `src/rag_chain.py` and inspect `ask`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/rag_chain.py` (not executed during package generation):

```python
def ask(self, question: str) -> ChatResponse:
        original = question.strip()
        if not original:
            return ChatResponse(answer="Please enter a question.", refused=True)

        # --- Step 1: Normalize (cheap, always on) ---
        normalized = normalize_query(original)
        logger.debug("Normalized: %r -> %r", original, normalized)

        # --- Step 2: LLM rewrite (optional, can be disabled in settings) ---
        if self._rewriter and self._settings.enable_query_rewriting:
            rewritten = self._rewriter.rewrite(normalized)
        else:
            rewritten = normalized
        logger.debug("Rewritten:  %r -> %r", normalized, rewritten)

        # --- Step 3: Retrieve with rewritten query ---
        retrieval = self._retriever.retrieve(
            query=original,
            rewritten_query=rewritten,
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For grounded generation and streamlit, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-01.md`](../exercises/exercise-05-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand prompt context, optional rewriting, and chat flow, identify its source location, and state a limitation. The key project-specific fact is: Understand prompt context, optional rewriting, and chat flow. In this repository, the claim must be grounded in the documented behavior and source paths: src/rag_chain.py; src/prompt.py; app/app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
