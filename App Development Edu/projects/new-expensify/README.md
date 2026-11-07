# New Expensify — source-grounded mini-project course

## Purpose and expected result

Build an expense-report learning app with validation, workflow transitions, category totals, local chat, settings, and persistent local state. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/new-expensify/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Reports contain expenses, not just totals** — Expense and Report types, seed records, and derived totals (`src/model.ts`).
- **02. Reject invalid rows and summarize categories** — Positive amount/title validation, category aggregation, and money formatting (`src/model.ts`).
- **03. Draft, submission, approval, and rejection rules** — Allowed status transitions, submission preconditions, and immutable updates (`src/model.ts`).
- **04. A report chat is a local message list** — Message append, trimming/search, and conversation display (`src/model.ts`).
- **05. Share and save reports, messages, and settings** — Context initialization, AsyncStorage adapter, store keys, hydration and effects (`src/store.ts`).
- **06. Connect report, chat, and settings screens** — Navigation tabs, shared controls/theme, action wiring, and UI status (`App.tsx`).
- **07. Test invariants and explain privacy limits** — Unit coverage, test command, PII sensitivity, and runtime evidence (`test/model.test.ts`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Seed reports and the CAD profile are demo data; no accounting backend is connected.
- This is not a tax, compliance, or accounting rules engine.
- Approvals are local demo transitions; they do not represent an employer’s authorization.
- No real-time chat, identity system, or server moderation is implemented.
- AsyncStorage is local, unencrypted key/value persistence; it is not financial-grade secure storage.
- The UI does not implement identity, backend sync, or payment settlement.
- Do not store real employee expense data in this educational app.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, AsyncStorage. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Financial-data boundary:** report, chat, and settings flows are local educational state; there is no employer authorization, accounting service, or backend sync. Do not use real expense records.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
