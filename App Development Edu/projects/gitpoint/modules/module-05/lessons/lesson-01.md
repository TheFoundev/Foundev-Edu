# Connect the app shell to repository and issue screens: Begin with the idea

**Lesson ID:** `gitpoint-05-ui-state-and-navigation-lesson-01`  
**Module ID:** `gitpoint-05-ui-state-and-navigation`  
**Source focus:** `App.tsx` → `App`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Connect the app shell to repository and issue screens** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `App.tsx`, `src/githubContext.tsx`, `src/screens/ReposScreen.tsx`, `src/screens/IssuesScreen.tsx`, `src/screens/ProfileScreen.tsx`, `src/components.tsx`, `src/theme.ts`.

## Source evidence

Excerpt from [`App.tsx`](../../../../../../App%20Development/gitpoint/App.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
{ key: 'issues', label: 'Issues', icon: '◌', component: IssuesScreen },
  { key: 'profile', label: 'Profile', icon: '○', component: ProfileScreen },
] as const;

export default function App() {
  const [active, setActive] = useState<(typeof TABS)[number]['key']>(TABS[0].key);
  const current = TABS.find((tab) => tab.key === active) ?? TABS[0];
  const Screen = current.component;

  return (
    <SafeAreaView style={styles.root}>
      <StatusBar style="dark" />
      <View style={styles.body}>
        <GitHubProvider>
          <Screen />
        </GitHubProvider>
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

The lesson should produce a source-backed explanation of **Connect the app shell to repository and issue screens**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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
- [Source file](../../../../../../App%20Development/gitpoint/App.tsx)
