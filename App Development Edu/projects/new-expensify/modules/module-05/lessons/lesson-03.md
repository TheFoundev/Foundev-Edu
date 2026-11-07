# Share and save reports, messages, and settings: Check behavior and limits

**Lesson ID:** `new-expensify-05-context-store-and-persistence-lesson-03`  
**Module ID:** `new-expensify-05-context-store-and-persistence`  
**Source focus:** `src/expenseContext.tsx` → `expenseContext`

## Purpose and learning objectives

Use `src/expenseContext.tsx` at `expenseContext` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

A feature is only reliable within the cases it handles. In plain terms, **Share and save reports, messages, and settings** means: The provider is the app-wide coordinator and the store is its persistence seam. Follow load and save for the three stored domains and inspect malformed-data recovery tests. Today we trace one normal path and one boundary.

### Step toward the implementation

Use `src/expenseContext.tsx` at `expenseContext` to inspect a failure or edge case. Follow its caller and test rather than inferring behavior from the screen. The source files for this module are `src/expenseContext.tsx`, `src/store.ts`, `App.tsx`.

## Source evidence

Excerpt from [`src/expenseContext.tsx`](../../../../../../App%20Development/new-expensify/src/expenseContext.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
};

const store = new ExpenseStore(backend);

type ExpenseContextValue = {
  reports: Report[];
  messages: Message[];
  settings: typeof seedSettings;
  ready: boolean;
  /** Move a report to another state. */
  submit(reportId: string): { ok: boolean; error?: string };
  /** Add an expense to a report. */
  addExpense(reportId: string, expense: Expense): void;
  /** Send a message in the chat. */
  sendMessage(body: string): void;
  /** Change a setting. */
  updateSettings(next: Partial<typeof seedSettings>): void;
};

const ExpenseContext = createContext<ExpenseContextValue | null>(null);

/** Holds the reports, the chat and the settings, and keeps them on the device. */
export function ExpenseProvider({ children }: { children: React.ReactNode }) {
  const [reports, setReports] = useState<Report[]>(seedReports);
```

### Read it step by step

1. Find the focus cue `expenseContext` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Share and save reports, messages, and settings**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `expenseContext` in `src/expenseContext.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/new-expensify/src/expenseContext.tsx)
