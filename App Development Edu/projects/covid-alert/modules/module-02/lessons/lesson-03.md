# A service-shaped simulation: Check behavior and limits

**Lesson ID:** `covid-alert-02-simulated-check-service-lesson-03`  
**Module ID:** `covid-alert-02-simulated-check-service`  
**Source focus:** `src/exposure.ts` → `exposure`

## Purpose and learning objectives

Use `src/exposure.ts` at `exposure` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **A service-shaped simulation** means: A service interface is a plug shape. The current plug is a simulator that returns configured outcomes. Trace its implementation to checkStatusLabel and the status UI so a clear result cannot be mistaken for a real scan. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `src/exposure.ts` at `exposure` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `src/exposure.ts`, `src/screens/StatusScreen.tsx`.

## Source evidence

Excerpt from [`src/exposure.ts`](../../../../../../App%20Development/covid-alert/src/exposure.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
/**
 * The exposure check and the symptom model.
 *
 * Pure logic, no imports, so it can be unit tested without a React Native
 * runtime.
 */

export type Check = {
  id: string;
  /** The stamp shown in the history, for example "Apr 23, 08:10". */
  date: string;
  /** The same moment as an ISO timestamp, so it can be compared reliably. */
  checkedAt: string;
  result: 'clear' | 'exposed';
  note: string;
  source: string;
};

export type ExposureResult = {
  status: 'clear' | 'exposed';
  checkedAt: string;
```

### Read it step by step

1. Find the focus cue `exposure` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **A service-shaped simulation**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `exposure` in `src/exposure.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/covid-alert/src/exposure.ts)
