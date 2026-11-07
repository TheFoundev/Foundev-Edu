# Agree on a small language of remote-control events: Trace the source

**Lesson ID:** `peyara-remote-mouse-01-event-protocol-and-validation-lesson-02`  
**Module ID:** `peyara-remote-mouse-01-event-protocol-and-validation`  
**Source focus:** `src/protocol.ts` → `protocol`

## Purpose and learning objectives

Open `src/protocol.ts` and locate `protocol`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Agree on a small language of remote-control events** is like following one item through a workshop: locate the input, see what changes, then find the output. Two programs need to agree on message words. Learn the event shapes, then trace validation and JSON encoding on the phone and decoding at the relay.

### Step toward the implementation

Open `src/protocol.ts` and locate `protocol`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/protocol.ts`, `server/relay.js`, `test/protocol.test.ts`.

## Source evidence

Excerpt from [`src/protocol.ts`](../../../../../../App%20Development/peyara-remote-mouse/src/protocol.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
/**
 * The protocol between the phone and the relay.
 *
 * Pure functions, no imports, so both halves of the app (the Expo client and
 * the Node relay) can be tested without a React Native or a network.
 */

export type RelayEvent =
  | { type: 'move'; dx: number; dy: number }
  | { type: 'click'; button: 'left' | 'right' }
  | { type: 'scroll'; dy: number }
  | { type: 'text'; text: string }
  | { type: 'key'; key: string };

export type EventType = RelayEvent['type'];

/** The events the relay understands. */
export const EVENT_TYPES: EventType[] = ['move', 'click', 'scroll', 'text', 'key'];

/** The special keys the relay can press. */
export const SPECIAL_KEYS = ['enter', 'backspace', 'tab', 'escape'];
```

### Read it step by step

1. Find the focus cue `protocol` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Agree on a small language of remote-control events**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `protocol` in `src/protocol.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/peyara-remote-mouse/src/protocol.ts)
