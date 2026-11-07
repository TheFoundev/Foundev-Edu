# Integrate a safe wallet-demo workflow: Trace the source

**Lesson ID:** `bluewallet-08-mini-project-integration-lesson-02`  
**Module ID:** `bluewallet-08-mini-project-integration`  
**Source focus:** `src/screens/SendScreen.tsx` → `SendScreen`

## Purpose and learning objectives

Open `src/screens/SendScreen.tsx` and locate `SendScreen`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Integrate a safe wallet-demo workflow** is like following one item through a workshop: locate the input, see what changes, then find the output. Map address input to validation, UTXO planning, and the final refusal boundary. Prepare a demo that shows what would be needed for signing while preventing real-fund expectations.

### Step toward the implementation

Open `src/screens/SendScreen.tsx` and locate `SendScreen`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/screens/SendScreen.tsx`, `src/walletContext.tsx`, `src/wallet-core.ts`, `test/wallet.test.ts`.

## Source evidence

Excerpt from [`src/screens/SendScreen.tsx`](../../../../../../App%20Development/bluewallet/src/screens/SendScreen.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
import { formatSats } from '../data';
import { useWallet } from '../walletContext';
import { isValidAddress } from '../address';

export default function SendScreen() {
  const { send, quoteFee } = useWallet();
  const [address, setAddress] = useState('');
  const [amount, setAmount] = useState('');
  const [note, setNote] = useState('');
  const [error, setError] = useState('');
  const [fee, setFee] = useState(0);
  const [sending, setSending] = useState(false);

  useEffect(() => {
    const sats = Number(amount);
    if (!Number.isFinite(sats) || sats <= 0) {
      setFee(0);
      return;
    }
    let cancelled = false;
    quoteFee(sats).then((value) => {
      if (!cancelled) setFee(value);
    });
    return () => {
```

### Read it step by step

1. Find the focus cue `SendScreen` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Integrate a safe wallet-demo workflow**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

## Practical exercise

Complete [`exercise-01.json`](../exercises/exercise-01.json). Add an input or edge case, cite the source, and write the expected result before changing code.

## Common mistakes and debugging

- Inferring feature behavior from the product name or screen alone.
- Skipping the caller, model/state layer, or error path.
- Treating local sample data or a mock response as a real service result.
- Debug by tracing input → validation → transformation → output and then checking the relevant test.

## Best practices and security

Protect credentials and personal data, validate untrusted inputs, request only necessary device permissions, and keep provider/device behavior explicitly unverified until tested in an authorized environment.

## Summary

You began with the module’s plain meaning, traced `SendScreen` in `src/screens/SendScreen.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/bluewallet/src/screens/SendScreen.tsx)
