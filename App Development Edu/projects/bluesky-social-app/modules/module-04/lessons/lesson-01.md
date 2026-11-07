# One shared feed and its stored snapshot

**Lesson ID:** `bluesky-social-app-04-state-and-persistence-lesson-01`  
**Project:** Bluesky Social App  
**Source focus:** `src/store.ts` — `export class FeedStore`

## Purpose and learning objectives

In plain terms, this lesson teaches **Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/store.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: AsyncStorage is persistent local key/value storage; it is not encrypted account sync.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Context state lifecycle, storage adapter, migration defaults, and corrupt data**. This is a learning implementation, so keep the limit in view: AsyncStorage is persistent local key/value storage; it is not encrypted account sync.

## Learning objectives

1. Describe the everyday behavior: Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values.
2. Find the relevant implementation in `src/store.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `src/feedContext.tsx`, `src/store.ts`, `src/persistence.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Context state lifecycle, storage adapter, migration defaults, and corrupt data**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: AsyncStorage is persistent local key/value storage; it is not encrypted account sync.

### 3. Read the real implementation

The excerpt below is copied directly from `src/store.ts` around `export class FeedStore`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
export class FeedStore {
  private backend: KeyValueStore;

  constructor(backend: KeyValueStore) {
    this.backend = backend;
  }

  /**
   * Read the saved state. A corrupt or missing value gives an empty state
   * instead of an error, so a bad write can never break the app.
   */
  async load(): Promise<FeedState> {
    let raw: string | null = null;
    try {
      raw = await this.backend.getItem(FEED_KEY);
    } catch {
      return { posts: [], liked: {}, bookmarks: {} };
    }
```



The selected symbol is `export class FeedStore`. Relate its code to this source map:

- `src/feedContext.tsx` — inspect how this part participates in context state lifecycle, storage adapter, migration defaults, and corrupt data.
- `src/store.ts` — inspect how this part participates in context state lifecycle, storage adapter, migration defaults, and corrupt data.
- `src/persistence.ts` — inspect how this part participates in context state lifecycle, storage adapter, migration defaults, and corrupt data.

### 4. Step-by-step source reading

1. Open `src/store.ts` and search for `export class FeedStore`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values. The known limitation is explicit: AsyncStorage is persistent local key/value storage; it is not encrypted account sync. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `bluesky-social-app-04-state-and-persistence-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/store.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `export class FeedStore` in `src/store.ts`, and traced the related files. The implemented behavior is **Context is the shared clipboard for screens; the store is the filing cabinet. Follow load, state initialization, effects that save changes, and the storage adapter. Inspect defaults for older saves with no bookmarks and malformed values**; the boundary is **AsyncStorage is persistent local key/value storage; it is not encrypted account sync**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/store.ts`](../../../../../../projects/bluesky-social-app/src/store.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Atproto](https://atproto.com/guides/overview), [Atproto Write](https://atproto.com/guides/writing-data), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
