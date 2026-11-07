# Bluesky Social App — source-grounded mini-project course

## Purpose and expected result

Build a local-first social-feed learning app with publishing, topic filtering, profile views, likes, bookmarks, and resilient persistence. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/bluesky-social-app/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. The feed as a small library** — Post records, seed fixtures, and pure feed operations (`src/feed.ts`).
- **02. From typed text to a post** — Composer validation, length limits, and immutable insertion (`src/feed.ts`).
- **03. Likes and saved posts** — LikeMap, BookmarkMap, toggles, and the saved-post projection (`src/feed.ts`).
- **04. One shared feed and its stored snapshot** — Context state lifecycle, storage adapter, migration defaults, and corrupt data (`src/store.ts`).
- **05. Screens, reusable controls, and app shell** — Tab selection, screen composition, action props, and theme tokens (`App.tsx`).
- **06. Test the model and define the network boundary** — Node test coverage, pure-model boundaries, and absent protocol integration (`test/feed.test.ts`).
- **07. Integrating a coherent social-feed release** — End-to-end feature tracing, persistence evidence, and safe demo scope (`src/feedContext.tsx`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Posts are local sample records; mergeRemotePosts is a helper and does not itself call a network.
- Publishing stores a local post; there is no authenticated AT Protocol write.
- Bookmarks and likes are per-device demo state, not synced account records.
- AsyncStorage is persistent local key/value storage; it is not encrypted account sync.
- The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server.
- No AT Protocol login, moderation, network feed, or remote post creation is implemented.
- The app is a learning implementation, not upstream Bluesky client parity.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, AsyncStorage. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Protocol boundary:** the code provides local feed behavior and a `mergeRemotePosts` helper, but no AT Protocol authentication, request client, record creation, moderation, or remote sync.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
