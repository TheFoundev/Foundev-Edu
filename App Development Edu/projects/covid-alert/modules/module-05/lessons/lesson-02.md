# Local persistence and the screen flow: Trace the source

**Lesson ID:** `covid-alert-05-state-storage-and-ui-lesson-02`  
**Module ID:** `covid-alert-05-state-storage-and-ui`  
**Source focus:** `src/exposureContext.tsx` → `exposureContext`

## Purpose and learning objectives

Open `src/exposureContext.tsx` and locate `exposureContext`. Read the signature, guards, transformation, and return/state update in that order. By the end, explain the behavior and identify what the source does not establish.

## Prerequisites

Complete the previous lesson in this module. Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).

## Progressive explanation

### Beginner explanation

In everyday terms, the code path behind **Local persistence and the screen flow** is like following one item through a workshop: locate the input, see what changes, then find the output. The provider is a shared notebook service for screens. Follow app startup through storage load, check action through update, and persistence save; inspect the resource screen and error/corrupt-data fallback behavior.

### Step toward the implementation

Open `src/exposureContext.tsx` and locate `exposureContext`. Read the signature, guards, transformation, and return/state update in that order. The source files for this module are `src/exposureContext.tsx`, `src/store.ts`, `src/persistence.ts`, `src/screens/ResourcesScreen.tsx`, `src/components.tsx`, `src/theme.ts`, `App.tsx`.

## Source evidence

Excerpt from [`src/exposureContext.tsx`](../../../../../../App%20Development/covid-alert/src/exposureContext.tsx); copied from the source, not executed during package refinement. Read surrounding lines for full context.

```tsx
type ExposureService,
} from './exposure';
import { initialChecks } from './data';

type ExposureContextValue = {
  checks: Check[];
  service: ExposureService;
  ready: boolean;
  /** Run an exposure check and add it to the history. */
  runCheck(): Promise<Check>;
};

const ExposureContext = createContext<ExposureContextValue | null>(null);

/** Holds the check history and the exposure service. */
export function ExposureProvider({
  children,
  service: injected,
}: {
  children: React.ReactNode;
  service?: ExposureService;
}) {
  const service = useMemo(() => injected ?? new SimulatedExposureService(), [injected]);
  const [checks, setChecks] = useState<Check[]>(initialChecks);
```

### Read it step by step

1. Find the focus cue `exposureContext` and identify its arguments or input values.
2. Follow the condition or transformation and identify the returned value or state update.
3. Trace one caller and compare the result with the README claim.
4. Note any local-only, mock, placeholder, or external-service boundary.

## Expected behavior and boundaries

The lesson should produce a source-backed explanation of **Local persistence and the screen flow**. A test or code excerpt establishes only the behavior it covers; it does not prove an external API, device, deployment, or provider works.

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

You began with the module’s plain meaning, traced `exposureContext` in `src/exposureContext.tsx`, and identified one limit or testable boundary.

## Knowledge checks

1. What input or action reaches the source focus?
2. What does the code change or return?
3. Which edge case or integration boundary needs verification?

## References

- [Project README](../../../README.md)
- [Setup guide](../../../setup-guide.md)
- [Source file](../../../../../../App%20Development/covid-alert/src/exposureContext.tsx)
