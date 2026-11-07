# Mentor solution guide — Kickstarter for iOS

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

- **A project card starts with a project record:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: The catalogue is sample content and does not come from Kickstarter.
- **Find projects in a local catalogue:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: Search is local and only covers the included sample records.
- **Validate a pledge without moving money:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: No charge, payment authorization, or server-side pledge is performed.
- **Save choices and persist local identifiers:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: Saved/backed IDs persist locally; changing pledge totals is sample in-memory state and does not sync.
- **Build a screen flow around one observable store:** confirm the learner understands `Sources/ContentView.swift` and does not claim beyond: The source is a compact educational client, not production Kickstarter UI.
- **Use XCTest and XcodeGen to check the sample:** confirm the learner understands `Tests/ProjectCoreTests.swift` and does not claim beyond: This workspace lacked Xcode; build and UI behavior remain unverified.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
