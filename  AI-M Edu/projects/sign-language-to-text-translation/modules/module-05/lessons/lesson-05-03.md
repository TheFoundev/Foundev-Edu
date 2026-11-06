# CLI, Library, and Static Demo: Validate outputs and identify limitations for cli, library, and static demo

**Lesson ID:** `lesson-05-03`  
**Module:** CLI, Library, and Static Demo  
**Source focus:** `sign_language_translator/cli.py` → `runPipeline`

## Purpose and learning objectives

This lesson begins with an everyday explanation and then follows the implementation used by SignBridge: Rule-Based Sign Language Text Translation. By the end, you can describe slt command, package structure, UI limitations, trace the cli, library, and static demo implementation to source code, and identify one way it can fail.

## Prerequisites

Basic Python and the project setup guide. For later lessons, first complete the preceding lesson in this module.

## The idea in plain language

In everyday language, this module is about slt command, package structure, UI limitations. First understand what information enters this stage, what it changes, and what it sends onward.

## What this project actually implements

The source-specific focus for this module is `runPipeline` in `js/app.js`. Use the excerpt below to trace the actual inputs, transformation, and output for slt command, package structure, UI limitations. Where a behavior is absent, follow the documented boundary rather than assuming it exists.

This is a source-grounded description, not a claim that code was run. The repository-specific limitation to keep visible is: The core is rule-based gloss restructuring and token-to-clip mapping, not video recognition or general language translation. Clip coverage and dialect/culture constraints need signer review.

## Step-by-step source investigation

1. Open `js/app.js` and inspect `runPipeline`.
2. Read its inputs and output, then follow its caller and the next step in the data flow.
3. Record the data representation at each boundary (text, image, table, vector, score, or response).
4. Inspect validation, fallback, and exception behavior.
5. Compare the behavior with `PROJECT_OVERVIEW.md` and `WORKFLOW.md`; report any contradiction instead of silently choosing a claim.

## Code-reading example

Source excerpt from `js/app.js` (not executed during package generation):

```javascript
function runPipeline() {
    var text = inputText ? inputText.value : "";
    updateCounters(text);

    if (!text.trim()) {
      renderEmptyAll();
      if (cliCmd) cliCmd.textContent = buildCliCommand("<text>");
      setStatus("Nothing to translate \u2014 type a sentence in station 01.");
      return;
    }

    var tagged = tokenizeTag(text, currentLang);
    renderTokens(tagged);

    var result = currentLang === "en"
      ? restructureEnglish(tagged)
      : restructurePassthrough(tagged);
```

Read the arguments first, trace the transformation and conditions, then locate the returned value or side effect. This source excerpt was not executed during package generation.

## Expected behavior

A correct investigation yields a traceable input → processing → result path, a source citation, and one explicit caveat. For cli, library, and static demo, use the repository's own output format and the available test fixture where possible.

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

You can now validate outputs and identify limitations for cli, library, and static demo, identify its source location, and state a limitation. The key project-specific fact is: Validate outputs and identify limitations for cli, library, and static demo. In this repository, the claim must be grounded in the documented behavior and source paths: sign_language_translator/cli.py; index.html; js/app.js.

## Knowledge check

1. What input enters this stage, and what output leaves it?
2. Which source path proves the behavior?
3. What assumption would make the output unreliable?

## References

- The matching source repository files `PROJECT_OVERVIEW.md` and `WORKFLOW.md` (paths relative to that repository).
- [Python documentation](https://docs.python.org/3/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
