# Mentor solution guide — New Expensify

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

- **Reports contain expenses, not just totals:** confirm the learner understands `src/model.ts` and does not claim beyond: Seed reports and the CAD profile are demo data; no accounting backend is connected.
- **Reject invalid rows and summarize categories:** confirm the learner understands `src/model.ts` and does not claim beyond: This is not a tax, compliance, or accounting rules engine.
- **Draft, submission, approval, and rejection rules:** confirm the learner understands `src/model.ts` and does not claim beyond: Approvals are local demo transitions; they do not represent an employer’s authorization.
- **A report chat is a local message list:** confirm the learner understands `src/model.ts` and does not claim beyond: No real-time chat, identity system, or server moderation is implemented.
- **Share and save reports, messages, and settings:** confirm the learner understands `src/store.ts` and does not claim beyond: AsyncStorage is local, unencrypted key/value persistence; it is not financial-grade secure storage.
- **Connect report, chat, and settings screens:** confirm the learner understands `App.tsx` and does not claim beyond: The UI does not implement identity, backend sync, or payment settlement.
- **Test invariants and explain privacy limits:** confirm the learner understands `test/model.test.ts` and does not claim beyond: Do not store real employee expense data in this educational app.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
