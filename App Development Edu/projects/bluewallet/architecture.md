# Architecture — BlueWallet

Build and inspect a wallet-learning demo covering address validation, transaction planning, wallet adapters, and defensive refusal of incomplete transaction broadcast.

## Data and behavior map

1. **A wallet screen is a view of money records** — `src/data.ts` (`export type Transaction`): Transaction shape, satoshi formatting, seeded records, and tab shell. Related files: src/data.ts; src/screens/WalletScreen.tsx; src/components.tsx; src/theme.ts; App.tsx.
2. **Address checks before payment planning** — `src/address.ts` (`export function isValidAddress`): Bech32 checksum and witness program validation; Base58 prefix/length screening; accepted address boundary. Related files: src/address.ts; src/screens/SendScreen.tsx.
3. **Hashing and script-hash derivation** — `src/address.ts` (`export function scriptHashFromSegwitAddress`): SHA-256 implementation and Electrum script hash preparation. Related files: src/sha256.ts; src/address.ts; test/wallet.test.ts.
4. **Plan inputs, fee, change, and dust** — `src/wallet-core.ts` (`export function buildUnsignedTransaction`): UTXO selection, fee estimate, amount validation, and unsigned output construction. Related files: src/wallet-core.ts; src/screens/SendScreen.tsx.
5. **Demo wallet versus Electrum adapter** — `src/wallet-core.ts` (`this.protocol = options.protocol ?? 'ssl';`): WalletCore boundary, DemoWalletCore, ElectrumWalletCore, and WebSocket transport. Related files: src/wallet-core.ts; src/persistence.ts; src/walletContext.tsx.
6. **Why unsigned bytes must not be broadcast** — `src/wallet-core.ts` (`async broadcast(tx: UnsignedTransaction)`): UnsignedTransaction type, signing gap, refusal path, and no-send regression test. Related files: src/wallet-core.ts; src/walletContext.tsx; test/wallet.test.ts.
7. **Store wallet state without inventing chain truth** — `src/store.ts` (`export class WalletStore`): Key/value adapter, JSON parsing, corrupt state, and local transaction storage. Related files: src/store.ts; src/persistence.ts; test/store.test.ts.
8. **Integrate a safe wallet-demo workflow** — `src/walletContext.tsx` (`buildTransaction`): Validation-to-plan flow, explicit limitations, test evidence, and release boundary. Related files: src/screens/SendScreen.tsx; src/walletContext.tsx; src/wallet-core.ts; test/wallet.test.ts.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, Bitcoin address formats, Electrum JSON-RPC adapter with React Native WebSocket transport (not operational as configured).
- Explicit limits across modules: ['Seed transactions and the receive address are placeholders; never send funds to them', 'Validation is not ownership proof: the Base58 path checks only prefix and length rather than checksum, and the implementation is not a substitute for audited wallet software', 'A correct hash does not sign a transaction or protect a connection', 'The transaction is unsigned; fee size/rate assumptions are simplified, the change output currently uses an empty placeholder address, and no real payment should be made', 'Source mismatch: the client constructs a React Native WebSocket but defaults to protocol ssl (and accepts tcp), neither of which is an accepted WebSocket URL scheme. A raw Electrum TCP/TLS endpoint needs a compatible WebSocket gateway or a different transport. The adapter also sends only when the socket is OPEN while calls can be issued immediately, so a first request may be silently dropped. No live Electrum connection was tested', 'Key management, signing, raw serialization, Lightning, and production broadcast are not implemented', 'Local changes can survive restarts but are not proof of confirmed on-chain transactions', 'Do not connect real keys or funds to this educational build'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
