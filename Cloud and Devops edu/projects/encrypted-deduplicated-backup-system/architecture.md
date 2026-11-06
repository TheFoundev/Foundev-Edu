# Architecture

## Implemented system

Content-defined boundaries, chunk hashes, per-chunk encryption, repository manifest, restore path, unit tests.

## Data and control flow

Input bytes → rolling-hash chunks → chunk ID → encrypted chunk file → manifest → decrypt and concatenate on restore.

## Module source map

- **Chunk and Manifest Model:** ChunkInfo/PutResult/Repository describe chunk metadata and stored content.
- **Password, Salt, and Key Derivation:** NewSalt, deriveKey, and pbkdf2Key derive a 32-byte key.
- **Content-Defined Chunk Boundaries:** ContentDefined uses rolling hash with min/average/max boundaries.
- **Hash IDs and Deduplication:** chunkID hashes bytes; Put checks chunk presence before writing.
- **Encrypt and Authenticate Chunks:** seal creates a nonce and stores ciphertext/tag; openSealed authenticates before returning plaintext.
- **Write Repository and Manifest:** Repository.Put returns PutResult; Save serializes repository state.
- **Restore and Verify Content:** OpenRepository loads persisted state; Restore iterates chunk metadata and opens stored chunk bytes.
- **Test Deduplication and Restore Drills:** TestBackupDedupAndRestore; TestContentDefinedChunking; TestTheKeyIsDerivedWithASalt.
- **Operational Limits and Recovery:** Restore reads encrypted local chunks; the code has no remote backend, scheduler, retention policy, snapshots, or prune command.

## Boundaries and risks

- The repository is local; no object-store transport, scheduling, snapshot history, prune, or replication exists.
- Homegrown PBKDF2 and chunking must be reviewed carefully before production use.
- Chunks are stored as separate files, not pack files; backup names/manifest semantics matter.
- A key/secret loss can make encrypted backups unrecoverable.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
