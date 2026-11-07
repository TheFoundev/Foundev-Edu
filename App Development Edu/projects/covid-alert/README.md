# COVID Alert — source-grounded mini-project course

## Purpose and expected result

Build an educational symptom and simulated exposure-check app with clearly labelled outcomes and local history. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/covid-alert/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. What a check record means** — Check and ExposureResult types, symptom catalogue, resources, and sample data (`src/data.ts`).
- **02. A service-shaped simulation** — ExposureService interface, simulated implementation, and simulation labelling (`src/exposure.ts`).
- **03. From selected symptoms to an informational score** — Weights, duplicate/unknown filtering, thresholds, advice, and disclaimer (`src/exposure.ts`).
- **04. History ordering and next-check time** — toCheck, lastCheck, formatting, interval calculation, and empty state (`src/exposure.ts`).
- **05. Local persistence and the screen flow** — Provider lifecycle, AsyncStorage adapter, resources screen, reusable controls, and tabs (`src/exposureContext.tsx`).
- **06. Verify behavior and avoid overstating results** — Simulation tests, storage failures, labels, disclosure, and evidence limits (`test/exposure.test.ts`).
- **07. Present a complete transparent health-demo journey** — Screen-to-model integration, clear-state wording, limitations, and demo script (`src/exposure.ts`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Seeded content is demonstration data; no public-health data source is contacted.
- No Bluetooth, Apple/Google exposure notification, diagnosis, or contact-tracing integration exists.
- The score is educational and is not medical advice or a validated clinical decision tool.
- The configured interval is a UI rule, not health guidance.
- History stays on the device in this demo; local storage is not a protected health record system.
- A passing unit suite does not validate clinical advice, health policy, or native exposure notifications.
- Never encourage a learner to make health decisions from the demo output.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, AsyncStorage. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Simulation boundary:** checks use `SimulatedExposureService`; the source has no Bluetooth or native exposure-notification integration. Symptom scoring is an informational rule, not clinical advice.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
