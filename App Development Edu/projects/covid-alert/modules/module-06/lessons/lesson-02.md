# Verify behavior and avoid overstating results: Trace the source

**Lesson ID:** `covid-alert-06-tests-privacy-and-accessibility-lesson-02`  
**Module ID:** `covid-alert-06-tests-privacy-and-accessibility`  
**Source focus:** `test/exposure.test.ts` → `exposure.test`

## Purpose and learning objectives

Open `test/exposure.test.ts` and locate `exposure.test`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Verify behavior and avoid overstating results** is like following one item through a workshop: locate the input, see what changes, then find the output. Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device.

### Step toward the implementation

Open `test/exposure.test.ts` and locate `exposure.test`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `test/exposure.test.ts`, `src/components.tsx`, `README.md`.

## Source evidence

Excerpt from [`test/exposure.test.ts`](../../../../../../App%20Development/covid-alert/test/exposure.test.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```text
Source excerpt unavailable; inspect this source path and locate the focus symbol before teaching this module.
```

### Read it step by step

1. Find the focus cue `exposure.test` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Verify behavior and avoid overstating results**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

## Practical exercise

Complete [`exercise-01.json`](../exercises/exercise-01.json). Add an input or edge case, cite the source, and write the expected result before changing code.

## Common mistakes and debugging

- Inferring feature behavior from the product name or screen alone.
- Skipping the caller, model/state layer, or error path.
- Treating local sample data or a mock response as a real service result.
- Debug by tracing input → validation → transformation → output and then checking the relevant test.

## Best practices and security

Protect credentials and personal data, validate untrusted inputs, request only necessary device permissions, and keep provider/device behavior explicitly unverified until tested in an authorized environment.

## Summary

You began with the module’s plain meaning, traced `exposure.test` in `test/exposure.test.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/covid-alert/test/exposure.test.ts)
