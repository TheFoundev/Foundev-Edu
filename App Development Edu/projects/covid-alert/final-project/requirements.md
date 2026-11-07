# Final project requirements — COVID Alert

## Objective

Deliver a working, demonstrable extension of the existing COVID Alert app. The extension must reuse the source architecture and show understanding across all 7 modules. It must not claim provider or production functionality that is absent.

## Functional requirements

- Demonstrate the core workflow covered by the app and all relevant modules.
- Implement one approved feature extension grounded in the current models/screens/services.
- Validate inputs and show actionable empty, error, and success states.
- Persist only the state the source architecture intends to persist.
- Add tests for normal behavior and meaningful edge/failure cases.

## Non-functional requirements

- Keep UI, domain rules, persistence, and external-service boundaries separated.
- Document security/privacy assumptions and known limitations.
- Preserve accessibility basics and usable layout on target form factors.
- Avoid hard-coded secrets and unsafe network defaults; do not process real money or health decisions.
- Keep dependencies minimal and describe any new dependency and licensing impact.

## Milestones

1. **Source audit:** map user journey, owner files, current tests, and unimplemented claims.
2. **Design:** define data flow, state transitions, failure states, and acceptance checks.
3. **Core implementation:** extend the domain rule and add unit tests.
4. **UI integration:** connect controls, loading/empty/error states, and persistence.
5. **Verification:** run available tests/builds, perform manual target-device checks, record environment and gaps.
6. **Demo and handoff:** show feature, tests, architecture, security choices, and known limitations.

## Deliverables

- Source changes in the existing app project.
- Tests and exact test/build commands with truthful results.
- A short architecture/data-flow note and updated project README.
- A 3–5 minute demo or recording showing the expected behavior and one edge case.
- A review log listing known defects, unverified integrations, and future work.

## Acceptance criteria

- Every change maps to named source files and a module learning objective.
- Feature works in the declared target environment without requiring undisclosed infrastructure.
- Automated tests cover domain behavior and regression boundaries.
- Manual checklist covers navigation, accessibility, persistence, and runtime behavior where available.
- Documentation distinguishes implemented, simulated, external, proposed, and unverified behavior.
- Security controls and warnings remain visible and accurate.

## Testing checklist

- [ ] Existing tests pass or failures are documented with environment details.
- [ ] Added tests cover expected, invalid, empty, and failure inputs.
- [ ] Typecheck/build runs on the supported host where available.
- [ ] Manual app flow verified on target simulator/device.
- [ ] Persistence/relaunch behavior checked.
- [ ] External integration tested only against an authorized non-production environment.
- [ ] Demo data and limitations are obvious to a reviewer.
