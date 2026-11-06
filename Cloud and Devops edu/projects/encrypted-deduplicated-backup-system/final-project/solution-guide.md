# Mentor Solution Guide

## Source findings

The project implements: Content-defined boundaries, chunk hashes, per-chunk encryption, repository manifest, restore path, unit tests.

Review known limitations:
- The repository is local; no object-store transport, scheduling, snapshot history, prune, or replication exists.
- Homegrown PBKDF2 and chunking must be reviewed carefully before production use.
- Chunks are stored as separate files, not pack files; backup names/manifest semantics matter.
- A key/secret loss can make encrypted backups unrecoverable.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
