# Kickstarter for iOS — source-grounded mini-project course

## Purpose and expected result

Build a SwiftUI crowdfunding discovery demo with local project search, detail views, save/back workflows, validation, and local state persistence. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/kickstarter-for-ios/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. A project card starts with a project record** — Project fields, computed progress, identity, and sample catalogue (`Sources/Models.swift`).
- **02. Find projects in a local catalogue** — Category data, search matching, sort ordering, and discovery rendering (`Sources/Core.swift`).
- **03. Validate a pledge without moving money** — Pledge validation, status changes, detail state, and progress display (`Sources/Core.swift`).
- **04. Save choices and persist local identifiers** — ProjectStore, UserDefaults keys, toggling, and backed/saved projections (`Sources/Models.swift`).
- **05. Build a screen flow around one observable store** — Environment object injection, NavigationStack, and view actions (`Sources/ContentView.swift`).
- **06. Use XCTest and XcodeGen to check the sample** — Core rule tests, temporary UserDefaults, target generation, and simulator checklist (`Tests/ProjectCoreTests.swift`).

The build is a learning implementation, not upstream product parity. Key limits include:

- The catalogue is sample content and does not come from Kickstarter.
- Search is local and only covers the included sample records.
- No charge, payment authorization, or server-side pledge is performed.
- Saved/backed IDs persist locally; changing pledge totals is sample in-memory state and does not sync.
- The source is a compact educational client, not production Kickstarter UI.
- This workspace lacked Xcode; build and UI behavior remain unverified.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Swift, SwiftUI, UserDefaults, XCTest, XcodeGen. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Payment boundary:** project data is sample content and backing updates local demo state; no Kickstarter API or payment processor is called.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
