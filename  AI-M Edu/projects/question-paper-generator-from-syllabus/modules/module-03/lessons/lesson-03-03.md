# Prompt Contracts and Local LLM: Validate outputs and identify limitations for prompt contracts and local llm

**Lesson ID:** `lesson-03-03`  
**Module:** Prompt Contracts and Local LLM  
**Source focus:** `content_generate.py` → `generate_content_with_ollama`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by ExamForge: Syllabus-Based Question Generation. By the end, you can describe Ollama llama2, constrained generation, and output validation, trace the prompt contracts and local llm implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about Ollama llama2, constrained generation, and output validation. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `generate_content_with_ollama` in `content_generate.py`. Use the excerpt below to trace the actual inputs, transformation, and output for Ollama llama2, constrained generation, and output validation. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The app depends on remote curriculum catalogue and a local Ollama llama2 service; question correctness is not guaranteed. Requirements omit dependencies noted in workflow; teacher review is mandatory.

## Step-by-step source investigation

1. Open `content_generate.py` and inspect `generate_content_with_ollama`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `content_generate.py` (not executed during package generation):

```python
def generate_content_with_ollama(prompt, content_type, chapter_number, chapter_name, text_limit=200):
    """Generate content using Ollama for a specific content type."""
    try:
        prompt_templates = {
            "Chapter Summaries": f"Summarize the following chapter content in {text_limit} words or less, suitable for a class 10 student:\n{prompt}",
            "Important Points": f"List 5-7 key points or formulas from the following chapter content, in simple language:\n{prompt}",
            "Definition Bank": f"Extract 3-5 key terms and their definitions from the following chapter content, in simple words:\n{prompt}",
            "Formula Sheet": f"List all formulas from the following chapter content with a brief explanation for each:\n{prompt}",
            "Concept Explanation": f"Explain the main concepts from the following chapter content in simple terms, suitable for a class 10 student:\n{prompt}",
            "Solved Examples": f"Create 2-3 solved example problems based on the following chapter content:\n{prompt}",
            "Practice Questions": f"Generate 5 practice questions (with answers) based on the following chapter content:\n{prompt}",
            "Quiz Creation": f"Create a 5-question multiple-choice quiz (with 4 options and correct answers) based on the following chapter content:\n{prompt}",
            "Fill in the Blanks": f"Generate 5 fill-in-the-blank questions (with answers) based on the following chapter content:\n{prompt}",
            "True/False": f"Generate 5 true/false questions (with answers) based on the following chapter content:\n{prompt}",
            "Higher Order Thinking (HOTS)": f"Generate 3 higher-order thinking questions based on the following chapter content:\n{prompt}",
            "Real Life Applications": f"Describe 2-3 real-life applications of the concepts in the following chapter content:\n{prompt}"
        }

        final_prompt = prompt_templates.get(content_type, prompt)
        response = ollama.generate(model='llama3', prompt=final_prompt)
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For prompt contracts and local llm, use the repository's own output format and the available test fixture where possible.

## Practical exercise

Complete [`exercise-03-03.md`](../exercises/exercise-03-03.md).

## Common mistakes and debugging

- Confusing a visual mockup or demo heuristic with the model/pipeline implementation.
- Assuming an absent data file, weight, service, or credential is bundled.
- Reporting accuracy without checking class balance, split strategy, or an appropriate baseline.
- Editing a pipeline before establishing input shape and output contract.
- Treating confidence/similarity as calibrated probability or proof.

## Best practices and responsible use

Keep data provenance and split boundaries explicit, make errors visible, log no sensitive raw inputs unnecessarily, and retain a human correction path for consequential outputs. Test failure and missing-artifact cases as well as the happy path.

## Summary

You can now validate outputs and identify limitations for prompt contracts and local llm, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for prompt contracts and local llm. In this repository, the claim must be grounded in the documented behavior and source paths: content_generate.py; app.py.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
