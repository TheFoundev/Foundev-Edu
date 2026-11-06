# Mentor Solution Guide

## Source findings

The project implements: CID/base32 helpers, local store, API server, optional client, static page, and Node tests.

Review known limitations:
- README states no IPFS daemon/network is used; storage is local and not replicated/announced.
- Only raw codec/single-block behavior is modeled; real IPFS UnixFS chunking/DAGs can produce different CIDs.
- A CID is generally not the same as a simple whole-file hash.
- No pinning, quotas, or garbage collection.

## Review sequence

1. Ask the learner to map the source and identify which external systems are absent.
2. Review the threat/trust boundary and operational failure modes.
3. Check the proposed change against the relevant module and source file.
4. Require separate evidence for unit tests, service integration, and production behavior.
5. Review rollback, secret handling, and cleanup before considering deployment complete.

Do not treat local tests as independent audits, production readiness, or successful provider integration.
