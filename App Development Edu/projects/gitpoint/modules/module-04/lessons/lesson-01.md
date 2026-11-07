# Keep a last-known view when storage or network fails: Begin with the idea

**Lesson ID:** `gitpoint-04-cache-and-offline-behavior-lesson-01`  
**Module ID:** `gitpoint-04-cache-and-offline-behavior`  
**Source focus:** `src/store.ts` → `store`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Keep a last-known view when storage or network fails** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: A cache is a last-known copy, not the source of truth. Follow provider initialization and storage fallbacks, then inspect tests for malformed JSON and a failing backend.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/store.ts`, `src/githubContext.tsx`, `test/github.test.ts`.

## Source evidence

Excerpt from [`src/store.ts`](../../../../../../App%20Development/gitpoint/src/store.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
* The repositories and the issues that were fetched last are kept on the
 * device, so the app shows something the moment it opens and keeps working
 * when the network is gone.
 *
 * No imports, so the store can be tested without a React Native runtime.
 */

export type CacheEntry<T> = {
  value: T;
  savedAt: string;
};

export type KeyValueStore = {
  getItem(key: string): Promise<string | null>;
  setItem(key: string, value: string): Promise<void>;
  removeItem(key: string): Promise<void>;
};

/** An in-memory key/value store, used by the tests and as a fallback. */
export function createMemoryStore(): KeyValueStore & { dump(): Record<string, string> } {
  const values = new Map<string, string>();

  return {
    async getItem(key) {
```

### Read it step by step

1. Find the focus cue `store` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Keep a last-known view when storage or network fails**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `store` in `src/store.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/gitpoint/src/store.ts)
