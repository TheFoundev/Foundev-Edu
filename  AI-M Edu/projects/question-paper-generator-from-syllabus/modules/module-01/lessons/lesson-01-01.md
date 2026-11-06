# Syllabus and Chapter Selection: Understand board/class/subject and catalogue API

**Lesson ID:** `lesson-01-01`  
**Module:** Syllabus and Chapter Selection  
**Source focus:** `content_generate.py` → `fetch_textbooks_list`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe board/class/subject and catalogue API, trace the syllabus and chapter selection implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about board/class/subject and catalogue API. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

ExamForge contains **no trained model and no classical ML algorithm**. The "intelligence" is a
general-purpose LLM used in a constrained, verifiable way.

**Prompting contract.** Each generation route builds a `system_prompt` that pins the output shape:

- *MCQ*: one object per topic with `question`, `options` (exactly four), `correct_option`,
  `class`, `subject`, `chapter`, `topic`, `subtopic`.
- *Study material*: a single JSON object keyed by content type — `chaptersummaries1`,
  `definitionbank1`, `formulasheet1`, `importantpoints1`, `solvedexamples2`, plus quiz, FIB,
  true/false, HOTS and real-life-application sections.
- *FIB*: `paragraph`, `concepts` (8, ≤9 letters), `word_bank`, `questions` (8, each containing
  `______`), `answers` (8).

**Output sanitising.** `sanitize_ollama_json()` strips Markdown fences, removes trailing commas and
repairs a malformed `"answers"` block before `json.loads()`. If the result still fails to parse, the
UI shows "The AI model returned a malformed JSON object that could not be repaired."

**Answer verification by agreement.** `verify_answer_wi

[Excerpt shortened; consult the cited source guide for full detail.]

Connect this explanation to `content_generate.py` and the source focus `fetch_textbooks_list`.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `content_generate.py` and inspect `fetch_textbooks_list`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `content_generate.py` (not executed during package generation):

```python
def fetch_textbooks_list(api_url, board, class_name, subject):
    """Fetch textbooks and return s3_folder for the matching book."""
    try:
        # Cache the API response
        cache_path = os.path.join(DATA_DIR, 'allbooks.json')
        if os.path.exists(cache_path):
            with open(cache_path, 'r', encoding='utf-8') as f:
                textbooks = json.load(f)
            logger.info("Using cached allbooks.json")
        else:
            session = requests.Session()
            retries = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
            session.mount('https://', HTTPAdapter(max_retries=retries))
            response = session.get(api_url, headers={}, timeout=30)
            response.raise_for_status()
            textbooks = response.json()
            os.makedirs(DATA_DIR, exist_ok=True, mode=0o755)
            with open(cache_path, 'w', encoding='utf-8') as f:
                json.dump(textbooks, f, indent=4)
            logger.info(f"Cached allbooks.json to {cache_path}")
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For syllabus and chapter selection, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-01-01.md`](../exercises/exercise-01-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand board/class/subject and catalogue api, identify its source location, and state a limitation. The key project-specific fact is: Understand board/class/subject and catalogue API. In this repository, the claim must be grounded in the documented behavior and source paths: content_generate.py; app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
