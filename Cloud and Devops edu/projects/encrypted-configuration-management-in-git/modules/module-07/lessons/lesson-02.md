# Trace the source implementation for rotate recipients with a grace period

**Lesson ID:** lesson-02  
**Module ID:** module-07  
**Estimated duration:** 30 minutes

## Purpose and learning objectives

This lesson introduces **Rotate Recipients with a Grace Period** in Encrypted Configuration Management in Git. Begin with the plain-language model, then trace the source implementation and examine its operational boundary.

## Prerequisites

Read the earlier lesson in this module. The project uses Python, SOPS, age, Git, CI, optional Ansible. Use a local, simulation, or test environment described in setup-guide.md.

## Topic in plain language

Rotation adds new readers while previous recipients remain until the grace-period drop step.

## Move from the idea to the source

Now trace the implementation for Rotate Recipients with a Grace Period. The source evidence is: rotate_env re-encrypts and updates previous_recipients; --drop-previous removes old recipients.

The distinction to keep in view is what the supplied files implement versus what a larger production system would require. The README lists known limitations and source discrepancies.

## Step-by-step

1. Open `secretsync/cli.py` and locate `previous_recipients`.
2. Trace values from input to state changes and result.
3. Compare the actual code excerpt with the authored source finding: rotate_env re-encrypts and updates previous_recipients; --drop-previous removes old recipients.
4. Separate source behavior from external infrastructure.

## Source-code walkthrough

**Source file(s):** secretsync/cli.py; secretsync/config.py

**Source:** `secretsync/cli.py:606–615`  
**Focus cue:** `previous_recipients`

````py
keys = load_config(root).keys[args.env]
    if args.drop_previous:
        print("  grace recipients dropped: only current recipients can decrypt now")
    elif keys.previous_recipients:
        print(
            f"  grace: {len(keys.previous_recipients)} previous recipient(s) still able "
            f"to decrypt until `rotate --env {args.env} --drop-previous`"
        )
    print(f"  last_rotated: {keys.last_rotated} "
          f"(reminder every {keys.rotation_reminder_days} days)")
````

Read the excerpt in context. Follow the focus cue to its caller or consumer, then state the behavior and one boundary. This copied source excerpt was not executed during content generation. For cryptography, secrets, infrastructure, and smart-contract topics, use official references and treat the package as educational material, not security approval.

## Expected behavior

The code-level finding is: rotate_env re-encrypts and updates previous_recipients; --drop-previous removes old recipients. The original application was not modified or deployed by this content package.

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
