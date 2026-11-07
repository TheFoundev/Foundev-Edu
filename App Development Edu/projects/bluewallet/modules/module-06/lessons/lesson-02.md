# Why unsigned bytes must not be broadcast: Trace the source

**Lesson ID:** `bluewallet-06-signing-and-broadcast-safety-lesson-02`  
**Module ID:** `bluewallet-06-signing-and-broadcast-safety`  
**Source focus:** `src/wallet-core.ts` → `wallet-core`

## Purpose and learning objectives

Open `src/wallet-core.ts` and locate `wallet-core`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Why unsigned bytes must not be broadcast** is like following one item through a workshop: locate the input, see what changes, then find the output. A payment plan is an unsigned instruction sheet, not a valid signed transaction. Trace the UI flow to broadcast and confirm the Electrum adapter throws before sending anything because signing and raw serialization are missing.

### Step toward the implementation

Open `src/wallet-core.ts` and locate `wallet-core`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/wallet-core.ts`, `src/walletContext.tsx`, `test/wallet.test.ts`.

## Source evidence

Excerpt from [`src/wallet-core.ts`](../../../../../../App%20Development/bluewallet/src/wallet-core.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```text
Source excerpt unavailable; inspect this source path and locate the focus symbol before teaching this module.
```

### Read it step by step

1. Find the focus cue `wallet-core` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Why unsigned bytes must not be broadcast**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `wallet-core` in `src/wallet-core.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluewallet/src/wallet-core.ts)
