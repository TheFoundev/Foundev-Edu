# Hybrid Ranking and Adaptive Retrieval: Validate outputs and identify limitations for hybrid ranking and adaptive retrieval

**Lesson ID:** `lesson-04-03`  
**Module:** Hybrid Ranking and Adaptive Retrieval  
**Source focus:** `src/retriever.py` → `_hybrid_retrieve`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe BM25, weighted fusion, adaptive-k, and relevance gate, trace the hybrid ranking and adaptive retrieval implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about BM25, weighted fusion, adaptive-k, and relevance gate. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 3. Weighted hybrid fusion

In `_hybrid_retrieve()` the two lists are merged on the first 120 characters of the page content:

```
final = 0.7 * semantic_score  +  0.3 * bm25_rank_score
```

Duplicates are combined rather than repeated, and the merged list is truncated to `k` and sorted descending.

Connect this explanation to `src/retriever.py` and the source focus `_hybrid_retrieve`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `src/retriever.py` and inspect `_hybrid_retrieve`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/retriever.py` (not executed during package generation):

```python
def _hybrid_retrieve(self, query: str, k: int) -> tuple[list[Document], list[float]]:
        """Merge semantic (70%) + BM25 (30%), de-duplicate, sort by combined score."""
        semantic_pairs = self._semantic_retrieve(query, k)

        if self._bm25 is not None:
            bm25_pairs = self._bm25_retrieve(query, k)
        else:
            bm25_pairs = []

        # Weighted merge keyed on first 120 chars of page content
        merged: dict[str, tuple[Document, float]] = {}

        for doc, score in semantic_pairs:
            key = doc.page_content[:120]
            merged[key] = (doc, score * 0.7)

        for doc, score in bm25_pairs:
            key = doc.page_content[:120]
            if key in merged:
                existing_doc, existing_score = merged[key]
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For hybrid ranking and adaptive retrieval, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-03.md`](../exercises/exercise-04-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for hybrid ranking and adaptive retrieval, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for hybrid ranking and adaptive retrieval. In this repository, the claim must be grounded in the documented behavior and source paths: src/retriever.py; src/query_normalizer.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
