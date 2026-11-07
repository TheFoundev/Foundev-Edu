# Final project requirements — Abstractive Document Summarization

## Objective

Build a reproducible, source-grounded demonstration and explanation of Abstractive Document Summarization. The submission must clearly distinguish the behavior that exists in the repository from an extension proposed by the learner.

## Functional requirements
1. Trace a representative input through the implemented system and cite source files.
2. Implement or reproduce one bounded, source-aligned feature in an isolated branch/workspace.
3. Validate inputs and handle at least one failure mode.
4. Present results with the required context, caveats, and human correction path.

## Non-functional requirements
- Reproducible setup with documented dependency/data/model requirements.
- No secrets or real sensitive personal data in code, logs, or screenshots.
- Clear separation between inference, presentation, and proposed functionality.
- Appropriate metrics and subgroup/error checks for the domain.

## Milestones
1. Repository and artifact audit.
2. Data-flow and architecture diagram.
3. Minimal source-aligned implementation.
4. Tests for normal, edge, and missing-resource cases.
5. Evaluation, limitation, and responsible-use review.
6. Reproducible report and demo.

## Deliverables
Source changes or a notebook; setup note; architecture/data-flow diagram; tests; small synthetic or consented data fixture; evaluation note; limitation/ethics note; demo output.

## Acceptance criteria
- Every key claim maps to source or an explicitly labeled proposal.
- A new learner can follow setup without undisclosed credentials.
- Tests include at least one edge case and one failure case.
- Evaluation matches the task and data split; no unsupported performance claims.
- The demo does not claim production or consequential-decision readiness.

## Testing checklist
- [ ] Valid input and expected output
- [ ] Empty/malformed input
- [ ] Missing data, model, network, or service dependency as applicable
- [ ] Repeated run or deterministic behavior where expected
- [ ] Privacy/security and human-review check

## Extensions
Compare a baseline; add calibrated uncertainty; improve accessibility; add monitoring/drift checks; expand a dataset only with documented provenance and permission.
