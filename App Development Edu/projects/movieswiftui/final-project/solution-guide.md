# Mentor solution guide — MovieSwiftUI

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

- **A movie record and a useful catalogue:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: The displayed catalogue is seeded sample data; live movie-service access is not configured.
- **Convert untrusted response data into movie records:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: No API credentials or live server call are present in the sample app.
- **Narrow and order the catalogue:** confirm the learner understands `Sources/Core.swift` and does not claim beyond: Results only cover the in-memory catalogue available to the store.
- **Remember a watchlist without a service account:** confirm the learner understands `Sources/Models.swift` and does not claim beyond: Local watchlist persistence does not create an account or sync across devices.
- **Compose discovery, detail, and reusable poster views:** confirm the learner understands `Sources/Components.swift` and does not claim beyond: Poster URLs/assets may be absent; do not imply a live streaming/catalogue integration.
- **Read test evidence and plan runtime checks:** confirm the learner understands `Tests/MovieCoreTests.swift` and does not claim beyond: No Xcode or simulator execution was available in this build environment.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
