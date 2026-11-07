# Operate the relay without exposing a control port: Check behavior and limits

**Lesson ID:** `peyara-remote-mouse-07-operation-and-security-lesson-03`  
**Module ID:** `peyara-remote-mouse-07-operation-and-security`  
**Source focus:** `server/config.js` → `config`

## Purpose and learning objectives

Use `server/config.js` at `config` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Operate the relay without exposing a control port** means: Remote keyboard/mouse is powerful. Learn to keep the relay local, review every opt-in before a LAN demo, and account for native robotjs build requirements and host permissions. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `server/config.js` at `config` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `server/config.js`, `server/index.js`, `README.md`.

## Source evidence

Excerpt from [`server/config.js`](../../../../../../App%20Development/peyara-remote-mouse/server/config.js); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```js
const DEFAULT_HOST = '127.0.0.1';
const DEFAULT_PORT = 8765;

function readConfig(env = process.env) {
  const host = String(env.HOST || DEFAULT_HOST).trim();
  const port = Number(env.PORT || DEFAULT_PORT);
  const sensitivity = Number(env.SENSITIVITY || 1.5);
  const networkListener = !['127.0.0.1', 'localhost', '::1'].includes(host);

  if (!Number.isInteger(port) || port < 1 || port > 65535) {
    throw new Error('PORT must be an integer from 1 to 65535.');
  }
  if (!Number.isFinite(sensitivity) || sensitivity <= 0 || sensitivity > 10) {
    throw new Error('SENSITIVITY must be greater than 0 and no more than 10.');
  }
  if (networkListener && env.ALLOW_NETWORK_LISTEN !== 'true') {
    throw new Error('Binding beyond loopback requires ALLOW_NETWORK_LISTEN=true.');
  }

  return {
    host,
    port,
    sensitivity,
```

### Read it step by step

1. Find the focus cue `config` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Operate the relay without exposing a control port**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `config` in `server/config.js`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/peyara-remote-mouse/server/config.js)
