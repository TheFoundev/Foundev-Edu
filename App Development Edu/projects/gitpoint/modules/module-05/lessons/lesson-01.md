# Connect the app shell to repository and issue screens

**Lesson ID:** `gitpoint-05-ui-state-and-navigation-lesson-01`  
**Project:** GitPoint  
**Source focus:** `src/githubContext.tsx` — `export function GitHubProvider`

## Purpose and learning objectives

In plain terms, this lesson teaches **The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/githubContext.tsx` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: The UI does not reproduce every capability or policy of the upstream GitPoint app.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Context lifecycle, tabs, profile/repository/issue states, and reusable controls**. This is a learning implementation, so keep the limit in view: The UI does not reproduce every capability or policy of the upstream GitPoint app.

## Learning objectives

1. Describe the everyday behavior: The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile.
2. Find the relevant implementation in `src/githubContext.tsx` and explain the named symbol.
3. Trace the responsibility across the related files: `App.tsx`, `src/githubContext.tsx`, `src/screens/ReposScreen.tsx`, `src/screens/IssuesScreen.tsx`, `src/screens/ProfileScreen.tsx`, `src/components.tsx`, `src/theme.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Context lifecycle, tabs, profile/repository/issue states, and reusable controls**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: The UI does not reproduce every capability or policy of the upstream GitPoint app.

### 3. Read the real implementation

The excerpt below is copied directly from `src/githubContext.tsx` around `export function GitHubProvider`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```tsx
export function GitHubProvider({ children }: { children: React.ReactNode }) {
  const [repos, setRepos] = useState<Repo[]>(seedRepos as unknown as Repo[]);
  const [issues, setIssues] = useState<Issue[]>(seedIssues as unknown as Issue[]);
  const [profile, setProfile] = useState(seedProfile);
  const [rateLimit, setRateLimit] = useState<RateLimit | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [offline, setOffline] = useState(false);

  const load = useCallback(async () => {
    // The cache first.
    const cachedRepos = await cache.repos();
    if (cachedRepos?.value?.length) setRepos(cachedRepos.value as unknown as Repo[]);
    const cachedIssues = await cache.issues();
    if (cachedIssues?.value?.length) setIssues(cachedIssues.value as unknown as Issue[]);

    try {
      const [repoAnswer, issueAnswer, profileAnswer] = await Promise.all([
```



The selected symbol is `export function GitHubProvider`. Relate its code to this source map:

- `App.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/githubContext.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/screens/ReposScreen.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/screens/IssuesScreen.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/screens/ProfileScreen.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/components.tsx` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.
- `src/theme.ts` — inspect how this part participates in context lifecycle, tabs, profile/repository/issue states, and reusable controls.

### 4. Step-by-step source reading

1. Open `src/githubContext.tsx` and search for `export function GitHubProvider`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile. The known limitation is explicit: The UI does not reproduce every capability or policy of the upstream GitPoint app. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `gitpoint-05-ui-state-and-navigation-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/githubContext.tsx`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `export function GitHubProvider` in `src/githubContext.tsx`, and traced the related files. The implemented behavior is **The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile**; the boundary is **The UI does not reproduce every capability or policy of the upstream GitPoint app**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/githubContext.tsx`](../../../../../../projects/gitpoint/src/githubContext.tsx)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Github Rest](https://docs.github.com/en/rest), [Github Issues](https://docs.github.com/en/rest/issues/issues), [Github Repos](https://docs.github.com/en/rest/repos), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
