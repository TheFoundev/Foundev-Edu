# BlueWallet — source-grounded mini-project course

## Purpose and expected result

Build and inspect a wallet-learning demo covering address validation, transaction planning, wallet adapters, and defensive refusal of incomplete transaction broadcast. This package teaches the copied source project at undergraduate third-year mini-project depth. The expected result is that a learner can demonstrate the actual app workflow, trace its implementation, explain its limits, and produce a tested, reviewable extension.

## Use cases and implemented features

This is an educational companion to `../../../projects/bluewallet/`, not a replacement app. Actual features and limitations are listed in the source project's README and reconciled module by module here. The lessons quote current source excerpts; source files remain the implementation of record.

Curriculum topics:

- **01. A wallet screen is a view of money records** — Transaction shape, satoshi formatting, seeded records, and tab shell (`src/data.ts`).
- **02. Address checks before payment planning** — Bech32 checksum and witness program validation; Base58 prefix/length screening; accepted address boundary (`src/address.ts`).
- **03. Hashing and script-hash derivation** — SHA-256 implementation and Electrum script hash preparation (`src/address.ts`).
- **04. Plan inputs, fee, change, and dust** — UTXO selection, fee estimate, amount validation, and unsigned output construction (`src/wallet-core.ts`).
- **05. Demo wallet versus Electrum adapter** — WalletCore boundary, DemoWalletCore, ElectrumWalletCore, and WebSocket transport (`src/wallet-core.ts`).
- **06. Why unsigned bytes must not be broadcast** — UnsignedTransaction type, signing gap, refusal path, and no-send regression test (`src/wallet-core.ts`).
- **07. Store wallet state without inventing chain truth** — Key/value adapter, JSON parsing, corrupt state, and local transaction storage (`src/store.ts`).
- **08. Integrate a safe wallet-demo workflow** — Validation-to-plan flow, explicit limitations, test evidence, and release boundary (`src/walletContext.tsx`).

The build is a learning implementation, not upstream product parity. Key limits include:

- Seed transactions and the receive address are placeholders; never send funds to them.
- Validation is not ownership proof: the Base58 path checks only prefix and length rather than checksum, and the implementation is not a substitute for audited wallet software.
- A correct hash does not sign a transaction or protect a connection.
- The transaction is unsigned; fee size/rate assumptions are simplified, the change output currently uses an empty placeholder address, and no real payment should be made.
- Source mismatch: the client constructs a React Native WebSocket but defaults to protocol ssl (and accepts tcp), neither of which is an accepted WebSocket URL scheme. A raw Electrum TCP/TLS endpoint needs a compatible WebSocket gateway or a different transport. The adapter also sends only when the socket is OPEN while calls can be issued immediately, so a first request may be silently dropped. No live Electrum connection was tested.
- Key management, signing, raw serialization, Lightning, and production broadcast are not implemented.
- Local changes can survive restarts but are not proof of confirmed on-chain transactions.
- Do not connect real keys or funds to this educational build.

## Audience and prerequisites

Third-year undergraduate students with introductory programming and basic source-control experience. Read [prerequisites](prerequisites.md) for platform-specific preparation.

## Requirements and setup

The implementation stack is Expo, React Native, TypeScript, Bitcoin address formats, Electrum JSON-RPC adapter with React Native WebSocket transport (not operational as configured). Follow [setup-guide.md](setup-guide.md) and the adjacent source README. The JavaScript projects use Node.js/npm and Expo; the SwiftUI projects require macOS/Xcode. Do not treat package generation as an app build.

## Architecture and important components

See [architecture.md](architecture.md) and the lesson source maps. The course proceeds from a plain-language mental model to the app’s real model/service/store, screen wiring, tests, and operational boundary. The app-specific `App.tsx` or SwiftUI `App`/`ContentView` is the shell; module lessons map individual behaviors to their owners.

## Source discrepancies and human review

- **Dependency age:** source pins Expo `~51.0.28`, React Native `0.74.5`, and AsyncStorage `1.23.1`. The linked current Expo documentation may describe a newer SDK; use version-matched docs and review upgrade compatibility before changing the lockfile.
- **Wallet safety review:** `src/address.ts` screens Base58 strings by prefix and length but does not verify their checksum; `buildUnsignedTransaction` creates change with an empty placeholder address; and the Electrum transport defaults to `ssl://` while using a WebSocket constructor. The WebSocket adapter also may silently drop an RPC call sent before OPEN. Electrum broadcasting is deliberately refused because signing/serialization are absent. None of this path was runtime-verified.

## Tests and evidence

See source `package.json`, `test/`, or `Tests/` for actual test commands and assertions. Test infrastructure may use fakes and may not exist on the package-generation host. A passing structural package validator only checks content shape and references; it does not establish instructional accuracy, compile the app, validate an external API, or prove deployment.

## Security and privacy

Read each module's limits and [setup-guide.md](setup-guide.md). This package calls out sensitive boundaries including simulated health outcomes, unsigned wallet plans, local expense data, browser content rules, public client configuration, and Peyara's unauthenticated relay. Never use real secrets, funds, health decisions, or production personal data with these demos.

## Troubleshooting

Start with the named source file, then follow its caller and test. Confirm platform tools and dependencies before interpreting a build failure. For network-connected samples, verify endpoint and server compatibility without removing security controls. Use the project README for project-specific steps.

## Further learning

See [references.json](references.json), each module's lesson, and [glossary.md](glossary.md). Official documentation links are supplied for the protocols and frameworks the code references.
