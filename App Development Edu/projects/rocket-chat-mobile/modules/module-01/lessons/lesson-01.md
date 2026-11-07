# Channels and messages as typed records

**Lesson ID:** `rocket-chat-mobile-01-chat-records-and-seed-state-lesson-01`  
**Project:** Rocket.Chat Mobile  
**Source focus:** `src/chat.ts` — `export type Channel`

## Purpose and learning objectives

In plain terms, this lesson teaches **A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/chat.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Seed rows are local demo content and do not prove a server account exists.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Channel/ChatMessage models, seeded data, and unread display**. This is a learning implementation, so keep the limit in view: Seed rows are local demo content and do not prove a server account exists.

## Learning objectives

1. Describe the everyday behavior: A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them.
2. Find the relevant implementation in `src/chat.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `src/chat.ts`, `src/data.ts`, `src/screens/ChannelsScreen.tsx`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Channel/ChatMessage models, seeded data, and unread display**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Seed rows are local demo content and do not prove a server account exists.

### 3. Read the real implementation

The excerpt below is copied directly from `src/chat.ts` around `export type Channel`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
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
  channelId: string;
  sender: string;
  body: string;
  time: string;
  mine?: boolean;
};

```



The selected symbol is `export type Channel`. Relate its code to this source map:

- `src/chat.ts` — inspect how this part participates in channel/chatmessage models, seeded data, and unread display.
- `src/data.ts` — inspect how this part participates in channel/chatmessage models, seeded data, and unread display.
- `src/screens/ChannelsScreen.tsx` — inspect how this part participates in channel/chatmessage models, seeded data, and unread display.

### 4. Step-by-step source reading

1. Open `src/chat.ts` and search for `export type Channel`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them. The known limitation is explicit: Seed rows are local demo content and do not prove a server account exists. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `rocket-chat-mobile-01-chat-records-and-seed-state-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/chat.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `export type Channel` in `src/chat.ts`, and traced the related files. The implemented behavior is **A channel is a named room and a message is one entry in its timeline. Read the typed models and seed fixtures before tracing how lists display them**; the boundary is **Seed rows are local demo content and do not prove a server account exists**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/chat.ts`](../../../../../../projects/rocket-chat-mobile/src/chat.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Expo Env](https://docs.expo.dev/guides/environment-variables/), [Rocket Ddp](https://developer.rocket.chat/apidocs/which-api-should-i-use), [Rocket Ddp Methods](https://developer.rocket.chat/apidocs/realtime-method-calls), [Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
