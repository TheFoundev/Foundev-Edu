# Similarity Is Not a Verdict: Inspect the project implementation of similarity is not a verdict

**Lesson ID:** `lesson-01-02`  
**Module:** Similarity Is Not a Verdict  
**Source focus:** `app.py` → `sentence_matches`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Similarity Radar: Document Similarity Checking. By the end, you can describe scope, text input, and limitations of similarity, trace the similarity is not a verdict implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about scope, text input, and limitations of similarity. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.8 What is explicitly *not* computed

- No TF-IDF vectors, no cosine similarity, no n-gram fingerprints, no embeddings.
- No comparison between the input and the fetched pages' *content* — only the URL of a
  search result is used.
- No semantic matching: a paraphrase is invisible to this method.
- No stored corpus, no historical index, no incremental update.

---

Connect this explanation to `app.py` and the source focus `sentence_matches`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.

## Step-by-step source investigation

1. Open `app.py` and inspect `sentence_matches`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def sentence_matches(sentence, result):
    """True when the sentence (or its distinctive phrase) is found in the result."""
    needle = normalize(sentence)
    if not needle:
        return False
    haystack = normalize(' '.join([result.get('title', ''), result.get('body', ''), result.get('url', '')]))
    if not haystack:
        return False
    if needle in haystack:
        return True
    phrase = phrase_of(sentence)
    if phrase and len(phrase.split()) >= 4 and phrase in haystack:
        return True
    tokens = [token for token in needle.split() if len(token) > 3]
    return len(tokens) >= 6 and all(token in haystack for token in tokens)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For similarity is not a verdict, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-02.md`](../exercises/exercise-01-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of similarity is not a verdict, identify its source location, and state a limitation. The key project-specific fact is: ### 7.8 What is explicitly *not* computed

- No TF-IDF vectors, no cosine similarity, no n-gram fingerprints, no embeddings.
- No comparison between the input and the fetched pages' *content* — only the URL of a
  search result is used.
- No semantic matching: a paraphrase is invisible to this method.
- No stored corpus, no historical index, no incremental update.

---

Connect this explanation to `app.py` and the source focus `sentence_matches`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
