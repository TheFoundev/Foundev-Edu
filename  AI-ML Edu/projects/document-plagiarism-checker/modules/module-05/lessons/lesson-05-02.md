# Flask Routes and State: Inspect the project implementation of flask routes and state

**Lesson ID:** `lesson-05-02`  
**Module:** Flask Routes and State  
**Source focus:** `app.py` → `plagiarism`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Similarity Radar: Document Similarity Checking. By the end, you can describe request/response, stored scans, and front-end integration, trace the flask routes and state implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about request/response, stored scans, and front-end integration. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `plagiarism` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for request/response, stored scans, and front-end integration. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The repository uses live web search and source-pair scoring, not the advertised TF-IDF/local corpus model. Similarity is not proof of plagiarism; provider availability and document privacy require review.

## Step-by-step source investigation

1. Open `app.py` and inspect `plagiarism`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `app.py` (not executed during package generation):

```python
def plagiarism(name):
    text = ""
    try:
        if request.method == 'POST':
            posted_text = request.form.get('text', '')
            upload = request.files.get('file')
            filename = upload.filename if upload else ''
            if posted_text != '' and filename == '':
                with open(WORD_FILE, 'w', encoding='utf-8') as f:
                    f.write(posted_text)
                text = posted_text
            elif filename != '' and posted_text == '':
                if not allowed_file(filename):
                    flash('Only PDF files are allowed')
                    return redirect(url_for('index'))
                saved = save_upload(upload)
                text = extract_pdf_text(os.path.join(app.config['UPLOAD_FOLDER'], saved))
            else:
                flash('Please fill the form')
                return redirect(request.url)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For flask routes and state, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-02.md`](../exercises/exercise-05-02.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now inspect the project implementation of flask routes and state, identify its source location, and state a limitation. The key project-specific fact is: The source-specific focus for this module is `plagiarism` in `app.py`. Use the excerpt below to trace the actual inputs, transformation, and output for request/response, stored scans, and front-end integration. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
