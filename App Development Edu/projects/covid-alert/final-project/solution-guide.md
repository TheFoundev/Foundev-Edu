# Mentor solution guide — COVID Alert

## Review stance

Evaluate the learner's implementation against the source project, not against the full upstream product. The expected result is a small working feature and an honest demo. A proposal alone is not a completed mini-project.

## Suggested solution path

1. Begin with the source map and constraints in each of the 7 modules.
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

- **What a check record means:** confirm the learner understands `src/data.ts` and does not claim beyond: Seeded content is demonstration data; no public-health data source is contacted.
- **A service-shaped simulation:** confirm the learner understands `src/exposure.ts` and does not claim beyond: No Bluetooth, Apple/Google exposure notification, diagnosis, or contact-tracing integration exists.
- **From selected symptoms to an informational score:** confirm the learner understands `src/exposure.ts` and does not claim beyond: The score is educational and is not medical advice or a validated clinical decision tool.
- **History ordering and next-check time:** confirm the learner understands `src/exposure.ts` and does not claim beyond: The configured interval is a UI rule, not health guidance.
- **Local persistence and the screen flow:** confirm the learner understands `src/exposureContext.tsx` and does not claim beyond: History stays on the device in this demo; local storage is not a protected health record system.
- **Verify behavior and avoid overstating results:** confirm the learner understands `test/exposure.test.ts` and does not claim beyond: A passing unit suite does not validate clinical advice, health policy, or native exposure notifications.
- **Present a complete transparent health-demo journey:** confirm the learner understands `src/exposure.ts` and does not claim beyond: Never encourage a learner to make health decisions from the demo output.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
