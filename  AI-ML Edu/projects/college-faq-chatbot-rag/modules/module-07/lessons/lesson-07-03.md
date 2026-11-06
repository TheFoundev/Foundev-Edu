# Retrieval Debugging Lab: Validate outputs and identify limitations for retrieval debugging lab

**Lesson ID:** `lesson-07-03`  
**Module:** Retrieval Debugging Lab  
**Source focus:** `src/query_rewriter.py` → `rewrite`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe query normalization, empty retrieval, and chunk inspection, trace the retrieval debugging lab implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about query normalization, empty retrieval, and chunk inspection. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 2. BM25 keyword retrieval with rank-derived scores

`BM25Retriever.from_documents(all_chunks, k=top_k)` is built over the in-memory chunk list. Because BM25 returns no numeric scores through this interface, the code converts **rank** into a synthetic score:

```
score = max(0.5, 0.75 - rank * (0.25 / n))
```

so the best keyword hit scores `0.75` and the last one `0.50`.

Connect this explanation to `src/query_rewriter.py` and the source focus `rewrite`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `src/query_rewriter.py` and inspect `rewrite`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/query_rewriter.py` (not executed during package generation):

```python
def rewrite(self, query: str) -> str:
        """Return a rewritten, search-friendly version of *query*.

        Falls back to the original query on any error to avoid breaking
        the retrieval pipeline.
        """
        if not query or not query.strip():
            return query

        try:
            response = self._llm.invoke(
                [
                    SystemMessage(content=_SYSTEM_PROMPT),
                    HumanMessage(content=query.strip()),
                ]
            )
            rewritten = response.content.strip()
            if rewritten:
                logger.debug("Query rewrite: %r -> %r", query, rewritten)
                return rewritten
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For retrieval debugging lab, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-07-03.md`](../exercises/exercise-07-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for retrieval debugging lab, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for retrieval debugging lab. In this repository, the claim must be grounded in the documented behavior and source paths: src/query_rewriter.py; scripts/evaluate_retrieval.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
