# Map server-shaped data and manage channels/messages: Check behavior and limits

**Lesson ID:** `rocket-chat-mobile-03-response-mapping-and-local-operations-lesson-03`  
**Module ID:** `rocket-chat-mobile-03-response-mapping-and-local-operations`  
**Source focus:** `src/chat.ts` → `chat`

## Purpose and learning objectives

Use `src/chat.ts` at `chat` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Map server-shaped data and manage channels/messages** means: External objects need validation before entering a UI list. Follow mapping functions and local helpers, then see how a sent message is appended optimistically. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `src/chat.ts` at `chat` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `src/chat.ts`, `src/screens/ChatScreen.tsx`, `src/screens/ChannelsScreen.tsx`.

## Source evidence

Excerpt from [`src/chat.ts`](../../../../../../App%20Development/rocket-chat-mobile/src/chat.ts); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```ts
/**
 * The chat client.
 *
 * The client speaks the DDP protocol over a websocket: a JSON message with a
 * `msg` field, a `method` for the calls and a `id` for the answers. The
 * socket is given to the client, so the tests can answer without a network.
 *
 * No imports, so the client can be tested without a React Native runtime.
 */

export type Channel = {
  id: string;
  name: string;
  topic: string;
  unread: number;
  members: number;
  private?: boolean;
};

export type ChatMessage = {
  id: string;
```

### Read it step by step

1. Find the focus cue `chat` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Map server-shaped data and manage channels/messages**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `chat` in `src/chat.ts`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/rocket-chat-mobile/src/chat.ts)
