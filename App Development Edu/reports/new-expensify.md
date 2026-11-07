# Validation report — new-expensify

- Generated: 2026-11-07T09:03:58.613107+00:00
- Modules: 7; lessons: 21; questions: 70
- Structural result: **PASS**

## Passed checks

- Required package root files and project metadata checked.
- JSON parsed; package-internal and source links checked.
- Unique module, lesson, exercise, and question IDs checked.
- Per-module lesson references, 10-question assessments, option sets, answer keys, and explanations checked.
- Manifest counts and included_files checked.
- Required file inventory is complete; no unlisted package files detected.

## Errors

- None.

## Warnings and human/runtime review

- Structural validation does not establish instructional accuracy, compile apps, prove provider/API behavior, verify device behavior, or establish deployment.
- Confirm framework/provider documentation versions and run platform-specific builds in the intended environment.
- Source dependency review: Expo is pinned to `~51.0.28` and React Native to `0.74.5`; current official Expo references may describe a newer SDK, so learners must consult version-matched SDK documentation before changing dependencies.

## Source-specific findings

- **Reports contain expenses, not just totals:** A report is a folder containing expense rows. Read the typed shapes and seed data, then see how a displayed total should be derived from the rows rather than typed separately.; Seed reports and the CAD profile are demo data; no accounting backend is connected.
- **Reject invalid rows and summarize categories:** Validation is a gate before a row enters the report. Follow amount/title checks, then trace how category groups and totals are calculated and tested.; This is not a tax, compliance, or accounting rules engine.
- **Draft, submission, approval, and rejection rules:** A report workflow is a state machine: each action changes state only if the current state allows it. Trace the guard conditions and see what tests assert about invalid transitions.; Approvals are local demo transitions; they do not represent an employer’s authorization.
- **A report chat is a local message list:** A chat screen can feel live while messages remain local. Follow a typed message through the model and UI, and note there is no remote participant or server in this implementation.; No real-time chat, identity system, or server moderation is implemented.
- **Share and save reports, messages, and settings:** The provider is the app-wide coordinator and the store is its persistence seam. Follow load and save for the three stored domains and inspect malformed-data recovery tests.; AsyncStorage is local, unencrypted key/value persistence; it is not financial-grade secure storage.
- **Connect report, chat, and settings screens:** The same data model supports several screens. Follow each control’s handler back to context/model methods and distinguish display values from persisted settings.; The UI does not implement identity, backend sync, or payment settlement.
- **Test invariants and explain privacy limits:** Pure model tests make business rules repeatable, but they do not establish secure storage or accounting correctness. Build a demo and identify where real financial and privacy review would be needed.; Do not store real employee expense data in this educational app.

## Runtime and deployment status

No source application was executed or deployed by this validator. See the package README and the source project README for available local test commands; execute platform builds and authorized external-service checks separately.
