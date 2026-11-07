# Turn gestures and text into protocol messages

**Lesson ID:** `peyara-remote-mouse-02-touchpad-and-keyboard-input-lesson-01`  
**Project:** Peyara Remote Mouse  
**Source focus:** `src/screens/TouchpadScreen.tsx` — `PanResponder.create`

## Purpose and learning objectives

In plain terms, this lesson teaches **A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/screens/TouchpadScreen.tsx` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Only the relay can control the host; the mobile UI itself does not perform desktop input.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **PanResponder deltas, click/scroll actions, text and key events**. This is a learning implementation, so keep the limit in view: Only the relay can control the host; the mobile UI itself does not perform desktop input.

## Learning objectives

1. Describe the everyday behavior: A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function.
2. Find the relevant implementation in `src/screens/TouchpadScreen.tsx` and explain the named symbol.
3. Trace the responsibility across the related files: `src/screens/TouchpadScreen.tsx`, `src/screens/KeyboardScreen.tsx`, `src/data.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **PanResponder deltas, click/scroll actions, text and key events**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Only the relay can control the host; the mobile UI itself does not perform desktop input.

### 3. Read the real implementation

The excerpt below is copied directly from `src/screens/TouchpadScreen.tsx` around `PanResponder.create`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```tsx
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
  ).current;

  return (
```



The selected symbol is `PanResponder.create`. Relate its code to this source map:

- `src/screens/TouchpadScreen.tsx` — inspect how this part participates in panresponder deltas, click/scroll actions, text and key events.
- `src/screens/KeyboardScreen.tsx` — inspect how this part participates in panresponder deltas, click/scroll actions, text and key events.
- `src/data.ts` — inspect how this part participates in panresponder deltas, click/scroll actions, text and key events.

### 4. Step-by-step source reading

1. Open `src/screens/TouchpadScreen.tsx` and search for `PanResponder.create`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function. The known limitation is explicit: Only the relay can control the host; the mobile UI itself does not perform desktop input. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `peyara-remote-mouse-02-touchpad-and-keyboard-input-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/screens/TouchpadScreen.tsx`; UI labels alone do not define behavior.
- **Assuming a product-name feature exists:** compare the implementation and the limitation above with the project README.
- **Changing state in several places:** identify the owning model/store/context before editing.
- **Calling a test a full-system check:** determine whether it uses fake data, fake storage, a fake socket, or a real runtime.
- **Debug sequence:** reproduce the behavior, inspect the relevant input, log or assert the model result, verify the caller and rendered state, then check persistence or network boundaries separately.

## Best practices and security

- Keep this behavior small and testable; make validation and failure outcomes explicit.
- Preserve the typed boundary and avoid trusting unvalidated input.
- Do not place credentials, private keys, health details, financial records, or trusted-network controls in an insecure client setting.
- If a service integration is proposed, add authentication, transport protection, privacy review, and provider-specific tests before describing it as implemented.
- See the project-specific review items and [Owasp Mobile](https://mas.owasp.org/MASVS/).

## Summary

You started from the user task, named its everyday model, followed `PanResponder.create` in `src/screens/TouchpadScreen.tsx`, and traced the related files. The implemented behavior is **A touchpad sends movement differences, not a picture of the whole screen. Follow gesture callbacks and keyboard controls into the shared send function**; the boundary is **Only the relay can control the host; the mobile UI itself does not perform desktop input**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/screens/TouchpadScreen.tsx`](../../../../../../projects/peyara-remote-mouse/src/screens/TouchpadScreen.tsx)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
