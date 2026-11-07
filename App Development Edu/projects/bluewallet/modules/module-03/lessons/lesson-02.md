# Hashing and script-hash derivation: Trace the source

**Lesson ID:** `bluewallet-03-hashing-and-electrum-identifiers-lesson-02`  
**Module ID:** `bluewallet-03-hashing-and-electrum-identifiers`  
**Source focus:** `src/sha256.ts` → `sha256`

## Purpose and learning objectives

Open `src/sha256.ts` and locate `sha256`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Hashing and script-hash derivation** is like following one item through a workshop: locate the input, see what changes, then find the output. Hashing turns bytes into a fixed fingerprint; Electrum queries use a script-derived identifier. Follow the SHA implementation and the address-to-script-hash conversion, including byte order and test vectors.

### Step toward the implementation

Open `src/sha256.ts` and locate `sha256`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/sha256.ts`, `src/address.ts`, `test/wallet.test.ts`.

## Source evidence

Excerpt from [`src/sha256.ts`](../../../../../../App%20Development/bluewallet/src/sha256.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
return ((value >>> bits) | (value << (32 - bits))) >>> 0;
}

/** The SHA-256 digest of a byte array. */
export function sha256(bytes: Uint8Array): Uint8Array {
  const h = new Uint32Array([
    0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
    0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19,
  ]);

  const bitLength = bytes.length * 8;
  const paddedLength = (((bytes.length + 9) >> 6) + 1) << 6;
  const padded = new Uint8Array(paddedLength);
  padded.set(bytes);
  padded[bytes.length] = 0x80;

  const view = new DataView(padded.buffer);
  view.setUint32(paddedLength - 4, bitLength >>> 0, false);
  view.setUint32(paddedLength - 8, Math.floor(bitLength / 0x100000000), false);

  const w = new Uint32Array(64);

  for (let offset = 0; offset < paddedLength; offset += 64) {
    for (let i = 0; i < 16; i += 1) w[i] = view.getUint32(offset + i * 4, false);
```

### Read it step by step

1. Find the focus cue `sha256` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Hashing and script-hash derivation**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `sha256` in `src/sha256.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluewallet/src/sha256.ts)
