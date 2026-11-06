# Architecture

## Implemented system

CID/base32 helpers, local store, API server, optional client, static page, and Node tests.

## Data and control flow

Bytes → SHA-256 multihash + raw codec + CIDv1 + base32 → local file keyed by CID → retrieve and verify.

## Module source map

- **Content Addressing in Plain Terms:** cidFromBytes hashes input bytes and assembles a CIDv1 raw-codec value; local addressing does not provide network replication.
- **Hash Bytes and Build Multihash:** SHA256_MULTIHASH=0x12; MULTIHASH_LENGTH=32.
- **Assemble CIDv1 and Raw Codec:** CID_VERSION=1; RAW_CODEC=0x55; cidFromBytes(content).
- **Encode and Decode Base32:** base32encode/base32decode use lowercase RFC-style alphabet symbols.
- **Store and Verify Local Content:** createStore creates directory-backed operations; this is not a distributed IPFS node.
- **HTTP Server and Client Flow:** createIpfsServer injects a store; DEFAULT_API is localhost:5001.
- **Serve the Browser UI:** servePublic maps static files/content types from PUBLIC_DIR.
- **Tests and Real-IPFS Limits:** The client only calls a configured node URL; the included app does not provide an IPFS daemon, pinning service, replication, or garbage collection.

## Boundaries and risks

- README states no IPFS daemon/network is used; storage is local and not replicated/announced.
- Only raw codec/single-block behavior is modeled; real IPFS UnixFS chunking/DAGs can produce different CIDs.
- A CID is generally not the same as a simple whole-file hash.
- No pinning, quotas, or garbage collection.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
