# Mentor Solution Guide

## Source findings

The project implements: Task/Pipeline structs, DAG resolver, parameter substitution, workspace/results, runner, retry/timeout/finally logic, directory loader.

Review known limitations:
- No Kubernetes API server, Tekton CRDs, Pods, service accounts, or cluster execution are used.
- Commands run on the host; untrusted pipeline definitions can execute arbitrary commands.
- Definitions are Go structs/custom YAML reader rather than Tekton YAML CRDs.
- README's Notes says no retry/timeout/workspace despite earlier features/tests claiming they are implemented; inspect code, which does implement them in the local runner.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
