# Mentor solution guide — Firefox for iOS

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

- **Browser records and protection state:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: The sample model is not the complete Firefox account/profile model.
- **Turn an address-bar string into a destination:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: Search and navigation behavior is a teaching implementation and may omit edge cases of the full Firefox browser.
- **Render navigation through WebKit:** confirm the learner understands `Sources/WebView.swift` and does not claim beyond: The project does not embed Firefox’s Gecko engine.
- **Map a settings choice to tracker rules:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: Rules are a small sample, not Firefox’s full tracking-protection lists or guarantees.
- **Share browser state across screens:** confirm the learner understands `Sources/ContentView.swift` and does not claim beyond: Account sync, history sync, and production data management are not implemented.
- **Read the test suite and XcodeGen spec:** confirm the learner understands `Tests/BrowserCoreTests.swift` and does not claim beyond: The source was not built or deployed here; no runtime result is implied.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
