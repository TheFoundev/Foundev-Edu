# Test protocol edges and plan a compatible server demo

**Lesson ID:** `rocket-chat-mobile-07-tests-and-mini-project-integration-lesson-01`  
**Project:** Rocket.Chat Mobile  
**Source focus:** `test/chat.test.ts` — `fakeSocket`

## Purpose and learning objectives

In plain terms, this lesson teaches **Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `test/chat.test.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Fake socket assertions, endpoint test cases, dependency and provider review**. This is a learning implementation, so keep the limit in view: Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server.

## Learning objectives

1. Describe the everyday behavior: Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work.
2. Find the relevant implementation in `test/chat.test.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `test/chat.test.ts`, `package.json`, `README.md`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Fake socket assertions, endpoint test cases, dependency and provider review**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server.

### 3. Read the real implementation

The excerpt below is copied directly from `test/chat.test.ts` around `fakeSocket`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
  const { socket, sent } = fakeSocket();
  const client = new DdpClient(() => socket);
  await client.connect('wss://chat.example/websocket');

  push(socket, JSON.stringify({ msg: 'ping', id: 'ping-1' }));
  await new Promise((resolve) => setTimeout(resolve, 10));

  const pongs = sent.map((entry) => JSON.parse(entry)).filter((entry) => entry.msg === 'pong');
  assert.equal(pongs.length, 1);
  assert.equal(pongs[0].id, 'ping-1');
});
```



The selected symbol is `fakeSocket`. Relate its code to this source map:

- `test/chat.test.ts` — inspect how this part participates in fake socket assertions, endpoint test cases, dependency and provider review.
- `package.json` — inspect how this part participates in fake socket assertions, endpoint test cases, dependency and provider review.
- `README.md` — inspect how this part participates in fake socket assertions, endpoint test cases, dependency and provider review.

### 4. Step-by-step source reading

1. Open `test/chat.test.ts` and search for `fakeSocket`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work. The known limitation is explicit: Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `rocket-chat-mobile-07-tests-and-mini-project-integration-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `test/chat.test.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `fakeSocket` in `test/chat.test.ts`, and traced the related files. The implemented behavior is **Tests simulate server messages without a network. Use them to understand expected envelopes, then plan authenticated integration and server-version checks as future work**; the boundary is **Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`test/chat.test.ts`](../../../../../../projects/rocket-chat-mobile/test/chat.test.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Expo Env](https://docs.expo.dev/guides/environment-variables/), [Rocket Ddp](https://developer.rocket.chat/apidocs/which-api-should-i-use), [Rocket Ddp Methods](https://developer.rocket.chat/apidocs/realtime-method-calls), [Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
