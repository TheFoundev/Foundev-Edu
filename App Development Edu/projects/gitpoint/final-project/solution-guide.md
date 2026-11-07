# Mentor solution guide — GitPoint

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

- **Repositories and issues as typed records:** confirm the learner understands `src/github.ts` and does not claim beyond: Seed data is a fallback/demo and should not be confused with live account data.
- **Make and interpret GitHub API requests:** confirm the learner understands `src/github.ts` and does not claim beyond: Authentication, token storage, pagination breadth, and current provider quotas need review before production use.
- **Turn a list into useful repository and issue views:** confirm the learner understands `src/github.ts` and does not claim beyond: Filtering the current dataset is not the same as server-side search across all GitHub.
- **Keep a last-known view when storage or network fails:** confirm the learner understands `src/store.ts` and does not claim beyond: Cached repository/issue data can be stale and is not evidence of a current provider response.
- **Connect the app shell to repository and issue screens:** confirm the learner understands `src/githubContext.tsx` and does not claim beyond: The UI does not reproduce every capability or policy of the upstream GitPoint app.
- **Verify API logic and plan safe integration:** confirm the learner understands `test/github.test.ts` and does not claim beyond: Do not put a personal access token in a client bundle or commit it into source.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
