# Turn gestures and text into protocol messages: Trace the source

**Lesson ID:** `peyara-remote-mouse-02-touchpad-and-keyboard-input-lesson-02`  
**Module ID:** `peyara-remote-mouse-02-touchpad-and-keyboard-input`  
**Source focus:** `src/screens/TouchpadScreen.tsx` → `TouchpadScreen`

## Purpose and learning objectives

Open `src/screens/TouchpadScreen.tsx` and locate `TouchpadScreen`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Turn gestures and text into protocol messages** is like following one item through a workshop: locate the input, see what changes, then find the output. A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function.

### Step toward the implementation

Open `src/screens/TouchpadScreen.tsx` and locate `TouchpadScreen`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/screens/TouchpadScreen.tsx`, `src/screens/KeyboardScreen.tsx`, `src/data.ts`.

## Source evidence

Excerpt from [`src/screens/TouchpadScreen.tsx`](../../../../../../App%20Development/peyara-remote-mouse/src/screens/TouchpadScreen.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
import { Screen, Button } from '../components';
import { colors } from '../theme';
import { send, useConnectionStatus } from '../data';

export default function TouchpadScreen() {
  const connection = useConnectionStatus();
  const last = useRef({ x: 0, y: 0 });

  const responder = useRef(
    PanResponder.create({
      onStartShouldSetPanResponder: () => true,
      onMoveShouldSetPanResponder: () => true,
      onPanResponderGrant: (_, gesture) => {
        last.current = { x: gesture.x0, y: gesture.y0 };
      },
      onPanResponderMove: (_, gesture) => {
        const dx = gesture.moveX - last.current.x;
        const dy = gesture.moveY - last.current.y;
        if (Math.abs(dx) + Math.abs(dy) > 1) {
          send({ type: 'move', dx: Math.round(dx), dy: Math.round(dy) });
          last.current = { x: gesture.moveX, y: gesture.moveY };
        }
      },
    })
```

### Read it step by step

1. Find the focus cue `TouchpadScreen` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Turn gestures and text into protocol messages**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `TouchpadScreen` in `src/screens/TouchpadScreen.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/peyara-remote-mouse/src/screens/TouchpadScreen.tsx)
