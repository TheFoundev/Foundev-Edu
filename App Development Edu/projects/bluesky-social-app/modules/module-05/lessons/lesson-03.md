# Screens, reusable controls, and app shell: Check behavior and limits

**Lesson ID:** `bluesky-social-app-05-screens-and-navigation-lesson-03`  
**Module ID:** `bluesky-social-app-05-screens-and-navigation`  
**Source focus:** `App.tsx` → `App`

## Purpose and learning objectives

Use `App.tsx` at `App` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Screens, reusable controls, and app shell** means: The shell chooses which room is visible; reusable components and theme tokens keep each room consistent. Trace tabs into screen components, then follow props from shared controls to their event handlers. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `App.tsx` at `App` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `App.tsx`, `src/screens/FeedScreen.tsx`, `src/screens/DiscoverScreen.tsx`, `src/screens/ProfileScreen.tsx`, `src/components.tsx`, `src/theme.ts`.

## Source evidence

Excerpt from [`App.tsx`](../../../../../../App%20Development/bluesky-social-app/App.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
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
      </View>
      <View style={styles.tabBar}>
        {TABS.map((tab) => (
          <Pressable
            key={tab.key}
            onPress={() => setActive(tab.key)}
            style={[styles.tab, active === tab.key && styles.tabActive]}
          >
```

### Read it step by step

1. Find the focus cue `App` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Screens, reusable controls, and app shell**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `App` in `App.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluesky-social-app/App.tsx)
