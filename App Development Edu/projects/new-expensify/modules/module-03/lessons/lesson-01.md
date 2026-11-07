# Draft, submission, approval, and rejection rules

**Lesson ID:** `new-expensify-03-report-workflow-states-lesson-01`  
**Project:** New Expensify  
**Source focus:** `src/model.ts` — `export function canTransition`

## Purpose and learning objectives

In plain terms, this lesson teaches **A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/model.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Approvals are local demo transitions; they do not represent an employer’s authorization.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Allowed status transitions, submission preconditions, and immutable updates**. This is a learning implementation, so keep the limit in view: Approvals are local demo transitions; they do not represent an employer’s authorization.

## Learning objectives

1. Describe the everyday behavior: A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions.
2. Find the relevant implementation in `src/model.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `src/model.ts`, `src/screens/ReportsScreen.tsx`, `test/model.test.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Allowed status transitions, submission preconditions, and immutable updates**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Approvals are local demo transitions; they do not represent an employer’s authorization.

### 3. Read the real implementation

The excerpt below is copied directly from `src/model.ts` around `export function canTransition`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
export function canTransition(from: ReportStatus, to: ReportStatus): boolean {
  return (REPORT_TRANSITIONS[from] ?? []).includes(to);
}

/** The error message for an illegal move, or null. */
export function transitionError(from: ReportStatus, to: string): string | null {
  if (!REPORT_TRANSITIONS[to as ReportStatus]) return `"${to}" is not a state of a report.`;
  if (!canTransition(from, to as ReportStatus)) {
    return `A ${from} report cannot become ${to}.`;
  }
  return null;
}

/** The total of a report. */
export function totalOf(report: Report): number {
  return report.expenses.reduce((sum, expense) => sum + expense.amount, 0);
}

```



The selected symbol is `export function canTransition`. Relate its code to this source map:

- `src/model.ts` — inspect how this part participates in allowed status transitions, submission preconditions, and immutable updates.
- `src/screens/ReportsScreen.tsx` — inspect how this part participates in allowed status transitions, submission preconditions, and immutable updates.
- `test/model.test.ts` — inspect how this part participates in allowed status transitions, submission preconditions, and immutable updates.

### 4. Step-by-step source reading

1. Open `src/model.ts` and search for `export function canTransition`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions. The known limitation is explicit: Approvals are local demo transitions; they do not represent an employer’s authorization. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `new-expensify-03-report-workflow-states-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/model.ts`; UI labels alone do not define behavior.
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

You started from the user task, named its everyday model, followed `export function canTransition` in `src/model.ts`, and traced the related files. The implemented behavior is **A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions**; the boundary is **Approvals are local demo transitions; they do not represent an employer’s authorization**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/model.ts`](../../../../../../projects/new-expensify/src/model.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
