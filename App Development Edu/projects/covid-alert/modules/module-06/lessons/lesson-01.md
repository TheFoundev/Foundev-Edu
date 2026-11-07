# Verify behavior and avoid overstating results

**Lesson ID:** `covid-alert-06-tests-privacy-and-accessibility-lesson-01`  
**Project:** COVID Alert  
**Source focus:** `test/exposure.test.ts` — `empty history is labeled as unchecked`

## Purpose and learning objectives

In plain terms, this lesson teaches **Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `test/exposure.test.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: A passing unit suite does not validate clinical advice, health policy, or native exposure notifications.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Simulation tests, storage failures, labels, disclosure, and evidence limits**. This is a learning implementation, so keep the limit in view: A passing unit suite does not validate clinical advice, health policy, or native exposure notifications.

## Learning objectives

1. Describe the everyday behavior: Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device.
2. Find the relevant implementation in `test/exposure.test.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `test/exposure.test.ts`, `src/components.tsx`, `README.md`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Simulation tests, storage failures, labels, disclosure, and evidence limits**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: A passing unit suite does not validate clinical advice, health policy, or native exposure notifications.

### 3. Read the real implementation

The excerpt below is copied directly from `test/exposure.test.ts` around `empty history is labeled as unchecked`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
test('an empty history is labeled as unchecked, not clear', () => {
  assert.equal(checkStatusLabel(null), 'No check yet');
});

test('status copy labels both outcomes as simulated', () => {
  const clear: Check = { id: 'c1', date: 'today', checkedAt: '2026-04-23T08:10:00Z', result: 'clear', note: '', source: 'simulated' };
  const exposed: Check = { ...clear, result: 'exposed' };
  assert.match(checkStatusLabel(clear), /simulation/i);
  assert.match(checkStatusLabel(exposed), /simulation/i);
});

test('one matching code is written in the singular', async () => {
  const service = new SimulatedExposureService(1);
  const result = await service.check();
  assert.match(result.detail, /1 matching code in/);
});

test('a check is turned into a history row', async () => {
```



The selected symbol is `empty history is labeled as unchecked`. Relate its code to this source map:

- `test/exposure.test.ts` — inspect how this part participates in simulation tests, storage failures, labels, disclosure, and evidence limits.
- `src/components.tsx` — inspect how this part participates in simulation tests, storage failures, labels, disclosure, and evidence limits.
- `README.md` — inspect how this part participates in simulation tests, storage failures, labels, disclosure, and evidence limits.

### 4. Step-by-step source reading

1. Open `test/exposure.test.ts` and search for `empty history is labeled as unchecked`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device. The known limitation is explicit: A passing unit suite does not validate clinical advice, health policy, or native exposure notifications. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `covid-alert-06-tests-privacy-and-accessibility-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `test/exposure.test.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `empty history is labeled as unchecked` in `test/exposure.test.ts`, and traced the related files. The implemented behavior is **Tests can prove the model returns the expected simulation; they cannot prove a health service is present. Inspect assertions and visible disclaimers, then identify privacy and accessibility checks needed on-device**; the boundary is **A passing unit suite does not validate clinical advice, health policy, or native exposure notifications**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`test/exposure.test.ts`](../../../../../../projects/covid-alert/test/exposure.test.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
