# Explain build the hash-chained audit log using a plain-language model

**Lesson ID:** lesson-01  
**Module ID:** module-08  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Build the Hash-Chained Audit Log** in Encrypted Configuration Management in Git. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Python, SOPS, age, Git, CI, optional Ansible. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Each audit record hashes a canonical form and links to the prior digest; a separate head checkpoint helps detect tail truncation.

## Move from the idea to the source

Begin with this mental model: Each audit record hashes a canonical form and links to the prior digest; a separate head checkpoint helps detect tail truncation. Identify the actual components in secretsync/audit.py.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. State the idea in your own words before reading code.
2. Open `secretsync/audit.py` at the cited lines and identify the input and output.
3. Compare the analogy with the implementation: AuditLog appends JSONL; verify checks chain and head.
4. Write one question the analogy does not answer about real deployments.

## Source-code walkthrough

**Source file(s):** secretsync/audit.py

**Source:** `secretsync/audit.py:21–30`  
**Focus cue:** `AuditLog`

````py
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

__all__ = ["AuditError", "AuditLog", "GENESIS", "sha256_file", "sha256_bytes"]

GENESIS = "0" * 64
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: AuditLog appends JSONL; verify checks chain and head. The original application was not modified or deployed by this content package.

## Practical exercise

Trace one input through the named source. Record the input, validation, state/data change, result, and one failure path. Then design a safe verification plan with the expected result and evidence.

## Common mistakes and debugging

- Treating a README feature list as proof of a real integration.
- Assuming an interface-shaped model is compatible with a provider protocol.
- Confusing passing unit tests with a production guarantee or independent security audit.
- Running destructive host, cluster, contract, or cloud operations against real resources.
- Logging secrets or relying on hard-coded sample credentials.

## Best practices and security

Use disposable environments, least privilege, explicit credential handling, and bounded inputs. For contracts, secrets, infrastructure, and host command runners, inspect the target before execution and separate test from production resources.

## Summary

You moved from a beginner explanation to the actual source behavior and its operational limits. You can cite the file and explain one verification path.

## Knowledge check

1. Which file/function implements the behavior?
2. What data or state changes?
3. What does the source not prove or provide?

## References

Use the official links in references.json.
