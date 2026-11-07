# Verify API logic and plan safe integration

**Lesson ID:** `gitpoint-06-tests-security-and-mini-project-lesson-01`  
**Project:** GitPoint  
**Source focus:** `test/github.test.ts` — `fakeFetch`

## Purpose and learning objectives

In plain terms, this lesson teaches **Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `test/github.test.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Do not put a personal access token in a client bundle or commit it into source.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Mock response evidence, test script, public API boundary, and token risk**. This is a learning implementation, so keep the limit in view: Do not put a personal access token in a client bundle or commit it into source.

## Learning objectives

1. Describe the everyday behavior: Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client.
2. Find the relevant implementation in `test/github.test.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `test/github.test.ts`, `package.json`, `README.md`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Mock response evidence, test script, public API boundary, and token risk**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Do not put a personal access token in a client bundle or commit it into source.

### 3. Read the real implementation

The excerpt below is copied directly from `test/github.test.ts` around `fakeFetch`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
  const { fn } = fakeFetch([], 403);
  const client = new GitHubClient({ fetchFn: fn });

  await assert.rejects(() => client.listRepos('alexr'), (error: Error) => {
    assert.ok(error instanceof GitHubError);
    assert.equal((error as GitHubError).status, 403);
    return true;
  });
});

test('the repositories are sorted by the date they were updated', () => {
  const older = toRepo({ ...rawRepo, id: 1, name: 'older', updated_at: '2026-01-01T00:00:00Z' });
  const newer = toRepo({ ...rawRepo, id: 2, name: 'newer', updated_at: '2026-06-01T00:00:00Z' });
  assert.deepEqual(sortRepos([older, newer]).map((repo) => repo.name), ['newer', 'older']);
});

test('the issues are sorted by the date they were created', () => {
  const older = toIssue({ ...rawIssue, id: 1, created_at: '2026-01-01T00:00:00Z' });
```



The selected symbol is `fakeFetch`. Relate its code to this source map:

- `test/github.test.ts` — inspect how this part participates in mock response evidence, test script, public api boundary, and token risk.
- `package.json` — inspect how this part participates in mock response evidence, test script, public api boundary, and token risk.
- `README.md` — inspect how this part participates in mock response evidence, test script, public api boundary, and token risk.

### 4. Step-by-step source reading

1. Open `test/github.test.ts` and search for `fakeFetch`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client. The known limitation is explicit: Do not put a personal access token in a client bundle or commit it into source. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `gitpoint-06-tests-security-and-mini-project-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `test/github.test.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `fakeFetch` in `test/github.test.ts`, and traced the related files. The implemented behavior is **Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client**; the boundary is **Do not put a personal access token in a client bundle or commit it into source**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`test/github.test.ts`](../../../../../../projects/gitpoint/test/github.test.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Github Rest](https://docs.github.com/en/rest), [Github Issues](https://docs.github.com/en/rest/issues/issues), [Github Repos](https://docs.github.com/en/rest/repos), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
