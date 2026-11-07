# Validation report — gitpoint

- Generated: 2026-11-07T09:03:58.568810+00:00
- Modules: 6; lessons: 18; questions: 60
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

- **Repositories and issues as typed records:** An API response is not yet a screen-ready object. Learn the normalized types and mapper functions, then compare sample rows with fields expected from GitHub.; Seed data is a fallback/demo and should not be confused with live account data.
- **Make and interpret GitHub API requests:** An HTTP client sends a request and turns a response into a useful shape. Trace URL construction and response handling, then inspect how API errors and rate-limit metadata are represented.; Authentication, token storage, pagination breadth, and current provider quotas need review before production use.
- **Turn a list into useful repository and issue views:** Filtering is like applying a sieve to a list. Trace text matching and state filtering into the screens, then verify which fields participate and how empty results are shown.; Filtering the current dataset is not the same as server-side search across all GitHub.
- **Keep a last-known view when storage or network fails:** A cache is a last-known copy, not the source of truth. Follow provider initialization and storage fallbacks, then inspect tests for malformed JSON and a failing backend.; Cached repository/issue data can be stale and is not evidence of a current provider response.
- **Connect the app shell to repository and issue screens:** The shell selects a screen while context provides shared API and cache state. Follow a tap from navigation through state into the rendered list and profile.; The UI does not reproduce every capability or policy of the upstream GitPoint app.
- **Verify API logic and plan safe integration:** Mocked responses prove mapping logic without contacting GitHub. Compare tests with API behavior and identify secure credential handling and pagination work needed for a real account client.; Do not put a personal access token in a client bundle or commit it into source.

## Runtime and deployment status

No source application was executed or deployed by this validator. See the package README and the source project README for available local test commands; execute platform builds and authorized external-service checks separately.
