# Mentor solution guide — Peyara Remote Mouse

## Review stance

Evaluate the learner's implementation against the source project, not against the full upstream product. The expected result is a small working feature and an honest demo. A proposal alone is not a completed mini-project.

## Suggested solution path

1. Begin with the source map and constraints in each of the 8 modules.
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

- **Agree on a small language of remote-control events:** confirm the learner understands `src/protocol.ts` and does not claim beyond: Validation narrows malformed input but does not authenticate a sender.
- **Turn gestures and text into protocol messages:** confirm the learner understands `src/screens/TouchpadScreen.tsx` and does not claim beyond: Only the relay can control the host; the mobile UI itself does not perform desktop input.
- **Connect, report status, and retry carefully:** confirm the learner understands `src/connection.ts` and does not claim beyond: Retry logic does not add TLS, pairing, or authentication to the relay.
- **Remember the relay address with a storage seam:** confirm the learner understands `src/settings.ts` and does not claim beyond: A LAN address is private configuration; only connect to a relay you trust.
- **Map validated events to host actions under explicit controls:** confirm the learner understands `server/config.js` and does not claim beyond: There is no TLS or client authentication; network use remains unsafe on untrusted networks.
- **Debug one event from finger to cursor:** confirm the learner understands `server/relay.js` and does not claim beyond: The test suite does not prove the phone and host can reach each other on a real network.
- **Operate the relay without exposing a control port:** confirm the learner understands `server/index.js` and does not claim beyond: No pairing, TLS, client authentication, or internet-safe deployment is included.
- **Deliver a tested phone-to-host demo:** confirm the learner understands `src/data.ts` and does not claim beyond: Do not operate the unauthenticated relay outside a controlled trusted environment.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
