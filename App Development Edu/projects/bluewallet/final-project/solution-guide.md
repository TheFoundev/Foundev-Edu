# Mentor solution guide — BlueWallet

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

- **A wallet screen is a view of money records:** confirm the learner understands `src/data.ts` and does not claim beyond: Seed transactions and the receive address are placeholders; never send funds to them.
- **Address checks before payment planning:** confirm the learner understands `src/address.ts` and does not claim beyond: Validation is not ownership proof: the Base58 path checks only prefix and length rather than checksum, and the implementation is not a substitute for audited wallet software.
- **Hashing and script-hash derivation:** confirm the learner understands `src/address.ts` and does not claim beyond: A correct hash does not sign a transaction or protect a connection.
- **Plan inputs, fee, change, and dust:** confirm the learner understands `src/wallet-core.ts` and does not claim beyond: The transaction is unsigned; fee size/rate assumptions are simplified, the change output currently uses an empty placeholder address, and no real payment should be made.
- **Demo wallet versus Electrum adapter:** confirm the learner understands `src/wallet-core.ts` and does not claim beyond: Source mismatch: the client constructs a React Native WebSocket but defaults to protocol ssl (and accepts tcp), neither of which is an accepted WebSocket URL scheme. A raw Electrum TCP/TLS endpoint needs a compatible WebSocket gateway or a different transport. The adapter also sends only when the socket is OPEN while calls can be issued immediately, so a first request may be silently dropped. No live Electrum connection was tested.
- **Why unsigned bytes must not be broadcast:** confirm the learner understands `src/wallet-core.ts` and does not claim beyond: Key management, signing, raw serialization, Lightning, and production broadcast are not implemented.
- **Store wallet state without inventing chain truth:** confirm the learner understands `src/store.ts` and does not claim beyond: Local changes can survive restarts but are not proof of confirmed on-chain transactions.
- **Integrate a safe wallet-demo workflow:** confirm the learner understands `src/walletContext.tsx` and does not claim beyond: Do not connect real keys or funds to this educational build.

Use [evaluation-rubric.json](evaluation-rubric.json). Deduct for unsupported feature claims, untested state transitions, secrets in client code, fake tests presented as external-service proof, or weakening a safety boundary to make the demo appear functional. Optional extensions should be scoped as future work until implemented and tested.
