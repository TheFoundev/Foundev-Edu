# Mentor solution guide — DuckDuckGo for iOS

## Review stance

Evaluate the learner's implementation against the source project, not against the full upstream product. The expected result is a small working feature and an honest demo. A proposal alone is not a completed mini-project.

## Suggested solution path

1. Begin with the source map and constraints in each of the 6 modules.
2. Require a short written flow from user action to owning model/service, shared state, persistence, and UI.
3. Have the learner implement a focused extension and add isolated tests before UI wiring.
4. Review the failure case and verify that it does not imply an absent external service.
5. Require an end-to-end demonstration on a supported simulator/device and a recorded toolchain.

## Expected evidence

- A code diff that references the relevant source files and learning objectives.
- Passing relevant unit tests, with new regression coverage.
- A reproducible setup/build or an explicit environment limitation.
- A demo of the normal path and one failure/edge path.
- Updated documentation covering security, privacy, and remaining limits.

## Project-specific mentor checks

- **Decide whether text is a web address or a search:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: The engine routing is a sample rule; it does not implement DuckDuckGo product services.
- **Tabs as identifiable records:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: Persisted URLs are ordinary browsing data and this sample has limited privacy guarantees.
- **Embed a web page inside a SwiftUI screen:** confirm the learner understands `Sources/WebView.swift` and does not claim beyond: This is an educational WebKit wrapper, not a custom browser engine or hardened production browser.
- **Content rules and private-mode clearing:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: The sample rules are limited; a counter is not proof that every tracker was blocked.
- **Compose browse, tabs, and settings views:** confirm the learner understands `Sources/ContentView.swift` and does not claim beyond: The views demonstrate a subset of a browser workflow and are not a production browser UX.
- **Test routing, tab lifecycle, and privacy claims:** confirm the learner understands `Tests/BrowserCoreTests.swift` and does not claim beyond: No Xcode build was run in this workspace; simulator behavior remains unverified.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
