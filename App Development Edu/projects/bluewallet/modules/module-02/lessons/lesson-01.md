# Address checks before payment planning: Begin with the idea

**Lesson ID:** `bluewallet-02-address-validation-lesson-01`  
**Module ID:** `bluewallet-02-address-validation`  
**Source focus:** `src/address.ts` → `address`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Address checks before payment planning** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: An address is like a destination label with a built-in error check. Follow Bech32 decoding from characters to checksum and witness data, compare the simpler Base58 prefix/length screen, and see how the send screen rejects input before requesting a transaction plan.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/address.ts`, `src/screens/SendScreen.tsx`.

## Source evidence

Excerpt from [`src/address.ts`](../../../../../../App%20Development/bluewallet/src/address.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
/**
 * Address handling.
 *
 * A bech32 decoder (BIP-173) and the script hash an Electrum server indexes
 * a wallet by. Pure functions, no imports, so they can be unit tested.
 */

import { sha256HexReversed } from './sha256';

const CHARSET = 'qpzry9x8gf2tvdw0s3jn54khce6mua7l';
const GENERATOR = [0x3b6a57b2, 0x26508e6d, 0x1ea119fa, 0x3d4233dd, 0x2a1462b3];

/** The bech32 checksum of a payload, for the given constant. */
function polymod(values: number[]): number {
  let chk = 1;
  for (const value of values) {
    const top = chk >>> 25;
    chk = ((chk & 0x1ffffff) << 5) ^ value;
    for (let i = 0; i < 5; i += 1) {
      if ((top >>> i) & 1) chk ^= GENERATOR[i];
    }
```

### Read it step by step

1. Find the focus cue `address` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Address checks before payment planning**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `address` in `src/address.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluewallet/src/address.ts)
