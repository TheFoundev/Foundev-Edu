# Mentor solution guide — Bluesky Social App

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

- **The feed as a small library:** confirm the learner understands `src/feed.ts` and does not claim beyond: Posts are local sample records; mergeRemotePosts is a helper and does not itself call a network.
- **From typed text to a post:** confirm the learner understands `src/feed.ts` and does not claim beyond: Publishing stores a local post; there is no authenticated AT Protocol write.
- **Likes and saved posts:** confirm the learner understands `src/feed.ts` and does not claim beyond: Bookmarks and likes are per-device demo state, not synced account records.
- **One shared feed and its stored snapshot:** confirm the learner understands `src/store.ts` and does not claim beyond: AsyncStorage is persistent local key/value storage; it is not encrypted account sync.
- **Screens, reusable controls, and app shell:** confirm the learner understands `App.tsx` and does not claim beyond: The tabs and suggested feeds are local UI; they are not loaded from a Bluesky server.
- **Test the model and define the network boundary:** confirm the learner understands `test/feed.test.ts` and does not claim beyond: No AT Protocol login, moderation, network feed, or remote post creation is implemented.
- **Integrating a coherent social-feed release:** confirm the learner understands `src/feedContext.tsx` and does not claim beyond: The app is a learning implementation, not upstream Bluesky client parity.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
