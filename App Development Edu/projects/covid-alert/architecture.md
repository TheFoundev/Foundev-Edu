# Architecture — COVID Alert

Build an educational symptom and simulated exposure-check app with clearly labelled outcomes and local history.

## Data and behavior map

1. **What a check record means** — `src/data.ts` (`export const symptomItems`): Check and ExposureResult types, symptom catalogue, resources, and sample data. Related files: src/exposure.ts; src/data.ts.
2. **A service-shaped simulation** — `src/exposure.ts` (`export class SimulatedExposureService`): ExposureService interface, simulated implementation, and simulation labelling. Related files: src/exposure.ts; src/screens/StatusScreen.tsx.
3. **From selected symptoms to an informational score** — `src/exposure.ts` (`export function assessSymptoms`): Weights, duplicate/unknown filtering, thresholds, advice, and disclaimer. Related files: src/exposure.ts; src/screens/SymptomsScreen.tsx.
4. **History ordering and next-check time** — `src/exposure.ts` (`export function nextCheckDue`): toCheck, lastCheck, formatting, interval calculation, and empty state. Related files: src/exposure.ts; src/screens/StatusScreen.tsx.
5. **Local persistence and the screen flow** — `src/exposureContext.tsx` (`export function ExposureProvider`): Provider lifecycle, AsyncStorage adapter, resources screen, reusable controls, and tabs. Related files: src/exposureContext.tsx; src/store.ts; src/persistence.ts; src/screens/ResourcesScreen.tsx; src/components.tsx; src/theme.ts; App.tsx.
6. **Verify behavior and avoid overstating results** — `test/exposure.test.ts` (`empty history is labeled as unchecked`): Simulation tests, storage failures, labels, disclosure, and evidence limits. Related files: test/exposure.test.ts; src/components.tsx; README.md.
7. **Present a complete transparent health-demo journey** — `src/exposure.ts` (`checkStatusLabel`): Screen-to-model integration, clear-state wording, limitations, and demo script. Related files: App.tsx; src/screens/StatusScreen.tsx; src/screens/SymptomsScreen.tsx; src/exposure.ts.

## Runtime boundaries

- Stack: Expo, React Native, TypeScript, AsyncStorage.
- Explicit limits across modules: ['Seeded content is demonstration data; no public-health data source is contacted', 'No Bluetooth, Apple/Google exposure notification, diagnosis, or contact-tracing integration exists', 'The score is educational and is not medical advice or a validated clinical decision tool', 'The configured interval is a UI rule, not health guidance', 'History stays on the device in this demo; local storage is not a protected health record system', 'A passing unit suite does not validate clinical advice, health policy, or native exposure notifications', 'Never encourage a learner to make health decisions from the demo output'].
- Source code is the implementation of record; compare each claim with project README and tests.
- Read each lesson’s directly quoted source excerpt and linked source path before changing behavior.
- No application is claimed to have been deployed or connected to production infrastructure.
