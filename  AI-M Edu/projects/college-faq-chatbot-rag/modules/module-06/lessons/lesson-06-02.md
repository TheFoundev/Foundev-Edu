# Evaluation, Safety, and Operations: Inspect the project implementation of evaluation, safety, and operations

**Lesson ID:** `lesson-06-02`  
**Module:** Evaluation, Safety, and Operations  
**Source focus:** `scripts/evaluate.py` → `run_ragas_evaluation`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by CampusWise: College FAQ Retrieval-Augmented Generation. By the end, you can describe RAGAS, source attribution, privacy, and failure analysis, trace the evaluation, safety, and operations implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about RAGAS, source attribution, privacy, and failure analysis. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 8. Evaluation metrics (RAGAS)

`run_ragas_evaluation()` collects answers + contexts for the 8 ground-truth pairs and scores them with **faithfulness** (is the answer grounded in the retrieved context?), **answer relevancy** (does it address the question?), **context precision** (are the retrieved chunks relevant?) and **context recall** (were all the needed chunks retrieved?).

---

Connect this explanation to `src/evaluation/ragas_eval.py` and the source focus `run_ragas_evaluation`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: A local vector database and external LLM configuration are required; retrieved snippets can still be incomplete or wrong. The static console is not the Streamlit chat backend.

## Step-by-step source investigation

1. Open `src/evaluation/ragas_eval.py` and inspect `run_ragas_evaluation`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/evaluation/ragas_eval.py` (not executed during package generation):

```python
def run_ragas_evaluation(settings: Settings | None = None) -> pd.DataFrame:
    settings = settings or get_settings()

    # Collect responses via the production pipeline (identical to the UI).
    questions, contexts, answers = _collect_responses(settings)

    eval_data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truth": [str(item["ground_truth"]) for item in EVAL_QUESTIONS],
    }
    dataset = Dataset.from_dict(eval_data)

    # Build the RAGAS judge LLM and embeddings using the same credentials.
    embeddings = build_embeddings(settings)
    ragas_llm = ChatOpenAI(
        model=settings.llm_model,
        openai_api_key=settings.openrouter_api_key,
        openai_api_base=settings.openrouter_base_url,
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For evaluation, safety, and operations, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-06-02.md`](../exercises/exercise-06-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of evaluation, safety, and operations, identify its source location, and state a limitation. The key project-specific fact is: ### 8. Evaluation metrics (RAGAS)

`run_ragas_evaluation()` collects answers + contexts for the 8 ground-truth pairs and scores them with **faithfulness** (is the answer grounded in the retrieved context?), **answer relevancy** (does it address the question?), **context precision** (are the retrieved chunks relevant?) and **context recall** (were all the needed chunks retrieved?).

---

Connect this explanation to `src/evaluation/ragas_eval.py` and the source focus `run_ragas_evaluation`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
