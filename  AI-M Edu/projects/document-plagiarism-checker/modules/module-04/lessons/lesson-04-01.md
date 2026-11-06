# Scoring and PDF/Pasted Input: Understand scoring calculation, upload flow, and result rendering

**Lesson ID:** `lesson-04-01`  
**Module:** Scoring and PDF/Pasted Input  
**Source focus:** `app.py` → `plagiarism`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by Similarity Radar: Document Similarity Checking. By the end, you can describe scoring calculation, upload flow, and result rendering, trace the scoring and pdf/pasted input implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about scoring calculation, upload flow, and result rendering. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

### 7.6 Stage 6 — Scoring

```python
count      = len(inputan)                # total sentences
count_hasil = len(hasil_link_final)      # matches that survived the filter
hasil_persen += (count_hasil / count) * 100
```

The similarity index is a **share of sentences that had a hit**, in percent. It is *not*
a percentage of copied characters, *not* a per-sentence similarity and *not* comparable
with Turnitin's number. The UI labels it accordingly: *"similarity index · matched ÷ total
sentences"* (`templates/index.html:166`).

Connect this explanation to `app.py` and the source focus `plagiarism`.

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

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For scoring and pdf/pasted input, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-04-01.md`](../exercises/exercise-04-01.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now understand scoring calculation, upload flow, and result rendering, identify its source location, and state a limitation. The key project-specific fact is: Understand scoring calculation, upload flow, and result rendering. In this repository, the claim must be grounded in the documented behavior and source paths: app.py; templates/index.html.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
