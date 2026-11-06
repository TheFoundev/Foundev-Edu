# PDF/OMR Companion Tools: Validate outputs and identify limitations for pdf/omr companion tools

**Lesson ID:** `lesson-05-03`  
**Module:** PDF/OMR Companion Tools  
**Source focus:** `omr_generator_app.py` → `OMRGenerator`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe separate utilities and app boundaries, trace the pdf/omr companion tools implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about separate utilities and app boundaries. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `OMRGenerator` in `omr_pdf.py`. Use the excerpt below to trace the actual inputs, transformation, and output for separate utilities and app boundaries. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `omr_pdf.py` and inspect `OMRGenerator`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `omr_pdf.py` (not executed during package generation):

```python
class OMRGenerator(FPDF):
    def __init__(self, subject_questions):
        super().__init__()
        self.subjects = ["Mathematics-1", "Mathematics-2", "Physics", "Chemistry", "MAT"]
        self.subject_questions = subject_questions  # List of 5 integers
        self.total_questions = sum(subject_questions)
        self.bubble_diameter = 4.5
        self.page_height = 297
        self.page_width = 210
        self.set_auto_page_break(auto=False)
        self.set_font("Helvetica", "", 8)
        self.options = ['a', 'b', 'c', 'd']

    def header(self):
        img_size = 15
        # Top corners
        self.image("img1.jpg", x=10, y=10, w=img_size, h=img_size)
        self.image("img1.jpg", x=self.page_width - img_size - 10, y=10, w=img_size, h=img_size)
        # Bottom corners (adjusted upward to prevent overlap with signatures)
        self.image("img1.jpg", x=10, y=self.page_height - img_size - 5, w=img_size, h=img_size)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For pdf/omr companion tools, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-05-03.md`](../exercises/exercise-05-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for pdf/omr companion tools, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for pdf/omr companion tools. In this repository, the claim must be grounded in the documented behavior and source paths: omr_generator_app.py; generator.py; omr_pdf.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
