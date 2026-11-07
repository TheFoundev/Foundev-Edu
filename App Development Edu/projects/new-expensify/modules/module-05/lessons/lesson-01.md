# Share and save reports, messages, and settings: Begin with the idea

**Lesson ID:** `new-expensify-05-context-store-and-persistence-lesson-01`  
**Module ID:** `new-expensify-05-context-store-and-persistence`  
**Source focus:** `src/expenseContext.tsx` → `expenseContext`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Share and save reports, messages, and settings** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: The provider is the app-wide coordinator and the store is its persistence seam. Follow load and save for the three stored domains and inspect malformed-data recovery tests.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/expenseContext.tsx`, `src/store.ts`, `App.tsx`.

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
