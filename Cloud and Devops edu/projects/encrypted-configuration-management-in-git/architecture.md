# Architecture

## Implemented system

Config loader/YAML subset, real SOPS/age subprocess wrappers, encrypt/decrypt/rotate CLI, CI policy checks, plaintext scanner, audit chain/checkpoint, Git hooks and CI examples.

## Data and control flow

Plain config → SOPS encrypt to age recipients → encrypted file committed → CI identity decrypts → audit records and precommit/CI checks verify hygiene.

## Module source map

- **Threat Model and Secret Lifecycle:** authorize_decrypt checks CI identity and marker policy; the README distinguishes stolen clones, compromised CI, shared recipients, and scanner misses.
- **Load Environment and Recipient Config:** load_config builds EnvKeys, CreationRule, and DecryptPolicy; recipients are validated.
- **Read the Mini-YAML Subset:** loads tokenizes/indents and parses scalars, flow lists/maps, sequences, and mappings.
- **Find and Invoke SOPS/Age Tools:** find_tool checks environment/config/path/.tools; sops_encrypt/decrypt call subprocess helpers.
- **Encrypt Files for Recipients:** cmd_encrypt checks configured file/recipients and records an audit action.
- **Authorize CI Decryption:** detect_ci, check_marker, authorize_decrypt determine allow/deny.
- **Rotate Recipients with a Grace Period:** rotate_env re-encrypts and updates previous_recipients; --drop-previous removes old recipients.
- **Build the Hash-Chained Audit Log:** AuditLog appends JSONL; verify checks chain and head.
- **Scan Tracked Files for Plaintext:** scan_paths uses configured patterns/globs; run_check combines coverage, ciphertext, audit, and plaintext findings.
- **Use the Pre-Commit and CI Gates:** README directs git config core.hooksPath .githooks; CI runs tests and example automation.
- **Use the Ansible Example Carefully:** The project README describes Ansible as an example integration, not required core runtime.
- **Verify and State the Security Limits:** AuditLog.verify checks a local hash chain and plaintext scanning uses configured patterns; neither detects every compromise or plaintext secret.

## Boundaries and risks

- SOPS upstream repository is archived; check maintained releases/forks and current binary provenance.
- Decrypt policy is a guard inside this CLI, not an OS sandbox; CI identity can decrypt its authorized environment.
- Audit hash chain is tamper-evident, not tamper-proof; an attacker able to rewrite records and checkpoint can rewrite history.
- Plaintext scanner is pattern-based and can miss secrets; encrypted sample data and local identities must be handled carefully.
- README says Ansible optional; it is not equivalent to external secret management.

This package teaches the checked-in implementation and records gaps between the source and broader platform concepts named by the project. It does not certify security or production readiness.
