# Map validated events to host actions under explicit controls

**Lesson ID:** `peyara-remote-mouse-05-relay-mapping-and-config-lesson-01`  
**Project:** Peyara Remote Mouse  
**Source focus:** `server/config.js` — `function readConfig`

## Purpose and learning objectives

In plain terms, this lesson teaches **The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `server/config.js` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: There is no TLS or client authentication; network use remains unsafe on untrusted networks.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping**. This is a learning implementation, so keep the limit in view: There is no TLS or client authentication; network use remains unsafe on untrusted networks.

## Learning objectives

1. Describe the everyday behavior: The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in.
2. Find the relevant implementation in `server/config.js` and explain the named symbol.
3. Trace the responsibility across the related files: `server/config.js`, `server/relay.js`, `server/index.js`, `server/test/config.test.js`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: There is no TLS or client authentication; network use remains unsafe on untrusted networks.

### 3. Read the real implementation

The excerpt below is copied directly from `server/config.js` around `function readConfig`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```javascript
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
```



The selected symbol is `function readConfig`. Relate its code to this source map:

- `server/config.js` — inspect how this part participates in loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping.
- `server/relay.js` — inspect how this part participates in loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping.
- `server/index.js` — inspect how this part participates in loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping.
- `server/test/config.test.js` — inspect how this part participates in loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping.

### 4. Step-by-step source reading

1. Open `server/config.js` and search for `function readConfig`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in. The known limitation is explicit: There is no TLS or client authentication; network use remains unsafe on untrusted networks. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `peyara-remote-mouse-05-relay-mapping-and-config-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `server/config.js`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `function readConfig` in `server/config.js`, and traced the related files. The implemented behavior is **The relay is the boundary that can move the computer. Read configuration before message handling: loopback and logging are defaults, network binding needs explicit acknowledgement, and real input needs its own opt-in**; the boundary is **There is no TLS or client authentication; network use remains unsafe on untrusted networks**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`server/config.js`](../../../../../../projects/peyara-remote-mouse/server/config.js)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Websocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
