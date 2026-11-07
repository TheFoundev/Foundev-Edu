# A wallet screen is a view of money records

**Lesson ID:** `bluewallet-01-wallet-model-and-ui-lesson-01`  
**Project:** BlueWallet  
**Source focus:** `src/data.ts` — `export type Transaction`

## Purpose and learning objectives

In plain terms, this lesson teaches **A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/data.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Seed transactions and the receive address are placeholders; never send funds to them.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Transaction shape, satoshi formatting, seeded records, and tab shell**. This is a learning implementation, so keep the limit in view: Seed transactions and the receive address are placeholders; never send funds to them.

## Learning objectives

1. Describe the everyday behavior: A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network.
2. Find the relevant implementation in `src/data.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `src/data.ts`, `src/screens/WalletScreen.tsx`, `src/components.tsx`, `src/theme.ts`, `App.tsx`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Transaction shape, satoshi formatting, seeded records, and tab shell**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Seed transactions and the receive address are placeholders; never send funds to them.

### 3. Read the real implementation

The excerpt below is copied directly from `src/data.ts` around `export type Transaction`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
export type Transaction = {
  id: string;
  type: 'received' | 'sent';
  amountSats: number;
  counterparty: string;
  date: string;
  status: 'confirmed' | 'pending';
};

/**
 * The demo wallet the app ships with.
 *
 * The balance is not a constant any more: it is the sum of the transactions
 * below, which the wallet core computes.
 */
export const seedTransactions: Transaction[] = [
  { id: 't1', type: 'received', amountSats: 82000, counterparty: 'bc1q…9x2f', date: 'Apr 22, 10:14', status: 'confirmed' },
  { id: 't2', type: 'sent', amountSats: 24000, counterparty: 'bc1q…7m1k', date: 'Apr 20, 16:02', status: 'confirmed' },
```



The selected symbol is `export type Transaction`. Relate its code to this source map:

- `src/data.ts` — inspect how this part participates in transaction shape, satoshi formatting, seeded records, and tab shell.
- `src/screens/WalletScreen.tsx` — inspect how this part participates in transaction shape, satoshi formatting, seeded records, and tab shell.
- `src/components.tsx` — inspect how this part participates in transaction shape, satoshi formatting, seeded records, and tab shell.
- `src/theme.ts` — inspect how this part participates in transaction shape, satoshi formatting, seeded records, and tab shell.
- `App.tsx` — inspect how this part participates in transaction shape, satoshi formatting, seeded records, and tab shell.

### 4. Step-by-step source reading

1. Open `src/data.ts` and search for `export type Transaction`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network. The known limitation is explicit: Seed transactions and the receive address are placeholders; never send funds to them. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `bluewallet-01-wallet-model-and-ui-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

## Common mistakes and debugging

- **Reading only the screen:** follow the action to `src/data.ts`; UI labels alone do not define behavior.
- **Assuming a product-name feature exists:** compare the implementation and the limitation above with the project README.
- **Changing state in several places:** identify the owning model/store/context before editing.
- **Calling a test a full-system check:** determine whether it uses fake data, fake storage, a fake socket, or a real runtime.
- **Debug sequence:** reproduce the behavior, inspect the relevant input, log or assert the model result, verify the caller and rendered state, then check persistence or network boundaries separately.

## Best practices and security

- Keep this behavior small and testable; make validation and failure outcomes explicit.
- Preserve the typed boundary and avoid trusting unvalidated input.
- Do not place credentials, private keys, health details, financial records, or trusted-network controls in an insecure client setting.
- If a service integration is proposed, add authentication, transport protection, privacy review, and provider-specific tests before describing it as implemented.
- See the project-specific review items and [Owasp Mobile](https://mas.owasp.org/MASVS/).

## Summary

You started from the user task, named its everyday model, followed `export type Transaction` in `src/data.ts`, and traced the related files. The implemented behavior is **A wallet dashboard is a summary board. Learn the Transaction record and satoshi units, then trace the sample rows and balance display into the screen. Separate sample values from values supplied by a network**; the boundary is **Seed transactions and the receive address are placeholders; never send funds to them**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/data.ts`](../../../../../../projects/bluewallet/src/data.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Bitcoin Bip173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki), [Electrum](https://electrum-protocol.readthedocs.io/en/latest/protocol.html), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
