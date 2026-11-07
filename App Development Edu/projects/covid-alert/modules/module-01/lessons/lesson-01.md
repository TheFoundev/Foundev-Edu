# What a check record means

**Lesson ID:** `covid-alert-01-domain-model-and-fixtures-lesson-01`  
**Project:** COVID Alert  
**Source focus:** `src/data.ts` — `export const symptomItems`

## Purpose and learning objectives

In plain terms, this lesson teaches **A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional**. After finishing, you can:

- Explain the behavior above to a new learner using the project’s actual behavior.
- Locate and trace the implementation in `src/data.ts` and distinguish it from nearby UI or storage layers.
- Describe the exact limitation: Seeded content is demonstration data; no public-health data source is contacted.
- Use the provided exercise to inspect, change, or debug this part without claiming integrations that are absent.

## Prerequisites

- Read the project [README](../../../README.md) and [setup guide](../../../setup-guide.md).
- Be comfortable opening a source file and reading a function or view declaration. The [glossary](../../../glossary.md) defines project terms.

## Begin with the everyday picture

The everyday problem is simple: A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional. First understand what the user is trying to do and what result they expect; then follow the source to see how the code handles it. The core implementation concept is **Check and ExposureResult types, symptom catalogue, resources, and sample data**. This is a learning implementation, so keep the limit in view: Seeded content is demonstration data; no public-health data source is contacted.

## Learning objectives

1. Describe the everyday behavior: A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional.
2. Find the relevant implementation in `src/data.ts` and explain the named symbol.
3. Trace the responsibility across the related files: `src/exposure.ts`, `src/data.ts`.
4. Identify a realistic failure or safety boundary and state how the source handles it.

## Progressive explanation

### 1. Start with the user-visible problem

The user is trying to complete one small task in the app: A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional. A reliable implementation gives that task a clear input, an explicit result, and a predictable state change. In this project, the main concept is **Check and ExposureResult types, symptom catalogue, resources, and sample data**.

### 2. Build the mental model

Treat the source file as the rulebook for this operation. The other files in the map provide the event, data, or rendered result. Do not assume a network, payment, account, or platform capability just because the product concept usually has one. Here the documented limit is: Seeded content is demonstration data; no public-health data source is contacted.

### 3. Read the real implementation

The excerpt below is copied directly from `src/data.ts` around `export const symptomItems`. Use it to identify inputs, state or return values, and the next boundary. The full file is authoritative when the excerpt omits surrounding context.

```typescript
export const symptomItems = [
  { id: 'fever', label: 'Fever or chills' },
  { id: 'cough', label: 'New or worsening cough' },
  { id: 'breath', label: 'Shortness of breath' },
  { id: 'taste', label: 'Loss of taste or smell' },
  { id: 'throat', label: 'Sore throat' },
  { id: 'fatigue', label: 'Unusual fatigue' },
];

export const resources = [
  { name: 'Local public health line', detail: '1-800-555-0199 · 8:00–20:00 daily' },
  { name: 'Emergency services', detail: '911 for severe breathing difficulty' },
  { name: 'Vaccination info', detail: 'Book through your provincial health portal' },
  { name: 'Mental health support', detail: '1-866-555-0142 · free and confidential' },
];
```



The selected symbol is `export const symptomItems`. Relate its code to this source map:

- `src/exposure.ts` — inspect how this part participates in check and exposureresult types, symptom catalogue, resources, and sample data.
- `src/data.ts` — inspect how this part participates in check and exposureresult types, symptom catalogue, resources, and sample data.

### 4. Step-by-step source reading

1. Open `src/data.ts` and search for `export const symptomItems`.
2. Read the containing function/type and write down its input, output, and state effects.
3. Follow the user action or caller into the related files listed above. Note where the source crosses from UI into model, storage, or service code.
4. Compare the implemented path with the project README’s feature and limitation notes. Mark statements that are sample data, local state, simulation, or an external integration.
5. Read the closest test or configuration file (if present) and separate asserted behavior from untested runtime behavior.
6. Make one small change in your own working copy, run the documented check when available, and record what the check does not prove.

### 5. Expected behavior and limitations

Expected behavior follows the source focus: A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional. The known limitation is explicit: Seeded content is demonstration data; no public-health data source is contacted. A structural test or pure unit test can support the local rule, but cannot establish that an outside API, device permission, simulator, server, payment provider, or deployment works.

## Practical exercise

Complete exercise `covid-alert-01-domain-model-and-fixtures-exercise-01` in `exercises/exercise-01.json`. The exercise asks you to inspect the named source, implement or debug a bounded change, add evidence, and preserve the stated safety constraints. Estimated time: 45–90 minutes.

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

You started from the user task, named its everyday model, followed `export const symptomItems` in `src/data.ts`, and traced the related files. The implemented behavior is **A record is a dated note about an app action, not a diagnosis. Read the types and fixtures, identify where sample checks and symptom choices come from, and mark which information is fictional**; the boundary is **Seeded content is demonstration data; no public-health data source is contacted**.

## Knowledge checks

1. Which source file owns the core rule, and which file calls it?
2. What does the named implementation actually change or return?
3. What is deliberately absent, simulated, local-only, or still unverified?
4. Which test would you add to guard the behavior after a change?

## References

- Project source: [`src/data.ts`](../../../../../../projects/covid-alert/src/data.ts)
- Project documentation: [README](../../../README.md), [architecture](../../../architecture.md), [setup guide](../../../setup-guide.md)
- Official learning references: [React Native](https://reactnative.dev/docs/getting-started), [Expo](https://docs.expo.dev/), [Async Storage](https://docs.expo.dev/versions/latest/sdk/async-storage/), [Node Test](https://nodejs.org/api/test.html), [Owasp Mobile](https://mas.owasp.org/MASVS/)
