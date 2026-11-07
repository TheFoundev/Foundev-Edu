# Store wallet state without inventing chain truth: Trace the source

**Lesson ID:** `bluewallet-07-local-persistence-and-failure-cases-lesson-02`  
**Module ID:** `bluewallet-07-local-persistence-and-failure-cases`  
**Source focus:** `src/store.ts` → `store`

## Purpose and learning objectives

Open `src/store.ts` and locate `store`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Store wallet state without inventing chain truth** is like following one item through a workshop: locate the input, see what changes, then find the output. Local storage is a notebook, not a blockchain. Read the storage adapter and store tests, then distinguish persisted demo history from provider-synchronized history.

### Step toward the implementation

Open `src/store.ts` and locate `store`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/store.ts`, `src/persistence.ts`, `test/store.test.ts`.

## Source evidence

Excerpt from [`src/store.ts`](../../../../../../App%20Development/bluewallet/src/store.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
/**
 * Local persistence for the wallet.
 *
 * The store talks to a tiny key/value interface, so the app can use
 * AsyncStorage while the tests use the in-memory implementation.
 */

import type { Transaction } from './wallet-core';

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
      return values.has(key) ? values.get(key)! : null;
    },
```

### Read it step by step

1. Find the focus cue `store` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Store wallet state without inventing chain truth**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
- [Source file](../../../../../../App%20Development/bluewallet/src/store.ts)
