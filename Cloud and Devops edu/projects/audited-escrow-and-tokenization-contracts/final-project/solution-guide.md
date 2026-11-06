# Mentor Solution Guide

## Source findings

The project implements: Escrow states, partial funding, disputes/timeouts, pull-payment credits; TokenizedAsset roles/provenance/royalties; factory indexes; tests include a reentrancy attacker.

Review known limitations:
- The title says audited, but no independent audit report is supplied.
- Passing tests do not establish contract security.
- The .env key is a placeholder; use local/test networks only.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
