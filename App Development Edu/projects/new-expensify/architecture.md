# Architecture — New Expensify

Build an expense-report learning app with validation, workflow transitions, category totals, local chat, settings, and persistent local state.

## Data and behavior map

1. **Reports contain expenses, not just totals** — `src/model.ts` (`export type Report`): Expense and Report types, seed records, and derived totals. Related files: src/model.ts; src/data.ts; src/screens/ReportsScreen.tsx.
2. **Reject invalid rows and summarize categories** — `src/model.ts` (`export function checkExpense`): Positive amount/title validation, category aggregation, and money formatting. Related files: src/model.ts; test/model.test.ts; src/screens/ReportsScreen.tsx.
3. **Draft, submission, approval, and rejection rules** — `src/model.ts` (`export function canTransition`): Allowed status transitions, submission preconditions, and immutable updates. Related files: src/model.ts; src/screens/ReportsScreen.tsx; test/model.test.ts.
4. **A report chat is a local message list** — `src/model.ts` (`export function addMessage`): Message append, trimming/search, and conversation display. Related files: src/model.ts; src/screens/ChatScreen.tsx; test/model.test.ts.
5. **Share and save reports, messages, and settings** — `src/store.ts` (`export class ExpenseStore`): Context initialization, AsyncStorage adapter, store keys, hydration and effects. Related files: src/expenseContext.tsx; src/store.ts; App.tsx.
6. **Connect report, chat, and settings screens** — `App.tsx` (`const TABS`): Navigation tabs, shared controls/theme, action wiring, and UI status. Related files: src/screens/ReportsScreen.tsx; src/screens/ChatScreen.tsx; src/screens/SettingsScreen.tsx; src/components.tsx; src/theme.ts; App.tsx.
7. **Test invariants and explain privacy limits** — `test/model.test.ts` (`expense needs a title and a positive amount`): Unit coverage, test command, PII sensitivity, and runtime evidence. Related files: test/model.test.ts; package.json; README.md.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, AsyncStorage.
- Explicit limits across modules: ['Seed reports and the CAD profile are demo data; no accounting backend is connected', 'This is not a tax, compliance, or accounting rules engine', 'Approvals are local demo transitions; they do not represent an employer’s authorization', 'No real-time chat, identity system, or server moderation is implemented', 'AsyncStorage is local, unencrypted key/value persistence; it is not financial-grade secure storage', 'The UI does not implement identity, backend sync, or payment settlement', 'Do not store real employee expense data in this educational app'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
