# GitPoint — source-grounded mini-project course

## Purpose and expected result

Build a GitHub-oriented repository and issue browser with API mapping, search/filtering, cached state, and clear authentication limits. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/gitpoint/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. Repositories and issues as typed records** — Repository/issue shapes, response mapping, sample data, and sort fields (`src/github.ts`).
- **02. Make and interpret GitHub API requests** — Fetch client, request paths, headers, response mapping, GitHubError, and rate-limit headers (`src/github.ts`).
- **03. Turn a list into useful repository and issue views** — Search fields, date ordering, state filters, and list rendering (`src/github.ts`).
- **04. Keep a last-known view when storage or network fails** — Cache keys, load/save, corrupt data, provider startup, and fallback state (`src/store.ts`).
- **05. Connect the app shell to repository and issue screens** — Context lifecycle, tabs, profile/repository/issue states, and reusable controls (`src/githubContext.tsx`).
- **06. Verify API logic and plan safe integration** — Mock response evidence, test script, public API boundary, and token risk (`test/github.test.ts`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Seed data is a fallback/demo and should not be confused with live account data.
- Authentication, token storage, pagination breadth, and current provider quotas need review before production use.
- Filtering the current dataset is not the same as server-side search across all GitHub.
- Cached repository/issue data can be stale and is not evidence of a current provider response.
- The UI does not reproduce every capability or policy of the upstream GitPoint app.
- Do not put a personal access token in a client bundle or commit it into source.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, GitHub REST API, AsyncStorage. Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **API boundary:** local request/mapping tests use fakes; no API authentication session or production token management is provided. Do not embed a personal access token in the mobile bundle.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
