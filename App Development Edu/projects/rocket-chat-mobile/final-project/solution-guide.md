# Mentor solution guide — Rocket.Chat Mobile

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

- **Channels and messages as typed records:** confirm the learner understands `src/chat.ts` and does not claim beyond: Seed rows are local demo content and do not prove a server account exists.
- **A client opens a socket and speaks DDP messages:** confirm the learner understands `src/chat.ts` and does not claim beyond: The app-specific methods channels.list, chat.sendMessage, and chat.getMessages are not verified Rocket.Chat method names; DDP method calls are marked deprecated in current Rocket.Chat documentation.
- **Map server-shaped data and manage channels/messages:** confirm the learner understands `src/chat.ts` and does not claim beyond: Method names and response shapes are a demo contract; confirm them against the target server version.
- **Make offline mode explicit and reject placeholders:** confirm the learner understands `src/chat.ts` and does not claim beyond: Only a compatible real wss endpoint should be configured; no server was tested here.
- **Hydrate local chat state and coordinate shared actions:** confirm the learner understands `src/store.ts` and does not claim beyond: Local chat persistence is not end-to-end encrypted server sync.
- **Connect channels, messages, and profile UI:** confirm the learner understands `src/screens/ChatScreen.tsx` and does not claim beyond: The app has no login, push notification integration, or upstream client parity.
- **Test protocol edges and plan a compatible server demo:** confirm the learner understands `test/chat.test.ts` and does not claim beyond: Current Rocket.Chat docs recommend REST by default and mark DDP method calls deprecated; the custom method names in this source have not been verified against a server.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
