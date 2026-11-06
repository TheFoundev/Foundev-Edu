# Text Extraction and Input Boundaries: Inspect the project implementation of text extraction and input boundaries

**Lesson ID:** `lesson-01-02`  
**Module:** Text Extraction and Input Boundaries  
**Source focus:** `src/extractor.py` → `extract_text_from_pdf`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by TalentMatch Lens: Resume and Job Description Matching. By the end, you can describe resume documents, job descriptions, and parsing, trace the text extraction and input boundaries implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about resume documents, job descriptions, and parsing. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `extract_text_from_pdf` in `src/extractor.py`. Use the excerpt below to trace the actual inputs, transformation, and output for resume documents, job descriptions, and parsing. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The embedding model is used zero-shot and no evaluation/training data is supplied. Similarity can encode proxy bias and must not rank or reject applicants without meaningful human review.

## Step-by-step source investigation

1. Open `src/extractor.py` and inspect `extract_text_from_pdf`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `src/extractor.py` (not executed during package generation):

```python
def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts all text from a PDF file, page by page.

    Args:
        file_bytes: Raw bytes of the uploaded PDF file.

    Returns:
        A single string containing all extracted text.
    """
    text_chunks = []
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # Some pages (e.g., scanned images) may return None
                text_chunks.append(page_text)
    return "\n".join(text_chunks)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For text extraction and input boundaries, use the repository's own output format and the available test fixture where possible.

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

You can now inspect the project implementation of text extraction and input boundaries, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `extract_text_from_pdf` in `src/extractor.py`. Use the excerpt below to trace the actual inputs, transformation, and output for resume documents, job descriptions, and parsing. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
