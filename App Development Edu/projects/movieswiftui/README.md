# MovieSwiftUI — source-grounded mini-project course

## Purpose and expected result

Build a SwiftUI movie-discovery mini app with catalogue mapping, search, genre selection, sorting, detail pages, and a persistent watchlist. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/movieswiftui/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. A movie record and a useful catalogue** — Movie fields, identity, MovieInfo projection, and seed records (`Sources/Models.swift`).
- **02. Convert untrusted response data into movie records** — Response decoding/mapping and missing-field rejection (`Sources/Core.swift`).
- **03. Narrow and order the catalogue** — Text search fields, genre filtering, rating/year ordering, and UI controls (`Sources/Core.swift`).
- **04. Remember a watchlist without a service account** — Store defaults, add/remove operations, and UserDefaults reload (`Sources/Models.swift`).
- **05. Compose discovery, detail, and reusable poster views** — Navigation, card poster rendering, shared store, and detail fields (`Sources/Components.swift`).
- **06. Read test evidence and plan runtime checks** — Mapping/filter tests, watchlist persistence tests, XcodeGen targets, and simulator review (`Tests/MovieCoreTests.swift`).

The build is a learning implementation, not upstream product parity. Key limits include:

- The displayed catalogue is seeded sample data; live movie-service access is not configured.
- No API credentials or live server call are present in the sample app.
- Results only cover the in-memory catalogue available to the store.
- Local watchlist persistence does not create an account or sync across devices.
- Poster URLs/assets may be absent; do not imply a live streaming/catalogue integration.
- No Xcode or simulator execution was available in this build environment.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Swift, SwiftUI, UserDefaults, XCTest, XcodeGen. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Catalogue boundary:** sample records and mapper logic are present, but this app does not call a live movie catalogue API; poster fields may be empty.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
