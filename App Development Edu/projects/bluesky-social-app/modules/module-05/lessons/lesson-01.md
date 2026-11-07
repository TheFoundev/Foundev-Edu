# Screens, reusable controls, and app shell

**Lesson ID:** `bluesky-social-app-05-screens-and-navigation-lesson-01`  
**Project:** Bluesky Social App  
**Source focus:** `App.tsx` — `const TABS`

## Purpose and learning objectives

In plain terms, this lesson teaches **The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `App.tsx` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Tab selection, screen composition, action props, and theme tokens**. This is a learning implementation, so keep the limit in view: The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server.

## Learning objectives

1. Describe the everyday behavior: The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers.
2. Find the relevant implementation in `App.tsx` and explain the named symbol.
3. Trace the responsibility across the related files: `App.tsx`, `src/screens/FeedScreen.tsx`, `src/screens/DiscoverScreen.tsx`, `src/screens/ProfileScreen.tsx`, `src/components.tsx`, `src/theme.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Tab selection, screen composition, action props, and theme tokens**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server.

### 3. Read the real implementation

The excerpt below is copied directly from `App.tsx` around `const TABS`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```tsx
const TABS = [
  { key: 'feed', label: 'Home', icon: '◎', component: FeedScreen },
  { key: 'discover', label: 'Discover', icon: '◇', component: DiscoverScreen },
  { key: 'profile', label: 'Profile', icon: '○', component: ProfileScreen },
] as const;

export default function App() {
  const [active, setActive] = useState(TABS[0].key);
  const current = TABS.find((tab) => tab.key === active) ?? TABS[0];
  const Screen = current.component;

  return (
    <SafeAreaView style={styles.root}>
      <StatusBar style="dark" />
      <View style={styles.body}>
        <FeedProvider>
          <Screen />
        </FeedProvider>
```



The selected symbol is `const TABS`. Relate its code to this source map:

- `App.tsx` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.
- `src/screens/FeedScreen.tsx` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.
- `src/screens/DiscoverScreen.tsx` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.
- `src/screens/ProfileScreen.tsx` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.
- `src/components.tsx` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.
- `src/theme.ts` — inspect how this part participates in tab selection, screen composition, action props, and theme tokens.

### 4. Step-by-step source reading

1. Open `App.tsx` and search for `const TABS`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers. The known limitation is explicit: The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `bluesky-social-app-05-screens-and-navigation-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `App.tsx`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `const TABS` in `App.tsx`, and traced the related files. The implemented behavior is **The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers**; the boundary is **The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`App.tsx`](../../../../../../projects/bluesky-social-app/App.tsx)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Atproto](https://atproto.com/guides/overview), [Atproto Write](https://atproto.com/guides/writing-data), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
