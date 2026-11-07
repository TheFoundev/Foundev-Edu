# Peyara Remote Mouse — source-grounded mini-project course

## Purpose and expected result

Build a phone touchpad and keyboard plus a WebSocket relay, with validated messages, reconnect logic, storage, and safe-by-default relay settings. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/peyara-remote-mouse/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Agree on a small language of remote-control events** — Event union, JSON encoding, decoding, bounds, and unknown-event rejection (`src/protocol.ts`).
- **02. Turn gestures and text into protocol messages** — PanResponder deltas, click/scroll actions, text and key events (`src/screens/TouchpadScreen.tsx`).
- **03. Connect, report status, and retry carefully** — Socket lifecycle, connection snapshots, exponential delay, max retry, and manual disconnect (`src/connection.ts`).
- **04. Remember the relay address with a storage seam** — Host validation, settings key, AsyncStorage adapter, and load/save flow (`src/settings.ts`).
- **05. Map validated events to host actions under explicit controls** — Loopback default, bind acknowledgement, port/sensitivity validation, opt-in robotjs, event mapping (`server/config.js`).
- **06. Debug one event from finger to cursor** — End-to-end protocol path, fallback logging, and evidence from isolated tests (`server/relay.js`).
- **07. Operate the relay without exposing a control port** — Safe defaults, trusted LAN warning, robotjs native dependency, and shutdown/review (`server/index.js`).
- **08. Deliver a tested phone-to-host demo** — Integration checklist, UI feedback, observable connection state, demonstration, and safe teardown (`src/data.ts`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Validation narrows malformed input but does not authenticate a sender.
- Only the relay can control the host; the mobile UI itself does not perform desktop input.
- Retry logic does not add TLS, pairing, or authentication to the relay.
- A LAN address is private configuration; only connect to a relay you trust.
- There is no TLS or client authentication; network use remains unsafe on untrusted networks.
- The test suite does not prove the phone and host can reach each other on a real network.
- No pairing, TLS, client authentication, or internet-safe deployment is included.
- Do not operate the unauthenticated relay outside a controlled trusted environment.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, Node.js, WebSocket, optional robotjs. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Operational boundary:** safe defaults are loopback and logging-only; LAN binding and host input require separate opt-ins. The relay has no TLS or client authentication.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
