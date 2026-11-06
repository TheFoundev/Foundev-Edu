# Preprocessing and Sentence Embeddings: Inspect the project implementation of preprocessing and sentence embeddings

**Lesson ID:** `lesson-02-02`  
**Module:** Preprocessing and Sentence Embeddings  
**Source focus:** `src/preprocessor.py` → `clean_text`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TalentMatch Lens: Resume and Job Description Matching. By the end, you can describe all-MiniLM-L6-v2 and 384-dimensional vectors, trace the preprocessing and sentence embeddings implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about all-MiniLM-L6-v2 and 384-dimensional vectors. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

**The model.** `all-MiniLM-L6-v2` — a pretrained sentence-transformer (MiniLM architecture, 6 layers,
384-dim output, ~80–90 MB). It is used **zero-shot**: the repository contains no training script,
no dataset, no fine-tuning code and no evaluation metrics. Sentence-Transformers (rather than raw
BERT) is the right tool because BERT produces one vector *per token*; averaging those yields poor
sentence-level similarity, whereas a sentence-transformer is trained so the whole-text embedding is
directly comparable by cosine similarity.

**Normalisation.** `ResumeEmbedder.encode()` sets `normalize_embeddings=True`, so every vector has
unit length and cosine similarity equals the dot product.

**Scoring.** `cosine_similarity(jd_embedding, resume_embeddings)[0]` in `src/matcher.py` gives one
score in `[-1, 1]` per candidate. Cosine is chosen over Euclidean distance because it measures the
*angle* between vectors, not their magnitude — important because resume lengths vary widely and a
3-page resume should not out-score a 1-page one purely by containing more text.

**The explainability layer

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `src/preprocessor.py` and the source focus `clean_text`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.

## Step-by-step source investigation

1. Open `src/preprocessor.py` and inspect `clean_text`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/preprocessor.py` (not executed during package generation):

```python
def clean_text(text: str) -> str:
    """
    Lightly cleans text before embedding generation.

    We intentionally do NOT aggressively strip stopwords or lemmatize
    here, because sentence-transformer models expect natural, fluent
    text to produce the best embeddings. Over-cleaning would actually
    HURT embedding quality.

    Args:
        text: Raw extracted text.

    Returns:
        Cleaned text with normalized whitespace and no weird symbols.
    """
    # Remove email addresses and URLs (they add noise, not meaning)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    # Remove excessive special characters but keep basic punctuation
    text = re.sub(r"[^a-zA-Z0-9.,;:()/#+\-\s]", " ", text)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For preprocessing and sentence embeddings, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-02-02.md`](../exercises/exercise-02-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of preprocessing and sentence embeddings, identify its source location, and state a limitation. The key project-specific fact is: **The model.** `all-MiniLM-L6-v2` — a pretrained sentence-transformer (MiniLM architecture, 6 layers,
384-dim output, ~80–90 MB). It is used **zero-shot**: the repository contains no training script,
no dataset, no fine-tuning code and no evaluation metrics. Sentence-Transformers (rather than raw
BERT) is the right tool because BERT produces one vector *per token*; averaging those yields poor
sentence-level similarity, whereas a sentence-transformer is trained so the whole-text embedding is
directly comparable by cosine similarity.

**Normalisation.** `ResumeEmbedder.encode()` sets `normalize_embeddings=True`, so every vector has
unit length and cosine similarity equals the dot product.

**Scoring.** `cosine_similarity(jd_embedding, resume_embeddings)[0]` in `src/matcher.py` gives one
score in `[-1, 1]` per candidate. Cosine is chosen over Euclidean distance because it measures the
*angle* between vectors, not their magnitude — important because resume lengths vary widely and a
3-page resume should not out-score a 1-page one purely by containing more text.

**The explainability layer

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `src/preprocessor.py` and the source focus `clean_text`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
