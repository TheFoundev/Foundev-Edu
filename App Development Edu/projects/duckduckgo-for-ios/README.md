# DuckDuckGo for iOS — source-grounded mini-project course

## Purpose and expected result

Build a SwiftUI/WebKit browser sample with search routing, tabs, settings, tracker-rule demonstrations, and a private-mode data policy. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/duckduckgo-for-ios/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Decide whether text is a web address or a search** — Input classification, scheme handling, empty input, and search-engine selection (`Sources/Core.swift`).
- **02. Tabs as identifiable records** — BrowserTab identity, selected-tab behavior, close rules, and UserDefaults persistence (`Sources/Models.swift`).
- **03. Embed a web page inside a SwiftUI screen** — UIViewRepresentable/WebKit bridge, navigation state, and page loading (`Sources/WebView.swift`).
- **04. Content rules and private-mode clearing** — Rule-list JSON, rule compilation, blocked-count reporting, and private data behavior (`Sources/Core.swift`).
- **05. Compose browse, tabs, and settings views** — Observable store injection, navigation, toolbar actions, and settings binding (`Sources/ContentView.swift`).
- **06. Test routing, tab lifecycle, and privacy claims** — XCTest coverage, XcodeGen project configuration, and documentation boundary (`Tests/BrowserCoreTests.swift`).

The build is a learning implementation, not upstream product parity. Key limits include:

- The engine routing is a sample rule; it does not implement DuckDuckGo product services.
- Persisted URLs are ordinary browsing data and this sample has limited privacy guarantees.
- This is an educational WebKit wrapper, not a custom browser engine or hardened production browser.
- The sample rules are limited; a counter is not proof that every tracker was blocked.
- The views demonstrate a subset of a browser workflow and are not a production browser UX.
- No Xcode build was run in this workspace; simulator behavior remains unverified.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Swift, SwiftUI, WebKit, XCTest, XcodeGen. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Engine boundary:** the sample wraps Apple WebKit (`WKWebView`); Firefox for iOS does not embed Gecko. Content-rule behavior is a limited sample, not a production tracker-protection guarantee.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
