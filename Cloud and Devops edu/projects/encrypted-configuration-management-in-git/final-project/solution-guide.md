# Mentor Solution Guide

## Source findings

The project implements: Config loader/YAML subset, real SOPS/age subprocess wrappers, encrypt/decrypt/rotate CLI, CI policy checks, plaintext scanner, audit chain/checkpoint, Git hooks and CI examples.

Review known limitations:
- SOPS upstream repository is archived; check maintained releases/forks and current binary provenance.
- Decrypt policy is a guard inside this CLI, not an OS sandbox; CI identity can decrypt its authorized environment.
- Audit hash chain is tamper-evident, not tamper-proof; an attacker able to rewrite records and checkpoint can rewrite history.
- Plaintext scanner is pattern-based and can miss secrets; encrypted sample data and local identities must be handled carefully.
- README says Ansible optional; it is not equivalent to external secret management.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
