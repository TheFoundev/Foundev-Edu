# Firefox for iOS — source-grounded mini-project course

## Purpose and expected result

Build a SwiftUI/WebKit browser-shell mini app with URL/search handling, tab state, protection settings, and rule-based tracking controls. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/firefox-for-ios/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Browser records and protection state** — Tab, protection-level, and tracker data types (`Sources/Models.swift`).
- **02. Turn an address-bar string into a destination** — URL recognition, scheme normalization, and search fallback (`Sources/Core.swift`).
- **03. Render navigation through WebKit** — Representable wrapper, load calls, and browser controls (`Sources/WebView.swift`).
- **04. Map a settings choice to tracker rules** — Protection modes, rule selection, rule compilation, and observed count (`Sources/Core.swift`).
- **05. Share browser state across screens** — Observable store lifecycle, tab navigation, and settings binding (`Sources/ContentView.swift`).
- **06. Read the test suite and XcodeGen spec** — XCTest assertions, target configuration, and what a test does not establish (`Tests/BrowserCoreTests.swift`).

The build is a learning implementation, not upstream product parity. Key limits include:

- The sample model is not the complete Firefox account/profile model.
- Search and navigation behavior is a teaching implementation and may omit edge cases of the full Firefox browser.
- The project does not embed Firefox’s Gecko engine.
- Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees.
- Account sync, history sync, and production data management are not implemented.
- The source was not built or deployed here; no runtime result is implied.

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
