# Rocket.Chat Mobile — source-grounded mini-project course

## Purpose and expected result

Build a channel/message mobile demo with a small DDP client, typed mapping, persistent offline state, and an explicit endpoint configuration boundary. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/rocket-chat-mobile/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Channels and messages as typed records** — Channel/ChatMessage models, seeded data, and unread display (`src/chat.ts`).
- **02. A client opens a socket and speaks DDP messages** — Socket abstraction, connect/session, method IDs, ping/pong, timeout and close (`src/chat.ts`).
- **03. Map server-shaped data and manage channels/messages** — toChannels/toMessages, filtering, unread counts, optimistic append (`src/chat.ts`).
- **04. Make offline mode explicit and reject placeholders** — EXPO_PUBLIC_CHAT_URL, secure WebSocket validation, `.example` rejection, idle status (`src/chat.ts`).
- **05. Hydrate local chat state and coordinate shared actions** — AsyncStorage adapter, load/save effects, context actions, and optimistic state (`src/store.ts`).
- **06. Connect channels, messages, and profile UI** — Tab shell, selected channel, offline banner, reconnect control, shared components, and status rendering (`src/screens/ChatScreen.tsx`).
- **07. Test protocol edges and plan a compatible server demo** — Fake socket assertions, endpoint test cases, dependency and provider review (`test/chat.test.ts`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Seed rows are local demo content and do not prove a server account exists.
- The app-specific methods channels.list, chat.sendMessage, and chat.getMessages are not verified Rocket.Chat method names; DDP method calls are marked deprecated in current Rocket.Chat documentation.
- Method names and response shapes are a demo contract; confirm them against the target server version.
- Only a compatible real wss endpoint should be configured; no server was tested here.
- Local chat persistence is not end-to-end encrypted server sync.
- The app has no login, push notification integration, or upstream client parity.
- Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, AsyncStorage, WebSocket, Rocket.Chat DDP demo client. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Provider compatibility:** current Rocket.Chat documentation recommends REST by default and marks DDP method calls deprecated. This source uses custom names (`channels.list`, `chat.sendMessage`, `chat.getMessages`) that were not verified against a server. Offline mode is the default and no server was contacted.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
