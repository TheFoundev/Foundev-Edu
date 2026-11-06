# Assess failure and operational limits of scan tracked files for plaintext

**Lesson ID:** lesson-03  
**Module ID:** module-09  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Scan Tracked Files for Plaintext** in Encrypted Configuration Management in Git. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Python, SOPS, age, Git, CI, optional Ansible. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

The scanner applies secret-shaped patterns and exclusions to tracked files; pattern scanning cannot identify every possible secret.

## Move from the idea to the source

Move from the happy path to operational reasoning. For this project, scan_paths uses configured patterns/globs; run_check combines coverage, ciphertext, audit, and plaintext findings.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Identify a failure, boundary, or unexpected input.
2. Use `secretsync/check.py` and the `scan_paths` path to predict behavior: scan_paths uses configured patterns/globs; run_check combines coverage, ciphertext, audit, and plaintext findings.
3. Describe a safe local/test verification and what evidence to collect.
4. State what additional code or infrastructure would be needed before making a production claim.

## Source-code walkthrough

**Source file(s):** secretsync/plaintext.py; secretsync/check.py

**Source:** `secretsync/check.py:120–129`  
**Focus cue:** `scan_paths`

````py
errors.append(f"file contains age private key material: {rel}")
    else:
        warnings.append("not a git repository: tracked-file checks fell back to a filesystem walk")

    # 4. plaintext secret-shaped keys in tracked structured files ----------
    findings = plaintext.scan_paths(base, files, config.plaintext_patterns, config.scan_exclude)
    for finding in findings:
        errors.append(f"plaintext secret in tracked file: {finding}")

    # 5. audit trail -------------------------------------------------------
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: scan_paths uses configured patterns/globs; run_check combines coverage, ciphertext, audit, and plaintext findings. The original application was not modified or deployed by this content package.

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
