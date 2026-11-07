# History ordering and next-check time: Begin with the idea

**Lesson ID:** `covid-alert-04-check-history-and-time-lesson-01`  
**Module ID:** `covid-alert-04-check-history-and-time`  
**Source focus:** `src/exposure.ts` → `exposure`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **History ordering and next-check time** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: A history list is a stack of dated events. Trace how a service response becomes a row, how newest checks are selected, and how a due timestamp is calculated. Notice that no history means “No check yet.”

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/exposure.ts`, `src/screens/StatusScreen.tsx`.

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

The lesson should produce a source-backed explanation of **History ordering and next-check time**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
