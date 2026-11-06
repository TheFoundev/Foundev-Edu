# Mentor Solution Guide

## Source findings

The project implements: Blob/tree/commit object store, branches/log/diff, JSON save/load, small YAML-like workflow parser, job/step dependency runner.

Review known limitations:
- Objects are stored in a local JSON state, not packed or served over Git protocol.
- Workflow parser supports only a small syntax subset; it is not full YAML or GitHub Actions.
- Runner executes commands on the host without container isolation; never run untrusted workflow files.
- README's wording that steps are recorded conflicts with tests/implementation showing HostRunner executes them; study source, not that sentence.
- Prebuilt executable files are present in the repository; their provenance is not established by source review, so do not run them blindly.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
