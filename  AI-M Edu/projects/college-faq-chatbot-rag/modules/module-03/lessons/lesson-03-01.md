# Chroma Retrieval and MMR: Understand candidate retrieval, diversity, and relevance

**Lesson ID:** `lesson-03-01`  
**Module:** Chroma Retrieval and MMR  
**Source focus:** `src/vector_store.py` → `_semantic_retrieve`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe candidate retrieval, diversity, and relevance, trace the chroma retrieval and mmr implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about candidate retrieval, diversity, and relevance. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 1. MMR (Maximal Marginal Relevance) semantic search

`self._vector_store.max_marginal_relevance_search(query, k=k, fetch_k=fetch_k, lambda_mult=lambda_mult)` selects chunks that are relevant *and* mutually diverse. With `lambda_mult = 0.5` the trade-off is balanced: `0` favours diversity, `1` favours relevance. `fetch_k = 20` candidates are pulled from ChromaDB before the diversity pass.

Connect this explanation to `src/retriever.py` and the source focus `_semantic_retrieve`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `src/retriever.py` and inspect `_semantic_retrieve`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/retriever.py` (not executed during package generation):

```python
def _semantic_retrieve(self, query: str, k: int) -> list[tuple[Document, float]]:
        """MMR-based semantic retrieval with post-hoc scoring."""
        fetch_k = max(k * 2, self._settings.fetch_k)
        try:
            mmr_docs = self._vector_store.max_marginal_relevance_search(
                query,
                k=k,
                fetch_k=fetch_k,
                lambda_mult=self._settings.lambda_mult,
            )
            # Retrieve scores post-hoc via a broader similarity search
            scored = self._vector_store.similarity_search_with_relevance_scores(
                query, k=fetch_k
            )
            score_map: dict[str, float] = {d.page_content[:80]: s for d, s in scored}
            pairs: list[tuple[Document, float]] = []
            for doc in mmr_docs:
                key = doc.page_content[:80]
                pairs.append((doc, score_map.get(key, 0.0)))
            return pairs
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For chroma retrieval and mmr, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-01.md`](../exercises/exercise-03-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand candidate retrieval, diversity, and relevance, identify its source location, and state a limitation. The key project-specific fact is: Understand candidate retrieval, diversity, and relevance. In this repository, the claim must be grounded in the documented behavior and source paths: src/vector_store.py; src/retriever.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
