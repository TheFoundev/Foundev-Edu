# Connect report, chat, and settings screens: Begin with the idea

**Lesson ID:** `new-expensify-06-screens-and-controls-lesson-01`  
**Module ID:** `new-expensify-06-screens-and-controls`  
**Source focus:** `src/screens/ReportsScreen.tsx` → `ReportsScreen`

## Purpose and learning objectives

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Basic programming and a way to read the source project.Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

Imagine **Connect report, chat, and settings screens** as a small part of a phone app: it receives a value or action and helps produce a result. This module’s plain-language model is: The same data model supports several screens. Follow each control’s handler back to context/model methods and distinguish display values from persisted settings.

### Step toward the implementation

Before reading the excerpt, name the input, the result the user expects, and one assumption the app makes. The source files for this module are `src/screens/ReportsScreen.tsx`, `src/screens/ChatScreen.tsx`, `src/screens/SettingsScreen.tsx`, `src/components.tsx`, `src/theme.ts`, `App.tsx`.

## Source evidence

Excerpt from [`src/screens/ReportsScreen.tsx`](../../../../../../App%20Development/new-expensify/src/screens/ReportsScreen.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
import { colors } from '../theme';
import { useExpenses } from '../expenseContext';
import { awaitingApproval, byCategory, money, totalOf, totalOfAll } from '../model';

export default function ReportsScreen() {
  const { reports, submit } = useExpenses();
  const [open, setOpen] = useState<string | null>('rep1');
  const [message, setMessage] = useState('');

  return (
    <Screen title="Expense reports" subtitle="Draft, submit and track reimbursements.">
      {message ? <Text style={styles.meta}>{message}</Text> : null}
      <View style={styles.summary}>
        <View><Text style={styles.summaryValue}>{reports.length}</Text><Text style={styles.summaryLabel}>reports</Text></View>
        <View><Text style={styles.summaryValue}>{money(totalOfAll(reports))}</Text><Text style={styles.summaryLabel}>total</Text></View>
        <View><Text style={styles.summaryValue}>{awaitingApproval(reports).length}</Text><Text style={styles.summaryLabel}>awaiting approval</Text></View>
      </View>

      {reports.map((report) => {
        const expanded = open === report.id;
        return (
          <Card key={report.id}>
            <Pressable onPress={() => setOpen(expanded ? null : report.id)}>
              <View style={styles.rowBetween}>
```

### Read it step by step

1. Find the focus cue `ReportsScreen` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Connect report, chat, and settings screens**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `ReportsScreen` in `src/screens/ReportsScreen.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/new-expensify/src/screens/ReportsScreen.tsx)
