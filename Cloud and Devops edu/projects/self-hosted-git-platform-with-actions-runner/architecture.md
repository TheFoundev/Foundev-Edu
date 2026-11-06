# Architecture

## Implemented system

Blob/tree/commit object store, branches/log/diff, JSON save/load, small YAML-like workflow parser, job/step dependency runner.

## Data and control flow

Files → Git-style objects/commit → branch pointer; workflow text → jobs/steps → dependency gates → host command execution → results.

## Module source map

- **Git Object Types and Hashing:** gitObjectHash/hashOf build object hash input; tests compare Git-compatible hashes.
- **Build Commits and Branch Pointers:** Commit/CommitAs stores objects and updates branch head.
- **Read History, Branches, and Diff:** Log, Head, Branches, CreateBranch, Checkout, and Diff provide repository navigation.
- **Save and Load Repository State:** Save/Load serialize repository state.
- **Parse Workflow Definitions:** ParseWorkflow supports list/key job shapes, run/uses/needs/env fields.
- **Resolve Jobs and Steps:** jobBlocked and stepBlocked check needs/dependencies and prior failures.
- **Run Commands on the Host:** runStep uses process execution and captures output/exit code.
- **Handle Failures and Results:** Runner.Run returns StepResults with status/output.
- **Test Hashes and Workflow Semantics:** The test suite verifies selected formats and commands, not full Git/Actions compatibility.
- **Security and Product Boundaries:** The CLI entry point starts the local repository/runner; source has no Git server, OAuth, container runner, or multi-user boundary.

## Boundaries and risks

- Objects are stored in a local JSON state, not packed or served over Git protocol.
- Workflow parser supports only a small syntax subset; it is not full YAML or GitHub Actions.
- Runner executes commands on the host without container isolation; never run untrusted workflow files.
- README's wording that steps are recorded conflicts with tests/implementation showing HostRunner executes them; study source, not that sentence.
- Prebuilt executable files are present in the repository; their provenance is not established by source review, so do not run them blindly.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
