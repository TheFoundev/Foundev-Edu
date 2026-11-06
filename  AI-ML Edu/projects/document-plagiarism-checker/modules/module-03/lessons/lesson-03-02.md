# Live Search and Source Pairing: Inspect the project implementation of live search and source pairing

**Lesson ID:** `lesson-03-02`  
**Module:** Live Search and Source Pairing  
**Source focus:** `app.py` → `scan_text`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Similarity Radar: Document Similarity Checking. By the end, you can describe web search results, pairing rule, and blocked domains, trace the live search and source pairing implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about web search results, pairing rule, and blocked domains. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.4 Stage 4 — The pairing rule (important)

```python
for j in range(len(list(search(...)))):
    if i != j:
        continue
    hasil_plagiarism.append(inputan[i])
    hasil_link.append(list(search(...))[j])
```

The `continue` short-circuits every result index except the one equal to the sentence
index. Consequences, stated plainly:

- Sentence 0 is checked against **result 0**, sentence 1 against **result 1**, and so on.
- With `num=10`, **only the first 10 sentences of a document can ever produce a match**;
  sentence 11 has no result index 11 to pair with.
- A sentence is counted as "matched" when *a* result exists at that index and its domain is
  not blocked — the sentence is not actually compared against that page's text.
- `search()` is invoked **twice per sentence** (once for the length, once for the element),
  so each sentence costs two HTTP round trips plus two 2-second pauses ≈ 4 s.

Connect this explanation to `app.py` and the source focus `scan_text`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.

## Step-by-step source investigation

1. Open `app.py` and inspect `scan_text`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def scan_text(text):
    """Look up every sentence and collect the ones found online."""
    sentences = split_sentences(text)
    matched_sentences = []
    matched_links = []
    engine_down = bool(sentences)
    for sentence in sentences:
        phrase = phrase_of(sentence)
        query = '"' + (phrase or sentence.strip().replace('"', "'")) + '"'
        results = search_results(query)
        if results is None:
            time.sleep(SEARCH_DELAY)
            continue
        engine_down = False
        for result in results:
            if is_blocked(result['url']):
                continue
            if sentence_matches(sentence, result):
                matched_sentences.append(sentence)
                matched_links.append(result['url'])
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For live search and source pairing, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-02.md`](../exercises/exercise-03-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of live search and source pairing, identify its source location, and state a limitation. The key project-specific fact is: ### 7.4 Stage 4 — The pairing rule (important)

```python
for j in range(len(list(search(...)))):
    if i != j:
        continue
    hasil_plagiarism.append(inputan[i])
    hasil_link.append(list(search(...))[j])
```

The `continue` short-circuits every result index except the one equal to the sentence
index. Consequences, stated plainly:

- Sentence 0 is checked against **result 0**, sentence 1 against **result 1**, and so on.
- With `num=10`, **only the first 10 sentences of a document can ever produce a match**;
  sentence 11 has no result index 11 to pair with.
- A sentence is counted as "matched" when *a* result exists at that index and its domain is
  not blocked — the sentence is not actually compared against that page's text.
- `search()` is invoked **twice per sentence** (once for the length, once for the element),
  so each sentence costs two HTTP round trips plus two 2-second pauses ≈ 4 s.

Connect this explanation to `app.py` and the source focus `scan_text`.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
