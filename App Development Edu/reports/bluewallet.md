# Validation report — bluewallet

- Generated: 2026-11-07T05:29:16.094709+00:00
- Modules: 8; lessons: 8; questions: 80
- Structural result: **PASS**

## Passed checks

- Required package root files and project metadata checked.
- JSON parsed; package-internal and source links checked.
- Unique module, lesson, exercise, and question IDs checked.
- Per-module lesson references, 10-question assessments, option sets, answer keys, and explanations checked.
- Manifest counts and included_files checked.
- Required file inventory is complete; no unlisted package files detected.

## Errors

- None.

## Warnings and human/runtime review

- Structural validation does not establish instructional accuracy, compile apps, prove provider/API behavior, verify device behavior, or establish deployment.
- Confirm framework/provider documentation versions and run platform-specific builds in the intended environment.
- Source dependency review: Expo is pinned to `~51.0.28` and React Native to `0.74.5`; current official Expo references may describe a newer SDK, so learners must consult version-matched SDK documentation before changing dependencies.
- BlueWallet has no key management or signing; Electrum broadcast intentionally refuses unsigned transactions. Never use real funds.

## Source-specific findings

- **A wallet screen is a view of money records:** A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network.; Seed transactions and the receive address are placeholders; never send funds to them.
- **Address checks before payment planning:** An address is like a destination label with a built-in error check. Follow Bech32 decoding from characters to checksum and witness data, compare the simpler Base58 prefix/length screen, and see how the send screen rejects input before requesting a transaction plan.; Validation is not ownership proof: the Base58 path checks only prefix and length rather than checksum, and the implementation is not a substitute for audited wallet software.
- **Hashing and script-hash derivation:** Hashing turns bytes into a fixed fingerprint; Electrum queries use a script-derived identifier. Follow the SHA implementation and the address-to-script-hash conversion, including byte order and test vectors.; A correct hash does not sign a transaction or protect a connection.
- **Plan inputs, fee, change, and dust:** A UTXO is an unspent piece of value. The planner selects enough pieces to cover amount plus estimated fee, then considers change and a dust threshold. Trace the UI request into buildUnsignedTransaction.; The transaction is unsigned; fee size/rate assumptions are simplified, the change output currently uses an empty placeholder address, and no real payment should be made.
- **Demo wallet versus Electrum adapter:** An adapter lets the same screen ask different backends for wallet operations. Compare the local demo with the Electrum client and trace how context selects/wires it and how JSON-RPC messages travel.; Source mismatch: the client constructs a React Native WebSocket but defaults to protocol ssl (and accepts tcp), neither of which is an accepted WebSocket URL scheme. A raw Electrum TCP/TLS endpoint needs a compatible WebSocket gateway or a different transport. The adapter also sends only when the socket is OPEN while calls can be issued immediately, so a first request may be silently dropped. No live Electrum connection was tested.
- **Why unsigned bytes must not be broadcast:** A payment plan is an unsigned instruction sheet, not a valid signed transaction. Trace the UI flow to broadcast and confirm the Electrum adapter throws before sending anything because signing and raw serialization are missing.; Key management, signing, raw serialization, Lightning, and production broadcast are not implemented.
- **Store wallet state without inventing chain truth:** Local storage is a notebook, not a blockchain. Read the storage adapter and store tests, then distinguish persisted demo history from provider-synchronized history.; Local changes can survive restarts but are not proof of confirmed on-chain transactions.
- **Integrate a safe wallet-demo workflow:** Map address input to validation, UTXO planning, and the final refusal boundary. Prepare a demo that shows what would be needed for signing while preventing real-fund expectations.; Do not connect real keys or funds to this educational build.

## Runtime and deployment status

No source application was executed or deployed by this validator. See the package README and the source project README for available local test commands; execute platform builds and authorized external-service checks separately.
